// Florescer Cultural - Main JavaScript (Versão Simplificada)

document.addEventListener('DOMContentLoaded', function() {
    console.log('🌸 Florescer Cultural inicializado - Nova versão');
    
    // Inicializar funcionalidades principais
    initScrollAnimations();
    initSmoothScroll();
    initCountdownTimer();
    initVisualEffects();
    
    // Verificar se ainda há backend conectado
    if (typeof updateCounters === 'function') {
        updateCountersOnLoad();
        setInterval(updateCounters, 30000); // A cada 30 segundos
    }
});

// Animações no scroll
function initScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                
                // Adicionar delay para elementos em sequência
                const siblings = entry.target.parentElement.querySelectorAll('.animate-on-scroll');
                const index = Array.from(siblings).indexOf(entry.target);
                entry.target.style.transitionDelay = `${index * 0.15}s`;
            }
        });
    }, observerOptions);

    // Observar todos os elementos com animação
    document.querySelectorAll('.animate-on-scroll').forEach(el => {
        observer.observe(el);
    });
}

// Smooth scroll para âncoras
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const target = document.querySelector(targetId);
            
            if (target) {
                const headerOffset = 80; // Ajuste conforme necessário
                const elementPosition = target.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
}

// Countdown Timer
function initCountdownTimer() {
    const eventDate = new Date('2025-09-20T15:00:00').getTime();
    
    function updateCountdown() {
        const now = new Date().getTime();
        const distance = eventDate - now;
        
        if (distance > 0) {
            const days = Math.floor(distance / (1000 * 60 * 60 * 24));
            const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((distance % (1000 * 60)) / 1000);
            
            // Atualizar elementos se existirem
            const elements = {
                'days': days.toString().padStart(2, '0'),
                'hours': hours.toString().padStart(2, '0'),
                'minutes': minutes.toString().padStart(2, '0'),
                'seconds': seconds.toString().padStart(2, '0')
            };
            
            Object.entries(elements).forEach(([id, value]) => {
                const element = document.getElementById(id);
                if (element) {
                    element.textContent = value;
                }
            });
        } else {
            // Evento já começou
            const countdownContainer = document.getElementById('countdown');
            if (countdownContainer) {
                countdownContainer.innerHTML = 
                    '<div class="event-started">🌸 O evento começou! 🌸</div>';
            }
        }
    }
    
    // Atualizar imediatamente e depois a cada segundo
    updateCountdown();
    setInterval(updateCountdown, 1000);
}

// Atualizar contadores (se backend estiver disponível)
async function updateCounters() {
    try {
        const response = await fetch('/api/stats');
        if (!response.ok) throw new Error('API não disponível');
        
        const data = await response.json();
        updateCounterElements(data);
        
    } catch (error) {
        console.warn('Backend não disponível, usando valores estáticos:', error);
        // Usar valores padrão se backend não estiver disponível
        updateCounterElements({
            vagas_restantes: 150,
            brindes_restantes: 15,
            total_inscritos: 0
        });
    }
}

function updateCountersOnLoad() {
    // Primeira atualização imediata
    updateCounters();
}

function updateCounterElements(data) {
    // Atualizar elementos de contador
    const elements = {
        'vagas-counter': `${data.vagas_restantes} Vagas`,
        'vagas-restantes': data.vagas_restantes,
        'brindes-restantes': data.brindes_restantes,
        'brindes-counter': data.brindes_restantes
    };
    
    Object.entries(elements).forEach(([id, value]) => {
        const element = document.getElementById(id);
        if (element) {
            element.textContent = value;
            
            // Animação sutil de atualização
            element.style.transform = 'scale(1.05)';
            element.style.transition = 'transform 0.3s ease';
            
            setTimeout(() => {
                element.style.transform = 'scale(1)';
            }, 300);
        }
    });
}

