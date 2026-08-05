# Fonte de dados oficial — WPP Smart-Fit-NET D-1

**Tipo**: Base de dados de campanhas
**Atualização**: Diária (D-1)
**Status**: Fonte oficial de dados/resultados

---

## Path

`C:\Users\lucas.martins\OneDrive - insidemedia.net\Documentos\Obsidian Vault\Campanhas\Dados\Database\WPP_Smart-Fit-NET_DataBase_D-1.xlsx`

---

## Estrutura

- Aba única: `DataBase_D-1`
- Granularidade: diária, por veículo/campanha
- Linhas: ~18.400
- Colunas: 14 (A–N)

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
- Skills que referenciam: `marketing-analytics`, `data-analysis`

---

## Histórico

| Data | Evento |
|---|---|
| 2026-08-04 | Criação inicial. Configurado como referência no `opencode.jsonc`, documentado no Architecture v1, Install doc e skills. |
