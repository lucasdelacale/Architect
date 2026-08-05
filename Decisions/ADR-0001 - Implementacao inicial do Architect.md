# ADR-0001 — Implementação inicial do Architect

- Status: Aceito
- Data: 2026-08-04
- Autor: Lucas Martins + Architect

## Contexto

Criar uma organização digital de especialistas em IA no OpenCode, substituindo o uso de um assistente único. Requisitos: agentes com papéis claros, colaboração entre especialistas, preservação de conhecimento no Obsidian, revisão de decisões e evolução contínua da própria arquitetura.

## Decisão

Implementar o Architect no escopo global (`~/.config/opencode/`) com:

- **4 modos de execução** primary substituindo os modos padrão `plan`/`build` do OpenCode:
  - `sysyphus` (worker principal) — único que altera arquivos de config/code/sistema.
  - `odysseus` (planejador crítico) — `edit: deny`.
  - `atena` (revisão e pensamento crítico) — `edit: deny`.
  - `hermes` (pesquisa) — cria apenas notas no Obsidian.
- **8 subagentes especialistas** mode `subagent` (delegáveis via Task ou @nome).
- **1 meta-agente subagent** (`architect-evolution`) para auditoria e evolução.

Acompanham: 5 skills reutilizáveis, 7 workflows (commands) com lógica condicional, e documentação completa no vault Obsidian `Architect`.

## Detalhes da decisão

- **Escopo global**: copiloto profissional multi-contexto (trabalho + projetos pessoais).
- **Grid de Delegação (Sysyphus/Odysseus/Atena)**: os agentes são classificados em operacional, estratégia e julgamento crítico. O orquestrador usa a tabela para delegar; nenhum agente pinna modelo, que é escolhido pelo usuário no TUI por sessão.
- **Somente Sysyphus altera arquivos de config/code/sistema**: `odysseus` e `atena` têm `edit: deny`; `hermes` edita apenas o vault Obsidian.
- **Obsidian como memória**: path fixo da vault permitido via `permission.external_directory` e `references`. Histórico orienta, nunca limita.
- **Backup**: configuração inicial preservada em `Backups/2026-08-04_v1/` e transição de modos em `Backups/2026-08-04_v2/`.
- **Idioma**: PT-BR em comunicação e documentação; código em inglês.

## Consequências

- Positive: especialização, colaboração, memória persistente, evolução guiada.
- Negative: cadeia de subagents consome mais contexto; mitigado com briefing enxuto e síntese entre estágios.
- Riscos: caminhos OneDrive com sync (mitigado com backups); escolha de modelo é manual via TUI (sem `model` definido no config global).

## Próximos passos

- Revisar o Grid de Delegação (Sysyphus/Odysseus/Atena) em `Architecture/Architect Architecture v1.md` conforme o uso real.
- Reiniciar o OpenCode para carregar a configuração.
- Rodar `/evolution-audit` após o primeiro ciclo de uso.

## Links

- [[Architecture/Architect Architecture v1]]
- [[Evolution/README]]