// Efeitos visuais
function initVisualEffects() {
    // Efeito de sparkles em botões importantes
    document.addEventListener('click', function(e) {
        if (e.target.classList.contains('btn-primary') || 
            e.target.classList.contains('btn-pulse')) {
            createSparkleEffect(e.target, e.clientX, e.clientY);
        }
    });

    // Parallax suave para elementos flutuantes
    let ticking = false;
    
    function updateParallax() {
        const scrollY = window.pageYOffset;
        const elements = document.querySelectorAll('.ornament');
        
        elements.forEach((element, index) => {
            const speed = (index % 3 + 1) * 0.3;
            element.style.transform = `translateY(${scrollY * speed}px) rotate(${scrollY * 0.1}deg)`;
        });
        
        ticking = false;
    }
    
    window.addEventListener('scroll', () => {
        if (!ticking) {
            requestAnimationFrame(updateParallax);
            ticking = true;
        }
    });
}

function createSparkleEffect(button, clickX, clickY) {
    const rect = button.getBoundingClientRect();
    const centerX = rect.left + rect.width / 2;
    const centerY = rect.top + rect.height / 2;
    
    // Criar múltiplas partículas
    for (let i = 0; i < 8; i++) {
        setTimeout(() => {
            createSparkle(
                centerX + (Math.random() - 0.5) * rect.width,
                centerY + (Math.random() - 0.5) * rect.height
            );
        }, i * 50);
    }
}

function createSparkle(x, y) {
    const sparkle = document.createElement('div');
    sparkle.className = 'sparkle-particle';
    
    // Escolher cor aleatória da paleta
    const colors = ['var(--amarelo-sol)', 'var(--rosa-coral)', 'var(--verde-claro)'];
    const color = colors[Math.floor(Math.random() * colors.length)];
    
    sparkle.style.cssText = `
        position: fixed;
        left: ${x}px;
        top: ${y}px;
        width: 6px;
        height: 6px;
        background: ${color};
        border-radius: 50%;
        pointer-events: none;
        z-index: 1000;
        animation: sparkle-animation 1.2s ease-out forwards;
    `;
    
    document.body.appendChild(sparkle);
    
    setTimeout(() => {
        if (sparkle.parentNode) {
            sparkle.remove();
        }
    }, 1200);
}

// Easter egg: sequência de teclas especial
let konamiCode = [];
const konamiSequence = [
    'ArrowUp', 'ArrowUp', 'ArrowDown', 'ArrowDown',
    'ArrowLeft', 'ArrowRight', 'ArrowLeft', 'ArrowRight',
    'KeyB', 'KeyA'
];

document.addEventListener('keydown', function(e) {
    konamiCode.push(e.code);
    
    if (konamiCode.length > konamiSequence.length) {
        konamiCode.shift();
    }
    
    if (JSON.stringify(konamiCode) === JSON.stringify(konamiSequence)) {
        activateEasterEgg();
        konamiCode = [];
    }
});

function activateEasterEgg() {
    // Chuva de flores
    for (let i = 0; i < 30; i++) {
        setTimeout(() => {
            createFallingFlower();
        }, i * 150);
    }
    
    // Mensagem especial
    showSpecialMessage('🌸 Você descobriu o jardim secreto! 🌸');
}

function createFallingFlower() {
    const flowers = ['🌸', '🌺', '🌻', '🌷', '🌹', '🌼'];
    const flower = document.createElement('div');
    flower.textContent = flowers[Math.floor(Math.random() * flowers.length)];
    flower.style.cssText = `
        position: fixed;
        left: ${Math.random() * window.innerWidth}px;
        top: -50px;
        font-size: ${1.5 + Math.random() * 1}rem;
        pointer-events: none;
        z-index: 1000;
        animation: fall-flower 4s linear forwards;
        transform: rotate(${Math.random() * 360}deg);
    `;
    
    document.body.appendChild(flower);
    
    setTimeout(() => {
        if (flower.parentNode) {
            flower.remove();
        }
    }, 4000);
}

