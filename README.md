# 🌸 Florescer Cultural

Uma landing page elegante para eventos culturais com sistema completo de inscrições, códigos únicos e painel administrativo.

## ✨ Características

- 🎨 **Design Elegante**: Baseado no guia de marca (preto e dourado)
- 📱 **Responsivo**: Funciona perfeitamente em mobile e desktop
- 🎫 **Sistema de Inscrições**: Com códigos QR únicos
- 🎁 **Brindes Limitados**: Primeiros 15 inscritos ganham brinde especial
- 💰 **Pagamentos**: Mercado Pago e WhatsApp/PIX
- 👨‍💼 **Painel Admin**: Controle completo dos participantes
- 🌱 **Sustentável**: Foco em consciência ambiental

## 🚀 Instalação Rápida

### 1. Clonar/Baixar o projeto
```bash
# Se você tem git instalado
git clone [url-do-projeto]
cd florescer-cultural

# Ou baixe e extraia o ZIP
```

### 2. Instalar Python (se não tiver)
- Baixe em: https://python.org
- Versão recomendada: 3.8 ou superior

### 3. Instalar dependências
```bash
# No terminal/prompt, dentro da pasta do projeto:
pip install -r requirements.txt
```

### 4. Inicializar banco de dados
```bash
python init_database.py
```

### 5. Executar aplicação
```bash
python run.py
```

## 📋 Estrutura do Projeto

```
florescer-cultural/
├── app.py                 # Aplicação principal Flask
├── config.py             # Configurações
├── utils.py              # Funções auxiliares
├── init_database.py      # Script de inicialização do banco
├── run.py                # Script para executar facilmente
├── requirements.txt      # Dependências Python
├── .env                  # Configurações (criado automaticamente)
├── static/
│   ├── css/
│   │   └── style.css     # Estilos principais
│   ├── js/
│   │   └── main.js       # JavaScript principal
│   ├── images/           # Imagens do site
│   └── qrcodes/          # QR codes gerados
├── templates/
│   ├── base.html         # Template base
│   ├── index.html        # Página principal
│   ├── confirmacao.html  # Página de confirmação
│   └── admin.html        # Painel administrativo
└── database/
    └── eventos.db        # Banco SQLite (criado automaticamente)
```

## 🌐 Páginas Disponíveis

- **`/`** - Landing page principal
- **`/admin`** - Painel administrativo
- **`/confirmacao/[codigo]`** - Página de confirmação com QR code
- **`/api/stats`** - API com estatísticas em tempo real

## ⚙️ Configuração

### Arquivo .env

O arquivo `.env` é criado automaticamente, mas você deve editá-lo:

```env
# Chave secreta (mude em produção)
SECRET_KEY=sua-chave-super-secreta

# Mercado Pago (obtenha em: https://mercadopago.com.br/developers)
MERCADOPAGO_ACCESS_TOKEN=seu_access_token_aqui
MERCADOPAGO_PUBLIC_KEY=sua_public_key_aqui

# WhatsApp (apenas números, com código do país)
WHATSAPP_NUMERO=5541999999999

# Preço do ingresso
PRECO_INGRESSO=25.00

# URL base (para produção, use sua URL real)
BASE_URL=http://localhost:5000
```

### Personalização

#### Alterar informações do evento:
1. Edite `config.py` para dados básicos
2. Edite `templates/index.html` para conteúdo
3. Edite `static/css/style.css` para cores e estilos

#### Alterar capacidade e brindes:
```python
# Em config.py
EVENTO_CAPACIDADE = 150  # Número máximo de participantes
BRINDES_LIMITADOS = 15   # Primeiros X ganham brinde
```

## 🛠️ Funcionalidades Principais

### Sistema de Inscrições
- ✅ Formulário com validação
- ✅ Códigos únicos gerados automaticamente
- ✅ QR codes personalizados
- ✅ Controle de capacidade
- ✅ Brindes especiais limitados

### Métodos de Pagamento
- **Mercado Pago**: Cartão, PIX, débito
- **WhatsApp**: PIX manual via WhatsApp

### Painel Administrativo
- 📊 Estatísticas em tempo real
- 👥 Lista completa de participantes
- 🔍 Busca e filtros
- 📱 Visualização de QR codes
- 📊 Exportação para CSV
- 💬 Integração WhatsApp
- 🖨️ Impressão de listas

### Recursos Especiais
- 🎁 **Códigos Únicos**: Sistema de brindes limitados
- 📍 **Local Secreto**: Revelado após inscrição
- ♻️ **Sustentabilidade**: Foco ambiental
- 🌸 **Animações**: Elementos florais animados
- 📱 **PWA Ready**: Pode ser instalado como app

## 🎨 Personalização Visual

### Cores do Tema
```css
:root {
    --gold-light: #E1C16E;    /* Dourado claro */
    --gold-medium: #C7A44C;   /* Dourado médio */
    --gold-dark: #B8943A;     /* Dourado escuro */
    --black: #000000;         /* Preto absoluto */
    --white: #FFFFFF;         /* Branco */
}
```

### Fontes Utilizadas
- **Cinzel Decorative**: Títulos principais
- **Playfair Display**: Subtítulos elegantes
- **Montserrat**: Texto corrido

### Modificar Layout
1. **Hero Section**: Edite `templates/index.html` (linha ~10)
2. **Cores**: Modifique `static/css/style.css` (variáveis CSS)
3. **Logo**: Substitua elementos em `templates/index.html`

## 🌐 Deploy/Hospedagem

### Opções Gratuitas

