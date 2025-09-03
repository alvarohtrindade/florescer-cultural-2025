# 🎨 Guia de Personalização - Florescer Cultural 2025

## ✨ Visão Geral

A nova versão da landing page foi completamente redesenhada com base na paleta de cores do flyer oficial, implementando o conceito **"Primavera Celestial"** - uma fusão harmoniosa entre o azul do céu e as cores vibrantes das flores.

### 🎯 Principais Melhorias Implementadas

- **Identidade Visual Unificada**: Paleta baseada nas cores do flyer
- **Sistema Flexível de Lineup**: Arquivo JSON configurável
- **Performance Otimizada**: Lazy loading e animações eficientes
- **Acessibilidade Completa**: WCAG AA compliance
- **SEO Avançado**: Schema.org e Open Graph
- **Responsividade Superior**: Mobile-first design

## 🌈 Paleta de Cores (Baseada no Flyer)

### Cores Principais
```css
:root {
    /* Background Celestial */
    --sky-blue: #5c98fa;        /* Céu do flyer */
    --cloud-white: #edeeee;     /* Nuvens do flyer */
    
    /* Texto */
    --text-gold: #fbed41;       /* Dourado do flyer */
    --text-white: #ffffff;      /* Branco do flyer */
    
    /* Flores Vibrantes */
    --flower-pink-1: #fe74a5;   /* Rosa principal */
    --flower-pink-2: #b5005c;   /* Rosa escuro */
    --flower-pink-3: #c82050;   /* Rosa médio */
    --flower-coral: #fc898e;    /* Coral */
    --flower-yellow: #ffdc7a;   /* Amarelo claro */
    --flower-yellow-dark: #dfa40a; /* Amarelo escuro */
    --flower-green-1: #4c8d0e;  /* Verde escuro */
    --flower-green-2: #59af00;  /* Verde médio */
    --flower-green-3: #3fad43;  /* Verde claro */
}
```

### Como Personalizar Cores

Para alterar a paleta de cores, edite as variáveis CSS no arquivo `templates/index.html` na seção `<style>`:

```css
/* Exemplo: Mudança para tema roxo */
:root {
    --sky-blue: #6a5acd;        /* Novo fundo */
    --flower-pink-1: #9370db;   /* Novo destaque */
    /* ... outras variáveis */
}
```

## 🎵 Sistema de Lineup Configurável

### Arquivo JSON (data/lineup.json)

O lineup é agora controlado por um arquivo JSON, facilitando atualizações:

```json
[
  {
    "id": "artista_unico_id",
    "nome": "NOME DO ARTISTA",
    "horario": "13:00",
    "duracao": "1h30",
    "horario_completo": "13:00 - 14:30",
    "ordem": 1,
    "cor_destaque": "#fe74a5",
    "bio": "Descrição do artista e sua apresentação.",
    "redes_sociais": {
      "instagram": "https://instagram.com/artista",
      "spotify": "https://open.spotify.com/artist/123",
      "soundcloud": "https://soundcloud.com/artista"
    }
  }
]
```

### Campos Obrigatórios

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `id` | String | Identificador único (sem espaços) |
| `nome` | String | Nome do artista (MAIÚSCULO recomendado) |
| `horario` | String | Horário de início (formato "HH:MM") |
| `duracao` | String | Duração da apresentação |
| `ordem` | Number | Ordem de apresentação |
| `cor_destaque` | String | Cor em hexadecimal |
| `bio` | String | Biografia/descrição do artista |

### Campos Opcionais

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `redes_sociais` | Object | Links para Instagram, Spotify, SoundCloud |
| `horario_completo` | String | Formato "HH:MM - HH:MM" |

### Cores Sugeridas para Artistas

Use as cores do flyer para manter consistência visual:

```json
"cor_destaque": "#fe74a5"  // Rosa principal
"cor_destaque": "#ffdc7a"  // Amarelo vibrante
"cor_destaque": "#59af00"  // Verde médio
"cor_destaque": "#c82050"  // Rosa escuro
"cor_destaque": "#fc898e"  // Coral
"cor_destaque": "#dfa40a"  // Dourado
"cor_destaque": "#4c8d0e"  // Verde escuro
"cor_destaque": "#3fad43"  // Verde claro
```

## 🚀 ALTERAÇÕES ESSENCIAIS - GUIA RÁPIDO

### ⚡ Informações Fundamentais do Evento

**Para alterar as informações principais, edite diretamente no arquivo `templates/index.html`:**

#### 🎫 **Link de Inscrições (SYMPLA)**
**Localização:** Linha ~944
```html
<a href="https://www.sympla.com.br/evento/florescer-cultural---curitiba/3085364"
```
**Como alterar:** Substitua a URL completa pelo novo link do evento.

#### 📅 **Data do Evento**
**Localização:** Linha ~714 (visual) e linha ~934 (countdown)
```html
<!-- Visual -->
<div class="event-date">21 de Setembro de 2025</div>

<!-- Countdown JavaScript -->
const eventDate = new Date('2025-09-21T13:00:00').getTime();
```

#### ⏰ **Horário**
**Localização:** Linha ~735
```html
<h3 class="detail-title">7 horas de música</h3>
<p class="detail-info">Das 13h às 20h</p>
```

#### 📍 **Local**
**Localização:** Linhas ~863-869
```html
<h2 class="location-title">Ninho do Largo</h2>
<p><strong>R. Desembargador Ermelino de Leão, 511</strong></p>
<p>Centro Histórico, Curitiba - PR</p>
```

#### 🎤 **Mestre de Cerimônia**
**Localização:** Linha ~939
```html
<div class="mc-name">NACHI</div>
```

