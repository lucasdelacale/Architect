# Architect Data Module

Módulo de dados do Architect para integração com fontes externas.

## Componentes

### Google Sheets Multi-Sheet Loader (v2.0)

Integração com múltiplas abas de uma planilha Google Sheets pública, com cache inteligente e refresh automático.

**Arquivos:**
- `google_sheets_multi_loader.py` - Script principal de integração (v2.0)
- `GOOGLE_SHEETS_MULTI_INTEGRATION.md` - Documentação técnica completa
- `example_usage.py` - Exemplo de uso

**Funcionalidades:**
- Carregamento de dados D-1 (performance)
- Carregamento de dados de controle por plataforma
- Busca de benchmarks por campanha
- **Cache em memória** (TTL configurável) e **em disco** (JSON persistido)
- **Refresh automático** (seletivo por plataforma ou total)
- **Métricas de performance** (hits, misses, taxa de acerto)
- Tratamento de erros e fallback automático

### Google Sheets Loader (legado)

Script original para carregamento apenas da aba Database. Substituído pelo multi-aba para uso geral.

## Uso Rápido

```python
from data.google_sheets_multi_loader import load_all_sheets_data

# Carregar todos os dados (com cache)
d1_data, control_data = load_all_sheets_data()

# Acessar dados de controle do Google Ads
google_control = control_data['google']
print(google_control[['Campanha', 'Projetado', 'CPA Plan', 'Conversões Plan']])
```

## Uso Avançado (v2.0)

```python
from data.google_sheets_multi_loader import (
    refresh_all_data,
    get_cache_metrics,
    set_cache_ttl
)

# Forçar refresh de todos os dados
d1, control = refresh_all_data()

# Ver métricas do cache
metrics = get_cache_metrics()
print(f"Taxa de acerto: {metrics['hit_rate_percent']}%")

# Configurar TTL (10 minutos)
set_cache_ttl(600)
```

## Documentação

- `GOOGLE_SHEETS_MULTI_INTEGRATION.md` - Documentação técnica completa v2.0
- `Google Sheets Integration.md` - Visão geral da integração