#### 1. Railway (Recomendado)
```bash
# 1. Crie conta em railway.app
# 2. Conecte seu repositório GitHub
# 3. Deploy automático!
```

#### 2. Render
```bash
# 1. Crie conta em render.com
# 2. Conecte repositório
# 3. Configure:
#    - Build Command: pip install -r requirements.txt
#    - Start Command: python app.py
```

#### 3. PythonAnywhere
```bash
# 1. Crie conta gratuita
# 2. Upload dos arquivos
# 3. Configure web app Flask
```

### Configuração para Produção

#### 1. Editar .env
```env
SECRET_KEY=chave-super-secreta-complexa
BASE_URL=https://seudominio.com
FLASK_ENV=production
FLASK_DEBUG=False
```

#### 2. Configurar Mercado Pago
1. Acesse: https://mercadopago.com.br/developers
2. Crie aplicação
3. Copie credenciais para `.env`

#### 3. Configurar Domínio (Opcional)
- Registre domínio personalizado
- Configure DNS para apontar para seu deploy

## 📊 API Endpoints

### GET /api/stats
Retorna estatísticas do evento:
```json
{
    "total_inscritos": 25,
    "vagas_restantes": 125,
    "brindes_restantes": 10
}
```

### POST /inscrever
Processa nova inscrição:
```json
{
    "nome": "Nome Completo",
    "email": "email@exemplo.com",
    "telefone": "(41) 99999-9999",
    "metodo_pagamento": "mercadopago"
}
```

## 🔧 Troubleshooting

### Problemas Comuns

#### 1. "Módulo não encontrado"
```bash
# Certifique-se de que instalou as dependências
pip install -r requirements.txt
```

#### 2. "Banco de dados não encontrado"
```bash
# Execute o script de inicialização
python init_database.py
```

#### 3. "Erro de porta já em uso"
```bash
# Mude a porta em app.py (linha final)
app.run(port=5001)  # ou outra porta
```

#### 4. QR codes não aparecem
- Verifique se a pasta `static/qrcodes/` existe
- Verifique permissões de escrita
- Execute: `mkdir -p static/qrcodes`

#### 5. Estilos não carregam
- Verifique se `static/css/style.css` existe
- Limpe cache do navegador (Ctrl+F5)
- Verifique console do navegador (F12)

### Logs e Debug

#### Ver logs da aplicação:
```bash
# Execute com debug ativo
FLASK_DEBUG=True python app.py
```

#### Verificar banco de dados:
```bash
# Execute o verificador
python init_database.py
# Escolha apenas verificar (não inserir dados teste)
```

## 📱 Recursos Mobile

### PWA (Progressive Web App)
O site pode ser instalado como app no celular:
1. Abra no Chrome mobile
2. Menu → "Adicionar à tela inicial"
3. Use como app nativo!

### Otimizações Mobile
- ✅ Design totalmente responsivo
- ✅ Touch-friendly (botões grandes)
- ✅ Scroll suave
- ✅ Imagens otimizadas
- ✅ Formulários mobile-first

## 🎯 Funcionalidades Avançadas

### Easter Eggs
- **Konami Code**: Sequência especial de teclas para efeito visual
- **Sparkles**: Clique nos botões principais para efeito de partículas
- **Animações**: Elementos flutuantes e transições suaves

### Analytics (Opcional)
Para adicionar Google Analytics:
1. Edite `templates/base.html`
2. Adicione código de tracking antes do `</head>`

### SEO
- ✅ Meta tags configuradas
- ✅ Open Graph para redes sociais
- ✅ URLs amigáveis
- ✅ Sitemap automático

## 🤝 Contribuição

### Como Contribuir
1. Fork o projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

### Roadmap
- [ ] Integração com Instagram
- [ ] Sistema de check-in por QR code
- [ ] Dashboard com gráficos
- [ ] Notificações push
- [ ] Sistema de avaliação pós-evento

## 📄 Licença

Este projeto foi desenvolvido especificamente para o **Florescer Cultural 2025**.

### Uso Permitido
- ✅ Modificar para outros eventos
- ✅ Estudar o código
- ✅ Melhorias e correções

### Créditos
- **Design**: Baseado no guia de marca Florescer Cultural
- **Desenvolvimento**: Sistema personalizado em Flask
- **Tipografia**: Google Fonts (Cinzel, Playfair Display, Montserrat)

## 📞 Suporte

### Precisa de Ajuda?

1. **Documentação**: Leia este README completamente
2. **Issues**: Verifique problemas conhecidos
3. **Discord/Telegram**: Grupo de suporte (se disponível)
4. **Email**: Contato direto com desenvolvedores

### Informações do Sistema
- **Versão**: 1.0.0
- **Python**: 3.8+
- **Flask**: 2.3+
- **Banco**: SQLite3
- **Frontend**: HTML5, CSS3, JavaScript ES6

---

## 🌸 Sobre o Florescer Cultural

O **Florescer Cultural** é mais que um evento - é uma experiência que une música, arte e consciência ambiental para celebrar a chegada da primavera de forma única e transformadora.

### Data e Local
- 📅 **Data**: 20 de Setembro de 2025
- 🕐 **Horário**: 15:00 às 23:00
- 📍 **Local**: Ninho do Largo, Curitiba
- 👥 **Capacidade**: 150 pessoas

### Objetivo
Celebrar a primavera reunindo amigos através da música e arte, com ações práticas de sustentabilidade e valorização de artistas independentes.

---

**Desenvolvido com 🌸 para celebrar a primavera**

*© 2025 Florescer Cultural. Todos os direitos reservados.*