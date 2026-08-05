---
description: Auditoria completa sob demanda da arquitetura do Architect. Identifica gargalos, agentes/skills pouco usados, oportunidades de automação e propõe melhorias.
agent: architect
---

Acione o **architect-evolution** (via Task tool) para realizar uma auditoria completa do sistema Architect.

Foco: $ARGUMENTS (se vazio, auditoria completa: arquitetura, agentes, skills, workflows, modelos, gargalos, automações).

O auditor deve:

1. Revisar a arquitetura atual (`Architecture/` e `Decisions/` no vault).
2. Analisar padrões de uso e gargalos.
3. Propor melhorias com problema → solução → benefício → esforço.
4. Salvar o relatório em `Evolution/Audits/` no Obsidian.

Regra fundamental: nenhuma alteração estrutural sem aprovação do usuário. Apresente apenas propostas e aguarde decisão.
