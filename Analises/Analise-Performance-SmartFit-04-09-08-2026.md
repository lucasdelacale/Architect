# 📊 ANÁLISE DE PERFORMANCE - SMART FIT - ÚLTIMOS 7 DIAS

**Período:** 04/08/2026 a 09/08/2026
**Fonte:** [[Data/Google Sheets Integration|Google Sheets]] (1qJn7qBhEmKV5wbsqrDQ-9o5WKQZ2x5EcZNanDNDwzM4)
**Data de Geração:** 10/08/2026
**Status:** `#em_andamento`

---

## 1. CONTEXTUALIZAÇÃO

Esta análise cobre os últimos 7 dias de performance da campanha Smart Fit, utilizando a base de dados oficial D-1 integrada via Google Sheets. O objetivo é identificar tendências, anomalias e oportunidades de otimização para o [[Agents/growth-strategist|growth-strategist]] gerar hipóteses estratégicas.

**Nota anterior relacionada:** [[Analises/relatorio-performance-30d-07-2026|Relatório de Performance 30 dias - Jul/2026]]

---

## 2. KPIs CONSOLIDADOS (7 DIAS)

| Métrica | Valor | Variação vs 30d* |
|---|---|---|
| **Investimento Total** | R$ 596.826,17 | - |
| **Impressões** | 98.897.432 | - |
| **Cliques** | 2.205.847 | - |
| **CTR** | 2,23% | ⬆️ (+0,64pp vs 1,59%) |
| **CPC Médio** | R$ 0,27 | ⬇️ (-$0,11 vs $0,38) |
| **Conversões Totais** | 3.661 | - |
| **CPA** | R$ 163,02 | ⬆️ (+$24,89 vs $138,13) |
| **Instalações** | 24.065 | - |
| **CPI** | R$ 24,80 | - |

*Variação calculada em relação ao [[Analises/relatorio-performance-30d-07-2026|relatório anterior de 30 dias]]

---

## 3. ANÁLISE POR VEÍCULO

### 3.1 TikTok
| Métrica | Valor | Status |
|---|---|---|
| Investimento | R$ 152.419,25 | Maior investimento |
| Impressões | 45.231.000 | - |
| Cliques | 1.125.400 | - |
| CTR | 2,49% | ✅ |
| CPC | R$ 0,14 | ✅ EXCELENTE |
| Instalações | 6.230 | - |
| **CPI** | **R$ 24,47** | ✅ BOM |

**Insight:** Maior investimento com bom CPI para instalações. Performa bem para Top of Funnel.

### 3.2 Google Ads - Demand Gen
| Métrica | Valor | Status |
|---|---|---|
| Investimento | R$ 37.215,80 | - |
| Impressões | 8.432.100 | - |
| Cliques | 187.650 | - |
| CTR | 2,23% | ✅ |
| CPC | R$ 0,20 | ✅ |
| **Conversões** | **3** | ⚠️ CRÍTICO |
| **CPA** | **R$ 12.405,27** | ⚠️ EXTREMAMENTE ALTO |

**Insight:** Possível problema de tracking ou feed de conversões. Investimento significativo com retorno mínimo registrado.

### 3.3 Google Ads - YouTube
| Métrica | Valor | Status |
|---|---|---|
| Investimento | R$ 21.347,60 | - |
| Impressões | 12.876.500 | - |
| Cliques | 321.400 | - |
| CTR | 2,50% | ✅ |
| CPC | R$ 0,07 | ✅ EXCELENTE |
| **Conversões** | **0** | ⚠️ CRÍTICO |
| **Instalações** | **0** | ⚠️ CRÍTICO |

**Insight:** Alto volume de impressões e cliques sem nenhuma conversão ou instalação registrada. Verificar integração GA4/AppsFlyer.

### 3.4 Meta/FB-IG
| Métrica | Valor | Status |
|---|---|---|
| Investimento | R$ 80.234,50 | - |
| Impressões | 18.654.300 | - |
| Cliques | 412.800 | - |
| CTR | 2,21% | ✅ |
| CPC | R$ 0,19 | ✅ |
| Conversões | 514 | - |
| **CPA** | **R$ 156,09** | ⚠️ ACIMA DO BENCHMARK |

**Insight:** CPA elevado comparado ao benchmark histórico. Considerar otimização de criativos e segmentação.

### 3.5 Google Ads - App
| Métrica | Valor | Status |
|---|---|---|
| Investimento | R$ 45.678,90 | - |
| Impressões | 6.543.200 | - |
| Cliques | 156.780 | - |
| CTR | 2,40% | ✅ |
| CPC | R$ 0,29 | ✅ |
| Instalações | 5.234 | - |
| **CPI** | **R$ 8,73** | ✅ EXCELENTE |

**Insight:** Melhor CPI para instalações. Canal eficiente para conversão de app.

---

## 4. DESCOBERTAS IMPORTANTES

### 4.1 🔴 Problemas Críticos
1. **Google Ads Demand Gen**: R$ 37K investidos com apenas 3 conversões (possível problema de tracking)
2. **Google Ads YouTube**: R$ 21K investidos com zero conversões e zero instalações
3. **09/08/2026**: Instalações = 0 (possível falha de integração ou dia incompleto)

### 4.2 🟡 Atenção Necessária
4. **Funil de Consideração**: Alto volume (41,8 MM impressões) mas baixa conversão (205)
5. **Meta/FB-IG**: CPA de R$ 156 acima do benchmark histórico de R$ 138

### 4.3 🟢 Oportunidades
6. **TikTok**: Maior investimento (R$ 152K) com bom CPI (R$ 24,47) para instalações
7. **Google Ads App**: Melhor CPI (R$ 8,73) para instalações - considerar aumentar investimento

---

## 5. PRÓXIMOS PASSOS

| Prioridade | Ação | Responsável |
|---|---|---|
| 🔴 Alta | Investigar tracking de conversões no Demand Gen e YouTube | [[Agents/performance-analyst|performance-analyst]] |
| 🔴 Alta | Verificar integração de dados em 09/08/2026 | [[Agents/data-engineer|data-engineer]] |
| 🟡 Média | Gerar hipóteses de otimização baseadas nestes dados | [[Agents/growth-strategist|growth-strategist]] |
| 🟡 Média | Revisar critérios de segmentação no Meta/FB-IG | [[Agents/growth-strategist|growth-strategist]] |
| 🟢 Baixa | Documentar aprendizados sobre CPI por veículo | [[Agents/knowledge-manager|knowledge-manager]] |

---

## 6. CONEXÕES

- **Dados:** [[Data/Fonte de dados oficial - WPP Smart-Fit-NET D-1]], [[Data/Google Sheets Integration]]
- **Análises anteriores:** [[Analises/relatorio-performance-30d-07-2026]], [[Analises/relatorio-cruzamento-otimizacoes-07-07-2026-a-06-08-2026]]
- **Agentes:** [[Agents/performance-analyst]], [[Agents/growth-strategist]], [[Agents/knowledge-manager]]
- **Decisões:** Pendente - aguardando análise do growth-strategist

---

## 7. METADADOS

```yaml
cliente: Smart Fit
periodo: 2026-08-04/2026-08-09
fonte: Google Sheets
registros: 10239
status: em_andamento
proximo_passo: "Geração de hipóteses pelo growth-strategist"
data_criacao: 2026-08-10
responsavel: knowledge-manager
```

---

**Nota:** Esta análise é um snapshot dos últimos 7 dias. Para análise completa, consultar [[Analises/relatorio-performance-30d-07-2026|relatório de 30 dias]].
