# ADR-0003 - Migração Google Sheets para v2.0 com Cache

**Data**: 2026-08-11
**Status**: Aceito
**Decisor**: Lucas Martins

---

## Contexto

A integração Google Sheets original (v1.0) utilizava `gspread` e `oauth2client` para autenticação, sem suporte a cache. Cada requisição gerava uma chamada à API, impactando performance em consultas repetidas.

## Decisão

Migrar para `google_sheets_multi_loader.py` v2.0 com:
- Cache em memória (TTL configurável, padrão 5min)
- Cache em disco (persistência JSON)
- Refresh automático (seletivo por plataforma ou total)
- Métricas de performance
- Dependências simplificadas: `pandas` + `requests`

## Consequências

### Positivas
- Performance significativamente melhorada em consultas repetidas
- Redução de chamadas à API do Google Sheets
- Persistência de dados entre sessões
- Visibilidade sobre performance do cache

### Negativas
- Necessidade de gerenciar cache (expiração, invalidação)
- Espaço em disco para cache persistido
- Script original `google_sheets_loader.py` mantido como legado

### Neutras
- API pública da planilha permanece inalterada
- Estrutura de dados idêntica à v1.0

---

## Notas

- Documentação completa: [[Data/GOOGLE_SHEETS_MULTI_INTEGRATION]]
- Integração: [[Data/Google Sheets Integration]]
- Changelog: [[CHANGELOG]] v2.0.0
