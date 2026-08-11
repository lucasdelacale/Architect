# Google Sheets Multi-Sheet Integration

**Tipo**: Integração de dados  
**Data**: 2026-08-11  
**Status**: Implementado  
**Versão**: 3.0

---

## Visão Geral

Integração avançada com Google Sheets para acesso automatizado a múltiplas abas de uma planilha pública. Esta versão suporta carregamento de dados de performance (D-1) e dados de controle por plataforma de mídia digital.

---

## Funcionalidades

### 1. Carregamento Multi-Sheet
- **Dados D-1**: Performance diária por veículo/campanha
- **Dados de Controle**: Benchmarks por plataforma (Google Ads, DV360, Facebook, TikTok, Bing)

### 2. Cache Inteligente
- **Cache em memória**: TTL configurável (padrão: 5 minutos)
- **Cache em disco**: Persistência para uso offline
- **Invalidação automática**: Dados expirados são removidos
- **Métricas de performance**: Contagem de hits, misses e taxa de acerto

### 3. Consultas Específicas
- Busca de benchmarks por ID de campanha
- Filtro por plataforma específica
- Validação automática de estrutura

### 4. Tratamento de Erros
- Fallback automático entre GID e nome da aba
- Logging detalhado para diagnóstico
- Tratamento de conexão e dados vazios

### 5. Refresh Automático
- Função para forçar atualização de dados
- Invalidação seletiva por plataforma
- Logs de quando o cache foi atualizado

### 6. Tratamento de Linha de Total
- **Identificação automática**: Linha 2 (após cabeçalho) é sempre o total da plataforma
- **Separação de dados**: DataFrame `platform_totals` (total) e `campaign_details` (campanhas)
- **Flag is_total**: Indica se a linha é total ou campanha individual
- **Métricas corretas**: Soma para métricas acumuladas, média para métricas de performance

---

## Sistema de Cache

### Arquitetura

O sistema de cache implementado oferece duas camadas de persistência:

1. **Cache em Memória**: Acesso rápido durante a sessão
2. **Cache em Disco**: Persistência para uso offline e entre sessões

### Configuração

```python
from architect.data.google_sheets_multi_loader import _cache, set_cache_ttl

# Configurar TTL do cache (padrão: 300 segundos = 5 minutos)
set_cache_ttl(600)  # 10 minutos

# Ou acessar diretamente
_cache.ttl = 600
```

### Métricas de Performance

```python
from architect.data.google_sheets_multi_loader import get_cache_metrics

metrics = get_cache_metrics()
print(f"Entradas no cache: {metrics['cache_size_entries']}")
print(f"Tamanho do cache: {metrics['cache_size_mb']} MB")
print(f"Total de requisições: {metrics['total_requests']}")
print(f"Cache hits: {metrics['cache_hits']}")
print(f"Taxa de acerto: {metrics['hit_rate_percent']}%")
```

### Controle de Cache

```python
from architect.data.google_sheets_multi_loader import (
    refresh_data,
    refresh_all_data,
    clear_cache_metrics
)

# Refresh de plataforma específica (ignora cache)
google_data = refresh_data("google")

# Refresh de todos os dados (invalida todo o cache)
d1, control = refresh_all_data()

# Limpar métricas de performance
clear_cache_metrics()
```

### Uso Opcional do Cache

Todas as funções de carregamento suportam o parâmetro `use_cache`:

