# 🚀 Instalação Rápida - Florescer Cultural

## ⚡ Passos Rápidos (5 minutos)

### 1. 📥 Baixar o Projeto
- Baixe o ZIP do projeto
- Extraia em uma pasta de sua escolha
- Abra o terminal/prompt nesta pasta

### 2. 🐍 Verificar Python
```bash
python --version
```
Se não tiver Python instalado, baixe em: https://python.org (versão 3.8+)

### 3. 📦 Instalar Dependências
```bash
pip install -r requirements.txt
```

### 4. 🗄️ Criar Banco de Dados
```bash
python init_database.py
```
- Responda "s" se quiser dados de teste

### 5. 🌐 Executar
```bash
python run.py
```

### 6. ✅ Acessar
- Abra: http://localhost:5000
- Admin: http://localhost:5000/admin

---

## 🔧 Se Algo Der Errado

### Erro: "comando não encontrado"
```bash
# Tente com python3
python3 --version
python3 -m pip install -r requirements.txt
python3 run.py
```

### Erro: "permissão negada"
- **Windows**: Execute como Administrador
- **Mac/Linux**: Use `sudo` se necessário

### Erro: "porta em uso"
- Feche outros programas que usam porta 5000
- Ou mude a porta em `app.py` (última linha)

### QR codes não aparecem
```bash
mkdir -p static/qrcodes
```

---

## 📋 Checklist Pós-Instalação

- [ ] Site abre em http://localhost:5000
- [ ] Formulário de inscrição funciona
- [ ] Admin acessível em /admin
- [ ] QR codes são gerados
- [ ] Banco de dados tem participantes teste

---

## 🎯 Próximos Passos

### Personalizar o Evento
1. **Editar informações**: Abra `templates/index.html`
2. **Alterar cores**: Modifique `static/css/style.css`
3. **Configurar pagamentos**: Edite arquivo `.env`

### Fazer Deploy
1. **Railway**: Conecte repositório GitHub
2. **Render**: Upload e configure
3. **Vercel**: Para versão estática

### Configurar Mercado Pago
1. Crie conta em mercadopago.com.br/developers
2. Obtenha credenciais
3. Coloque no arquivo `.env`

---

## ⚠️ Importante

- ✅ **Funciona offline**: Não precisa de internet para testar
- 📱 **Mobile friendly**: Testa no celular também
- 🔒 **Dados seguros**: Tudo fica local até você fazer deploy
- 🎨 **Totalmente customizável**: Mude cores, textos, layout

---

## 💡 Dicas de Uso

### Para Desenvolvedores
- Use `FLASK_DEBUG=True` para desenvolvimento
- Acesse `/api/stats` para ver dados JSON
- Verifique console do navegador (F12) para logs

### Para Organizadores de Evento
- Teste primeiro com dados falsos
- Configure WhatsApp para suporte
- Prepare materiais para divulgação
- Teste processo completo antes do evento

### Para Deploy
- Mude `SECRET_KEY` em produção
- Configure domínio personalizado
- Ative HTTPS
- Configure backup do banco

---

## 🆘 Ajuda Rápida

**Site não abre?**
- Verifique se executou `python run.py`
- Tente http://127.0.0.1:5000

**Formulário não funciona?**
- Veja mensagens de erro no navegador (F12)
- Verifique se banco existe (`database/eventos.db`)

**QR codes não aparecem?**
- Verifique pasta `static/qrcodes/`
- Execute como administrador se necessário

**Admin não funciona?**
- Acesse: http://localhost:5000/admin
- Verifique se há participantes no banco

---

## 🌸 Pronto!

Agora você tem uma landing page completa para eventos culturais!

**Recursos inclusos:**
- ✅ Landing page elegante
- ✅ Sistema de inscrições  
- ✅ QR codes únicos
- ✅ Painel administrativo
- ✅ Integração WhatsApp
- ✅ Códigos de brinde especiais
- ✅ Design responsivo

**Próximo evento? Reutilize facilmente!**

---

*Desenvolvido com 🌸 para o Florescer Cultural 2025*