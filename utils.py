import secrets
import string
import qrcode
from PIL import Image, ImageDraw, ImageFont
import os
from config import Config

def gerar_codigo_unico():
    """Gera um código único de 8 caracteres alfanumérico"""
    chars = string.ascii_uppercase + string.digits
    codigo = ''.join(secrets.choice(chars) for _ in range(8))
    return f"FC{codigo}"

def criar_qr_code(codigo, nome_participante):
    """Cria QR code personalizado para o participante"""
    try:
        # Dados para o QR code
        dados_qr = f"FLORESCER_CULTURAL|{codigo}|{nome_participante}|20/09/2025"
        
        # Configurar QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=10,
            border=4,
        )
        
        qr.add_data(dados_qr)
        qr.make(fit=True)
        
        # Criar imagem do QR code com cores personalizadas
        img = qr.make_image(fill_color='#C7A44C', back_color='#000000')
        
        # Converter para RGB se necessário
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        # Criar uma imagem maior com informações adicionais
        width, height = img.size
        nova_altura = height + 100
        nova_img = Image.new('RGB', (width, nova_altura), '#000000')
        
        # Colar o QR code na nova imagem
        nova_img.paste(img, (0, 0))
        
        # Tentar adicionar texto (se a fonte não existir, pula essa parte)
        try:
            draw = ImageDraw.Draw(nova_img)
            # Fonte padrão se não encontrar fontes personalizadas
            font_size = 20
            try:
                font = ImageFont.truetype("arial.ttf", font_size)
            except:
                font = ImageFont.load_default()
            
            # Adicionar código
            text = f"Código: {codigo}"
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
            x = (width - text_width) // 2
            y = height + 10
            draw.text((x, y), text, fill='#C7A44C', font=font)
            
            # Adicionar nome do evento
            text2 = "FLORESCER CULTURAL"
            bbox2 = draw.textbbox((0, 0), text2, font=font)
            text_width2 = bbox2[2] - bbox2[0]
            x2 = (width - text_width2) // 2
            y2 = height + 40
            draw.text((x2, y2), text2, fill='#E1C16E', font=font)
            
            # Adicionar data
            text3 = "20/09/2025"
            bbox3 = draw.textbbox((0, 0), text3, font=font)
            text_width3 = bbox3[2] - bbox3[0]
            x3 = (width - text_width3) // 2
            y3 = height + 70
            draw.text((x3, y3), text3, fill='#C7A44C', font=font)
            
        except Exception as e:
            print(f"Erro ao adicionar texto ao QR code: {e}")
        
        # Salvar QR code
        caminho = f"static/qrcodes/{codigo}.png"
        nova_img.save(caminho)
        
        return caminho
        
    except Exception as e:
        print(f"Erro ao criar QR code: {e}")
        return None

def validar_pagamento(codigo_participante, metodo):
    """Valida o pagamento (placeholder para integração real)"""
    # Aqui você implementaria a validação real com Mercado Pago
    # Por enquanto, retorna True para simulação
    return True

def formatar_telefone(telefone):
    """Formata número de telefone para WhatsApp"""
    # Remove caracteres especiais
    apenas_numeros = ''.join(filter(str.isdigit, telefone))
    
    # Adiciona código do país se não tiver
    if len(apenas_numeros) == 11 and not apenas_numeros.startswith('55'):
        return f"55{apenas_numeros}"
    elif len(apenas_numeros) == 10 and not apenas_numeros.startswith('55'):
        return f"5541{apenas_numeros}"
    
    return apenas_numeros

def gerar_link_whatsapp(codigo, nome, email, preco="25.00"):
    """Gera link do WhatsApp com mensagem pré-formatada"""
    mensagem = f"""🌸 *FLORESCER CULTURAL - 20/09/2025*

Olá! Finalizando minha inscrição no evento:

👤 *Nome:* {nome}
📧 *Email:* {email}
🎫 *Código:* {codigo}
💰 *Valor:* R$ {preco}

Aguardo instruções para pagamento via PIX! 

Obrigado! 🎵"""
    
    # Codificar mensagem para URL
    import urllib.parse
    mensagem_encoded = urllib.parse.quote(mensagem)
    
    return f"https://wa.me/{Config.WHATSAPP_NUMERO}?text={mensagem_encoded}"

def verificar_vagas_disponiveis():
    """Verifica quantas vagas ainda estão disponíveis"""
    import sqlite3
    
    conn = sqlite3.connect('database/eventos.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT COUNT(*) FROM participantes')
    total_inscritos = cursor.fetchone()[0]
    
    conn.close()
    
    vagas_restantes = Config.EVENTO_CAPACIDADE - total_inscritos
    return max(0, vagas_restantes)

def verificar_brindes_disponiveis():
    """Verifica quantos brindes ainda estão disponíveis"""
    import sqlite3
    
    conn = sqlite3.connect('database/eventos.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT COUNT(*) FROM participantes WHERE tem_brinde = TRUE')
    brindes_dados = cursor.fetchone()[0]
    
    conn.close()
    
    brindes_restantes = Config.BRINDES_LIMITADOS - brindes_dados
    return max(0, brindes_restantes)