```python
from architect.data.google_sheets_multi_loader import load_d1_data, load_platform_control

# Carregar com cache (padrão)
d1_data = load_d1_data(use_cache=True)

# Carregar sem cache (sempre busca dados atualizados)
d1_data = load_d1_data(use_cache=False)

# Carregar plataforma específica sem cache
google_data = load_platform_control("google", use_cache=False)
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

Cada arquivo JSON contém:
- `data`: Dados em formato JSON (records)
- `columns`: Lista de colunas do DataFrame
- `timestamp`: Timestamp da última atualização

---

## Estrutura da Planilha

### Estrutura das Abas de Controle

Cada aba de controle possui a seguinte estrutura:

| Linha | Conteúdo | Descrição |
|-------|----------|-----------|
| 1 | Cabeçalho | Nomes das colunas |
| 2 | **TOTAL da plataforma** | Soma ou média das campanhas |
| 3+ | Campanhas individuais | Dados de cada campanha |

**Importante**: A linha 2 é sempre o total da plataforma e será tratada separadamente pelo script.

### Abas Suportadas

| Aba | GID | Conteúdo |
|-----|-----|----------|
| Database | 0 | Dados D-1 (performance) |
| Google Ads \| NET | - | Controle Google Ads |
| DV360 \| NET | - | Controle DV360 |
| FACEBOOK Ads\| NET | - | Controle Facebook |
| TIKTOK Ads\| NET | - | Controle TikTok |
| BING Ads\| NET | - | Controle Bing |

### Colunas Dados D-1

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| date | string | Data (DD/MM/AAAA) |
| id | string | ID da campanha |
| tx_vehicle | string | Nome do veículo |
| tx_funnel | string | Funil de conversão |
| Investimento | float | Valor investido |
| Impressoes | int | Impressões |
| Cliques | int | Cliques |
| Sessoes_GA4 | int | Sessões GA4 |
| Sessoes_App | int | Sessões App |
| sessoes_totais | int | Sessões totais |
| conversoes_app | int | Conversões App |
| conversoes_ga4 | int | Conversões GA4 |
| conversoes_totais | int | Conversões totais |
| instalacoes | int | Instalações |

### Colunas Dados de Controle (Estrutura Real)

| Coluna | Tipo | Descrição | Tipo de Métrica |
|--------|------|-----------|-----------------|
| Campanha | string | Nome da campanha | - |
| Funil | string | AWARENESS/CONSIDERAÇÃO/CONVERSÃO | - |
| Tipo | string | Tipo da campanha | - |
| Nº | string | ID da campanha | - |
| Audiência | string | Segmentação de audiência | - |
| Projetado | float | Investimento mensal planejado | **SOMA** |
| Custo | float | Investimento realizado | **SOMA** |
| Sobra | float | Diferença entre projetado e realizado | **SOMA** |
| Consumo ontem | float | Consumo do dia anterior | **SOMA** |
| Investimento Diarizado | float | Investimento diário | **SOMA** |
| Pacing | float | % do budget gasto | **MÉDIA** |
| MTD | float | Month to Date | **SOMA** |
| % Desvio Consumo X planejado | float | Percentual de desvio | **MÉDIA** |
| Diarizado ajustado | float | Investimento diário ajustado | - |
| Linear | float | Referência linear | **SOMA** |
| Diferença Plan X Realizado | float | Diferença entre planejado e realizado | **SOMA** |
| compensado | float | Valor compensado | **SOMA** |
| CPA | float | CPA realizado | **MÉDIA** |
| Conv. | int | Conversões realizadas | **SOMA** |
| CPA Plan | float | CPA planejado | **MÉDIA** |
| Conversões Plan | int | Conversões planejadas | **SOMA** |

---

## Uso

### Instalação

```bash
# Instalar dependências
pip install pandas requests

# Ou usar requirements.txt
echo "pandas>=1.3.0" >> requirements.txt
echo "requests>=2.26.0" >> requirements.txt
```

### Exemplos Básicos

#### 1. Carregar Todos os Dados

```python
from architect.data.google_sheets_multi_loader import load_all_sheets_data

# Carregar dados D-1 e controle
d1_data, control_data = load_all_sheets_data()

print(f"Dados D-1: {len(d1_data)} linhas")
print(f"Plataformas carregadas: {list(control_data.keys())}")
```

#### 2. Carregar Dados Específicos

```python
from architect.data.google_sheets_multi_loader import load_d1_data, load_platform_control

# Apenas dados D-1
d1_df = load_d1_data()

# Apenas dados de controle do Google Ads
google_control = load_platform_control("google")
print(google_control[['Campanha', 'Projetado', 'CPA Plan', 'Conversões Plan']])
```

#### 3. Buscar Benchmarks de Campanha

```python
from architect.data.google_sheets_multi_loader import get_campaign_benchmarks

# Buscar benchmarks por ID
benchmarks = get_campaign_benchmarks('ID-467')

if benchmarks['found_in']:
    print(f"Campanha encontrada em: {', '.join(benchmarks['found_in'])}")
    print(f"CPA Plan: {benchmarks['cpa_plan']}")
    print(f"Conversões Plan: {benchmarks['conv_plan']}")
    print(f"Projetado: {benchmarks['projetado']}")
