---
name: campaign-timeline
description: Use ao analisar performance de campanhas de midia com linha do tempo, correlacionando dados diarios com otimizacoes registradas. Gera relatorios no formato timeline com metricas e observacoes. Use quando o pedido envolver analise de campanha especifica, evolucao de performance, ou correlacao entre otimizacoes e resultados.
---

# Campaign Timeline Analysis

## O que e

Skill para analise de performance de campanhas de midia utilizando formato de **linha do tempo**, correlacionando dados diarios de metricas com otimizacoes registradas no vault.

## Quando usar

- Analise de performance de campanha especifica (ex: como foi a performance do ID-104?)
- Correlacao entre otimizacoes e resultados (ex: o que aconteceu depois da mudanca de tCPA?)
- Evolucao de metricas ao longo do periodo
- Diagnostico de anomalias em campanhas
- Relatorios para cliente ou equipe

## Fonte de dados

**Primaria:** Base D-1 WPP Smart-Fit-NET
- Path: Campanhas/Dados/Database/WPP_Smart-Fit-NET_DataBase_D-1.xlsx
- Colunas: date, id, tx_vehicle, tx_funnel, Investimento, Impressoes, Cliques, Sessoes_GA4, Sessoes_App, conversoes_app, conversoes_ga4, conversoes_totais, sessoes_totais, instalacoes

**Complementar:** Logs de otimizacoes do vault
- Campanhas/Otimizacoes/ID-*.md - Historico de otimizacoes por campanha
- Workflow/Arquivo.md - Log de atividades diarias
- Workflow/Otimizacoes.md - Otimizacoes do dia

## Formato do Relatorio

### Estrutura obrigatoria

`
# Analise [Nome da Campanha] - [Veiculo] - [Periodo]

**Data:** [data de geracao]
**Periodo Analisado:** [data inicio] a [data fim]
**Fonte:** Base D-1 WPP Smart-Fit-NET
**Status:** [Status da analise]

---

## 1. Contexto
- O que e a campanha
- O que aconteceu no periodo
- Hipotese inicial

## 2. Linha do Tempo
[Tabela com dados diarios + observacoes]

## 3. Analise por Periodo
[Tabela consolidada por fases]

## 4. Anomalias Detectadas
[Lista de anomalias com evidencias]

## 5. Otimizacoes Registradas
[Tabela com datas e fontes]

## 6. Comparativo Geral
[Antes vs Depois]

## 7. Conclusoes
[Pontos-chave]

## 8. Proximos Passos
[Acoes priorizadas]

## 9. Referencias
[Wikilinks para notas relacionadas]
`

### Formato da Linha do Tempo

A tabela de linha do tempo deve seguir este formato exato:

`
| Data | Investimento | Conversoes | CPA Conv | Instalacoes | CPA Inst | Observacao |
|---|---|---|---|---|---|---|
| DD/MM | R$ X.XXX | XXX | R$ XX | X.XXX | R$ X,XX | |
| DD/MM | R$ X.XXX | XXX | R$ XX | X.XXX | R$ X,XX | <- [Otimizacao realizada] |
| **DD/MM** | **R$ X.XXX** | **XXX** | **R$ XX** | **X.XXX** | **R$ X,XX** | **<<< [Evento importante]** |
`

### Convencoes de Observacao

| Simbolo | Significado |
|---|---|
| <- | Otimizacao registrada naquele dia |
| <<< | Evento importante (pico, queda, reestruturacao) |
| >>> | Marco temporal (inicio/fim de teste) |
| ** (negrito) | Linha com evento significativo |

### Metricas por Veiculo

| Veiculo | Metricas Principais |
|---|---|
| Google Ads Search | CPM, CTR, CPC, CPA, Conv, Impressoes, Cliques |
| Google Ads App | CPM, CTR, CPC, CPA Conv, CPA Inst, Conv, Inst |
| Meta Ads | CPM, CTR, CPC, CPA, Conv, Frequencia |
| TikTok | CPM, CTR, CPC, CPA, Conv, Views |
| PMax | CPM, CTR, CPC, CPA, Conv, Impressoes |

## Workflow de Execucao

### 1. Extrair dados da base
`python
import pandas as pd

path = 'Campanhas/Dados/Database/WPP_Smart-Fit-NET_DataBase_D-1.xlsx'
df = pd.read_excel(path, engine='openpyxl')
df['date'] = pd.to_datetime(df['date'])

# Filtrar campanha especifica
df_campaign = df[df['id'] == 'ID-XXX']
`

### 2. Buscar otimizacoes no vault
- Ler Campanhas/Otimizacoes/ID-XXX.md
- Ler Workflow/Arquivo.md para o periodo
- Identificar otimizacoes relevantes

### 3. Gerar linha do tempo
- Cruzar dados diarios com otimizacoes
- Marcar eventos com simbolos (<<<)
- Calcular metricas derivadas (CPM, CTR, CPC, CPA)

### 4. Analisar anomalias
- Identificar picos e quedas
- Correlacionar com otimizacoes
- Formular hipoteses

### 5. Gerar relatorio
- Seguir estrutura obrigatoria
- Incluir wikilinks para fontes
- Salvar em Analises/

## Regras

1. **Sempre incluir fonte**: dados D-1 + logs de otimizacoes
2. **Nao afirmar causalidade**: correlacao != causalidade
3. **Marcar incertezas**: usar possivel, hipotese, requer investigacao
4. **Incluir comparacoes**: antes vs depois de otimizacoes
5. **Priorizar acoes**: sempre ter Proximos Passos com prioridades

## Exemplo de Uso

**Pedido:** Analise a performance do ID-104 nos ultimos 14 dias

**Execucao:**
1. Extrair dados de ID-104 da base D-1
2. Buscar otimizacoes em Campanhas/Otimizacoes/ID-104.md
3. Cruzar com Workflow/Arquivo.md do periodo
4. Gerar linha do tempo com observacoes
5. Identificar anomalias e correlacoes
6. Salvar em Analises/Analise ID-104 - [periodo].md

## Referencias

- [[Campanhas/Otimizacoes/ID-104]] - Exemplo de log de otimizacao
- [[Workflow/Arquivo]] - Log de atividades
- [[Analises/Analise Campanhas App - Google Ads - Jul-Ago 2026]] - Exemplo de relatorio gerado
- [[Architect/Skills/marketing-analytics]] - Framework de analise
- [[Architect/Skills/data-analysis]] - Tecnicas de analise de dados
