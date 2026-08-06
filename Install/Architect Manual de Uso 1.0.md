# Architect — Manual de Uso

**Versão:** 1.0  
**Data:** 2026-08-06  
**Última atualização:** Fase 5 concluída

---

## O que é o Architect?

O Architect é um framework de equipes de IA especializadas construído sobre o OpenCode, projetado para profissionais de Growth e Performance Marketing.

**Filosofia:** Build AI teams, not AI assistants.

O Architect transforma o OpenCode em uma organização digital de especialistas. Um orquestrador coordena agentes com papéis claros que colaboram, preservam conhecimento no Obsidian e revisam decisões antes de entregá-las.

---

## Arquitetura Geral

```
Usuário (TUI)
    ↓
Modos de execução (Odysseus / Sysyphus / Atena / Hermes)
    ↓
Subagentes especialistas (via Task tool)
    ↓
Skills + Workflows
    ↓
Fonte de dados D-1 + Obsidian
```

---

## Equipe de Agentes

### Modos de Execução (4 agentes primary)

| Agente | Papel | Edita arquivos |
|---|---|---|
| **Odysseus** | Planejador crítico — estratégia e orquestração | Não |
| **Sysyphus** | Worker principal — execução operacional | Sim (único) |
| **Atena** | Revisão e pensamento crítico — auditoria | Não |
| **Hermes** | Pesquisa — consultas rápidas e notas no Obsidian | Sim (apenas vault) |

### Subagentes Especialistas (11 agentes)

| Agente | Especialidade |
|---|---|
| **growth-strategist** | Head de Growth, estratégia e hipóteses |
| **performance-analyst** | Análise multicanal e inteligência acionável |
| **experimentation-scientist** | Causalidade e experimentação |
| **knowledge-manager** | Gestão do conhecimento no Obsidian |
| **creative-director** | Design, HTML/CSS, relatórios e dashboards |
| **communication-strategist** | Tradução executiva e storytelling |
| **automation-engineer** | Scripts, APIs, integrações, Git |
| **critical-reviewer** | Auditor independente |
| **architect-evolution** | Meta-agente de evolução da arquitetura |
| **budget-optimizer** | Otimização de orçamento entre canais |
| **creative-analyst** | Análise de performance de criativos |

---

## Skills Disponíveis (8 skills)

| Skill | Gatilho |
|---|---|
| `marketing-analytics` | Análise de métricas de mídia e campanhas |
| `data-analysis` | Tratamento de dados, estatística, visualização |
| `campaign-timeline` | Análise de campanhas com linha do tempo |
| `obsidian-management` | Organização e recuperação de notas no Obsidian |
| `html-report-system` | Relatórios, dashboards e apresentações em HTML |
| `development-workflow` | Git, código, arquitetura técnica |
| `proactive-monitoring` | Monitoramento proativo com alertas |

---

## Workflows Disponíveis (9 commands)

| Command | Fluxo | Descrição |
|---|---|---|
| `/campaign-analysis` | 7 estágios | Análise completa de campanha multicanal |
| `/executive-report` | 3 estágios | Relatório executivo a partir de dados |
| `/dev` | 2 estágios | Desenvolvimento de automações e scripts |
| `/handoff` | 1 estágio | Gera documento de contexto para próxima sessão |
| `/daily-check` | 4 estágios | Verificação diária proativa de campanhas |
| `/evolution-audit` | 1 agente | Auditoria completa da arquitetura |
| `/evolution-weekly` | 1 agente | Relatório semanal de evolução |
| `/evolution-monthly` | 1 agente | Relatório mensal de evolução |
| `/evolution-quarterly` | 1 agente | Relatório trimestral de evolução |

---

## Como Usar

### 1. Iniciando uma Sessão

Ao abrir o OpenCode, o Odysseus é o agente padrão. Ele orquestra toda a equipe.

**Exemplo:** "Analise a performance do ID-104 nos últimos 14 dias"

### 2. Comandos Rápidos

| Comando | Quando usar |
|---|---|
| `/campaign-analysis [campanha]` | Análise completa de uma campanha |
| `/executive-report [dados]` | Gerar relatório executivo |
| `/handoff [contexto]` | Salvar contexto para próxima sessão |
| `/daily-check [escopo]` | Verificação diária proativa |
| `/dev [tarefa]` | Desenvolver automação ou script |