```

#### 4. Testar Conexão

```python
from architect.data.google_sheets_multi_loader import test_connection

if test_connection():
    print("Conexão OK")
else:
    print("Falha na conexão - verificar planilha pública")
```

### Exemplo Completo

```python
from architect.data.google_sheets_multi_loader import (
    load_all_sheets_data,
    get_campaign_benchmarks,
    test_connection,
    load_platform_totals,
    get_platform_summary,
    calculate_platform_metrics
)

def main():
    # 1. Testar conexão
    if not test_connection():
        print("Erro: Não foi possível conectar à planilha")
        return
    
    # 2. Carregar todos os dados
    print("Carregando dados...")
    d1_data, control_data = load_all_sheets_data()
    
    # 3. Analisar dados D-1
    print(f"\n=== Dados D-1 ===")
    print(f"Total de registros: {len(d1_data)}")
    print(f"Colunas: {list(d1_data.columns)}")
    
    # 4. Analisar dados de controle
    print(f"\n=== Dados de Controle ===")
    for platform, df in control_data.items():
        print(f"{platform}: {len(df)} campanhas")
    
    # 5. Buscar benchmarks específicos
    print(f"\n=== Benchmarks Campanha 467 ===")
    benchmarks = get_campaign_benchmarks("467")
    
    if benchmarks['found_in']:
        print(f"Plataformas: {benchmarks['found_in']}")
        print(f"Nome: {benchmarks['campanha']}")
        print(f"Funil: {benchmarks['funil']}")
        print(f"Projetado: R$ {benchmarks['projetado']:.2f}")
        print(f"CPA Plan: R$ {benchmarks['cpa_plan']:.2f}")
        print(f"Conversões Plan: {benchmarks['conv_plan']}")
    else:
        print("Campanha não encontrada")
    
    # 6. Exemplo de tratamento de linha de total
    print(f"\n=== Exemplo de Tratamento de Total ===")
    
    # Carregar totais da plataforma Google
    google_totals = load_platform_totals("google")
    print(f"Total da plataforma Google:")
    print(f"  Investimento Projetado: R$ {google_totals['Projetado'].iloc[0]:.2f}")
    print(f"  Investimento Realizado: R$ {google_totals['Custo'].iloc[0]:.2f}")
    
    # Carregar resumo completo
    google_summary = get_platform_summary("google")
    print(f"\nResumo completo Google:")
    print(f"  Total de campanhas: {google_summary['campaign_count']}")
    
    # Calcular métricas corretas
    google_metrics = calculate_platform_metrics("google")
    print(f"\nMétricas calculadas Google:")
    print(f"  Investimento Projetado: R$ {google_metrics['investimento_projetado']:.2f}")
    print(f"  Investimento Realizado: R$ {google_metrics['investimento_realizado']:.2f}")
    print(f"  Conversões Realizadas: {google_metrics['conversoes_realizadas']}")
    print(f"  Conversões Planejadas: {google_metrics['conversoes_planejadas']}")
    print(f"  Pacing Médio: {google_metrics['pacing_medio']:.2f}%")
    print(f"  CPA Médio: R$ {google_metrics['cpa_medio']:.2f}")
    print(f"  ROI Planejado: {google_metrics['roi_planejado']:.4f}")
    print(f"  ROI Realizado: {google_metrics['roi_realizado']:.4f}")

if __name__ == "__main__":
    main()
