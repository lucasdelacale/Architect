# Architect

Sistema de agentes AI para automação e análise de performance de campanhas de mídia digital.

## Filosofia

**Build AI teams, not AI assistants.**

Cada agente tem uma função específica e restrições claras. O sistema é projetado para trabalho em equipe, não para assistentes genéricos.

## Arquitetura

### Agentes Principais

| Agente | Modo | Função |
|--------|------|--------|
| **Odysseus** | primary | Planejador estratégico. Pergunta, valida e sugere antes de delegar. |
| **Sysyphus** | primary | Executor principal. ÚNICO agente que altera arquivos. |
| **Atena** | subagent | Revisão crítica. Auditoria independente. |
| **Hermes** | subagent | Pesquisador. Busca informações e contexto. |

### Subagentes de Especialidade

| Agente | Função |
|--------|--------|
| growth-strategist | Estratégia, hipóteses, metodologia |
| performance-analyst | Análise de dados de mídia multicanal |
| experimentation-scientist | Causalidade e experimentação |
| knowledge-manager | Gestão do conhecimento no Obsidian |
| creative-director | HTML/CSS, relatórios, dashboards |
| communication-strategist | Tradução executiva e storytelling |
| automation-engineer | Scripts, APIs, integrações, Git |
| critical-reviewer | Auditor antes da finalização |
| architect-evolution | Meta-agente de auditoria |

## Fluxo de Trabalho

```
Usuário → Odysseus (planeja) → Sysyphus (executa)
                ↓
         Subagentes (especializados)
```

## Configuração

- Arquivo principal: `opencode.jsonc`
- Agentes definidos em: `.opencode/agent/` ou inline no JSON
- Skills: `.opencode/skills/`
- Referências: `references` no opencode.jsonc

## Fonte de Dados

- **Primária**: Google Sheets público (v2.0 com cache inteligente)
  - Link: [https://docs.google.com/spreadsheets/d/1qJn7qBhEmKV5wbsqrDQ-9o5WKQZ2x5EcZNanDNDwzM4/](https://docs.google.com/spreadsheets/d/1qJn7qBhEmKV5wbsqrDQ-9o5WKQZ2x5EcZNanDNDwzM4/)
  - Script: `architect/data/google_sheets_multi_loader.py` (v2.0 — cache, refresh, métricas)
  - Config: `architect/config/sheets_config.json`
  - Dependências: `pip install pandas requests`
  - Cache: em memória (TTL 5min) e em disco (`architect/data/cache/`)
- **Backup**: Excel local (`WPP_Smart-Fit-NET_DataBase_D-1.xlsx`)
- **Documentação detalhada**: [[Data/Google Sheets Integration]] | [[Data/GOOGLE_SHEETS_MULTI_INTEGRATION]]

## Skills Disponíveis

| Skill | Função |
|-------|--------|
| campaign-timeline | Análise de performance com linha do tempo |
| data-analysis | Tratamento e análise estatística |
| development-workflow | Código, automações, APIs, Git |
| html-report-system | Relatórios, dashboards, materiais visuais |
| marketing-analytics | Métricas de mídia e campanhas |
| obsidian-management | Gestão do vault no Obsidian |
| proactive-monitoring | Monitoramento e alertas de performance |

## Regras Fundamentais

1. **Apenas Sysyphus altera arquivos** — nenhum outro modo deve modificar config, code ou sistema
2. **Odysseus planeja** — pergunta antes de agir, delega execução
3. **Atena audita** — questiona conclusões antes da entrega
4. **Hermes pesquisa** — recupera contexto rápido

## Histórico

- **2026-08-08**: Atualização da configuração de agentes com permissões por modo
- **2026-08-04**: Criação inicial da arquitetura
