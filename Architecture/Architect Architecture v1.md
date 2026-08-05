# Architect Architecture v1

**Building AI teams, not AI assistants.**

Versão: 1.0
Data: 2026-08-04
Status: Implementado

---

## Visão geral

O Architect transforma o OpenCode em uma organização digital de especialistas em IA. Um orquestrador coordena especialistas que colaboram, preservam conhecimento e revisam decisões.

Princípios:

- Agentes com papéis claros.
- Especialistas colaboram via delegação.
- Conhecimento é preservado no Obsidian.
- Decisões são revisadas pelo Critical Reviewer.
- Modelos são recursos substituíveis — nenhum agente pinna modelo.

## Estrutura de pastas

### Configuração (`~/.config/opencode/`)

```
opencode.jsonc                          # config central (default_agent, references, permissions)
agents/                                 # 3 modos de execução + 9 subagentes
skills/                                 # 5 skills
commands/                               # 7 workflows
```

### Vault Obsidian

```
C:\Users\lucas.martins\OneDrive - insidemedia.net\Documentos\Obsidian Vault\Architect\
├── Architecture\      # esta documentação (fonte de verdade)
├── Agents\            # 1 doc por agente
├── Skills\            # 1 doc por skill
├── Workflows\         # 1 doc por workflow
├── Evolution\
│   ├── Audits\
│   ├── Weekly\
│   ├── Monthly\
│   └── Quarterly\
├── Decisions\         # ADRs
├── Backups\           # snapshots da configuração
└── Install\           # prompt de instalação do Architect
```

## Equipe de agentes

### Modos de execução (substituem plan/build do OpenCode)

| Agente | Mode | Papel | Edita arquivos |
|---|---|---|---|
| `sysyphus` | primary | Worker principal — execução operacional | Sim (único para config/code/sistema) |
| `odysseus` | primary | Planejador crítico — estratégia e orquestração | Não |
| `atena` | primary | Revisão e pensamento crítico — auditoria e causalidade | Não |
| `hermes` | primary | Pesquisa — consultas rápidas e notas no Obsidian | Sim (apenas vault Obsidian) |

### Subagentes especialistas (delegáveis via Task ou @nome)

| Agente | Mode | Papel |
|---|---|---|
| `growth-strategist` | subagent | Head de Growth, estratégia e hipóteses |
| `performance-analyst` | subagent | Análise multicanal e inteligência acionável |
| `experimentation-scientist` | subagent | Causalidade e experimentação |
| `knowledge-manager` | subagent | Gestão do conhecimento no Obsidian |
| `creative-director` | subagent | Design, HTML/CSS, relatórios e dashboards |
| `communication-strategist` | subagent | Tradução executiva |
| `automation-engineer` | subagent | Scripts, APIs, integrações, Git |
| `critical-reviewer` | subagent | Auditor independente |
| `architect-evolution` | subagent | Meta-agente do Evolution System |

## Skills

| Skill | Gatilho |
|---|---|
| `obsidian-management` | Ler/criar/organizar notas no vault Architect |
| `marketing-analytics` | Análise de métricas de mídia e campanhas |
| `data-analysis` | Tratamento de dados, estatística, visualização |
| `html-report-system` | Relatórios, apresentações, dashboards em HTML |
| `development-workflow` | Git, código, arquitetura técnica |

## Workflows

| Command | Fluxo |
|---|---|
| `/campaign-analysis` | knowledge-manager → growth-strategist → performance-analyst → experimentation-scientist (condicional) → critical-reviewer → communication-strategist → creative-director |
| `/executive-report` | performance-analyst → communication-strategist → creative-director |
| `/dev` | automation-engineer → critical-reviewer |
| `/evolution-audit` | auditoria sob demanda (architect-evolution) |
| `/evolution-weekly` / `/evolution-monthly` / `/evolution-quarterly` | relatórios periódicos |

## Fonte de dados oficial (D-1)

O Architect possui uma única base de dados oficial de campanhas, atualizada diariamente pelo usuário:

**`WPP_Smart-Fit-NET_DataBase_D-1.xlsx`**