```

---

## API Reference

### Funções Principais

#### `load_all_sheets_data(use_cache=True)`

Carrega todos os dados da planilha.

**Parâmetros:**
- `use_cache` (bool): Se deve usar cache (padrão: True)

**Retorno:**
```python
Tuple[pd.DataFrame, Dict[str, pd.DataFrame]]
# (d1_data, control_data)
```

**Exceções:**
- `requests.exceptions.RequestException`: Erro de conexão
- `pd.errors.EmptyDataError`: Planilha vazia

---

#### `load_d1_data(use_cache=True)`

Carrega apenas dados D-1 (performance).

**Parâmetros:**
- `use_cache` (bool): Se deve usar cache (padrão: True)

**Retorno:**
```python
pd.DataFrame  # DataFrame com dados de performance
```

---

#### `load_platform_control(platform_name, use_cache=True)`

Carrega dados de controle de uma plataforma, excluindo a linha de total.

**Parâmetros:**
- `platform_name` (str): Nome da plataforma
  - Opções: `google`, `dv360`, `facebook`, `tiktok`, `bing`
- `use_cache` (bool): Se deve usar cache (padrão: True)

**Retorno:**
```python
pd.DataFrame  # DataFrame com campanhas individuais (exclui linha de total)
```

**Exceções:**
- `ValueError`: Plataforma não reconhecida

**Nota:** A linha 2 (após cabeçalho) é sempre o total da plataforma e será excluída deste DataFrame.

---

#### `load_platform_totals(platform_name, use_cache=True)`

Retorna DataFrame com apenas o total da plataforma.

**Parâmetros:**
- `platform_name` (str): Nome da plataforma
  - Opções: `google`, `dv360`, `facebook`, `tiktok`, `bing`
- `use_cache` (bool): Se deve usar cache (padrão: True)

**Retorno:**
```python
pd.DataFrame  # DataFrame com apenas a linha de total da plataforma
```

**Exceções:**
- `ValueError`: Plataforma não reconhecida

**Nota:** A linha 2 (após cabeçalho) é sempre o total da plataforma e será marcada com `is_total=True`.

---

#### `get_platform_summary(platform_name, use_cache=True)`

Retorna resumo completo: total + campanhas.

**Parâmetros:**
- `platform_name` (str): Nome da plataforma
  - Opções: `google`, `dv360`, `facebook`, `tiktok`, `bing`
- `use_cache` (bool): Se deve usar cache (padrão: True)

**Retorno:**
```python
Dict[str, Any]
# {
#     'totals': pd.DataFrame,  # Total da plataforma
#     'campaigns': pd.DataFrame,  # Campanhas individuais
#     'campaign_count': int  # Número de campanhas
# }
```

**Exceções:**
- `ValueError`: Plataforma não reconhecida

---

#### `calculate_platform_metrics(platform_name, use_cache=True)`

Calcula métricas da plataforma usando totais corretos.

**Parâmetros:**
- `platform_name` (str): Nome da plataforma
  - Opções: `google`, `dv360`, `facebook`, `tiktok`, `bing`
- `use_cache` (bool): Se deve usar cache (padrão: True)

**Retorno:**
```python
Dict[str, Any]
# {
#     'investimento_projetado': float,
#     'investimento_realizado': float,
#     'sobra': float,
#     'consumo_ontem': float,
#     'investimento_diarizado': float,
#     'mtd': float,
#     'linear': float,
#     'diferenca_plan_realizado': float,
#     'compensado': float,
#     'conversoes_realizadas': int,
#     'conversoes_planejadas': int,
#     'pacing_medio': float,
#     'desvio_medio': float,
#     'cpa_medio': float,
#     'cpa_plan_medio': float,
#     'desvio_percentual': float,
#     'roi_planejado': float,
#     'roi_realizado': float
# }
```

**Exceções:**
- `ValueError`: Plataforma não reconhecida

**Nota:** Métricas de soma (acumulado) são extraídas diretamente do total. Métricas de média são calculadas a partir das campanhas individuais.

---

#### `get_campaign_benchmarks(campaign_id, use_cache=True)`

Busca benchmarks de uma campanha específica.

**Parâmetros:**
- `campaign_id` (str): ID da campanha
- `use_cache` (bool): Se deve usar cache (padrão: True)

**Retorno:**
```python
Dict[str, Any]
# {
#     'campaign_id': str,
#     'platform': str,
#     'campanha': str,
#     'funil': str,
#     'projetado': float,
#     'cpa_plan': float,
#     'conv_plan': float,
#     'found_in': list
# }
```

---

#### `refresh_data(platform_name=None)`

Força refresh de dados, ignorando cache.

**Parâmetros:**
- `platform_name` (str): Nome da plataforma (None para todas)

**Retorno:**
```python
# Se platform_name especificado:
pd.DataFrame

