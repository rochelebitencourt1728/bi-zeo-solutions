# 🔧 Setup - Template BI Mensal

## Instalação Inicial

### 1. Instalar Dependências

```bash
# Atualizar pip
pip3 install --upgrade pip

# Instalar pandas e openpyxl
pip3 install pandas openpyxl
```

### 2. Verificar Instalação

```bash
# Testar se está funcionando
python3 -c "import pandas; print('✓ Pandas instalado')"
python3 -c "import openpyxl; print('✓ Openpyxl instalado')"
```

### 3. Testar Script

```bash
# Navegar para o diretório
cd /home/ubuntu/bi_zeo/template_mensal

# Ver ajuda
python3 gerar_bi_mensal.py
```

## Estrutura de Diretórios

```
/home/ubuntu/bi_zeo/
├── template_mensal/              # Este diretório
│   ├── gerar_bi_mensal.py       # Script principal
│   ├── README.md                # Documentação completa
│   ├── GUIA_RAPIDO.md           # Guia rápido
│   ├── SETUP.md                 # Este arquivo
│   └── exemplos/                # Exemplos (criar conforme necessário)
│
├── logo_connecta.png            # Logo Connecta (necessário)
├── logo_zeo.jpg                 # Logo Zeo (necessário)
├── dashboard_premium.html       # Dashboard completo (referência)
│
└── [arquivos de meses anteriores]
```

## Primeira Execução

### Passo 1: Preparar Dados

Crie um arquivo Excel com a estrutura:

```
Aba: "Realizado"

Coluna A (Resultado):
- RECEITAS OPERACIONAIS
- CUSTOS OPERACIONAIS
- DESPESAS OPERACIONAIS E OUTRAS RECEITAS
- RESULTADO OPERACIONAL

Coluna B (Jan):
- 38904
- -44017.68
- -49959.03
- -55072.71
```

### Passo 2: Executar Script

```bash
python3 gerar_bi_mensal.py seu_arquivo.xlsx "Fevereiro 2026"
```

### Passo 3: Verificar Resultado

- Abra o arquivo HTML gerado
- Verifique se os dados aparecem corretamente
- Compartilhe com o cliente

## Troubleshooting

### Problema: "ModuleNotFoundError: No module named 'pandas'"

**Solução:**
```bash
pip3 install pandas openpyxl
```

### Problema: "FileNotFoundError: [Errno 2] No such file or directory"

**Solução:**
- Use caminho completo do arquivo
- Verifique se o arquivo existe
- Exemplo: `/home/ubuntu/dados/painel_fevereiro.xlsx`

### Problema: "Dados não aparecem no HTML"

**Solução:**
1. Abra o arquivo Excel
2. Verifique se a aba se chama "Realizado"
3. Confirme se as colunas estão: `Resultado`, `Jan`, `Fev`, etc.
4. Verifique se os valores estão nas células corretas

### Problema: "Logos não aparecem"

**Solução:**
- Verifique se `logo_connecta.png` e `logo_zeo.jpg` existem
- Eles devem estar em `/home/ubuntu/bi_zeo/`
- O script busca automaticamente

## Configuração Avançada

### Alterar Diretório de Saída

Edite `gerar_bi_mensal.py` e procure por:

```python
gerador = GeradorBIMensal(arquivo_excel, mes_ano)
```

Altere para:

```python
gerador = GeradorBIMensal(arquivo_excel, mes_ano, diretorio_saida="/seu/diretorio")
```

### Personalizar Cores

Edite `gerar_bi_mensal.py` e procure pela seção `<style>`:

```css
/* Altere estas cores */
background: linear-gradient(135deg, #5A4A3A 0%, #3D3428 100%);
color: #D4A574;
```

### Adicionar Mais Dados

Edite a seção de processamento de dados:

```python
def processar_dados(self):
    # Adicione aqui novos campos
    for idx, row in self.dados.iterrows():
        # ... seu código
```

## Automação (Opcional)

### Criar Script de Automação (Linux/Mac)

Crie arquivo `gerar_bi_automatico.sh`:

```bash
#!/bin/bash

# Variáveis
ARQUIVO=$1
MES=$2
SCRIPT="/home/ubuntu/bi_zeo/template_mensal/gerar_bi_mensal.py"

# Executar
python3 $SCRIPT "$ARQUIVO" "$MES"

# Abrir no navegador (opcional)
# open "Resultado_Mensal_ZEO_${MES// /_}.html"
```

Tornar executável:
```bash
chmod +x gerar_bi_automatico.sh
```

Usar:
```bash
./gerar_bi_automatico.sh /caminho/dados.xlsx "Fevereiro 2026"
```

## Próximas Etapas

1. ✅ Instalar dependências
2. ✅ Testar script com dados de exemplo
3. ✅ Criar rotina mensal
4. ✅ Documentar processo
5. ⏳ Considerar automação completa

## Checklist de Setup

- [ ] Python 3 instalado
- [ ] pandas instalado
- [ ] openpyxl instalado
- [ ] Script testado
- [ ] Logos presentes
- [ ] Primeira execução bem-sucedida
- [ ] HTML gerado corretamente
- [ ] Dados aparecem no dashboard

## Suporte

Para problemas:
1. Consulte README.md
2. Verifique GUIA_RAPIDO.md
3. Entre em contato com a Connecta

---

**Versão:** 1.0  
**Data:** Fevereiro 2026  
**Desenvolvido por:** Connecta
