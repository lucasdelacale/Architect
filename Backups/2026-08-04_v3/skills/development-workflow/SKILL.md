---
name: development-workflow
description: Use ao desenvolver código, automações, scripts, integrar APIs, versionar com Git ou organizar arquitetura de projetos. Abrange convenções de Git, estrutura de projeto e padrões Python/JavaScript.
---

# Development Workflow

## Git

- Commits pequenos e coesos, mensagem clara no imperativo (ex.: `add caching to report builder`).
- Branches: `main` estável; `feature/<nome>` para trabalho novo.
- Antes de commitar: `git status`, `git diff`, `git log --oneline -10`.
- Nunca commitar segredos ou arquivos gerados (`.env`, `node_modules/`, `.venv/`).
- Só commit/amend/push/PR quando explicitamente solicitado.

## Estrutura de projeto

- Separe responsabilidades: dados, lógica, apresentação, config.
- `.env` para segredos (nunca versionar); documentar com `.env.example`.
- Requirements/dependências explícitas (`requirements.txt`, `package.json`).
- Testes junto do código; rodar antes de entregar.

## Python

- Idiomático, tipado (type hints), docstrings quando útil.
- Prefira funções puras; isolamento de efeitos colaterais.
- Tratamento de erros explícito.

## JavaScript

- Módulos claros; evitar estado global desnecessário.
- Async com `async/await`.
- Sem dependências pesadas para tarefas simples.

## Automações/APIs

- Entenda o contrato da API antes de integrar (auth, rate limit, erros).
- Automações devem ser idempotentes quando possível.
- Log claro de execução para diagnóstico.

## Regras

- Entenda o problema antes de escrever código.
- Prefira a solução mais simples que funciona.
- Documente o necessário para manutenção.
