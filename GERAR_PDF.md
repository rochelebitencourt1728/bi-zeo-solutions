# 📄 Guia - Gerar PDF do Dashboard

## 🎯 Visão Geral

Você pode converter o **Dashboard HTML para PDF** em segundos! Perfeito para:
- ✅ Enviar por email
- ✅ Imprimir
- ✅ Compartilhar offline
- ✅ Arquivar

---

## 🚀 Como Usar

### Opção 1: Linha de Comando (Recomendado)

```bash
# Navegar para o diretório
cd /home/ubuntu/bi_zeo

# Gerar PDF com nome automático
python3 html_para_pdf.py dashboard_premium.html

# Gerar PDF com nome personalizado
python3 html_para_pdf.py dashboard_premium.html "Meu_Dashboard.pdf"
```

### Opção 2: Python Script

```python
from weasyprint import HTML

# Converter HTML para PDF
HTML("dashboard_premium.html").write_pdf("dashboard.pdf")
```

---

## 📋 Exemplos Práticos

### Exemplo 1: Gerar PDF Simples
```bash
python3 html_para_pdf.py dashboard_premium.html
```
**Resultado:** `dashboard_premium_02022026.pdf`

### Exemplo 2: Gerar com Nome Customizado
```bash
python3 html_para_pdf.py dashboard_premium.html "BI_Janeiro_2026.pdf"
```
**Resultado:** `BI_Janeiro_2026.pdf`

### Exemplo 3: Salvar em Pasta Específica
```bash
python3 html_para_pdf.py dashboard_premium.html "/home/ubuntu/pdfs/dashboard.pdf"
```
**Resultado:** Arquivo salvo em `/home/ubuntu/pdfs/`

---

## ⚙️ Pré-requisitos

### Instalar Dependência
```bash
pip3 install weasyprint
```

### Verificar Instalação
```bash
python3 -c "from weasyprint import HTML; print('✓ WeasyPrint instalado')"
```

---

## 🎨 Qualidade do PDF

### Características
- ✅ Preserva cores e design
- ✅ Logos embutidos
- ✅ Gráficos renderizados
- ✅ Responsivo para impressão
- ✅ Tamanho otimizado (~300-400 KB)

### Resolução
- Padrão: 96 DPI (tela)
- Impressão: 300 DPI (recomendado)

---

## 📊 Fluxo Mensal Sugerido

```
1. Gerar Dashboard HTML
   ↓
2. Testar no navegador
   ↓
3. Converter para PDF
   ↓
4. Compartilhar com cliente
   ↓
5. Arquivar para referência
```

---

## 🔄 Automação (Script Bash)

Crie arquivo `gerar_pdf.sh`:

```bash
#!/bin/bash

# Variáveis
DASHBOARD="dashboard_premium.html"
MES=$(date +%B_%Y)
PDF="BI_ZEO_${MES}.pdf"

# Converter
python3 html_para_pdf.py "$DASHBOARD" "$PDF"

# Abrir (opcional)
# open "$PDF"  # macOS
# xdg-open "$PDF"  # Linux
```

Usar:
```bash
chmod +x gerar_pdf.sh
./gerar_pdf.sh
```

---

## 📧 Compartilhar PDF

### Via Email
```
Assunto: BI Mensal - Zeo Solutions - Janeiro 2026

Prezado(a),

Segue em anexo seu relatório financeiro em PDF.

Att,
Connecta
```

### Via WhatsApp
```
Seu BI mensal está pronto! 📊

Arquivo: Resultado_Mensal_ZEO_Janeiro2026.pdf

Qualquer dúvida, entre em contato!
```

### Via Nuvem (Google Drive, Dropbox)
1. Gere o PDF
2. Faça upload para nuvem
3. Compartilhe o link

---

## ⚠️ Troubleshooting

### Problema: "ModuleNotFoundError: No module named 'weasyprint'"

**Solução:**
```bash
pip3 install weasyprint
```

### Problema: "Arquivo não encontrado"

**Solução:**
- Use caminho completo: `/home/ubuntu/bi_zeo/dashboard_premium.html`
- Verifique se o arquivo existe
- Confirme a ortografia

### Problema: "PDF vazio ou com problemas de renderização"

**Solução:**
- Verifique se o HTML está correto
- Teste no navegador primeiro
- Confirme que logos estão embutidas (base64)

### Problema: "Processo lento"

**Solução:**
- Normal: primeira execução leva 10-15 segundos
- Próximas execuções são mais rápidas
- Paciência! 😊

---

## 💡 Dicas

✅ **Use nomes descritivos:**
```bash
python3 html_para_pdf.py dashboard_premium.html "BI_ZEO_Janeiro_2026.pdf"
```

✅ **Organize em pastas:**
```bash
mkdir -p /home/ubuntu/bi_zeo/pdfs
python3 html_para_pdf.py dashboard_premium.html "/home/ubuntu/bi_zeo/pdfs/janeiro_2026.pdf"
```

✅ **Automatize mensalmente:**
```bash
# Cron job (executar todo mês)
0 9 1 * * cd /home/ubuntu/bi_zeo && python3 html_para_pdf.py dashboard_premium.html
```

---

## 📊 Comparação: HTML vs PDF

| Aspecto | HTML | PDF |
|---------|------|-----|
| Interativo | ✅ Sim | ❌ Não |
| Offline | ✅ Sim | ✅ Sim |
| Email | ⚠️ Pode ter problemas | ✅ Seguro |
| Impressão | ⚠️ Pode variar | ✅ Consistente |
| Tamanho | Menor | Maior |
| Compatibilidade | Navegador | Qualquer leitor PDF |

---

## 🎯 Próximas Etapas

1. ✅ Instalar WeasyPrint
2. ✅ Testar conversão
3. ✅ Gerar PDF mensal
4. ✅ Compartilhar com cliente
5. ✅ Arquivar para referência

---

## 📞 Suporte

Dúvidas? Consulte:
- Este guia (GERAR_PDF.md)
- Documentação WeasyPrint: https://weasyprint.org/
- Entre em contato com a Connecta

---

**Desenvolvido com ❤️ pela Connecta**

Versão: 1.0 | Data: Fevereiro 2026
