---
title: ADR-0003 - Skill Briefing como Pre-step Obrigatório
status: Aceita
date: 2026-08-11
tags: [adr, skills, briefing, arquitetura]
---

# ADR-0003 - Skill Briefing como Pre-step Obrigatório

## Contexto

O Architect possui múltiplas skills especializadas (data-analysis, marketing-analytics, campaign-timeline, etc.) que são acionadas conforme o tipo de tarefa. Entretanto, identificou-se um problema recorrente:

1. **Inputs vagos**: Usuários fornecem informações incompletas ou ambíguas
2. **Falta de contexto**: Dados essenciais para análise estão ausentes
3. **Retrabalho**: Skills precisam fazer múltiplas perguntas antes de executar
4. **Inconsistência**: Cada skill tratava a coleta de contexto de forma diferente

## Decisão

Implementar a **Skill Briefing** como **Step 0 obrigatório** no pipeline de qualquer tarefa do Architect.

### O que é a Skill Briefing

A skill briefing transforma inputs vagos em briefings estruturados, extraindo:
- **Objetivo**: O que o usuário quer alcançar
- **Contexto**: Dados disponíveis, restrições, histórico
- **Métricas**: KPIs relevantes, período, segmentação
- **Entregáveis**: Formato esperado, granularidade, destinatários
- **Prioridades**: O que é crítico vs. nice-to-have

### Como funciona

```
Input do Usuário (vago)
        ↓
    [SKILL BRIEFING] (Step 0)
        ↓
    Briefing Estruturado
        ↓
    [SKILL ROUTER] (Step 1)
        ↓
    Skill Especializada (data-analysis, marketing-analytics, etc.)
        ↓
    Resultado
```

### Fluxo detalhado

1. **Entrada**: Usuário envia mensagem com pedido
2. **Análise**: Briefing identifica tipo de pedido e dados faltantes
3. **Extração**: Se existem referências (architect, database, etc.), extrai dados relevantes
4. **Perguntas**: Se dados são insuficientes, faz perguntas cirúrgicas (máx 3 por turno)
5. **Consolidação**: Gera briefing estruturado em formato padronizado
6. **Roteamento**: Skill router recebe briefing completo e aciona skill correta

## Consequências

### Positivas
- **Eficiência**: Skills recebem contexto completo, reduzindo idas e voltas
- **Consistência**: Formato padronizado para todas as análises
- **Rastreabilidade**: Briefings ficam registrados para referência futura
- **Experiência do usuário**: Menos frustração com perguntas repetitivas

### Negativas
- **Latência inicial**: +1 passo antes da execução (compensado por menos retrabalho)
- **Complexidade**: Mais uma skill para manter
- **Treinamento**: Usuários podem não entender por que precisam fornecer mais info

### Mitigações
- Briefing é transparente: usuário vê o que está sendo extraído
- Perguntas são cirúrgicas e objetivas
- Briefings anteriores podem ser reutilizados para pedidos similares

## Alternativas Consideradas

1. **Cada skill coleta seu próprio contexto**: Rejected - gera inconsistência e retrabalho
2. **Formulário fixo obrigatório**: Rejected - experiência ruim, usuário pode não saber tudo
3. **AI tenta adivinhar contexto**: Rejected - alto risco de erro, gera retrabalho

## Skills Afetadas

Todas as 15 skills do Architect agora recebem briefing estruturado:
- data-analysis
- marketing-analytics
- campaign-timeline
- proactive-monitoring
- html-report-system
- development-workflow
- obsidian-management
- E outras 8 skills especializadas

## Referências

- [[Skill Briefing]] - Documentação completa da skill
- [[Skill Router]] - Atualizado com Step 0
- [[Architect Architecture v1]] - Seção "Sistema de Skills" atualizada
