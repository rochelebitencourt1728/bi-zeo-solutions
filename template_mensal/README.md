# Template BI Mensal - Zeo Solutions

## 📊 Visão Geral

Este template permite gerar automaticamente o **BI mensal da Zeo Solutions** mantendo o padrão visual e design profissional estabelecido em janeiro de 2026.

## 🎯 Características

✅ **Design Consistente**
- Logos da Connecta e Zeo Solutions
- Cores profissionais (marrom/bege + dourado)
- Layout responsivo

✅ **Dados Automáticos**
- Carrega dados do arquivo Excel
- Calcula indicadores automaticamente
- Gera gráficos e tabelas

✅ **Fácil de Usar**
- Script Python simples
- Apenas 2 parâmetros necessários
- Geração em segundos

## 📁 Estrutura de Arquivos

```
template_mensal/
├── gerar_bi_mensal.py          # Script principal
├── README.md                    # Este arquivo
├── GUIA_RAPIDO.md              # Guia rápido de uso
└── exemplos/
    └── dados_exemplo.xlsx      # Exemplo de arquivo Excel
```

## 🚀 Como Usar

### Pré-requisitos

```bash
# Instalar dependências
pip3 install pandas openpyxl
```

### Uso Básico

```bash
# Sintaxe
python3 gerar_bi_mensal.py <arquivo_excel> "<mes_ano>"

# Exemplo
python3 gerar_bi_mensal.py ../painel_realizado_2026-02-02.xlsx "Fevereiro 2026"
```

### Resultado

O script gera um arquivo HTML com o nome:
```
Resultado_Mensal_ZEO_Fevereiro_2026.html
```

## 📋 Formato do Arquivo Excel

O arquivo Excel deve ter:
- **Aba:** "Realizado"
- **Colunas:** 
  - `Resultado` - Descrição da linha
  - `Jan` - Valores de janeiro (ou outro mês)
  - `Fev`, `Mar`, etc. - Outros meses (opcional)

**Linhas obrigatórias:**
- `RECEITAS OPERACIONAIS`
- `CUSTOS OPERACIONAIS`
- `DESPESAS OPERACIONAIS E OUTRAS RECEITAS`
- `RESULTADO OPERACIONAL`

### Exemplo de Estrutura

| Resultado | Jan | Fev | Mar |
|-----------|-----|-----|-----|
| RECEITAS OPERACIONAIS | 38904 | 42000 | 45000 |
| CUSTOS OPERACIONAIS | -44017.68 | -45000 | -48000 |
| DESPESAS OPERACIONAIS E OUTRAS RECEITAS | -49959.03 | -50000 | -52000 |
| RESULTADO OPERACIONAL | -55072.71 | -53000 | -55000 |

## 🎨 Personalizações

### Alterar Mês e Ano

```bash
python3 gerar_bi_mensal.py dados.xlsx "Março 2026"
```

### Alterar Diretório de Saída

Edite o script e modifique:
```python
gerador = GeradorBIMensal(arquivo_excel, mes_ano, diretorio_saida="/caminho/desejado")
```

### Alterar Cores

Edite o arquivo `gerar_bi_mensal.py` e procure pela seção `<style>`:
```css
/* Cores principais */
background: linear-gradient(135deg, #5A4A3A 0%, #3D3428 100%); /* Marrom */
color: #D4A574; /* Dourado */
```

## 📊 Dados Gerados

O dashboard inclui:

✅ **Cards de Resumo**
- Total de Receitas
- Total de Custos
- Total de Despesas
- Resultado Operacional
- Margem de Contribuição
- Custo Total

✅ **Informações**
- Mês e ano
- Data de atualização
- Todos os valores em R$

## 🔄 Fluxo de Trabalho Mensal

1. **Receber dados** do cliente (arquivo Excel)
2. **Executar script:**
   ```bash
   python3 gerar_bi_mensal.py dados_fevereiro.xlsx "Fevereiro 2026"
   ```
3. **Abrir arquivo HTML** gerado no navegador
4. **Compartilhar** com o cliente

## ⚙️ Troubleshooting

### Erro: "Arquivo não encontrado"
- Verifique o caminho do arquivo Excel
- Use caminho absoluto se necessário

### Erro: "Módulo pandas não encontrado"
```bash
pip3 install pandas openpyxl
```

### Dados não aparecem
- Verifique se a aba se chama "Realizado"
- Confirme se as colunas estão nomeadas corretamente
- Verifique se os valores estão nas células corretas

## 📝 Exemplo Completo

```bash
# Navegar para o diretório
cd /home/ubuntu/bi_zeo/template_mensal

# Gerar BI para fevereiro
python3 gerar_bi_mensal.py /home/ubuntu/upload/painel_fevereiro_2026.xlsx "Fevereiro 2026"

# Abrir no navegador
# Arquivo gerado: Resultado_Mensal_ZEO_Fevereiro_2026.html
```

## 🎯 Próximas Melhorias

- [ ] Adicionar gráficos interativos
- [ ] Gerar comparativo com mês anterior
- [ ] Adicionar análise de projetos
- [ ] Exportar para PDF automaticamente
- [ ] Integração com Google Sheets

## 📞 Suporte

Para dúvidas ou problemas:
1. Verifique este README
2. Consulte o GUIA_RAPIDO.md
3. Revise o arquivo de exemplo

## 📄 Licença

Template desenvolvido para Zeo Solutions - Todos os direitos reservados.

---

**Versão:** 1.0  
**Data:** Fevereiro de 2026  
**Desenvolvido por:** Connecta
