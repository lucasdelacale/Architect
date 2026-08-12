"""
Script de teste para o sistema de cache do Google Sheets Multi-Sheet Loader.
"""

from google_sheets_multi_loader import (
    get_cache_metrics,
    set_cache_ttl,
    refresh_all_data,
    clear_cache_metrics
)

def test_cache():
    """Testa as funcionalidades básicas do cache."""
    print("=== Teste do Sistema de Cache ===\n")
    
    # Testar métricas iniciais
    print("1. Métricas Iniciais:")
    metrics = get_cache_metrics()
    print(f"   Entradas no cache: {metrics['cache_size_entries']}")
    print(f"   Tamanho do cache: {metrics['cache_size_mb']} MB")
    print(f"   Total de requisições: {metrics['total_requests']}")
    print(f"   Cache hits: {metrics['cache_hits']}")
    print(f"   Taxa de acerto: {metrics['hit_rate_percent']}%")
    
    # Configurar TTL
    print("\n2. Configurando TTL:")
    set_cache_ttl(600)
    print(f"   Novo TTL: {get_cache_metrics()['ttl_seconds']}s")
    
    # Limpar métricas
    clear_cache_metrics()
    print("\n3. Métricas Limpas:")
    print(f"   Total de requisições: {get_cache_metrics()['total_requests']}")
    
    print("\n=== Teste Concluído ===")

if __name__ == "__main__":
    test_cache()
