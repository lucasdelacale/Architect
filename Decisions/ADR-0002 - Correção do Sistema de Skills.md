# ADR-0002 - Correção do Sistema de Skills

## Status

Implementado

## Data

2026-08-11

## Contexto

O sistema de skills do OpenCode não estava ativando automaticamente em tarefas óbvias. Após análise, identificamos que:
1. Não existe mecanismo de matching automático no OpenCode
2. O sistema depende de instruções explícitas nos prompts dos agentes
3. Haviam dois locais diferentes de skills (desincronização)
4. Agentes mencionavam skills de forma opcional

## Decisões

### 1. Fonte Primária de Skills

**Decisão:** Manter `~/.config/opencode/skills/` como fonte primária.

**Justificativa:**
- Local padrão do OpenCode
- Já continha 7 skills funcionais
- OneDrive estava obsoleto e causava desincronização

### 2. Adição de `slash: true`

**Decisão:** Adicionar `slash: true` no frontmatter de todas as 8 skills.

**Justificativa:**
- Permite ativação via `/nome-da-skill`
- Melhora descoberta e usabilidade
- Padrão suportado pelo OpenCode

### 3. Instrução Obrigatória nos Agentes

**Decisão:** Adicionar "Regra Obrigatória: Uso de Skills" em todos os 15 agentes.

**Justificativa:**
- Força verificação de skills antes de executar tarefas
- Tabela de decisão padronizada
- Linguagem obrigatória (não opcional)

### 4. Criação da Skill Router

**Decisão:** Criar skill `skill-router` como roteador obrigatório.

**Justificativa:**
- Centraliza lógica de decisão
- Serve como ponto de entrada para qualquer tarefa
- Documenta mapeamento completo skill ↔ tarefa

## Consequências

### Positivas
- Ativação automática de skills em tarefas óbvias
- Padrão unificado em todos os agentes
- Melhor descoberta via slash commands
- Documentação completa no vault

### Negativas
- Necessidade de reiniciar OpenCode para reconhecer novas skills
- Manutenção de tabela de decisão em múltiplos locais

## Métricas de Sucesso

1. Pelo menos 2/3 tarefas de teste devem ativar skill corretamente
2. Todas as 8 skills devem estar disponíveis via `/nome-da-skill`
3. Agentes devem mencionar skill carregada nos resultados

## Referências

- [[Sistema de Skills - Arquitetura]]
- [[Architect Architecture v1]]