function showSpecialMessage(message) {
    const messageDiv = document.createElement('div');
    messageDiv.textContent = message;
    messageDiv.style.cssText = `
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: linear-gradient(135deg, var(--verde-principal), var(--rosa-coral));
        color: var(--off-white);
        padding: 2rem 3rem;
        border-radius: 20px;
        font-size: 1.8rem;
        font-weight: bold;
        z-index: 10000;
        text-align: center;
        box-shadow: 0 15px 40px rgba(76, 175, 80, 0.4);
        border: 3px solid var(--amarelo-sol);
        animation: special-message-animation 4s ease-in-out forwards;
        font-family: 'Cinzel Decorative', serif;
    `;
    
    document.body.appendChild(messageDiv);
    
    setTimeout(() => {
        if (messageDiv.parentNode) {
            messageDiv.remove();
        }
    }, 4000);
}

// Detectar preferências do usuário
function detectUserPreferences() {
    // Detectar modo escuro do sistema
    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        document.documentElement.style.setProperty('--off-white', '#2a2a2a');
        document.documentElement.style.setProperty('--cinza-terra', '#e0e0e0');
    }
    
    // Detectar preferência por animações reduzidas
    if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
        document.documentElement.style.setProperty('--animation-duration', '0.1s');
        // Desabilitar animações complexas
        const style = document.createElement('style');
        style.textContent = `
            *, *::before, *::after {
                animation-duration: 0.1s !important;
                animation-iteration-count: 1 !important;
                transition-duration: 0.1s !important;
            }
        `;
        document.head.appendChild(style);
    }
}

// Otimizações de performance
function optimizePerformance() {
    // Lazy loading para elementos pesados
    const observerOptions = {
        root: null,
        rootMargin: '50px',
        threshold: 0.1
    };
    
    const lazyObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const element = entry.target;
                
                // Carregar iframes do Sympla apenas quando necessário
                if (element.dataset.src && element.tagName === 'IFRAME') {
                    element.src = element.dataset.src;
                    element.removeAttribute('data-src');
                }
                
                lazyObserver.unobserve(element);
            }
        });
    }, observerOptions);
    
    // Observar iframes com data-src
    document.querySelectorAll('iframe[data-src]').forEach(iframe => {
        lazyObserver.observe(iframe);
    });
    
    // Debounce para eventos de scroll
    let scrollTimeout;
    const originalScrollHandler = window.onscroll;
    
    window.onscroll = function(e) {
        if (scrollTimeout) clearTimeout(scrollTimeout);
        scrollTimeout = setTimeout(() => {
            if (originalScrollHandler) originalScrollHandler(e);
        }, 16); // ~60fps
    };
}

// Analytics simplificado (placeholder)
function trackEvent(action, category = 'engagement', label = '') {
    // Integração com Google Analytics ou similar
    if (typeof gtag !== 'undefined') {
        gtag('event', action, {
            event_category: category,
            event_label: label
        });
    }
    
    console.log(`📊 Event tracked: ${category} - ${action} - ${label}`);
}

// Track interações importantes
function initEventTracking() {
    // Track cliques em CTAs
    document.addEventListener('click', function(e) {
        if (e.target.matches('a[href*="sympla"], .btn-primary')) {
            trackEvent('click_cta', 'conversion', 'sympla_redirect');
        }
        
        if (e.target.matches('a[href^="#"]')) {
            trackEvent('internal_navigation', 'engagement', e.target.getAttribute('href'));
        }
        
        if (e.target.matches('.social-link, .location-link')) {
            trackEvent('external_link', 'engagement', e.target.href);
        }
    });
    
    // Track tempo na página
    let startTime = Date.now();
    let maxScroll = 0;
    
    window.addEventListener('scroll', () => {
        const scrollPercent = Math.round((window.scrollY / (document.body.scrollHeight - window.innerHeight)) * 100);
        maxScroll = Math.max(maxScroll, scrollPercent);
    });
    
    window.addEventListener('beforeunload', () => {
        const timeSpent = Math.round((Date.now() - startTime) / 1000);
        trackEvent('page_engagement', 'behavior', `${timeSpent}s_${maxScroll}%`);
    });
}

