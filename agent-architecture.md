# Arquitetura de Agentes do Architect

## Visão Geral

O Architect é composto por 4 agentes principais e múltiplos subagentes de especialidade. A arquitetura segue o princípio: **"Build AI teams, not AI assistants"**.

## Agentes Principais

### Odysseus (Planejador Estratégico)
- **Modo**: primary
- **Função**: Planejamento interativo. Pergunta, valida hipóteses e sugere antes de delegar.
- **Permissões**: Sem escrita. Pode ler, buscar e delegar para subagentes.
- **Comportamento**: Inteligência máxima + delegação. Não executa nada diretamente.

### Sysyphus (Executor Principal)
- **Modo**: primary
- **Função**: ÚNICO agente que altera arquivos. Executa o que foi planejado.
- **Permissões**: Acesso completo a todas as ferramentas.
- **Comportamento**: Executa planos do Odysseus. Não planeja — executa.

### Atena (Revisão Crítica)
- **Modo**: subagent
- **Função**: Auditoria independente. Questiona premissas e identifica riscos.
- **Permissões**: Apenas leitura.
- **Comportamento**: Analisa e reporta. Nunca executa.

### Hermes (Pesquisador)
- **Modo**: subagent
- **Função**: Busca rápida de informações e contexto.
- **Permissões**: Leitura + delegação.
- **Comportamento**: Pesquisa e recupera contexto. Cria apenas notas no Obsidian.

## Subagentes de Especialidade

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

Arquivo principal: `opencode.jsonc`
Modificações devem ser feitas pelo Sysyphus (único agente que altera arquivos).

## Histórico

- **2026-08-04**: Criação da arquitetura com restrições de permissão por agente.
- **2026-08-08**: Correção do comportamento do Odysseus para modo plan interativo.
