# ADR-0004: Skill Briefing - Pre-step Obrigatório

## Status

Aceito

## Contexto

O sistema de skills do Architect não tinha uma camada de preparação que transformasse inputs vagos em briefings detalhados. Isso resultava em:
- Inputs vagos chegando às skills de execução
- Roteamento impreciso (skill-router com input ruim)
- Qualidade variável dos resultados

## Decisão

Criar skill `briefing` como pre-step obrigatório antes do skill-router.

### Arquitetura

```
Input vago → BRIEFING → Input rico → SKILL-ROUTER → SKILL DE EXECUÇÃO
```

### Justificativa

1. **Qualidade do input** → Melhora roteamento e execução
2. **Filosofia Odysseus** → "Build AI teams" precisa de briefings claros
3. **Alinhamento com workflow** → campaign-analysis já fazia isso (growth-strategist)
4. **Zero overhead** → Se input é claro, briefing apenas confirma

## Consequências

### Positivas
- Roteamento mais preciso
- Resultados de maior qualidade
- Padrão consistente de trabalho

### Negativas
- Uma etapa adicional (mitigada por ser rápida)
- Treinamento da equipe para usar consistently

## Alternativas Consideradas

1. **Briefing integrado ao router** → Rejeitado: complexifica o router
2. **Briefing apenas para inputs vagos** → Rejeitado: difícil detectar vaguidade
3. **Briefing como agente separado** → Rejeitado: overkill para esta função

## Referências

- [[Architect Architecture v1]]
- [[Skills/briefing]]
- [[Skills/skill-router]]