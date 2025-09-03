# 🎨 Guia Prático de Personalização - Florescer Cultural

## 📝 Como Alterar Textos e Conteúdo

### 1. Textos da Página Principal

**Arquivo:** `templates/index.html`

#### Título Principal
```html
<!-- Linha ~15 -->
<h1 class="main-title font-cinzel">FLORESCER</h1>
<h2 class="main-subtitle font-cinzel">CULTURAL</h2>
```

#### Slogan
```html
<!-- Linha ~25 -->
<p class="hero-slogan font-playfair animate-fade-in">
    "Onde a música encontra a primavera"
</p>
```

#### Mestre de Cerimônia
```html
<!-- Linha ~70 -->
<h3 class="mc-title font-playfair">Mestre de Cerimônia</h3>
<p class="mc-name font-cinzel">NACHI</p>
```

#### Informações do Evento
```html
<!-- Linha ~35-65 -->
<div class="info-text">
    <strong>20/09/2025</strong>  <!-- Data -->
    <span>Equinócio da Primavera</span>  <!-- Descrição -->
</div>
```

#### Textos das Seções
```html
<!-- Seção Sobre - Linha ~95 -->
<h2 class="section-title font-playfair">Celebrando a Primavera</h2>
<p class="section-description">
    O Florescer Cultural é mais que um evento...
</p>

<!-- Cards de Informação - Linha ~105 -->
<h3 class="card-title">Música & Conexão</h3>
<p class="card-text">
    Reunimos amigos através da música...
</p>
```

### 2. Line-up de Artistas

**Arquivo:** `templates/index.html` (Linha ~165)

```html
<div class="artist-card gradient-spring">
    <h3 class="artist-name">TRIO PRIMAVERA</h3>  <!-- Nome do Artista -->
    <p class="artist-description">
        Abertura especial celebrando...  <!-- Descrição -->
    </p>
</div>
```

### 3. Informações do Modal

**Arquivo:** `templates/index.html` (Linha ~250)

```html
<div class="form-notes">
    <p><strong>Local:</strong> Será revelado após confirmação</p>
    <p><strong>Entrada:</strong> Código QR será enviado por email</p>
    <p><strong>Brinde:</strong> Apenas para os primeiros 15 inscritos</p>
</div>
```

### 4. Preços e Configurações

**Arquivo:** `config.py`

```python
# Capacidade do evento
EVENTO_CAPACIDADE = 150

# Quantidade de brindes especiais
BRINDES_LIMITADOS = 15

# Preço do ingresso
PRECO_INGRESSO = float(os.environ.get('PRECO_INGRESSO', '25.00'))

# Informações do evento
EVENTO_NOME = 'Florescer Cultural'
EVENTO_DATA = '20/09/2025'
EVENTO_HORARIO = '15:00 - 23:00'
```

## 🎨 Como Alterar Cores e Estilos

### 1. Paleta de Cores

**Arquivo:** `static/css/style.css` (Linha ~15)

```css
:root {
    --gold-light: #E1C16E;    /* Dourado claro */
    --gold-medium: #C7A44C;   /* Dourado médio */
    --gold-dark: #B8943A;     /* Dourado escuro */
    --black: #000000;         /* Preto absoluto */
    --white: #FFFFFF;         /* Branco */
}
```

**Para alterar:** Substitua os códigos hexadecimais pelas cores desejadas.

### 2. Fontes

**Arquivo:** `static/css/style.css` (Linha ~30)

```css
.font-cinzel {
    font-family: 'Cinzel Decorative', serif;  /* Títulos principais */
}

.font-playfair {
    font-family: 'Playfair Display', serif;   /* Subtítulos */
}

.font-montserrat {
    font-family: 'Montserrat', sans-serif;    /* Texto corrido */
}
```

### 3. Tamanhos de Fonte

```css
.main-title {
    font-size: clamp(3rem, 8vw, 6rem);  /* Título principal */
}

.section-title {
    font-size: clamp(2.5rem, 5vw, 4rem);  /* Títulos de seção */
}
```

## 📍 Informações Específicas do Local

### 1. Local do Evento

**Arquivo:** `templates/confirmacao.html` (Linha ~85)

```html
<div class="detail-content">
    <h4>Local Revelado!</h4>
    <p><strong>Ninho do Largo</strong><br>
    R. Desembargador Ermelino de Leão, 511<br>
    Matriz, Curitiba</p>
</div>
```

### 2. WhatsApp para Contato

**Arquivo:** `.env`

```env
WHATSAPP_NUMERO=5541999999999  # Substitua pelo seu número
```

**Arquivo:** `config.py`

```python
WHATSAPP_NUMERO = os.environ.get('WHATSAPP_NUMERO') or '5541999999999'
```

## 📊 Capacidade e Limites

### 1. Alterar Capacidade Total

**Arquivo:** `config.py`

```python
EVENTO_CAPACIDADE = 150  # Mude para a capacidade desejada
```

### 2. Alterar Quantidade de Brindes

**Arquivo:** `config.py`

```python
BRINDES_LIMITADOS = 15  # Mude para a quantidade desejada
```

