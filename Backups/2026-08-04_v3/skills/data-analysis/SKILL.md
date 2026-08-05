---
name: data-analysis
description: Use ao tratar dados, realizar análises estatísticas, testar hipóteses, avaliar causalidade ou criar visualizações de dados. Cobre limpeza, estatística descritiva/inferencial, testes e visualização.
---

# Data Analysis

## Etapas

1. **Entender os dados**: origem, granularidade, período, métricas, dimensionamento.
2. **Limpar**: valores ausentes, outliers, duplicados, tipos, consistência.
3. **Explorar**: distribuições, tendências, segmentações.
4. **Analisar**: estatística descritiva e inferencial conforme o problema.
5. **Visualizar**: gráfico certo para a mensagem.
6. **Comunicar**: achados com limitações.

## Estatística

- Descritiva: média, mediana, desvio, quartis — sempre reportar distribuição, não só média.
- Inferencial: intervalo de confiança, significância, tamanho de efeito.
- Testes: t-test, chi-quadrado, ANOVA conforme tipo de dado e premissas.
- Causalidade: difference-in-differences, causal impact, holdout, lift — verificar premissas (tendências paralelas, spillover).

## Visualização

- Tendência ao longo do tempo → linha.
- Comparação entre grupos → barras.
- Distribuição → histograma/boxplot.
- Relação → scatter.
- Partes de um todo → barras empilhadas/treemap (evite pie com muitos itens).

## Regras

- Reporte incerteza e limitações sempre.
- Não afirme causalidade sem método causal.
- Gráficos devem ter título, eixo rotulado e fonte.
