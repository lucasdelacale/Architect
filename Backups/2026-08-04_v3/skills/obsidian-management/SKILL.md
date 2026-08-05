---
name: obsidian-management
description: Use ao ler, criar, organizar ou conectar notas no Obsidian; recuperar contexto, registrar aprendizados ou documentar no vault Architect. Abrange convenções de nota, wikilinks e estrutura de pastas do vault em C:\Users\lucas.martins\OneDrive - insidemedia.net\Documentos\Obsidian Vault\Architect.
---

# Obsidian Management

## Vault

Path raiz: `C:\Users\lucas.martins\OneDrive - insidemedia.net\Documentos\Obsidian Vault\Architect`

## Estrutura

- `Architecture/` — documentação da arquitetura do sistema (fonte de verdade).
- `Agents/` — 1 doc por agente.
- `Skills/` — 1 doc por skill.
- `Workflows/` — 1 doc por workflow.
- `Evolution/Audits|Weekly|Monthly|Quarterly` — relatórios de evolução.
- `Decisions/` — ADRs (Architecture Decision Records).
- `Backups/` — snapshots da configuração.
- `Install/` — prompt de instalação do Architect.

## Convenções

- Nome de notas: PascalCase, sem espaços, sem acentos (ex.: `Architect Architecture v1.md`).
- Use wikilinks `[[Nota]]` para conectar notas relacionadas.
- Toda nota nova de decisão vai em `Decisions/ADR-NNNN-titulo.md` (NNNN sequencial).
- Toda nota de análise/experimento deve registrar: data, contexto, hipótese, resultado, aprendizado.
- Ao criar conteúdo, espelhe a estrutura de pastas já existente.

## Fluxo de recuperação de contexto

1. Identifique termos-chave do pedido.
2. Busque notas relacionadas (decisões, experimentos, análises).
3. Sintetize o contexto recuperado e indique lacunas.
4. Nunca trate o histórico como limite para novas hipóteses.

## Boas práticas

- Backups antes de qualquer alteração estrutural.
- Uma ideia por nota.
- Conecte sempre com wikilinks.
- Prefira PT-BR.
