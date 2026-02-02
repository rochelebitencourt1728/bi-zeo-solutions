#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para converter Dashboard HTML para PDF
"""

from weasyprint import HTML, CSS
import sys
import os
from datetime import datetime

def converter_html_para_pdf(arquivo_html, arquivo_saida=None):
    """
    Converte arquivo HTML para PDF
    
    Args:
        arquivo_html: Caminho do arquivo HTML
        arquivo_saida: Caminho do arquivo PDF de saída (opcional)
    """
    
    # Validar arquivo de entrada
    if not os.path.exists(arquivo_html):
        print(f"✗ Arquivo não encontrado: {arquivo_html}")
        return False
    
    # Definir arquivo de saída
    if arquivo_saida is None:
        nome_base = os.path.splitext(os.path.basename(arquivo_html))[0]
        arquivo_saida = f"{nome_base}_{datetime.now().strftime('%d%m%Y')}.pdf"
    
    try:
        print(f"📄 Convertendo: {arquivo_html}")
        print(f"💾 Salvando em: {arquivo_saida}")
        
        # Converter HTML para PDF
        HTML(arquivo_html).write_pdf(arquivo_saida)
        
        # Verificar tamanho do arquivo
        tamanho_kb = os.path.getsize(arquivo_saida) / 1024
        
        print(f"✓ PDF gerado com sucesso!")
        print(f"  Arquivo: {arquivo_saida}")
        print(f"  Tamanho: {tamanho_kb:.1f} KB")
        
        return True
        
    except Exception as e:
        print(f"✗ Erro ao converter: {e}")
        return False

def main():
    """Função principal"""
    
    if len(sys.argv) < 2:
        print("Uso: python3 html_para_pdf.py <arquivo_html> [arquivo_saida.pdf]")
        print("\nExemplos:")
        print("  python3 html_para_pdf.py dashboard_premium.html")
        print("  python3 html_para_pdf.py dashboard_premium.html meu_dashboard.pdf")
        sys.exit(1)
    
    arquivo_html = sys.argv[1]
    arquivo_saida = sys.argv[2] if len(sys.argv) > 2 else None
    
    sucesso = converter_html_para_pdf(arquivo_html, arquivo_saida)
    sys.exit(0 if sucesso else 1)

if __name__ == "__main__":
    main()