### 3. Fluxo de Análise de Campanha

```
1. knowledge-manager → Recupera contexto no vault
2. growth-strategist → Define perguntas e hipóteses
3. performance-analyst → Analisa dados com framework das 4 perguntas
4. experimentation-scientist → Avalia causalidade (se necessário)
5. critical-reviewer → Revisa conclusões
6. communication-strategist → Estrutura mensagem executiva
7. creative-director → Produz material visual
```

### 4. Persistência entre Sessões

**Usando /handoff:**
```
/handoff Análise do ID-104 Google Search, período 01/07 a 14/07. CPA subiu 20%. Possível problema de criativo. Falta validar com dados de setembro.
```

O sistema salva em `Evolution/Handoffs/2026-08-06-id-104-google-search.md`

**Ao iniciar nova sessão:**
O knowledge-manager verifica handoffs recentes e oferece retomada.

### 5. Monitoramento Proativo

**Usando /daily-check:**
```
/daily-check Todas as campanhas ativas, período: ontem
```

O sistema detecta anomalias e alerta automaticamente.

### 6. Consultas Rápidas

Para perguntas simples, use o Odysseus diretamente:
- "Qual o CPA do Google Search na semana passada?"
- "Qual campanha está com maior investimento?"
- "Quantas conversões tivemos ontem?"

---

## Fonte de Dados

### Base Oficial D-1

**Arquivo:** `WPP_Smart-Fit-NET_DataBase_D-1.xlsx`

**Localização:** `Campanhas/Dados/Database/`

**Atualização:** Diária pelo usuário

**Colunas:**
| Col | Campo | Descrição |
|---|---|---|
| A | date | Data (dia) |
| B | id | Identificador da campanha |
| C | tx_vehicle | Veículo/canal |
| D | tx_funnel | Etapa do funil |
| E | Investimento | Investimento em mídia |
| F | Impressoes | Impressões |
| G | Cliques | Cliques |
| H | Sessoes_GA4 | Sessões GA4 |
| I | Sessoes_App | Sessões app |
| J | conversoes_app | Conversões app |
| K | conversoes_ga4 | Conversões GA4 |
| L | conversoes_totais | Conversões totais |
| M | sessoes_totais | Sessões totais |
| N | instalacoes | Instalações |

### Regras de Uso

1. Toda análise usa o D-1 como fonte primária
2. Sempre informar período e filtragem
3. Cruzar com `Otimizações.md` quando disponível
4. Dados externos são complementares, nunca substitutos

---

## Sistema de Conhecimento

### Estrutura do Vault

```
Architect/
├── Architecture/          # Documentação da arquitetura
├── Agents/                # Documentação dos agentes
├── Skills/                # Documentação das skills
├── Workflows/             # Documentação dos workflows
├── Evolution/             # Relatórios de evolução
│   ├── Audits/            # Auditorias
│   ├── Weekly/            # Relatórios semanais
│   ├── Monthly/           # Relatórios mensais
│   ├── Quarterly/         # Relatórios trimestrais
│   ├── Handoffs/          # Documentos de handoff
│   ├── Daily-Checks/      # Relatórios diários
│   └── Data-Issues.md     # Log de problemas de dados
├── Decisions/             # ADRs
├── Backups/               # Snapshots da configuração
└── Install/               # Este manual
```

### Arquivos Importantes

| Arquivo | Propósito |
|---|---|
| `Architecture/Learned-Patterns.md` | Padrões descobertos nas análises |
| `Evolution/Feedback-Loop.md` | Registro de acertos e erros |
| `Evolution/Data-Issues.md` | Log de problemas de dados |
| `Evolution/Handoffs/` | Documentos de contexto entre sessões |
| `Evolution/Daily-Checks/` | Relatórios de verificação diária |

---

## Capacidades Novas (v1.0)

### 1. Validação de Dados
O sistema valida automaticamente dados do D-1 antes de processar:
- Investimento > 0
- CTR entre 0% e 100%
- Conversões ≥ 0
- Consistência entre campos

