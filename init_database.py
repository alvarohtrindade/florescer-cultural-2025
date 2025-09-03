#!/usr/bin/env python3
"""
Script para inicializar o banco de dados do Florescer Cultural
Execute este arquivo para criar as tabelas necessárias
"""

import sqlite3
import os
from datetime import datetime

def criar_banco_dados():
    """Cria o banco de dados e as tabelas necessárias"""
    
    # Criar diretório se não existir
    os.makedirs('database', exist_ok=True)
    
    # Conectar ao banco
    conn = sqlite3.connect('database/eventos.db')
    cursor = conn.cursor()
    
    print("🗄️  Criando banco de dados...")
    
    # Criar tabela de participantes
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS participantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            telefone TEXT,
            codigo_unico TEXT UNIQUE NOT NULL,
            tem_brinde BOOLEAN DEFAULT FALSE,
            data_inscricao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            status_pagamento TEXT DEFAULT 'pendente',
            metodo_pagamento TEXT,
            observacoes TEXT
        )
    ''')
    
    # Criar tabela de códigos especiais (para controle adicional)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS codigos_especiais (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo TEXT UNIQUE NOT NULL,
            utilizado BOOLEAN DEFAULT FALSE,
            participante_id INTEGER,
            data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            data_utilizacao TIMESTAMP,
            FOREIGN KEY (participante_id) REFERENCES participantes (id)
        )
    ''')
    
    # Criar tabela de configurações do evento
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS configuracoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            chave TEXT UNIQUE NOT NULL,
            valor TEXT NOT NULL,
            descricao TEXT,
            data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Inserir configurações padrão
    configuracoes_padrao = [
        ('capacidade_maxima', '150', 'Capacidade máxima do evento'),
        ('brindes_limitados', '15', 'Quantidade de brindes especiais'),
        ('preco_ingresso', '25.00', 'Preço do ingresso em reais'),
        ('evento_ativo', 'true', 'Se o evento está aceitando inscrições'),
        ('data_evento', '2025-09-20', 'Data do evento'),
        ('horario_inicio', '15:00', 'Horário de início'),
        ('horario_fim', '23:00', 'Horário de término'),
        ('local_nome', 'Ninho do Largo', 'Nome do local'),
        ('local_endereco', 'R. Desembargador Ermelino de Leão, 511, Matriz', 'Endereço do local'),
        ('whatsapp_evento', '5541999999999', 'WhatsApp para contato'),
    ]
    
    for chave, valor, descricao in configuracoes_padrao:
        cursor.execute('''
            INSERT OR IGNORE INTO configuracoes (chave, valor, descricao)
            VALUES (?, ?, ?)
        ''', (chave, valor, descricao))
    
    # Criar tabela de logs para auditoria
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS logs_evento (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo TEXT NOT NULL,
            descricao TEXT NOT NULL,
            participante_id INTEGER,
            dados_adicionais TEXT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (participante_id) REFERENCES participantes (id)
        )
    ''')
    
    # Criar índices para melhor performance
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_participantes_email ON participantes(email)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_participantes_codigo ON participantes(codigo_unico)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_participantes_data ON participantes(data_inscricao)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_logs_tipo ON logs_evento(tipo)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_logs_timestamp ON logs_evento(timestamp)')
    
    # Commit e fechar
    conn.commit()
    conn.close()
    
    print("✅ Banco de dados criado com sucesso!")
    print("📊 Tabelas criadas:")
    print("   - participantes")
    print("   - codigos_especiais") 
    print("   - configuracoes")
    print("   - logs_evento")
    print("🔍 Índices criados para otimização")

def inserir_dados_teste():
    """Insere alguns dados de teste (opcional)"""
    
    resposta = input("\n🧪 Deseja inserir dados de teste? (s/N): ").lower()
    if resposta != 's':
        return
    
    conn = sqlite3.connect('database/eventos.db')
    cursor = conn.cursor()
    
    print("📝 Inserindo dados de teste...")
    
    # Dados de teste
    participantes_teste = [
        ('João Silva', 'joao@email.com', '(41) 99999-1111', 'FC12345678', True, 'mercadopago'),
        ('Maria Santos', 'maria@email.com', '(41) 99999-2222', 'FC87654321', True, 'whatsapp'),
        ('Pedro Costa', 'pedro@email.com', '(41) 99999-3333', 'FC11111111', False, 'mercadopago'),
        ('Ana Oliveira', 'ana@email.com', '(41) 99999-4444', 'FC22222222', False, 'whatsapp'),
        ('Carlos Ferreira', 'carlos@email.com', '(41) 99999-5555', 'FC33333333', True, 'mercadopago'),
    ]
    
    for nome, email, telefone, codigo, tem_brinde, metodo in participantes_teste:
        try:
            cursor.execute('''
                INSERT INTO participantes 
                (nome, email, telefone, codigo_unico, tem_brinde, metodo_pagamento, status_pagamento)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (nome, email, telefone, codigo, tem_brinde, metodo, 'confirmado'))
            
            # Log da inserção
            cursor.execute('''
                INSERT INTO logs_evento (tipo, descricao, dados_adicionais)
                VALUES (?, ?, ?)
            ''', ('inscricao_teste', f'Participante de teste inserido: {nome}', f'email: {email}'))
            
        except sqlite3.IntegrityError:
            print(f"⚠️  Participante {email} já existe, pulando...")
    
    conn.commit()
    conn.close()
    
    print("✅ Dados de teste inseridos!")

def verificar_banco():
    """Verifica se o banco foi criado corretamente"""
    
    if not os.path.exists('database/eventos.db'):
        print("❌ Banco de dados não encontrado!")
        return False
    
    conn = sqlite3.connect('database/eventos.db')
    cursor = conn.cursor()
    
    print("\n📊 Verificando estrutura do banco...")
    
    # Verificar tabelas
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tabelas = cursor.fetchall()
    
    print("📋 Tabelas encontradas:")
    for tabela in tabelas:
        cursor.execute(f"SELECT COUNT(*) FROM {tabela[0]}")
        count = cursor.fetchone()[0]
        print(f"   - {tabela[0]}: {count} registros")
    
    # Verificar configurações
    cursor.execute("SELECT chave, valor FROM configuracoes")
    configs = cursor.fetchall()
    
    print("\n⚙️  Configurações:")
    for chave, valor in configs:
        print(f"   - {chave}: {valor}")
    
    conn.close()
    return True

if __name__ == "__main__":
    print("🌸 Florescer Cultural - Inicialização do Banco de Dados")
    print("=" * 55)
    
    try:
        # Criar banco
        criar_banco_dados()
        
        # Opção de dados de teste
        inserir_dados_teste()
        
        # Verificar
        verificar_banco()
        
        print("\n✅ Inicialização concluída com sucesso!")
        print("🚀 Agora você pode executar: python app.py")
        
    except Exception as e:
        print(f"❌ Erro durante a inicialização: {e}")
        print("🔧 Verifique as permissões de escrita na pasta")