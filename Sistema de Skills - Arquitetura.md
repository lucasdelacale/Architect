# Sistema de Skills - Arquitetura

## Visão Geral

O sistema de skills do OpenCode permite modular instruções especializadas que são carregadas sob demanda. Skills são arquivos `.md` com frontmatter YAML.

## Locais de Armazenamento

### Fonte Primária (recomendada)
- **Path:** `~/.config/opencode/skills/`
- **Formato:** Pastas com `SKILL.md` dentro
- **Skills:** 8 (incluindo skill-router)

### Backup (obsoleto)
- **Path:** OneDrive/Architect/Skills/
- **Status:** Não utilizado (config removida)

## Skills Disponíveis

| Skill | Descrição | Uso |
|-------|-----------|-----|
| campaign-timeline | Análise de campanhas com linha do tempo | Análise de performance |
| data-analysis | Análise estatística e tratamento de dados | Testes, hipóteses |
| development-workflow | Código, scripts, automações | Desenvolvimento |
| html-report-system | Relatórios e dashboards HTML | Visualização |
| marketing-analytics | Métricas de mídia e benchmarks | Análise de mídia |
| obsidian-management | Gestão do vault Obsidian | Organização |
| proactive-monitoring | Monitoramento e alertas | Detecção de anomalias |
| skill-router | Roteador obrigatório de skills | Início de qualquer tarefa |

## Mecanismo de Ativação

1. **Via slash:** Digite `/nome-da-skill` no chat
2. **Via instrução:** Agente carrega automaticamente baseado na tarefa
3. **Via tool skill:** LLM chama explicitamente

## Regras de Uso

1. **SEMPRE verificar skills** antes de executar tarefa de análise
2. **Uma tarefa pode usar múltiplas skills**
3. **Priorizar skills específicas** sobre genéricas
4. **Documentar qual skill foi usada** no resultado

## Manutenção

- **Revisão trimestral:** Verificar se skills estão atualizadas
- **Owner:** Sysyphus (responsável por atualizações)
- **Versionamento:** Git (quando aplicável)

## Referências

- [[Architect Architecture v1]] - Arquitetura geral do sistema
- [[Skills/campaign-timeline]] - Exemplo de skill detalhada
