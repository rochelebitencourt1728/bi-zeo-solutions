# 🚀 Guia Rápido - BI Mensal Zeo Solutions

## ⚡ 3 Passos para Gerar o BI

### 1️⃣ Preparar Dados
- Obtenha o arquivo Excel com os dados do mês
- Certifique-se que tem as colunas: `Resultado`, `Jan`, `Fev`, etc.

### 2️⃣ Executar Script
```bash
python3 gerar_bi_mensal.py dados_fevereiro.xlsx "Fevereiro 2026"
```

### 3️⃣ Abrir Dashboard
- Arquivo gerado: `Resultado_Mensal_ZEO_Fevereiro_2026.html`
- Abra no navegador (Chrome, Firefox, Safari, Edge)
- Compartilhe com o cliente!

---

## 📋 Checklist Mensal

- [ ] Receber arquivo Excel do cliente
- [ ] Verificar se está em formato correto
- [ ] Executar: `python3 gerar_bi_mensal.py <arquivo> "<mes_ano>"`
- [ ] Abrir HTML e verificar dados
- [ ] Compartilhar com cliente
- [ ] Arquivar arquivo para referência

---

## 🎯 Exemplos de Uso

### Fevereiro 2026
```bash
python3 gerar_bi_mensal.py painel_fevereiro.xlsx "Fevereiro 2026"
```

### Março 2026
```bash
python3 gerar_bi_mensal.py painel_marco.xlsx "Março 2026"
```

### Abril 2026
```bash
python3 gerar_bi_mensal.py painel_abril.xlsx "Abril 2026"
```

---

## 💡 Dicas

✅ **Use caminhos completos** para evitar erros:
```bash
python3 gerar_bi_mensal.py /home/ubuntu/dados/painel_fevereiro.xlsx "Fevereiro 2026"
```

✅ **Verifique o arquivo Excel** antes de executar:
- Abra em Excel/LibreOffice
- Confirme aba "Realizado"
- Verifique valores nas colunas

✅ **Compartilhe o HTML** diretamente:
- Funciona offline
- Sem dependências
- Compatível com todos os navegadores

---

## ❌ Erros Comuns

| Erro | Solução |
|------|---------|
| "Arquivo não encontrado" | Use caminho completo do arquivo |
| "Módulo pandas não encontrado" | Execute: `pip3 install pandas openpyxl` |
| "Dados não aparecem" | Verifique se aba se chama "Realizado" |
| "Valores zerados" | Confirme se estão na coluna correta |

---

## 📞 Contato

Dúvidas? Consulte o README.md completo ou entre em contato com a Connecta.

---

**Última atualização:** Fevereiro 2026
