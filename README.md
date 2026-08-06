# Architect

> **Building AI teams, not AI assistants.**

Um framework de equipes de IA especializadas construído sobre o [OpenCode](https://opencode.ai), projetado para profissionais de Growth e Performance Marketing.

## O que é o Architect?

O Architect transforma o OpenCode em uma organização digital de especialistas. Um orquestrador coordena agentes com papéis claros que colaboram, preservam conhecimento no Obsidian e revisam decisões antes de entregá-las.

A filosofia é simples: **modelos são substituíveis, a arquitetura não.**

## Arquitetura

`
Usuário (TUI)
    ↓
Modos de execução (Odysseus / Sysyphus / Atena / Hermes)
    ↓
Subagentes especialistas (via Task tool)
    ↓
Skills + Workflows
    ↓
Fonte de dados D-1 + Obsidian
`

## Equipe de agentes

### Modos de execução

| Agente | Papel | Edita arquivos |
|---|---|---|
| odysseus | Planejador crítico — estratégia e orquestração | Não |
| sysyphus | Worker principal — execução operacional | Sim (único para config/code/sistema) |
| tena | Revisão e pensamento crítico — auditoria | Não |
| hermes | Pesquisa — consultas rápidas e notas no Obsidian | Sim (apenas vault Obsidian) |

### Subagentes especialistas

| Agente | Papel |
|---|---|
| growth-strategist | Head de Growth, estratégia e hipóteses |
| performance-analyst | Análise multicanal e inteligência acionável |
| experimentation-scientist | Causalidade e experimentação (DiD, A/B, Causal Impact) |
| knowledge-manager | Gestão do conhecimento no Obsidian |
| creative-director | Design, HTML/CSS, relatórios e dashboards |
| communication-strategist | Tradução executiva e storytelling |
| utomation-engineer | Scripts, APIs, integrações, Git |
| critical-reviewer | Auditor independente |
| rchitect-evolution | Meta-agente de evolução da própria arquitetura |

## Skills

| Skill | Gatilho |
|---|---|
| marketing-analytics | Análise de métricas de mídia e campanhas |
| data-analysis | Tratamento de dados, estatística, visualização |
| campaign-timeline | Análise de campanhas com linha do tempo e correlação com otimizações |
| obsidian-management | Organização e recuperação de notas no Obsidian |
| html-report-system | Relatórios, dashboards e apresentações em HTML |
| development-workflow | Git, código, arquitetura técnica |

## Workflows

| Command | Fluxo |
|---|---|
| /campaign-analysis | knowledge-manager → growth-strategist → performance-analyst → experimentation-scientist → critical-reviewer → communication-strategist → creative-director |
| /executive-report | performance-analyst → communication-strategist → creative-director |
| /dev | automation-engineer → critical-reviewer |
| /evolution-audit | architect-evolution (sob demanda) |
| /evolution-weekly / monthly / quarterly | Relatórios periódicos de evolução |

## Delegação Cognitiva Adaptativa

Nenhum agente pinna modelo. A economia vem de **como** os subagentes são acionados:

1. O orquestrador classifica a complexidade (baixa/média/alta).
2. Aciona o mínimo de especialistas necessário.
3. Monta briefing enxuto por estágio.
4. Encadeia com síntese obrigatória entre estágios.
5. Pula estágios condicionalmente.

### Grid de delegação

| Categoria | Baixa | Média | Alta |
|---|---|---|---|
| **Sysyphus** | — | creative-director, automation-engineer | knowledge-manager |
| **Odysseus** | — | communication-strategist, architect-evolution | growth-strategist |
| **Atena** | — | performance-analyst | experimentation-scientist, critical-reviewer |

## Regra fundamental de dados

**Campanhas sempre são tratadas por ID + Veículo.** Nunca agregar dados sem essa granularidade.

## Fonte de dados oficial (D-1)

Base de dados de campanhas atualizada diariamente pelo usuário, contendo ~18.400 linhas com granularidade diária por veículo/campanha.

**Colunas:** date, id, tx_vehicle, tx_funnel, Investimento, Impressoes, Cliques, Sessoes_GA4, Sessoes_App, conversoes_app, conversoes_ga4, conversoes_totais, sessoes_totais, instalacoes.

## Filosofia

- Modelos são recursos substituíveis — nenhum agente pinna modelo.
- Conhecimento é um ativo estratégico.
- O sistema deve evoluir junto com o usuário.
- Decisões são revisadas antes de serem entregues.
- A arquitetura é mais importante que o modelo utilizado.

## Estrutura do repositório

`
Architect/
├── Agents/          # Documentação dos agentes (13 docs)
├── Architecture/    # Fonte de verdade da arquitetura
├── Backups/         # Snapshots da configuração (v1, v2, v3)
├── Data/            # Documentação da base de dados oficial
├── Decisions/       # ADRs (Architecture Decision Records)
├── Evolution/       # Relatórios de evolução (Audits, Weekly, Monthly, Quarterly)
├── Install/         # Prompt de instalação do Architect
├── Skills/          # Documentação das skills
└── Workflows/       # Documentação dos workflows
`

## Dependências

- [OpenCode](https://opencode.ai)
- [Obsidian](https://obsidian.md) (vault de conhecimento)
- Git

## Como instalar

Consulte Install/Architect Install 1.0.md para o prompt completo de instalação.

## Licença

Projeto privado — Lucas Martins.
