# ADR-0002 — Auditoria de Limitadores e Oportunidades

- Status: Proposto
- Data: 2026-08-06
- Autor: Architect Evolution

## Contexto

O Architect v1 está implementado desde 2026-08-04 com 4 modos de execução, 9 subagentes, 6 skills e 7 workflows. Foi solicitada uma auditoria completa para identificar limitadores de potencial e oportunidades de melhoria.

## Análise

### Limitadores Identificados

1. **Camada de Dados Frágil** — Única planilha Excel, atualização manual, sem validação
2. **Ausência de Automação** — Tudo sob demanda, sem agendamento ou alertas
3. **Pipeline de Insights Limitado** — Sem predição, anomaly detection, ou recomendações automáticas
4. **Workflows Lineares** — Pipeline de 7 estágios para consultas simples
5. **Knowledge Management Não Estruturado** — Sem grafo, sem queries, sem aprendizado automático

### Oportunidades Priorizadas (Impacto vs Esforço)

| Prioridade | Oportunidade | Impacto | Esforço |
|---|---|---|---|
| P1 | Integração com APIs de plataformas | Altíssimo | Alto |
| P1 | Automação de coleta de dados | Altíssimo | Médio |
| P1 | Workflow de quick queries | Alto | Baixo |
| P2 | Sistema de alertas automáticos | Alto | Médio |
| P2 | Data pipeline validado | Alto | Médio |
| P2 | Agentes faltantes (Budget Optimizer, etc.) | Médio | Baixo |
| P3 | ML para predição/recomendação | Médio | Alto |
| P3 | Knowledge graph estruturado | Médio | Médio |

### Gap Crítico

**Automação de Dados + Quick Queries** — São as capacidades mais urgentes porque:
- Sem dados automatizados, todas as análises são comprometidas
- 80% das consultas são simples e não justificam pipeline completo
- É a fundação para qualquer evolução futura

## Decisão

Propor ao usuário a implementação da **Automação de Coleta de Dados** como prioridade máxima, seguindo o plano de 5 fases:

1. Automação de download do D-1 (2 dias)
2. Validação de dados (1 dia)
3. Quick queries workflow (1 dia)
4. Integração com 1 API (1 semana)
5. Sistema de alertas básico (3 dias)

Total: ~2.5 semanas

## Consequências

- **Positivas**: Ganho de 30% de produtividade, dados mais frescos, fundação para ML e automações
- **Negativas**: Requer desenvolvimento Python, manutenção de scripts, possível quebra com mudanças nos formatos de dados
- **Riscos**: Web scraping pode ser frágil; APIs podem ter custo; manutenção contínua necessária

## Próximos passos

1. Aprovar esta auditoria e ADR
2. Criar ADR-0003 para a Fase 1 (automação de download)
3. Designar automation-engineer para implementação
4. Backup da configuração atual antes de alterações

## Links

- [[Evolution/Audits/2026-08-06 Auditoria Completa]]
- [[Architecture/Architect Architecture v1]]
- [[Agents/automation-engineer]]