- **Path**: `C:\Users\lucas.martins\OneDrive - insidemedia.net\Documentos\Obsidian Vault\Campanhas\Dados\Database\WPP_Smart-Fit-NET_DataBase_D-1.xlsx`
- **Atualização**: diária (D-1) pelo usuário.
- **Status**: fonte oficial de dados/resultados para consultas, estudos, cruzamentos e otimizações.
- **Estrutura**: aba única `DataBase_D-1`, granularidade diária por veículo/campanha, ~18,4 mil linhas, 14 colunas.

### Colunas

| Col | Campo | Descrição |
|---|---|---|
| A | `date` | Data (dia) |
| B | `id` | Identificador da campanha |
| C | `tx_vehicle` | Veículo/canal (ex.: google-ads-search-branded, pmax, demand-gen, fb-ig, tiktok, growth-genius, criteo, voxus) |
| D | `tx_funnel` | Etapa do funil (awareness, consideracao, conversao, instalacoes) |
| E | `Investimento` | Investimento em mídia |
| F | `Impressoes` | Impressões |
| G | `Cliques` | Cliques |
| H | `Sessoes_GA4` | Sessões GA4 |
| I | `Sessoes_App` | Sessões app |
| J | `conversoes_app` | Conversões app |
| K | `conversoes_ga4` | Conversões GA4 |
| L | `conversoes_totais` | Conversões totais |
| M | `sessoes_totais` | Sessões totais |
| N | `instalacoes` | Instalações |

### Regras de uso

1. Toda análise de campanha usa o D-1 como fonte primária de dados/resultados.
2. Cruzamentos com otimizações devem referenciar sempre a versão mais recente do arquivo.
3. Sempre informar o período e a filtragem (veículo/funil) ao extrair dados.
4. Dados fora do D-1 (GA4, dashboards) são complementares, nunca substitutos da fonte oficial.

## Fontes complementares de dados

### Pasta Workflow (Otimizações e Tarefas)