# Se None:
Tuple[pd.DataFrame, Dict[str, pd.DataFrame]]
```

---

#### `refresh_all_data()`

Força refresh de todos os dados (invalida cache).

**Retorno:**
```python
Tuple[pd.DataFrame, Dict[str, pd.DataFrame]]
# (d1_data, control_data)
```

---

#### `get_cache_metrics()`

Retorna métricas do cache.

**Retorno:**
```python
Dict[str, Any]
# {
#     'cache_size_entries': int,
#     'cache_size_mb': float,
#     'request_count': int,
#     'total_requests': int,
#     'cache_hits': int,
#     'cache_misses': int,
#     'hit_rate_percent': float,
#     'ttl_seconds': int
# }
```

---

#### `set_cache_ttl(ttl_seconds)`

Configura o TTL do cache.

**Parâmetros:**
- `ttl_seconds` (int): Novo tempo de vida em segundos

---

#### `test_connection()`

Testa a conexão com a planilha.

**Retorno:**
```python
bool  # True se conexão OK, False caso contrário
```

---

## Configuração

### GIDs das Abas

Para obter os GIDs reais das abas:

1. Acesse a planilha no Google Sheets
2. Clique em uma aba
3. Observe o parâmetro `gid=` na URL do navegador
4. Atualize o dicionário `PLATFORM_GIDS` no script:

```python
PLATFORM_GIDS = {
    "database": "0",      # GID da aba Database
    "google": "123456",   # GID da aba Google Ads
    "dv360": "789012",    # GID da aba DV360
    "facebook": "345678", # GID da aba Facebook
    "tiktok": "901234",   # GID da aba TikTok
    "bing": "567890",     # GID da aba Bing
}
```

### Planilha Pública

Para que o script funcione, a planilha deve estar:

1. **Compartilhada publicamente**: Configurações de compartilhamento → "Qualquer pessoa com o link"
2. **Permissão de visualização**: Não é necessário editar, apenas visualizar

---

## Troubleshooting

### Erros Comuns

| Erro | Causa | Solução |
|------|-------|---------|
| `ConnectionError` | Sem acesso à internet ou planilha privada | Verificar conexão e permissões da planilha |
| `EmptyDataError` | Aba vazia ou GID incorreto | Verificar GID da aba no navegador |
| `KeyError` | Coluna esperada não encontrada | Verificar estrutura da planilha |
| `TimeoutError` | Planilha muito grande | Aumentar timeout ou dividir dados |

### Verificação de Saudade

```python
from architect.data.google_sheets_multi_loader import test_connection, load_all_sheets_data

# 1. Testar conexão
if not test_connection():
    print("Falha na conexão")
    exit(1)

# 2. Tentar carregar dados
try:
    d1, control = load_all_sheets_data()
    print(f"Dados D-1: {len(d1)} linhas")
    for platform, df in control.items():
        print(f"{platform}: {len(df)} linhas")
except Exception as e:
    print(f"Erro ao carregar dados: {e}")
```

### Logs

O script gera logs detalhados para diagnóstico:

```python
import logging
logging.basicConfig(level=logging.DEBUG)

# Agora as chamadas logarão detalhes
from architect.data.google_sheets_multi_loader import load_d1_data
d1 = load_d1_data()
```

---

## Dependências

```
pandas>=1.3.0
requests>=2.26.0
```

### Instalação

```bash
pip install pandas requests
```

---

## Compatibilidade

- **Python**: 3.8+
- **Planilha**: Google Sheets pública
- **Colunas**: Validação flexível (log de aviso para colunas faltando)
- **Volume**: Testado com 10.000+ linhas

---

## Próximos Passos

1. **Obter GIDs reais** das abas de controle
2. ~~**Configurar cache** para evitar requisições repetidas~~ ✅ Implementado
3. **Adicionar autenticação** (caso planilha deixe de ser pública)
4. ~~**Implementar refresh automático** periódico~~ ✅ Implementado
5. ~~**Tratar linha de total** da plataforma~~ ✅ Implementado

---

## Conexões

- [[Data/Google Sheets Integration]]
- [[Data/Fonte de dados oficial - WPP Smart-Fit-NET D-1]]
- [[Architecture/Architect Architecture v1]]

---

## Histórico

| Data | Evento |
|------|--------|
| 2026-08-10 | Implementação inicial com suporte multi-sheet |
| 2026-08-10 | Adicionadas funções de busca de benchmarks |
| 2026-08-10 | Documentação completa |
| 2026-08-11 | Versão 2.0: Adicionado cache em memória e disco, refresh automático e métricas |
| 2026-08-11 | Versão 3.0: Adicionado tratamento de linha de total da plataforma |