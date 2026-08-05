---
name: html-report-system
description: Use ao gerar relatórios, apresentações, dashboards ou materiais visuais em HTML/CSS. Fornece componentes, layouts, design tokens e padrões visuais executivos. Evite ao escrever código de aplicação genérico.
---

# HTML Report System

## Padrão executivo

- Narrativa primeiro: contexto → achados → recomendação.
- Hierarquia visual clara: título, subtítulo, corpo, callouts.
- Tipografia consistente (escala de 4-8px), espaçamento uniforme.
- Paleta limitada (1 primária + neutros + 1 acento), contraste acessível.
- Data na página, fonte das métricas, responsabilidade da emissão.

## Design tokens

```css
--color-primary:   #0B3D2E /* verde corporate */
--color-secondary: #E8F0EC
--color-accent:    #C8A24B
--color-text:      #1A1A1A
--color-muted:     #6B6B6B
--color-bg:        #FFFFFF
--font-sans: 'Inter', system-ui, sans-serif
--radius: 8px
--shadow: 0 1px 3px rgba(0,0,0,.08)
```

## Componentes

- **Header**: título, subtítulo, data, cliente.
- **KPI cards**: valor, variação, contexto, seta de direção.
- **Chart**: um gráfico por mensagem; título e fonte.
- **Callout**: destaque de insight/recomendação.
- **Table**: zebra leve, alinhamento numérico à direita, total em destaque.
- **Footer**: próximos passos, disclaimer metodológico.

## Layout

- Grid responsivo (12 colunas), breakpoints para mobile.
- Máximo ~1200px de largura de conteúdo.
- Print-friendly: `@media print` com cores adaptadas.

## Regras

- Nunca use lorem ipsum ou placeholders genéricos.
- Cada elemento deve ter propósito na narrativa.
- Dashboard sem narrativa = não entregar.