### 3. Alterar Preço

**Arquivo:** `.env`

```env
PRECO_INGRESSO=25.00  # Substitua pelo preço desejado
```

## 🎵 Line-up e Horários

### 1. Adicionar/Remover Artistas

**Arquivo:** `templates/index.html` (Linha ~165)

```html
<!-- Para adicionar um novo artista, copie este bloco: -->
<div class="lineup-item animate-on-scroll" data-time="21:00">
    <div class="time-marker">
        <span class="time">21:00 - 23:00</span>  <!-- Horário -->
    </div>
    <div class="artist-card gradient-finale">
        <h3 class="artist-name">NOME DO ARTISTA</h3>  <!-- Nome -->
        <p class="artist-description">
            Descrição da performance...  <!-- Descrição -->
        </p>
        <div class="music-note">🎤</div>  <!-- Ícone -->
    </div>
</div>
```

### 2. Estilos de Gradiente para Artistas

**Arquivo:** `static/css/style.css` (Linha ~650)

```css
.gradient-spring {   /* Verde primavera */
    background: linear-gradient(135deg, rgba(34, 139, 34, 0.2), rgba(199, 164, 76, 0.2));
}

.gradient-sunset {   /* Laranja pôr do sol */
    background: linear-gradient(135deg, rgba(255, 140, 0, 0.2), rgba(199, 164, 76, 0.2));
}

.gradient-night {    /* Roxo noturno */
    background: linear-gradient(135deg, rgba(75, 0, 130, 0.2), rgba(199, 164, 76, 0.2));
}

.gradient-finale {   /* Vermelho final */
    background: linear-gradient(135deg, rgba(220, 20, 60, 0.2), rgba(199, 164, 76, 0.2));
}
```

## 📱 Configurações de Pagamento

### 1. Mercado Pago

**Arquivo:** `.env`

```env
MERCADOPAGO_ACCESS_TOKEN=seu_token_aqui
MERCADOPAGO_PUBLIC_KEY=sua_chave_publica_aqui
```

### 2. Mensagem do WhatsApp

**Arquivo:** `config.py`

```python
MENSAGEM_WHATSAPP = """
🌸 *Florescer Cultural - 20/09/2025*

Olá! Gostaria de finalizar minha inscrição no evento.

*Dados da inscrição:*
• Código: {codigo}
• Nome: {nome}
• Email: {email}

*Valor:* R$ {preco}

Aguardo instruções para pagamento! 🎵
""".strip()
```

## 🎨 Personalização Visual Avançada

### 1. Animações

**Para desabilitar animações:**

**Arquivo:** `static/css/style.css`

```css
/* Adicione no final do arquivo */
.animate-fade-in,
.animate-on-scroll {
    animation: none !important;
    opacity: 1 !important;
    transform: none !important;
}
```

### 2. Bordas e Sombras

```css
.info-card, .about-card {
    border-radius: 12px;        /* Arredondar cantos */
    box-shadow: 0 4px 20px rgba(199, 164, 76, 0.2);  /* Sombra */
}
```

### 3. Espaçamentos

```css
.hero-section {
    padding: 100px 20px;  /* Espaçamento interno */
}

.about-section {
    padding: 100px 0;     /* Espaçamento entre seções */
}
```

## 🔧 Utilitários Rápidos

### 1. Ocultar Seções

```css
/* Para ocultar uma seção específica */
.lineup-section {
    display: none;
}
```

### 2. Alterar Ordem das Seções

**Arquivo:** `templates/index.html`

Mova os blocos `<section>` para reordenar as seções.

### 3. Adicionar Nova Seção

```html
<!-- Copie este template: -->
<section class="nova-secao">
    <div class="container">
        <h2 class="section-title font-playfair">Título da Nova Seção</h2>
        <p class="section-description">
            Descrição da nova seção...
        </p>
    </div>
</section>
```

## ⚡ Comandos Úteis

### 1. Aplicar Mudanças

```bash
# Após alterar qualquer arquivo:
# Salve o arquivo e recarregue a página (F5)
# Ou reinicie o servidor:
python run.py
```

### 2. Limpar Cache

```bash
# Se as mudanças não aparecem:
# Pressione Ctrl+F5 (Windows) ou Cmd+Shift+R (Mac)
```

### 3. Ver Erros

```bash
# Abra o console do navegador (F12)
# Aba "Console" para ver erros JavaScript
# Aba "Network" para ver erros de carregamento
```

## 📋 Checklist de Personalização

- [ ] Alterar nome do evento
- [ ] Alterar data e horários
- [ ] Configurar line-up de artistas
- [ ] Ajustar capacidade e brindes
- [ ] Configurar preços
- [ ] Personalizar cores (se necessário)
- [ ] Configurar WhatsApp
- [ ] Configurar Mercado Pago
- [ ] Testar formulário de inscrição
- [ ] Verificar responsividade mobile

---

**💡 Dica:** Sempre faça backup dos arquivos antes de grandes alterações!

**🆘 Problema?** Verifique o console do navegador (F12) para mensagens de erro.