// Service Worker para cache offline (opcional)
function initServiceWorker() {
    if ('serviceWorker' in navigator) {
        window.addEventListener('load', () => {
            navigator.serviceWorker.register('/sw.js')
                .then(registration => {
                    console.log('🔧 Service Worker registrado:', registration);
                })
                .catch(registrationError => {
                    console.log('❌ Falha no Service Worker:', registrationError);
                });
        });
    }
}

// Utilitários para manipulação do DOM
const utils = {
    // Debounce function
    debounce: function(func, wait, immediate) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                timeout = null;
                if (!immediate) func(...args);
            };
            const callNow = immediate && !timeout;
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
            if (callNow) func(...args);
        };
    },
    
    // Throttle function
    throttle: function(func, limit) {
        let inThrottle;
        return function(...args) {
            if (!inThrottle) {
                func.apply(this, args);
                inThrottle = true;
                setTimeout(() => inThrottle = false, limit);
            }
        };
    },
    
    // Animate number counting
    animateNumber: function(element, start, end, duration = 1000) {
        const range = end - start;
        const increment = range / (duration / 16);
        let current = start;
        
        const timer = setInterval(() => {
            current += increment;
            if ((increment > 0 && current >= end) || (increment < 0 && current <= end)) {
                current = end;
                clearInterval(timer);
            }
            element.textContent = Math.floor(current);
        }, 16);
    }
};

// Inicializar tudo
function initializeApp() {
    console.log('🌸 Inicializando Florescer Cultural...');
    
    detectUserPreferences();
    optimizePerformance();
    initEventTracking();
    
    // Opcional: Service Worker
    // initServiceWorker();
    
    console.log('✅ Florescer Cultural totalmente carregado!');
}

// CSS para as novas animações
const additionalStyles = document.createElement('style');
additionalStyles.textContent = `
    @keyframes sparkle-animation {
        0% { 
            opacity: 1; 
            transform: scale(0) rotate(0deg); 
        }
        50% { 
            opacity: 1; 
            transform: scale(1.2) rotate(180deg); 
        }
        100% { 
            opacity: 0; 
            transform: scale(0) rotate(360deg); 
        }
    }
    
    @keyframes fall-flower {
        0% { 
            transform: translateY(0) rotate(0deg);
            opacity: 1;
        }
        100% { 
            transform: translateY(${window.innerHeight + 100}px) rotate(360deg);
            opacity: 0;
        }
    }
    
    @keyframes special-message-animation {
        0% { 
            opacity: 0; 
            transform: translate(-50%, -50%) scale(0.5) rotate(-10deg);
        }
        20% { 
            opacity: 1; 
            transform: translate(-50%, -50%) scale(1.1) rotate(2deg);
        }
        25% { 
            transform: translate(-50%, -50%) scale(1) rotate(0deg);
        }
        75% { 
            opacity: 1; 
            transform: translate(-50%, -50%) scale(1) rotate(0deg);
        }
        100% { 
            opacity: 0; 
            transform: translate(-50%, -50%) scale(0.5) rotate(5deg);
        }
    }
    
    /* Melhorias de acessibilidade */
    .animate-on-scroll {
        transition: all 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    }
    
    .animate-on-scroll.visible {
        opacity: 1;
        transform: translateY(0);
    }
    
    /* Responsividade aprimorada */
    @media (max-width: 768px) {
        .sparkle-particle {
            width: 4px !important;
            height: 4px !important;
        }
        
        .event-started {
            font-size: 1.5rem !important;
        }
    }
    
    /* Modo escuro automático */
    @media (prefers-color-scheme: dark) {
        :root {
            --off-white: #1a1a1a;
            --cinza-terra: #e0e0e0;
            --cinza-claro: #b0b0b0;
        }
    }
    
    /* Redução de movimento */
    @media (prefers-reduced-motion: reduce) {
        *, *::before, *::after {
            animation-duration: 0.01ms !important;
            animation-iteration-count: 1 !important;
            transition-duration: 0.01ms !important;
        }
        
        .ornament {
            animation: none !important;
        }
    }
`;

document.head.appendChild(additionalStyles);

// Executar inicialização quando DOM estiver pronto
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initializeApp);
} else {
    initializeApp();
}