# Changelog

## [2.0.0] - 2026-08-11

### Added
- Cache em memória com TTL configurável (padrão: 5 minutos)
- Cache em disco com persistência JSON em `architect/data/cache/`
- Refresh automático: `refresh_data()` e `refresh_all_data()`
- Métricas de performance: `get_cache_metrics()` (hits, misses, taxa de acerto)
- Configuração de TTL: `set_cache_ttl()`
- Parâmetro `use_cache` em todas as funções de carregamento
- Documentação técnica completa em `Data/GOOGLE_SHEETS_MULTI_INTEGRATION.md`
- ADR-0003: Decisão de migração para v2.0 com cache

### Changed
- Script `google_sheets_multi_loader.py` consolidado como fonte primária
- Dependências migradas de `gspread`/`oauth2client` para `pandas`/`requests`
- Documentação atualizada em todos os arquivos para refletir v2.0
- Troubleshooting expandido com erros de cache

### Deprecated
- Script `google_sheets_loader.py` mantido como legado (uso desencorajado)

## [1.2.0] - 2026-08-10

### Added
- Integração com Google Sheets como fonte primária de dados D-1
- Script `google_sheets_loader.py` para carregamento automatizado
- Configuração `sheets_config.json` para parâmetros de integração
- Referência `database_sheets` no opencode.jsonc
- Documentação completa da integração em `Data/Google Sheets Integration.md`
- Testes aprovados (9/9), 10.239 linhas carregadas

### Changed
- Atualização da documentação para refletir nova fonte de dados
- Base Excel mantida como backup
- README.md atualizado com seção "Fonte de Dados" detalhada
- Troubleshooting adicionado à documentação da integração

## [1.1.0] - 2026-08-08

### Added
- Documentação completa da arquitetura de agentes
- Restrições de permissão por agente no opencode.jsonc
- Subagentes de especialidade configurados

### Changed
- Odysseus agora opera em modo plan interativo (pergunta antes de agir)
- Sysyphus é o único agente com permissão de escrita
- Atena e Hermes configurados como subagentes com restrições

### Removed
- Agentes padrão plan e build desabilitados

## [1.0.0] - 2026-08-04

### Added
- Criação inicial do sistema Architect
- 4 agentes principais: Odysseus, Sysyphus, Atena, Hermes
- Skills básicas configuradas
