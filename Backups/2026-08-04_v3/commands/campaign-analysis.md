---
description: Workflow completo de análise de campanha multicanal. Recupera contexto, define estratégia, analisa performance, avalia causalidade, revisa criticamente, comunica e desenha o relatório.
agent: odysseus
---

Execute o workflow de análise de campanha para o seguinte pedido:

$ARGUMENTS

Siga o fluxo abaixo, delegando a cada estágio via Task tool com briefing enxuto. Cada subagente deve retornar apenas uma síntese acionável e estruturada (não um rascunho), que será entrada do próximo estágio.

## Estágios

1. **knowledge-manager** — recupere contexto relevante no vault Architect (decisões, análises, experimentos anteriores sobre o tema).
2. **growth-strategist** — transforme o pedido em perguntas claras, hipóteses e metodologia. *Se não houver contexto relevante recuperado, pule este estágio e vá direto para o performance-analyst.*
3. **performance-analyst** — aplique o framework das 4 perguntas (o quê / por quê / impacto / decisão) usando os dados fornecidos.
4. **experimentation-scientist** — *somente se* o performance-analyst levantar hipótese causal ou o usuário pedir avaliação de causalidade. Avalie se as mudanças causaram os resultados.
5. **critical-reviewer** — revise a análise completa: lógica, evidências, premissas, riscos. Perguntas obrigatórias: existe outra explicação? correlação ≠ causalidade? os dados sustentam? um cliente contestaria?
6. **communication-strategist** — transforme a análise revisada em mensagem executiva clara.
7. **creative-director** — produza o material visual final (HTML/dashboard/relatório) com padrão executivo.

## Regras

- No mínimo 3 e no máximo 7 estágios, conforme a complexidade.
- Se o usuário fornecer dados, valide a interpretação no estágio do performance-analyst.
- Ao final, apresente: síntese da análise, decisões recomendadas, próximos passos.
- Responda em PT-BR.
