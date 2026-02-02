#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para gerar BI mensal da Zeo Solutions
Mantém o padrão visual e atualiza os dados automaticamente
"""

import pandas as pd
import base64
import json
from datetime import datetime
import sys
import os

class GeradorBIMensal:
    def __init__(self, arquivo_excel, mes_ano, diretorio_saida=None):
        """
        Inicializa o gerador de BI mensal
        
        Args:
            arquivo_excel: Caminho do arquivo Excel com os dados
            mes_ano: Mês e ano no formato "Janeiro 2026" ou "Fevereiro 2026"
            diretorio_saida: Diretório onde salvar o HTML (padrão: diretório atual)
        """
        self.arquivo_excel = arquivo_excel
        self.mes_ano = mes_ano
        self.diretorio_saida = diretorio_saida or os.getcwd()
        self.dados = None
        self.receitas = 0
        self.custos = 0
        self.despesas = 0
        self.resultado = 0
        
    def carregar_dados(self):
        """Carrega dados do arquivo Excel"""
        try:
            df = pd.read_excel(self.arquivo_excel, sheet_name='Realizado')
            self.dados = df
            print(f"✓ Dados carregados com sucesso de {self.arquivo_excel}")
            return True
        except Exception as e:
            print(f"✗ Erro ao carregar arquivo: {e}")
            return False
    
    def processar_dados(self):
        """Processa e extrai dados financeiros"""
        if self.dados is None:
            print("✗ Dados não carregados. Execute carregar_dados() primeiro.")
            return False
        
        try:
            # Extrair valores da primeira coluna de dados (Janeiro, Fevereiro, etc)
            # Ajuste conforme necessário baseado na estrutura do seu Excel
            for idx, row in self.dados.iterrows():
                resultado = str(row['Resultado']).strip() if 'Resultado' in row else ""
                jan_value = row['Jan'] if 'Jan' in row else 0
                
                if pd.isna(jan_value):
                    jan_value = 0
                
                if 'RECEITAS OPERACIONAIS' in resultado:
                    self.receitas = abs(float(jan_value))
                elif 'CUSTOS OPERACIONAIS' in resultado:
                    self.custos = abs(float(jan_value))
                elif 'DESPESAS OPERACIONAIS' in resultado and 'RESULTADO' not in resultado:
                    self.despesas = abs(float(jan_value))
                elif 'RESULTADO OPERACIONAL' in resultado:
                    self.resultado = abs(float(jan_value))
            
            print(f"✓ Dados processados:")
            print(f"  - Receitas: R$ {self.receitas:,.2f}")
            print(f"  - Custos: R$ {self.custos:,.2f}")
            print(f"  - Despesas: R$ {self.despesas:,.2f}")
            print(f"  - Resultado: R$ {self.resultado:,.2f}")
            return True
        except Exception as e:
            print(f"✗ Erro ao processar dados: {e}")
            return False
    
    def carregar_logos_base64(self):
        """Carrega logos e converte para base64"""
        try:
            # Caminhos dos logos (ajuste conforme necessário)
            logo_connecta_path = os.path.join(os.path.dirname(__file__), '..', 'logo_connecta.png')
            logo_zeo_path = os.path.join(os.path.dirname(__file__), '..', 'logo_zeo.jpg')
            
            with open(logo_connecta_path, 'rb') as f:
                connecta_b64 = base64.b64encode(f.read()).decode()
            
            with open(logo_zeo_path, 'rb') as f:
                zeo_b64 = base64.b64encode(f.read()).decode()
            
            print("✓ Logos carregados com sucesso")
            return f"data:image/png;base64,{connecta_b64}", f"data:image/jpeg;base64,{zeo_b64}"
        except Exception as e:
            print(f"✗ Erro ao carregar logos: {e}")
            return None, None
    
    def gerar_html(self):
        """Gera o arquivo HTML do dashboard"""
        logo_connecta, logo_zeo = self.carregar_logos_base64()
        if not logo_connecta or not logo_zeo:
            print("✗ Não foi possível carregar os logos")
            return False
        
        # Calcular percentuais
        total_custo_despesa = self.custos + self.despesas
        pct_custos = (self.custos / total_custo_despesa * 100) if total_custo_despesa > 0 else 0
        pct_despesas = (self.despesas / total_custo_despesa * 100) if total_custo_despesa > 0 else 0
        
        margem = self.receitas - self.custos
        pct_margem = (margem / self.receitas * 100) if self.receitas > 0 else 0
        
        # Template HTML (versão simplificada - use o dashboard_premium.html como base)
        html_content = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resultado Mensal - Zeo Solutions - {self.mes_ano}</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@3.9.1"></script>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            min-height: 100vh;
            padding: 20px;
        }}
        
        .container {{
            max-width: 1600px;
            margin: 0 auto;
        }}
        
        .header {{
            background: linear-gradient(135deg, #5A4A3A 0%, #3D3428 100%);
            color: white;
            padding: 30px;
            border-radius: 10px;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 20px;
        }}
        
        .header-logos {{
            display: flex;
            gap: 20px;
            align-items: center;
        }}
        
        .header-logos img {{
            height: 60px;
            object-fit: contain;
        }}
        
        .header-content {{
            flex: 1;
        }}
        
        .header h1 {{
            font-size: 32px;
            margin-bottom: 10px;
            color: #D4A574;
        }}
        
        .header p {{
            font-size: 16px;
            opacity: 0.9;
        }}
        
        .dashboard-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}
        
        .card {{
            background: white;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
        }}
        
        .card-title {{
            font-size: 14px;
            color: #666;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 10px;
            font-weight: 600;
        }}
        
        .card-value {{
            font-size: 32px;
            font-weight: bold;
            color: #111;
            margin-bottom: 5px;
        }}
        
        .card-value.positive {{
            color: #27AE60;
        }}
        
        .card-value.negative {{
            color: #C41E3A;
        }}
        
        .card-subtitle {{
            font-size: 12px;
            color: #999;
        }}
        
        .footer {{
            text-align: center;
            color: #666;
            font-size: 12px;
            margin-top: 40px;
            padding: 20px;
            background: white;
            border-radius: 10px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="header-logos">
                <img src="{logo_connecta}" alt="Connecta" title="Connecta">
                <img src="{logo_zeo}" alt="Zeo Solutions" title="Zeo Solutions">
            </div>
            <div class="header-content">
                <h1>Resultado Mensal - Zeo Solutions</h1>
                <p>Dashboard Financeiro - {self.mes_ano} | Atualizado em {datetime.now().strftime('%d de %B de %Y')}</p>
            </div>
        </div>
        
        <div class="dashboard-grid">
            <div class="card">
                <div class="card-title">Total de Receitas</div>
                <div class="card-value positive">R$ {self.receitas:,.2f}</div>
                <div class="card-subtitle">Receitas Operacionais</div>
            </div>
            
            <div class="card">
                <div class="card-title">Total de Custos</div>
                <div class="card-value negative">R$ {self.custos:,.2f}</div>
                <div class="card-subtitle">Custos Operacionais</div>
            </div>
            
            <div class="card">
                <div class="card-title">Total de Despesas</div>
                <div class="card-value negative">R$ {self.despesas:,.2f}</div>
                <div class="card-subtitle">Despesas Operacionais</div>
            </div>
            
            <div class="card">
                <div class="card-title">Resultado Operacional</div>
                <div class="card-value negative">R$ {self.resultado:,.2f}</div>
                <div class="card-subtitle">Receitas - Custos - Despesas</div>
            </div>
            
            <div class="card">
                <div class="card-title">Margem de Contribuição</div>
                <div class="card-value {'positive' if margem > 0 else 'negative'}">R$ {margem:,.2f}</div>
                <div class="card-subtitle">{pct_margem:.2f}% da Receita</div>
            </div>
            
            <div class="card">
                <div class="card-title">Custo Total</div>
                <div class="card-value negative">R$ {self.custos + self.despesas:,.2f}</div>
                <div class="card-subtitle">Custos + Despesas</div>
            </div>
        </div>
        
        <div class="footer">
            <p>📊 Resultado Mensal - Zeo Solutions | {self.mes_ano}</p>
            <p>Dashboard Financeiro - Todos os valores em Reais (R$)</p>
            <p>Gerado automaticamente em {datetime.now().strftime('%d/%m/%Y às %H:%M:%S')}</p>
        </div>
    </div>
</body>
</html>"""
        
        # Salvar arquivo
        nome_arquivo = f"Resultado_Mensal_ZEO_{self.mes_ano.replace(' ', '_')}.html"
        caminho_saida = os.path.join(self.diretorio_saida, nome_arquivo)
        
        try:
            with open(caminho_saida, 'w', encoding='utf-8') as f:
                f.write(html_content)
            print(f"✓ Dashboard gerado com sucesso: {caminho_saida}")
            return True
        except Exception as e:
            print(f"✗ Erro ao salvar arquivo: {e}")
            return False
    
    def executar(self):
        """Executa todo o processo de geração"""
        print(f"\n{'='*60}")
        print(f"Gerando BI Mensal - {self.mes_ano}")
        print(f"{'='*60}\n")
        
        if not self.carregar_dados():
            return False
        
        if not self.processar_dados():
            return False
        
        if not self.gerar_html():
            return False
        
        print(f"\n{'='*60}")
        print("✓ BI Mensal gerado com sucesso!")
        print(f"{'='*60}\n")
        return True


def main():
    """Função principal"""
    if len(sys.argv) < 3:
        print("Uso: python3 gerar_bi_mensal.py <arquivo_excel> <mes_ano>")
        print("Exemplo: python3 gerar_bi_mensal.py dados_janeiro.xlsx 'Janeiro 2026'")
        sys.exit(1)
    
    arquivo_excel = sys.argv[1]
    mes_ano = sys.argv[2]
    
    if not os.path.exists(arquivo_excel):
        print(f"✗ Arquivo não encontrado: {arquivo_excel}")
        sys.exit(1)
    
    gerador = GeradorBIMensal(arquivo_excel, mes_ano)
    sucesso = gerador.executar()
    sys.exit(0 if sucesso else 1)


if __name__ == "__main__":
    main()
