# Fonte de dados oficial — WPP Smart-Fit-NET D-1

**Tipo**: Base de dados de campanhas
**Atualização**: Diária (D-1)
**Status**: Fonte oficial de dados/resultados

---

## Path

### Fonte Primária (Google Sheets) — v2.0 com Cache
- **Google Sheets público**: [https://docs.google.com/spreadsheets/d/1qJn7qBhEmKV5wbsqrDQ-9o5WKQZ2x5EcZNanDNDwzM4/](https://docs.google.com/spreadsheets/d/1qJn7qBhEmKV5wbsqrDQ-9o5WKQZ2x5EcZNanDNDwzM4/)
- **Script multi-aba (v2.0)**: `architect/data/google_sheets_multi_loader.py` — cache inteligente, refresh automático, métricas
- **Script legado**: `architect/data/google_sheets_loader.py` — carrega apenas aba Database
- **Configuração**: `architect/config/sheets_config.json`
- **Cache**: em memória (TTL 5min) e em disco (`architect/data/cache/`)
- **Vantagens**: atualização automática, cache para performance, refresh sob demanda, acesso colaborativo

### Abas de Controle (v2.0 — Multi-aba com Cache)
- **Script multi-aba**: `architect/data/google_sheets_multi_loader.py` (v2.0)
- **Cache**: TTL configurável (padrão 5min), persistência em disco
- **Abas integradas**:
  - `Database` — dados D-1 (resultados)
  - `Google Ads | NET` — controle de planejamento Google Ads
  - `DV360 | NET` — controle de planejamento DV360
  - `FACEBOOK Ads| NET` — controle de planejamento Meta Ads
  - `TIKTOK Ads| NET` — controle de planejamento TikTok Ads
  - `BING Ads| NET` — controle de planejamento Bing Ads
- **Colunas de controle**: Projetado, CPA Plan, Conversões Plan, Pacing
- **Vantagem**: benchmarks integrados para análise de performance vs. planejado

### Backup (Excel Local)
- **Arquivo Excel**: `C:\Users\lucas.martins\OneDrive - insidemedia.net\Documentos\Obsidian Vault\Campanhas\Dados\Database\WPP_Smart-Fit-NET_DataBase_D-1.xlsx`
- **Status**: mantido como backup e referência histórica

---

## Estrutura

- **Planilha principal**: abas separadas (dados + controle por plataforma)
- **Aba Database**: granularidade diária, por veículo/campanha, ~18.400 linhas, 14 colunas
- **Abas de controle**: planejamento por plataforma (Google Ads, DV360, Meta, TikTok, Bing)

---

## Métricas Importantes

| Métrica | Coluna | Descrição |
|---------|--------|-----------|
| **CPA** | `conversoes_ga4` | Custo por conversão (Google Analytics) |
| **Instalações** | `instalacoes` | Downloads do aplicativo (métrica separada) |
| **Investimento** | `Investimento` | Custo total da campanha |

### Fórmula do CPA

```
CPA = Investimento / conversoes_ga4
```

### Nota sobre Instalações

- As instalações são métricas separadas de conversões
- Representam downloads do aplicativo
- Não devem ser somadas com conversões para calcular o CPA
- Usar apenas `conversoes_ga4` no numerador do cálculo

---

## Colunas

| Col | Campo | Descrição |
|---|---|---|
| A | `date` | Data (dia) |
| B | `id` | Identificador da campanha |
| C | `tx_vehicle` | Veículo/canal |
| D | `tx_funnel` | Etapa do funil |
| E | `Investimento` | Investimento em mídia |
| F | `Impressoes` | Impressões |
| G | `Cliques` | Cliques |
| H | `Sessoes_GA4` | Sessões GA4 |
| I | `Sessoes_App` | Sessões app |
| J | `conversoes_app` | Conversões app |
| K | `conversoes_ga4` | Conversões GA4 |
| L | `conversoes_totais` | Conversões totais |
| M | `sessoes_totais` | Sessões totais |
| N | `instalacoes` | Instalações |

---

## Veículos conhecidos (tx_vehicle)

- `google-ads-search-branded`
- `google-ads-search-non-branded`
- `google-ads-pmax`
- `google-ads-demand-gen`
- `fb-ig`
- `tiktok`
- `growth-genius`
- `criteo`
- `voxus`

## Etapas do funil (tx_funnel)

- `awareness`
- `consideracao`
- `conversao`
- `instalacoes`

---

## Regras de uso

1. Toda análise de campanha usa o D-1 como fonte primária de dados/resultados.
2. **Campanhas sempre são tratadas por ID + Veículo.** Nunca agregar dados sem essa granularidade. Agregações por veículo/funil são apenas visão consolidada.
3. Cruzamentos com otimizações devem referenciar sempre a versão mais recente do arquivo.
4. Sempre informar o período e a filtragem (veículo/funil) ao extrair dados.
5. Dados fora do D-1 (GA4, dashboards) são complementares, nunca substitutos da fonte oficial.

---

## Conexões

- [[Architecture/Architect Architecture v1]] — seção "Fonte de dados oficial"
- [[Install/Architect Install 1.0]] — seção "Base de dados oficial"
- [[Install/Architect Manual de Uso 1.0]] — seção "Base Oficial D-1"
- [[Data/Google Sheets Integration]] — documentação da integração (v2.0)
- [[Data/GOOGLE_SHEETS_MULTI_INTEGRATION]] — documentação técnica completa v2.0
- Skills que referenciam: `marketing-analytics`, `data-analysis`
- Script de integração: `architect/data/google_sheets_loader.py`
- Script multi-aba: `architect/data/google_sheets_multi_loader.py`
- Configuração: `architect/config/sheets_config.json`

---

## Histórico

| Data | Evento |
|---|---|
| 2026-08-04 | Criação inicial. Configurado como referência no `opencode.jsonc`, documentado no Architecture v1, Install doc e skills. |
| 2026-08-10 | Adicionada integração com Google Sheets como fonte primária. Script `google_sheets_loader.py` e configuração `sheets_config.json` criados. Excel mantido como backup. |
| 2026-08-11 | Expansão para multi-aba. Script `google_sheets_multi_loader.py` criado. Abas de controle adicionadas (Google Ads, DV360, Meta, TikTok, Bing). Benchmarks integrados para análise vs. planejado. |
| 2026-08-11 | **v2.0**: Cache em memória/disco, refresh automático, métricas de performance. Script multi-aba consolidado como fonte primária. |
| 2026-08-11 | Adicionada seção "Métricas Importantes" com definição correta de CPA (usa `conversoes_ga4`) e distinção de `instalacoes`. |
