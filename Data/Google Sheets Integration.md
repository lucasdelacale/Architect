# Google Sheets Integration — WPP Smart-Fit-NET D-1

**Tipo**: Integração de dados
**Data**: 2026-08-10
**Última atualização**: 2026-08-11 (v2.0 — cache e refresh automático)
**Versão**: 2.0
**Status**: Implementado

---

## Visão Geral

Integração com Google Sheets para acesso automatizado à base de dados oficial D-1 e abas de controle por plataforma, substituindo o download manual do arquivo Excel.

---

## Componentes

### Google Sheets
- **ID**: `1qJn7qBhEmKV5wbsqrDQ-9o5WKQZ2x5EcZNanDNDwzM4`
- **Link de acesso**: [https://docs.google.com/spreadsheets/d/1qJn7qBhEmKV5wbsqrDQ-9o5WKQZ2x5EcZNanDNDwzM4/](https://docs.google.com/spreadsheets/d/1qJn7qBhEmKV5wbsqrDQ-9o5WKQZ2x5EcZNanDNDwzM4/)
- **Estrutura**: planilha com abas separadas (dados + controle por plataforma)

### Scripts de Integração
- **Script multi-aba (v2.0)**: `architect/data/google_sheets_multi_loader.py`
  - Função: carrega dados de todas as abas (Database + controle) com cache inteligente
  - Retorna: tupla `(d1_data, control_data)` — DataFrame D-1 + dicionário de DataFrames por plataforma
  - Cache: em memória (TTL configurável) e em disco (JSON persistido)
  - Dependências: `pandas`, `requests`
- **Script principal (legado)**: `architect/data/google_sheets_loader.py`
  - Função: carrega apenas dados da aba Database
  - Nota: substituído pelo multi-aba para uso geral

### Configuração
- **Localização**: `architect/config/sheets_config.json`
- **Conteúdo**: ID da planilha, credenciais, parâmetros de carregamento

---

## Estrutura Multi-aba (NOVO)

A planilha Google Sheets foi expandida para incluir abas de controle por plataforma:

| Aba | Plataforma | Descrição | Colunas de Controle |
|---|---|---|---|
| `Database` | Dados D-1 | Resultados diários por veículo/campanha | 14 colunas (A–N) |
| `Google Ads \| NET` | Google Ads | Controle de planejamento | Projetado, CPA Plan, Conversões Plan, Pacing |
| `DV360 \| NET` | DV360 | Controle de planejamento | Projetado, CPA Plan, Conversões Plan, Pacing |
| `FACEBOOK Ads\| NET` | Meta Ads | Controle de planejamento | Projetado, CPA Plan, Conversões Plan, Pacing |
| `TIKTOK Ads\| NET` | TikTok Ads | Controle de planejamento | Projetado, CPA Plan, Conversões Plan, Pacing |
| `BING Ads\| NET` | Bing Ads | Controle de planejamento | Projetado, CPA Plan, Conversões Plan, Pacing |

### Vantagem dos Dados de Controle

- **Benchmarks integrados**: comparação direta entre performance real (D-1) e planejamento
- **Pacing**: acompanhamento de execução do orçamento por plataforma
- **CPA Plan**: referência de custo por aquisição planejado
- **Conversões Plan**: meta de conversões por plataforma
- **Análise integrada**: permite identificar desvios sem necessidade de fontes externas

---

## Vantagens

1. **Atualização automática**: dados sempre frescos, sem necessidade de download manual
2. **Acesso colaborativo**: múltiplos usuários podem acessar simultaneamente
3. **Histórico de versões**: Google Sheets mantém histórico de alterações
4. **API robusta**: interface programática para automações
5. **Backup automático**: dados na nuvem com redundância do Google
6. **Dados de controle integrados**: benchmarks de planejamento por plataforma
7. **Cache inteligente (v2.0)**: performance otimizada com cache em memória e disco
8. **Refresh automático (v2.0)**: funções para forçar atualização de dados
9. **Métricas de performance (v2.0)**: contagem de hits, misses e taxa de acerto

---

## Cache e Performance (v2.0)

O script `google_sheets_multi_loader.py` v2.0 utiliza cache inteligente para otimizar performance:

- **Cache em memória**: TTL configurável (padrão: 5 minutos / 300 segundos)
- **Cache em disco**: persistência JSON em `architect/data/cache/`
- **Refresh automático**: funções para forçar atualização seletiva ou total
- **Métricas**: contagem de hits, misses, taxa de acerto e tamanho do cache

### Uso do Cache

```python
from architect.data.google_sheets_multi_loader import (
    load_all_sheets_data,
    refresh_data,
    refresh_all_data,
    get_cache_metrics,
    set_cache_ttl
)

# Carregar com cache (default — sempre recomendado)
d1, control = load_all_sheets_data()

# Carregar sem cache (forçar requisição à API)
d1, control = load_all_sheets_data(use_cache=False)

# Forçar refresh de plataforma específica
google_data = refresh_data("google")

# Forçar refresh de todos os dados
d1, control = refresh_all_data()

# Ver métricas de performance
metrics = get_cache_metrics()
print(f"Taxa de acerto: {metrics['hit_rate_percent']}%")
print(f"Entradas: {metrics['cache_size_entries']}")
print(f"Tamanho: {metrics['cache_size_mb']} MB")

# Configurar TTL (em segundos)
set_cache_ttl(600)  # 10 minutos
```

### Estrutura do Cache em Disco

```
architect/data/cache/
├── sheet_0_database.json
├── sheet_0_google.json
├── sheet_0_dv360.json
├── sheet_0_facebook.json
├── sheet_0_tiktok.json
└── sheet_0_bing.json
```

Cada arquivo JSON contém: `data` (records), `columns` (lista de colunas) e `timestamp` (última atualização).

### Quando usar cada modo

| Cenário | Modo recomendado |
|---|---|
| Consulta normal / análise | `use_cache=True` (default) |
| Dados atualizados pós-upload | `refresh_all_data()` |
| Verificação de plataforma específica | `refresh_data("google")` |
| Debug / validação | `use_cache=False` |
| Monitoramento de performance | `get_cache_metrics()` |

---

## Uso

### Via Script Python (aba Database)
```python
from architect.data.google_sheets_loader import load_data

df = load_data()
```

### Via Script Python (multi-aba — v2.0 com cache)
```python
from architect.data.google_sheets_multi_loader import load_all_sheets_data

# Carrega com cache inteligente (default)
sheets_d1, sheets_control = load_all_sheets_data()

# Acessar dados D-1
df_database = sheets_d1

# Acessar dados de controle por plataforma
df_google_ads = sheets_control['google']
df_dv360 = sheets_control['dv360']
df_meta = sheets_control['facebook']
df_tiktok = sheets_control['tiktok']
df_bing = sheets_control['bing']
```

### Via Script Python (funções avançadas v2.0)
```python
from architect.data.google_sheets_multi_loader import (
    load_d1_data,
    load_platform_control,
    get_campaign_benchmarks,
    refresh_data,
    get_cache_metrics,
    test_connection
)

# Carregar apenas dados D-1
d1_df = load_d1_data()

# Buscar benchmarks de uma campanha específica
benchmarks = get_campaign_benchmarks('ID-467')

# Forçar refresh de dados atualizados
refresh_data("google")

# Verificar métricas do cache
metrics = get_cache_metrics()
```

### Via Architect
O script é integrado automaticamente quando o Architect precisa de dados D-1 ou de controle.

---

## Compatibilidade

- **Estrutura Database**: idêntica à base Excel (mesmas 14 colunas)
- **Granularidade Database**: diária, por veículo/campanha
- **Volume Database**: 10.239 linhas carregadas (teste inicial)
- **Abas de controle**: dados de planejamento por plataforma
- **Testes**: 9/9 aprovados (script principal)

---

## Manutenção

### Atualização da Planilha
- O usuário continua atualizando a planilha manualmente
- O script detecta novos dados automaticamente

### Monitoramento
- Verificar erros de conexão periodicamente
- Monitorar autenticação da API do Google Sheets

---

## Backup

A base Excel local é mantida como backup:
- **Arquivo**: `WPP_Smart-Fit-NET_DataBase_D-1.xlsx`
- **Localização**: `Campanhas/Dados/Database/`
- **Uso**: fallback em caso de indisponibilidade do Google Sheets

---

## Troubleshooting

### Erros Comuns

| Erro | Causa | Solução |
|------|-------|---------|
| `APIError: 403` | Credenciais inválidas ou permissão negada | Verificar `sheets_config.json` e permissões da planilha |
| `APIError: 404` | ID da planilha incorreto | Verificar ID em `sheets_config.json` |
| `TimeoutError` | Planilha muito grande ou lentidão da API | Aumentar timeout ou dividir dados |
| `ModuleNotFoundError` | Dependências não instaladas | Executar `pip install pandas requests` |
| `ConnectionError` | Sem acesso à internet ou planilha privada | Verificar conexão e permissões da planilha |
| `EmptyDataError` | Aba vazia ou GID incorreto | Verificar GID da aba no navegador |
| `CacheExpired` | Cache expirado (TTL atingido) | Dados serão recarregados automaticamente |
| `CacheWriteError` | Falha ao gravar cache em disco | Verificar permissões em `architect/data/cache/` |

### Verificação de Saúde

1. **Testar conexão**:
   ```python
   from architect.data.google_sheets_multi_loader import test_connection
   test_connection()
   ```

2. **Verificar dados**:
   ```python
   from architect.data.google_sheets_multi_loader import load_all_sheets_data
   d1, control = load_all_sheets_data()
   print(f"Linhas D-1: {len(d1)}")
   print(f"Plataformas: {list(control.keys())}")
   ```

3. **Verificar cache**:
   ```python
   from architect.data.google_sheets_multi_loader import get_cache_metrics
   metrics = get_cache_metrics()
   print(f"Taxa de acerto: {metrics['hit_rate_percent']}%")
   ```

4. **Forçar refresh se necessário**:
   ```python
   from architect.data.google_sheets_multi_loader import refresh_all_data
   d1, control = refresh_all_data()
   ```

5. **Logs**: Verificar `architect/logs/sheets_loader.log` para detalhes

### Contato

Para problemas persistentes, verificar:
- Status da API do Google Sheets: https://status.cloud.google.com/
- Documentação gspread: https://docs.gspread.org/

---

## Conexões

- [[Data/Fonte de dados oficial - WPP Smart-Fit-NET D-1]]
- [[Architecture/Architect Architecture v1]]
- [[Install/Architect Install 1.0]]
- [[Install/Architect Manual de Uso 1.0]]

---

## Histórico

| Data | Evento |
|---|---|
| 2026-08-10 | Implementação inicial da integração com Google Sheets |
| 2026-08-10 | Testes aprovados (9/9), 10.239 linhas carregadas |
| 2026-08-10 | Documentação completa e troubleshooting adicionado |
| 2026-08-11 | Expansão para multi-aba. Script `google_sheets_multi_loader.py` criado. Abas de controle adicionadas (Google Ads, DV360, Meta, TikTok, Bing). Benchmarks integrados para análise vs. planejado. |
| 2026-08-11 | **v2.0**: Cache em memória/disco, refresh automático, métricas de performance. Dependências migradas para `pandas` + `requests`. |