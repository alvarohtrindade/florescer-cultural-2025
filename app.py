from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
import sqlite3
import qrcode
import os
import secrets
import string
from datetime import datetime
from utils import gerar_codigo_unico, criar_qr_code, validar_pagamento
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Inicializar banco de dados
def init_db():
    conn = sqlite3.connect('database/eventos.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS participantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            telefone TEXT,
            codigo_unico TEXT UNIQUE,
            tem_brinde BOOLEAN DEFAULT FALSE,
            data_inscricao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            status_pagamento TEXT DEFAULT 'pendente',
            metodo_pagamento TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS codigos_especiais (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo TEXT UNIQUE NOT NULL,
            utilizado BOOLEAN DEFAULT FALSE,
            participante_id INTEGER,
            data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (participante_id) REFERENCES participantes (id)
        )
    ''')
    
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inscrever', methods=['POST'])
def inscrever():
    try:
        dados = request.get_json()
        nome = dados.get('nome')
        email = dados.get('email')
        telefone = dados.get('telefone')
        metodo_pagamento = dados.get('metodo_pagamento')
        
        # Verificar se email já existe
        conn = sqlite3.connect('database/eventos.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM participantes WHERE email = ?', (email,))
        
        if cursor.fetchone():
            conn.close()
            return jsonify({'success': False, 'message': 'Email já cadastrado!'})
        
        # Verificar quantos já se inscreveram
        cursor.execute('SELECT COUNT(*) FROM participantes')
        total_inscritos = cursor.fetchone()[0]
        
        if total_inscritos >= 150:
            conn.close()
            return jsonify({'success': False, 'message': 'Evento lotado!'})
        
        # Gerar código único
        codigo_unico = gerar_codigo_unico()
        
        # Verificar se ganha brinde (primeiros 15)
        tem_brinde = total_inscritos < 15
        
        # Inserir participante
        cursor.execute('''
            INSERT INTO participantes (nome, email, telefone, codigo_unico, tem_brinde, metodo_pagamento)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (nome, email, telefone, codigo_unico, tem_brinde, metodo_pagamento))
        
        participante_id = cursor.lastrowid
        
        # Criar QR Code
        qr_path = criar_qr_code(codigo_unico, nome)
        
        conn.commit()
        conn.close()
        
        # Redirecionar baseado no método de pagamento
        if metodo_pagamento == 'mercadopago':
            # Integração com Mercado Pago
            try:
                import mercadopago
                
                # Configurar SDK
                sdk = mercadopago.SDK(app.config.get('MERCADOPAGO_ACCESS_TOKEN', ''))
                
                # Criar preferência de pagamento
                preference_data = {
                    "items": [
                        {
                            "title": f"Florescer Cultural - {nome}",
                            "quantity": 1,
                            "unit_price": float(app.config.get('PRECO_INGRESSO', 25.00)),
                            "currency_id": "BRL"
                        }
                    ],
                    "payer": {
                        "name": nome,
                        "email": email,
                        "phone": {
                            "number": telefone
                        }
                    },
                    "back_urls": {
                        "success": f"{app.config.get('BASE_URL')}/confirmacao/{codigo_unico}",
                        "failure": f"{app.config.get('BASE_URL')}/?erro=pagamento_falhou",
                        "pending": f"{app.config.get('BASE_URL')}/?status=pendente"
                    },
                    "auto_return": "approved",
                    "external_reference": codigo_unico,
                    "notification_url": f"{app.config.get('BASE_URL')}/webhook/mercadopago",
                    "statement_descriptor": "FLORESCER CULTURAL"
                }
                
                preference_response = sdk.preference().create(preference_data)
                preference = preference_response["response"]
                
                if preference.get("init_point"):
                    return jsonify({
                        'success': True, 
                        'redirect': preference["init_point"],
                        'message': 'Redirecionando para pagamento...'
                    })
                else:
                    # Fallback para confirmação direta se Mercado Pago falhar
                    return jsonify({
                        'success': True, 
                        'redirect': f'/confirmacao/{codigo_unico}',
                        'message': 'Inscrição realizada! Complete o pagamento posteriormente.'
                    })
                    
            except Exception as mp_error:
                print(f"Erro Mercado Pago: {mp_error}")
                # Fallback para confirmação direta
                return jsonify({
                    'success': True, 
                    'redirect': f'/confirmacao/{codigo_unico}',
                    'message': 'Inscrição realizada! Complete o pagamento via PIX/transferência.'
                })
                
        else:  # WhatsApp
            from utils import gerar_link_whatsapp
            whatsapp_url = gerar_link_whatsapp(codigo_unico, nome, email)
            return jsonify({
                'success': True,
                'redirect': whatsapp_url,
                'message': 'Inscrição realizada! Complete o pagamento via WhatsApp.'
            })
            
    except Exception as e:
        print(f"Erro geral na inscrição: {e}")
        return jsonify({'success': False, 'message': f'Erro interno: {str(e)}'})

