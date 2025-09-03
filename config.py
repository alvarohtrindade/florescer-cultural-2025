import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'florescer-cultural-2025-dev-key'
    
    # Configurações do evento
    EVENTO_NOME = 'Florescer Cultural'
    EVENTO_DATA = '21/09/2025'
    EVENTO_HORARIO = '13:00 - 20:00'
    EVENTO_LOCAL_NOME = 'Ninho do Largo'
    EVENTO_LOCAL_ENDERECO = 'R. Desembargador Ermelino de Leão, 511, Matriz, Curitiba - PR'
    EVENTO_LOCAL_INSTAGRAM = '@ninhodolargo'
    EVENTO_CAPACIDADE = 100
    BRINDES_LIMITADOS = 15
    
    # Configurações do Sympla
    SYMPLA_EVENT_ID = os.environ.get('SYMPLA_EVENT_ID', '3085364')
    SYMPLA_EMBED_URL = f"https://www.sympla.com.br/evento/florescer-cultural---curitiba/{SYMPLA_EVENT_ID}/embed"
    SYMPLA_DIRECT_URL = f"https://www.sympla.com.br/evento/florescer-cultural---curitiba/{SYMPLA_EVENT_ID}"
    
    # Configurações antigas (mantidas para compatibilidade)
    MERCADOPAGO_ACCESS_TOKEN = os.environ.get('MERCADOPAGO_ACCESS_TOKEN')
    MERCADOPAGO_PUBLIC_KEY = os.environ.get('MERCADOPAGO_PUBLIC_KEY')
    WHATSAPP_NUMERO = os.environ.get('WHATSAPP_NUMERO') or '5541999999999'
    
    # Configurações de preço (agora gerenciadas pelo Sympla)
    PRECO_INGRESSO = float(os.environ.get('PRECO_INGRESSO', '25.00'))
    
    # URLs
    BASE_URL = os.environ.get('BASE_URL') or 'http://localhost:5000'
    
    # Nova configuração para o tipo de venda
    VENDA_TIPO = os.environ.get('VENDA_TIPO', 'sympla')  # 'sympla' ou 'interno'
    
    # Configurações de Analytics (opcional)
    GOOGLE_ANALYTICS_ID = os.environ.get('GOOGLE_ANALYTICS_ID')
    FACEBOOK_PIXEL_ID = os.environ.get('FACEBOOK_PIXEL_ID')
    
    # Configurações do banco de dados
    DATABASE_URL = os.environ.get('DATABASE_URL') or 'sqlite:///database/eventos.db'
    
    # Configurações de email (opcional para notificações)
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', 587))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    
    # Configurações de desenvolvimento
    DEBUG = os.environ.get('FLASK_DEBUG', 'False').lower() in ['true', '1', 'on']
    TESTING = False
    
    # Informações dos artistas
    LINEUP = [
        {
            'nome': 'TRIO PRIMAVERA',
            'horario': '15:00 - 17:00',
            'descricao': 'Abertura especial celebrando a chegada da primavera com melodias envolventes',
            'icone': '🎼',
            'gradient': 'gradient-spring'
        },
        {
            'nome': 'ALVARO',
            'horario': '17:00 - 19:00',
            'descricao': 'Set único com energia contagiante e sonoridades autorais',
            'icone': '🎵',
            'gradient': 'gradient-sunset'
        },
        {
            'nome': 'MALAK',
            'horario': '19:00 - 21:00',
            'descricao': 'Performance envolvente com influências contemporâneas e experimentais',
            'gradient': 'gradient-night'
        },
        {
            'nome': 'RADIOTIVITY MANIFEST',
            'horario': '18:00 - 20:00',
            'descricao': 'Fechamento épico com sound manifest que promete ser inesquecível',
            'icone': '🎤',
            'gradient': 'gradient-finale'
        }
    ]
    
    # Valores da sustentabilidade
    VALORES_SUSTENTABILIDADE = [
        {
            'titulo': 'Arrecadação de Alimentos',
            'descricao': 'Contribuição para fortalecimento da comunidade',
            'icone': '🥫'
        },
        {
            'titulo': 'Reciclagem Consciente',
            'descricao': 'Práticas ambientais durante todo o evento',
            'icone': '♻️'
        },
        {
            'titulo': 'Arte & Cultura Local',
            'descricao': 'Valorização de artistas independentes',
            'icone': '🎨'
        }
    ]
    
    # Configurações de SEO
    SEO_TITLE = 'Florescer Cultural - Onde a música encontra a primavera'
    SEO_DESCRIPTION = 'Celebre a chegada da primavera com música, arte e consciência ambiental. Um evento único que une cultura, sustentabilidade e conexões humanas em Curitiba.'
    SEO_KEYWORDS = 'evento cultural, música, primavera, arte, sustentabilidade, Curitiba, consciência ambiental, artistas independentes'
    SEO_IMAGE = '/static/images/florescer-cultural-og.jpg'  # Imagem para redes sociais
    
    # Configurações de segurança
    SESSION_COOKIE_SECURE = os.environ.get('SESSION_COOKIE_SECURE', 'False').lower() in ['true', '1', 'on']
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    
    # Rate limiting (se necessário)
    RATELIMIT_STORAGE_URL = os.environ.get('REDIS_URL') or 'memory://'
    RATELIMIT_DEFAULT = "100 per hour"
    
    @staticmethod
    def get_sympla_config():
        """Retorna configurações do Sympla formatadas"""
        return {
            'event_id': Config.SYMPLA_EVENT_ID,
            'embed_url': Config.SYMPLA_EMBED_URL,
            'direct_url': Config.SYMPLA_DIRECT_URL,
            'enabled': bool(Config.SYMPLA_EVENT_ID)
        }
    
    @staticmethod
    def get_event_info():
        """Retorna informações completas do evento"""
        return {
            'nome': Config.EVENTO_NOME,
            'data': Config.EVENTO_DATA,
            'horario': Config.EVENTO_HORARIO,
            'local': {
                'nome': Config.EVENTO_LOCAL_NOME,
                'endereco': Config.EVENTO_LOCAL_ENDERECO,
                'instagram': Config.EVENTO_LOCAL_INSTAGRAM
            },
            'capacidade': Config.EVENTO_CAPACIDADE,
            'brindes_limitados': Config.BRINDES_LIMITADOS,
            'preco': Config.PRECO_INGRESSO,
            'lineup': Config.LINEUP,
            'valores': Config.VALORES_SUSTENTABILIDADE
        }
    
    @staticmethod
    def get_seo_meta():
        """Retorna meta tags para SEO"""
        return {
            'title': Config.SEO_TITLE,
            'description': Config.SEO_DESCRIPTION,
            'keywords': Config.SEO_KEYWORDS,
            'image': Config.SEO_IMAGE,
            'url': Config.BASE_URL
        }


class DevelopmentConfig(Config):
    """Configuração para desenvolvimento"""
    DEBUG = True
    TESTING = False


class ProductionConfig(Config):
    """Configuração para produção"""
    DEBUG = False
    TESTING = False
    SESSION_COOKIE_SECURE = True
    
    # Configurações de logging para produção
    LOG_LEVEL = 'INFO'
    LOG_FILE = 'logs/florescer-cultural.log'


class TestingConfig(Config):
    """Configuração para testes"""
    TESTING = True
    DATABASE_URL = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False


# Mapeamento de configurações por ambiente
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}