#### 🎁 **Quantidade de Brindes**
**Localização:** Linha ~950
```html
Os primeiros <strong>10 nomes na lista</strong> ganham brinde exclusivo
```

---

## 📝 Personalizações Rápidas

### 1. Alterar Informações do Evento

Edite diretamente no HTML (`templates/index.html`):

```html
<!-- Data do evento -->
<div class="event-date">
    21 de Setembro de 2025  <!-- ALTERE AQUI -->
</div>

<!-- Nome do evento -->
<h1 class="hero-title">
    Florescer<br>Cultural  <!-- ALTERE AQUI -->
</h1>

<!-- Countdown JavaScript -->
<script>
    const eventDate = new Date('2025-09-21T13:00:00').getTime(); // ALTERE AQUI
</script>
```

### 2. Modificar Local do Evento

```html
<!-- Card do local -->
<h2 class="location-title">Ninho do Largo</h2> <!-- ALTERE AQUI -->
<p><strong>R. Desembargador Ermelino de Leão, 511</strong></p> <!-- ALTERE AQUI -->
<p>Centro Histórico, Curitiba - PR</p> <!-- ALTERE AQUI -->

<!-- Mapa do Google -->
<iframe src="https://www.google.com/maps/embed?pb=..."> <!-- ATUALIZE URL -->
```

### 3. Alterar Link de Inscrições

```html
<a href="https://www.sympla.com.br/evento/florescer-cultural---curitiba/3085364" 
   target="_blank" 
   class="btn-primary">
    Garantir nome na lista  <!-- ALTERE TEXTO SE NECESSÁRIO -->
</a>
```

### 4. Personalizar Mestre de Cerimônia

```html
<div class="mc-section">
    <div class="mc-label">Mestre de cerimônia</div>
    <div class="mc-name">NACHI</div> <!-- ALTERE AQUI -->
</div>
```

## 🎨 Personalizações Avançadas

### Elementos Florais de Fundo

Para alterar os elementos flutuantes:

```css
body::before {
    background: radial-gradient(circle, var(--flower-pink-1) 0%, transparent 70%);
    /* Altere --flower-pink-1 para outra cor */
}

body::after {
    background: radial-gradient(circle, var(--flower-yellow) 0%, transparent 70%);
    /* Altere --flower-yellow para outra cor */
}
```

### Animações

Para desabilitar animações (acessibilidade):

```css
@media (prefers-reduced-motion: reduce) {
    * {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
    }
}
```

### Gradientes Personalizados

```css
/* Exemplo de novo gradiente para títulos */
.hero-title {
    background: linear-gradient(135deg, #your-color-1, #your-color-2);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
```

## 📱 Responsividade

### Breakpoints Utilizados

```css
/* Tablet */
@media (max-width: 768px) {
    /* Ajustes para tablet */
}

/* Mobile */
@media (max-width: 480px) {
    /* Ajustes para mobile */
}
```

### Personalizações Mobile

Para ajustar elementos específicos no mobile:

```css
@media (max-width: 480px) {
    .hero-title {
        font-size: 2.5rem; /* Título menor no mobile */
    }
    
    .countdown-grid {
        grid-template-columns: repeat(2, 1fr); /* 2 colunas no mobile */
    }
}
```

## 🚀 Otimizações de Performance

### Lazy Loading de Imagens

Para adicionar imagens com lazy loading:

```html
<img data-src="caminho/para/imagem.jpg" 
     alt="Descrição da imagem"
     class="lazy">
```

### Minificação

Para produção, considere minificar o CSS e JavaScript usando ferramentas como:
- **CSS**: cssnano, clean-css
- **JavaScript**: terser, uglify-js

## 🔧 Troubleshooting

### Problemas Comuns

1. **Cores não aparecem**: Verifique se as variáveis CSS estão definidas corretamente
2. **Lineup não atualiza**: Confirme que o arquivo `data/lineup.json` está válido
3. **Animações lentas**: Considere reduzir `animation-duration` nos elementos
4. **Layout quebrado no mobile**: Teste com diferentes tamanhos de tela

### Validação do JSON

Para verificar se o arquivo JSON está válido:

```bash
python3 -c "
import json
with open('data/lineup.json', 'r') as f:
    data = json.load(f)
    print('✅ JSON válido!')
    print(f'📊 {len(data)} artistas encontrados')
"
```

## 📈 Próximos Passos

### Funcionalidades Futuras

1. **CMS Integration**: Sistema de gerenciamento de conteúdo
2. **Multi-idioma**: Suporte para português e inglês
3. **PWA**: Progressive Web App capabilities
4. **Analytics**: Integração com Google Analytics 4
5. **Newsletter**: Sistema de inscrição para updates

### Melhorias de Performance

1. **WebP Images**: Converter imagens para formato WebP
2. **Critical CSS**: Extrair CSS crítico para above-the-fold
3. **Service Worker**: Cache inteligente para offline
4. **CDN**: Content Delivery Network para assets

## 📞 Suporte

Para dúvidas sobre personalização:

1. **Consulte este guia** primeiro
2. **Teste em ambiente local** antes de fazer deploy
3. **Valide HTML/CSS** usando ferramentas online
4. **Teste responsividade** em múltiplos dispositivos

---

## 🌸 Créditos

**Design**: Baseado na identidade visual do flyer Florescer Cultural 2025
**Desenvolvimento**: Sistema otimizado com foco em performance e acessibilidade
**Paleta**: Extraída diretamente das cores oficiais do evento

*Desenvolvido com 🌸 para celebrar a primavera*