# Webhook do Mercado Pago
@app.route('/webhook/mercadopago', methods=['POST'])
def webhook_mercadopago():
    try:
        data = request.get_json()
        
        if data.get('type') == 'payment':
            payment_id = data.get('data', {}).get('id')
            
            if payment_id:
                import mercadopago
                sdk = mercadopago.SDK(app.config.get('MERCADOPAGO_ACCESS_TOKEN', ''))
                
                payment_response = sdk.payment().get(payment_id)
                payment = payment_response["response"]
                
                if payment.get('status') == 'approved':
                    external_reference = payment.get('external_reference')
                    
                    # Atualizar status no banco
                    conn = sqlite3.connect('database/eventos.db')
                    cursor = conn.cursor()
                    cursor.execute('''
                        UPDATE participantes 
                        SET status_pagamento = 'confirmado' 
                        WHERE codigo_unico = ?
                    ''', (external_reference,))
                    conn.commit()
                    conn.close()
        
        return jsonify({'status': 'ok'})
        
    except Exception as e:
        print(f"Erro no webhook: {e}")
        return jsonify({'status': 'error'}), 500

@app.route('/confirmacao/<codigo>')
def confirmacao(codigo):
    conn = sqlite3.connect('database/eventos.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT nome, email, tem_brinde, data_inscricao 
        FROM participantes 
        WHERE codigo_unico = ?
    ''', (codigo,))
    
    participante = cursor.fetchone()
    conn.close()
    
    if not participante:
        flash('Código não encontrado!', 'error')
        return redirect(url_for('index'))
    
    dados = {
        'nome': participante[0],
        'email': participante[1],
        'tem_brinde': participante[2],
        'data_inscricao': participante[3],
        'codigo': codigo
    }
    
    return render_template('confirmacao.html', dados=dados)

@app.route('/admin')
def admin():
    conn = sqlite3.connect('database/eventos.db')
    cursor = conn.cursor()
    
    # Estatísticas
    cursor.execute('SELECT COUNT(*) FROM participantes')
    total_inscritos = cursor.fetchone()[0]
    
    cursor.execute('SELECT COUNT(*) FROM participantes WHERE tem_brinde = TRUE')
    com_brinde = cursor.fetchone()[0]
    
    cursor.execute('SELECT * FROM participantes ORDER BY data_inscricao DESC')
    participantes = cursor.fetchall()
    
    conn.close()
    
    stats = {
        'total_inscritos': total_inscritos,
        'vagas_restantes': 150 - total_inscritos,
        'com_brinde': com_brinde,
        'sem_brinde': total_inscritos - com_brinde
    }
    
    return render_template('admin.html', stats=stats, participantes=participantes)

@app.route('/api/stats')
def api_stats():
    conn = sqlite3.connect('database/eventos.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT COUNT(*) FROM participantes')
    total = cursor.fetchone()[0]
    
    cursor.execute('SELECT COUNT(*) FROM participantes WHERE tem_brinde = TRUE')
    com_brinde = cursor.fetchone()[0]
    
    conn.close()
    
    return jsonify({
        'total_inscritos': total,
        'vagas_restantes': 150 - total,
        'brindes_restantes': 15 - com_brinde
    })

if __name__ == '__main__':
    # Criar pastas necessárias
    os.makedirs('database', exist_ok=True)
    os.makedirs('static/qrcodes', exist_ok=True)
    
    # Inicializar banco
    init_db()
    
    # Rodar aplicação
    app.run(debug=True, host='0.0.0.0', port=5000)