**Path**: `C:\Users\lucas.martins\OneDrive - insidemedia.net\Documentos\Obsidian Vault\Workflow\`

A pasta Workflow contém o registro operacional das otimizações e tarefas realizadas:

| Arquivo | Descrição |
|---------|-----------|
| `Otimizações.md` | Log de otimizações diárias (data, campanha, ação, responsável) |
| `Tarefas.md` | Lista de tarefas e prioridades (P0-P3) |
| `Arquivo.md` | Arquivo histórico de tarefas concluídas |
| `Diário.md` | Checklist operacional diário (investimento, pace, status) |
| `Observação.md` | Observações e notas técnicas |
| `Tracking.md` | Tracking de atividades |
| `Projetos.md` | Projetos em andamento |

### Regras de uso do Workflow

1. **Toda análise de performance** deve consultar `Otimizações.md` e `Arquivo.md` para identificar otimizações já implementadas.
2. **Cruzamento obrigatório**: Ao identificar melhoria/piora de performance, verificar se houve otimização correspondente no período.
3. **Referência cruzada**: Usar hashtags (#ID-XXX, #Google-ads, #Meta-ads, #TikTok-ads) para conectar otimizações com dados D-1.
4. **Atualização contínua**: O Workflow deve ser atualizado a cada otimização realizada para manter histórico consistente.

### Regra de cruzamento D-1 × Workflow

Ao realizar análise completa de campanha:

1. Extrair dados do D-1 (fonte primária de resultados)
2. Consultar `Otimizações.md` e `Arquivo.md` para otimizações do período
3. Cruzar: "O que mudou?" (otimização) × "O que aconteceu?" (resultado)
4. Identificar correlações e causalidades
5. Documentar conclusões com referência a ambas as fontes

## Delegação Cognitiva Adaptativa

Nenhum agente pinna modelo. A economia vem de **como** os subagentes entram em cena:

1. O orquestrador classifica a complexidade (baixa/média/alta).
2. Aciona o mínimo de especialistas necessário.
3. Monta briefing enxuto por estágio (nunca o histórico completo).
4. Encadeia com síntese obrigatória entre estágios.
5. Pula estágios condicionalmente (ex.: sem hipótese causal, não aciona experimentation-scientist).

---

# Grid de Delegação (Sysyphus / Odysseus / Atena)

O Architect classifica os agentes em três categorias cognitivas para direcionar a delegação de tarefas. A escolha do modelo de IA é sempre manual, feita pelo usuário no TUI por sessão.

## Categorias

* **Sysyphus** — operacional. Tarefas mecânicas, repetitivas e de execução.
* **Odysseus** — planejador. Estratégia, análise e a grande mente do Architect.
* **Atena** — julgamento crítico. Causalidade, decisões e auditoria.

## Tabela de classificação dos agentes

| Categoria | Baixa | Média | Alta |
|---|---|---|---|
| **Sysyphus** | — | creative-director, automation-engineer | knowledge-manager |
| **Odysseus** | — | communication-strategist, architect-evolution | growth-strategist |
| **Atena** | — | performance-analyst | experimentation-scientist, critical-reviewer |

## Como o Architect usa esta classificação

O orquestrador classifica a complexidade do pedido (baixa/média/alta), determina a categoria (Sysyphus/Odysseus/Atena) e delega ao agente correto via Task tool. A profundidade da cadeia (quantos estágios rodam) é decidida pela Delegação Cognitiva Adaptativa.

A escolha do modelo de cada sessão é responsabilidade do usuário, via TUI.

---

## Regra fundamental de dados

**Campanhas sempre são tratadas por ID + Veículo.** Nunca agregar dados sem essa granularidade.

- Cada linha da base D-1 representa uma combinação `id` × `tx_vehicle` × `tx_funnel` × `date`.
- Toda análise, cruzamento ou otimização deve manter o nível de granularidade: **ID da campanha + veículo**.
- Agregações por veículo ou por funil são permitidas apenas como visão consolidada, sempre indicando que são somatórios.
- Nunca misturar IDs de campanhas diferentes em uma mesma conclusão sem explicar a agregação.

## Regra fundamental de dados

**Campanhas sempre são tratadas por ID + Veículo.** Nunca agregar dados sem essa granularidade.

- Cada linha da base D-1 representa uma combinação `id` × `tx_vehicle` × `tx_funnel` × `date`.
- Toda análise, cruzamento ou otimização deve manter o nível de granularidade: **ID da campanha + veículo**.
- Agregações por veículo ou por funil são permitidas apenas como visão consolidada, sempre indicando que são somatórios.
- Nunca misturar IDs de campanhas diferentes em uma mesma conclusão sem explicar a agregação.

## Regra fundamental de dados

**Campanhas sempre são tratadas por ID + Veículo.** Nunca agregar dados sem essa granularidade.

- Cada linha da base D-1 representa uma combinação `id` × `tx_vehicle` × `tx_funnel` × `date`.
- Toda análise, cruzamento ou otimização deve manter o nível de granularidade: **ID da campanha + veículo**.
- Agregações por veículo ou por funil são permitidas apenas como visão consolidada, sempre indicando que são somatórios.
- Nunca misturar IDs de campanhas diferentes em uma mesma conclusão sem explicar a agregação.

## Regras globais dos agentes

Todos os agentes devem:

- Questionar hipóteses.
- Sugerir melhorias.
- Ensinar conceitos novos.
- Buscar metodologias avançadas.
- Explicar decisões.

Não devem:

- Apenas executar comandos.
- Aceitar a primeira hipótese.
- Limitar o pensamento ao histórico.

## Notas de implementação

- Config central: `~/.config/opencode/opencode.jsonc`.
- `default_agent`: `odysseus`.
- Modos padrão do OpenCode (`plan`/`build`) desabilitados.
- `sysyphus` é o único agente que altera arquivos de config/code/sistema; `hermes` edita apenas o vault Obsidian; `odysseus` e `atena` têm `edit: deny`.
- Vault Obsidian permitido via `permission.external_directory` e `references`.
- Backup da configuração inicial em `Backups/2026-08-04_v1/` e da transição em `Backups/2026-08-04_v2/`.
- Para aplicar mudanças de config, reiniciar o OpenCode.

## Links

- [[Install/Architect Install 1.0]]
- [[Agents/Odysseus]]
- [[Agents/Sysyphus]]
- [[Agents/Atena]]
- [[Decisions/ADR-0001 - Implementacao inicial do Architect]]