### 2. Tratamento de Erros
Se dados estiverem inconsistentes, o sistema:
- Informa o problema claramente
- Sinaliza impacto na análise
- Não força conclusões

### 3. Contexto Persistente
O sistema mantém contexto ativo por campanha durante toda a sessão:
- ID da campanha
- Veículo
- Período
- Hipóteses
- Status

### 4. Handoff entre Sessões
Use `/handoff` para salvar contexto e retomar depois.

### 5. Monitoramento Proativo
O sistema detecta anomalias automaticamente:
- CPA > 20% acima da média
- CTR < 20% abaixo da média
- Frequência > 3.0 (Meta)
- Investimento > 30% acima do planejado

### 6. Padrões Aprendidos
O sistema registra e consulta padrões descobertos:
- Performance (CPA, CTR, etc.)
- Sazonalidade (dias da semana, meses)
- Otimizações (impacto de mudanças)
- Dados (problemas recorrentes)

### 7. Feedback Loop
O sistema registra acertos e erros para melhoria contínua.

### 8. Benchmarks por Plataforma
Skills com benchmarks específicos para cada canal:
- Google Ads (Search, PMax, Demand Gen)
- Meta Ads
- TikTok Ads
- DV360/Programática

### 9. Novos Agentes
- **budget-optimizer**: Recomenda redistribuição de orçamento
- **creative-analyst**: Analisa performance de criativos

---

## Grid de Delegação

| Categoria | Baixa | Média | Alta |
|---|---|---|---|
| **Sysyphus** | — | creative-director, automation-engineer | knowledge-manager |
| **Odysseus** | — | communication-strategist, architect-evolution | growth-strategist |
| **Atena** | — | performance-analyst | experimentation-scientist, critical-reviewer |

---

## Dicas de Uso

### Para análises rápidas
Use o Odysseus diretamente sem delegar:
```
Qual o CPA do Google Search na semana passada?
```

### Para análises completas
Use o workflow `/campaign-analysis`:
```
/campaign-analysis ID-104, período 01/07 a 14/07
```

### Para relatórios executivos
Use o workflow `/executive-report`:
```
/executive-report Dados de julho 2026, foco em Google Ads
```

### Para salvar contexto
Use `/handoff` ao final de cada sessão longa:
```
/handoff Análise ID-104 em andamento. CPA subiu 20%. Falta validar criativo.
```

### Para monitoramento diário
Use `/daily-check` pela manhã:
```
/daily-check Todas as campanhas, período: ontem
```

### Para desenvolvimento
Use o workflow `/dev`:
```
/dev Script para extrair dados do D-1 automaticamente
```

---

## Solução de Problemas

| Problema | Solução |
|---|---|
| D-1 não encontrado | Verifique o path em `references.database` no opencode.jsonc |
| Agente não responde | Verifique se o agente está no config correto |
| Skill não carrega | Verifique se está em `~/.config/opencode/skills/` |
| Comando não funciona | Verifique se está em `~/.config/opencode/commands/` |
| Dados inconsistentes | O sistema sinalizará automaticamente |

---

## Próximos Passos

1. **Reinicie o OpenCode** para carregar todas as mudanças
2. **Teste o /handoff** para verificar continuidade
3. **Teste o /daily-check** para verificar proatividade
4. **Use o budget-optimizer** para otimizar orçamento
5. **Use o creative-analyst** para analisar criativos

---

## Changelog

### v1.0 (2026-08-06)
- Correção: campaign-timeline adicionada ao config
- Nova skill: proactive-monitoring
- Novos agentes: budget-optimizer, creative-analyst
- Novos comandos: /handoff, /daily-check
- Melhoria: Validação de dados obrigatória
- Melhoria: Tratamento de erros no performance-analyst
- Melhoria: Contexto persistente por campanha
- Melhoria: Benchmarks por plataforma
- Melhoria: Sistema de padrões aprendidos
- Melhoria: Feedback loop para melhoria contínua

---

## Links

- [[Architecture/Architect Architecture v1]]
- [[Agents/Odysseus]]
- [[Agents/Sysyphus]]
- [[Agents/Atena]]
- [[Agents/Hermes]]
- [[Architecture/Learned-Patterns]]
- [[Evolution/Feedback-Loop]]
