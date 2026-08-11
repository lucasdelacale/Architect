"""
Exemplo de uso do Google Sheets Multi-Sheet Loader
Demonstra como utilizar as principais funções do módulo.
"""

import sys
import os

# Adicionar o diretório atual ao path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

from google_sheets_multi_loader import (
    load_all_sheets_data,
    load_d1_data,
    load_platform_control,
    get_campaign_benchmarks,
    test_connection
)


def main():
    print("=== Exemplo de Uso: Google Sheets Multi-Sheet Loader ===\n")
    
    # 1. Testar conexão
    print("1. Testando conexão...")
    if not test_connection():
        print("   FALHA na conexao")
        return
    print("   OK Conexao\n")
    
    # 2. Carregar dados D-1
    print("2. Carregando dados D-1 (performance)...")
    d1_data = load_d1_data()
    print(f"   OK {len(d1_data)} linhas carregadas")
    print(f"   Colunas: {list(d1_data.columns)}\n")
    
    # 3. Carregar dados de controle do Google Ads
    print("3. Carregando dados de controle do Google Ads...")
    google_control = load_platform_control("google")
    print(f"   OK {len(google_control)} campanhas carregadas")
    print(f"   Colunas: {list(google_control.columns)}\n")
    
    # 4. Carregar todos os dados
    print("4. Carregando todos os dados...")
    d1, control_data = load_all_sheets_data()
    print(f"   OK Dados D-1: {len(d1)} linhas")
    print(f"   OK Plataformas carregadas: {list(control_data.keys())}")
    for platform, df in control_data.items():
        print(f"     - {platform}: {len(df)} linhas")
    print()
    
    # 5. Buscar benchmarks de uma campanha específica
    print("5. Buscando benchmarks de campanha...")
    # Nota: Use um ID de campanha real da sua planilha
    example_id = "467"  # Substitua por um ID real
    benchmarks = get_campaign_benchmarks(example_id)
    
    if benchmarks['found_in']:
        print(f"   OK Campanha {example_id} encontrada em: {', '.join(benchmarks['found_in'])}")
        print(f"   Nome: {benchmarks['campanha']}")
        print(f"   Funil: {benchmarks['funil']}")
        print(f"   Projetado: R$ {benchmarks['projetado']:.2f}" if benchmarks['projetado'] else "   Projetado: N/A")
        print(f"   CPA Plan: R$ {benchmarks['cpa_plan']:.2f}" if benchmarks['cpa_plan'] else "   CPA Plan: N/A")
        print(f"   Conversões Plan: {benchmarks['conv_plan']}" if benchmarks['conv_plan'] else "   Conversões Plan: N/A")
    else:
        print(f"   FALHA Campanha {example_id} nao encontrada")
    
    print("\n=== Exemplo Concluído ===")


if __name__ == "__main__":
    main()