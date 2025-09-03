#!/usr/bin/env python3
"""
Script para executar o Florescer Cultural
Este arquivo facilita a execução da aplicação
"""

import os
import sys
import subprocess
from pathlib import Path

def verificar_ambiente():
    """Verifica se o ambiente está configurado corretamente"""
    print("🔍 Verificando ambiente...")
    
    # Verificar se está no diretório correto
    if not os.path.exists('app.py'):
        print("❌ Arquivo app.py não encontrado!")
        print("💡 Execute este script na pasta raiz do projeto")
        return False
    
    # Verificar se o banco existe
    if not os.path.exists('database/eventos.db'):
        print("⚠️  Banco de dados não encontrado!")
        resposta = input("🛠️  Deseja criar o banco de dados agora? (s/N): ").lower()
        if resposta == 's':
            import init_database
            init_database.criar_banco_dados()
            init_database.inserir_dados_teste()
        else:
            print("❌ Banco de dados é necessário para executar a aplicação")
            return False
    
    # Verificar dependências
    try:
        import flask
        import qrcode
        import sqlite3
        print("✅ Dependências encontradas")
    except ImportError as e:
        print(f"❌ Dependência faltando: {e}")
        print("💡 Execute: pip install -r requirements.txt")
        return False
    
    # Verificar estrutura de pastas
    pastas_necessarias = ['static/css', 'static/js', 'static/images', 'static/qrcodes', 'templates', 'database']
    for pasta in pastas_necessarias:
        if not os.path.exists(pasta):
            print(f"📁 Criando pasta: {pasta}")
            os.makedirs(pasta, exist_ok=True)
    
    return True

def verificar_arquivo_env():
    """Verifica se o arquivo .env existe e tem as configurações necessárias"""
    if not os.path.exists('.env'):
        print("⚠️  Arquivo .env não encontrado!")
        resposta = input("🛠️  Deseja criar um arquivo .env básico? (s/N): ").lower()
        if resposta == 's':
            criar_env_basico()
        else:
            print("💡 Crie um arquivo .env com as configurações necessárias")
    else:
        print("✅ Arquivo .env encontrado")

def criar_env_basico():
    """Cria um arquivo .env básico"""
    env_content = """# Configurações do Florescer Cultural
SECRET_KEY=florescer-cultural-2025-super-secret-key-change-this

# Configurações do Mercado Pago (substitua pelos seus valores)
MERCADOPAGO_ACCESS_TOKEN=seu_access_token_aqui
MERCADOPAGO_PUBLIC_KEY=sua_public_key_aqui

# WhatsApp para contato (apenas números)
WHATSAPP_NUMERO=5541999999999

# Preço do ingresso
PRECO_INGRESSO=25.00

# URL base
BASE_URL=http://localhost:5000

# Ambiente
FLASK_ENV=development
FLASK_DEBUG=True
"""
    
    with open('.env', 'w', encoding='utf-8') as f:
        f.write(env_content)
    
    print("✅ Arquivo .env criado!")
    print("⚠️  IMPORTANTE: Edite o arquivo .env com suas configurações reais")

def mostrar_info_startup():
    """Mostra informações importantes na inicialização"""
    print("\n" + "="*60)
    print("🌸 FLORESCER CULTURAL - SERVIDOR INICIADO")
    print("="*60)
    print("🌐 Acesse: http://localhost:5000")
    print("👨‍💼 Admin: http://localhost:5000/admin")
    print("📊 Stats: http://localhost:5000/api/stats")
    print("="*60)
    print("💡 DICAS:")
    print("   • Pressione Ctrl+C para parar o servidor")
    print("   • Edite o arquivo .env para configurações")
    print("   • Execute init_database.py para resetar o banco")
    print("="*60)
    print("🎯 FUNCIONALIDADES:")
    print("   ✅ Landing page responsiva")
    print("   ✅ Sistema de inscrições")
    print("   ✅ Geração de QR codes")
    print("   ✅ Painel administrativo")
    print("   ✅ Integração WhatsApp")
    print("   ✅ Códigos únicos limitados")
    print("="*60 + "\n")

def executar_app():
    """Executa a aplicação Flask"""
    try:
        # Importar e executar
        from app import app
        
        # Mostrar informações
        mostrar_info_startup()
        
        # Executar servidor
        app.run(
            host='0.0.0.0',
            port=5000,
            debug=True,
            use_reloader=True
        )
        
    except KeyboardInterrupt:
        print("\n\n🛑 Servidor interrompido pelo usuário")
        print("👋 Obrigado por usar o Florescer Cultural!")
    except Exception as e:
        print(f"\n❌ Erro ao executar aplicação: {e}")
        print("🔧 Verifique as configurações e dependências")

def main():
    """Função principal"""
    print("🌸 Florescer Cultural - Inicializador")
    print("💻 Preparando ambiente para execução...\n")
    
    # Verificações
    if not verificar_ambiente():
        print("\n❌ Falha na verificação do ambiente")
        input("Pressione Enter para sair...")
        sys.exit(1)
    
    verificar_arquivo_env()
    
    print("\n✅ Ambiente verificado com sucesso!")
    print("🚀 Iniciando aplicação...\n")
    
    # Executar
    executar_app()

if __name__ == "__main__":
    main()