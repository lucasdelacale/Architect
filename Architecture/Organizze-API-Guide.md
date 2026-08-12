# Organizze API - Guia Completo de Integracao

> **Ultima atualizacao:** 2026-08-11
> **Status:** Pesquisa completa
> **Fontes:** developers.organizze.com.br, github.com/organizze/agent-tools, organizze.com.br/agentes

---

## Sumario

1. [Visao Geral](#visao-geral)
2. [Autenticacao](#autenticacao)
3. [REST API v2 - Endpoints](#rest-api-v2---endpoints)
4. [Conexao com Agentes de IA (MCP)](#conexao-com-agentes-de-ia-mcp)
5. [Precos e Planos](#precos-e-planos)
6. [Limitacoes](#limitacoes)
7. [Exemplos de Requisicoes](#exemplos-de-requisicoes)
8. [Integracao com Google Sheets](#integracao-com-google-sheets)
9. [Integracao com Obsidian](#integracao-com-obsidian)
10. [Ferramentas Disponiveis](#ferramentas-disponiveis)
11. [Projetos Open Source](#projetos-open-source)

---

## Visao Geral

O Organizze oferece duas formas principais de integracao:

| Tipo | Descricao | Uso Ideal |
|------|-----------|-----------|
| **REST API v2** | API REST classica com Basic Auth | Scripts, automacoes, integracao customizada |
| **MCP Remoto** | Conector OAuth para agentes de IA | ChatGPT, Claude, Manus (sem instalar nada) |

**URLs importantes:**
- Documentacao API: `https://developers.organizze.com.br/`
- MCP Remoto: `https://mcp.organizze.com.br/mcp`
- GitHub Agent Tools: `https://github.com/organizze/agent-tools`

---

## Autenticacao

### REST API v2 (Basic Auth)

```bash
curl https://api.organizze.com.br/rest/v2/accounts \
  -u "seu-email@exemplo.com:SUA_API_KEY" \
  -H "User-Agent: meu-app (seu-email@exemplo.com)"
```

**Como obter a API Key:**
1. Faca login em `https://app.organizze.com.br`
2. Va para **Configuracoes → Chaves de API**
3. Gere uma nova chave

**Regras:**
- `User-Agent` e **obrigatorio** em toda requisicao
- Chaves somente-leitura retornam `403` em operacoes de escrita
- Conta deve ter licenca ativa

### MCP Remoto (OAuth)

Para agentes de IA (ChatGPT, Claude, Manus):
1. Adicione o conector com URL: `https://mcp.organizze.com.br/mcp`
2. Faca login no Organizze pelo browser
3. Escolha a carteira e autorize o acesso
4. Pronto - sem necessidade de copiar API keys

**Descoberta OAuth:**
```
GET https://mcp.organizze.com.br/.well-known/oauth-protected-resource
GET https://mcp.organizze.com.br/.well-known/oauth-authorization-server
```

---

## REST API v2 - Endpoints

### Conventions

- Valores monetarios em **centavos** (inteiro): `amount_cents`, `limit_cents`
- Paginacao via header `Link` com `rel="first|last|next|prev"`
- Create/Update retornam `201` (nao `200`)

### Accounts (Contas)

| Metodo | Endpoint | Descricao |
|--------|----------|-----------|
| GET | `/rest/v2/accounts` | Listar contas |
| POST | `/rest/v2/accounts` | Criar conta |
| GET | `/rest/v2/accounts/{id}` | Obter conta (com saldo) |
| PUT | `/rest/v2/accounts/{id}` | Atualizar conta |
| DELETE | `/rest/v2/accounts/{id}` | Deletar conta |
| PUT | `/rest/v2/accounts/{id}/archive` | Arquivar |
| PUT | `/rest/v2/accounts/{id}/unarchive` | Desarquivar |

**Tipos:** `checking`, `savings`, `other`, `credit_card`

### Credit Cards (Cartoes)

| Metodo | Endpoint | Descricao |
|--------|----------|-----------|
| GET | `/rest/v2/credit_cards` | Listar cartoes |
| POST | `/rest/v2/credit_cards` | Criar cartao |
| GET | `/rest/v2/credit_cards/{id}` | Obter cartao |
| PUT | `/rest/v2/credit_cards/{id}` | Atualizar |
| DELETE | `/rest/v2/credit_cards/{id}` | Deletar |

**Campos:** `closing_day`, `due_day`, `limit_cents`, `card_network`

### Invoices (Faturas)

| Metodo | Endpoint | Descricao |
|--------|----------|-----------|
| GET | `/rest/v2/credit_cards/{cc_id}/invoices` | Listar faturas |
| GET | `/rest/v2/credit_cards/{cc_id}/invoices/{id}` | Obter fatura (c/ transacoes) |
| GET | `.../invoices/{id}/payments` | Pagamentos da fatura |
| POST | `.../invoices/{id}/payments` | Registrar pagamento |

### Transactions (Transacoes)

| Metodo | Endpoint | Descricao |
|--------|----------|-----------|
| GET | `/rest/v2/transactions` | Listar (filtro por data) |
| POST | `/rest/v2/transactions` | Criar transacao |
| GET | `/rest/v2/transactions/{id}` | Obter transacao |
| PUT | `/rest/v2/transactions/{id}` | Atualizar |
| DELETE | `/rest/v2/transactions/{id}` | Deletar |

**Filtros:** `start_date`, `end_date`, `account_id`, `page`

**Tags e recorrencia:**
```json
{
  "description": "Aluguel",
  "date": "2026-08-01",
  "amount_cents": 150000,
  "paid": true,
  "recurrence_attributes": {
    "periodicity": "monthly"
  },
  "tags": [{"name": "fixo"}]
}
```

### Transfers (Transferencias)

| Metodo | Endpoint | Descricao |
|--------|----------|-----------|
| GET | `/rest/v2/transfers` | Listar |
| POST | `/rest/v2/transfers` | Criar |
| GET | `/rest/v2/transfers/{id}` | Obter |
| PUT | `/rest/v2/transfers/{id}` | Atualizar |
| DELETE | `/rest/v2/transfers/{id}` | Deletar |

### Categories (Categorias)

| Metodo | Endpoint | Descricao |
|--------|----------|-----------|
| GET | `/rest/v2/categories` | Listar |
| POST | `/rest/v2/categories` | Criar |
| GET | `/rest/v2/categories/{id}` | Obter |
| PUT | `/rest/v2/categories/{id}` | Atualizar |
| DELETE | `/rest/v2/categories/{id}` | Deletar |

### Budgets (Orcamentos)

| Metodo | Endpoint | Descricao |
|--------|----------|-----------|
| GET | `/rest/v2/budgets` | Orcamentos do mes atual |
| GET | `/rest/v2/budgets?year=2026` | Orcamentos do ano |
| GET | `/rest/v2/budgets?year=2026&month=8` | Mes especifico |

### Balances (Saldos)

| Metodo | Endpoint | Descricao |
|--------|----------|-----------|
| GET | `/rest/v2/balances` | Saldo agregado |

### Bank Connections (Conexao Bancaria)

| Metodo | Endpoint | Descricao |
|--------|----------|-----------|
| GET | `/rest/v2/bank_connections` | Listar conexoes |
| POST | `/rest/v2/bank_connections` | Criar conexao |
| PUT | `/rest/v2/bank_connections/{id}` | Atualizar |
| DELETE | `/rest/v2/bank_connections/{id}` | Desconectar |

### Institutions (Instituicoes)

| Metodo | Endpoint | Descricao |
|--------|----------|-----------|
| GET | `/rest/v2/institutions` | Instituicoes suportadas |

### Users & Entities

| Metodo | Endpoint | Descricao |
|--------|----------|-----------|
| GET | `/rest/v2/users` | Usuarios da entidade |
| GET | `/rest/v2/users/{id}` | Obter usuario |
| GET | `/rest/v2/entities` | Espacos financeiros |
| GET | `/rest/v2/entities/{id}` | Obter entidade |

---

## Conexao com Agentes de IA (MCP)

### Como Funciona

O Organizze usa **MCP (Model Context Protocol)** para conectar a assistentes de IA. O conector remoto expoe **60 ferramentas** (32 leitura + 28 escrita).

### Conectar no ChatGPT

1. Abra ChatGPT
2. Acesse **Configuracoes → Pluggins**
3. Clique em "adicionar Novo Servidor"
4. Tipo: "Http com streaming"
5. URL: `https://mcp.organizze.com.br/mcp`
6. Clique em "autenticar" no Organizze
7. Faca login e escolha a carteira
8. Autorize o acesso

### Conectar no Claude

1. Abra Claude
2. Acesse **Conectores**
3. Adicione conector MCP remoto
4. URL: `https://mcp.organizze.com.br/mcp`
5. Faca login e autorize

### Conectar no Manus

1. Abra Manus
2. **Configuracoes → Integracoes**
3. MCP personalizado
4. URL: `https://mcp.organizze.com.br/mcp`
5. Login e autorizacao

### Perguntas Possiveis

```
"Quanto tenho disponivel nas minhas contas?"
"Registre um gasto com mercado de R$ 85"
"Em que categoria estou gastando mais?"
"Quanto ainda posso gastar este mes?"
"Qual cartao esta com a maior fatura?"
"Estou gastando mais do que mes passado?"
```

### Seguranca

- **Somente leitura por padrao** - escrita so com consentimento
- **Revogavel** em Configuracoes → Apps conectados
- **Login via OAuth** - sem copiar chaves no chat

---

## Precos e Planos

| Plano | Mensal | Anual (12x) | Avista | Diferencial |
|-------|--------|-------------|--------|-------------|
| **Manual** | R$ 35 | R$ 19,90/mes | R$ 199,90 | Controle manual |
| **Conectado** | R$ 45 | R$ 39,90/mes | R$ 399,90 | Ate 3 contas bancarias |
| **Conectado Plus** | R$ 69 | R$ 59,90/mes | R$ 599,90 | Ate 10 contas + PJ |

### Detalhes por Plano

**Plano Manual:**
- Controle manual de contas e cartoes
- Categorias e subcategorias
- Limite de gastos ilimitado
- Alertas de contas a pagar
- Relatorios completos
- Teste gratis 7 dias

**Plano Conectado (TODO do Manual +):**
- Ate 3 contas/cartoes conectados via Open Finance
- 1 atualizacao automatica/dia + 2 extras
- Conexao com contas Pessoa Fisica

**Plano Conectado Plus (TODO do Conectado +):**
- Ate 10 contas/cartoes conectados
- 4 atualizacoes extras/dia
- Conexao PF e Pessoa Juridica

### IA - Todos os Planos

A conexao com agentes de IA (ChatGPT, Claude, Manus) esta **disponivel para TODOS os planos** sem custo adicional.

---

## Limitacoes

1. **Dados dependem do Organizze** - IA responde apenas com dados disponiveis na conta
2. **Conexao Bancaria precisa ser sincronizada** - importar lancamentos antes de consultar
3. **Respostas podem variar** - IA interpreta perguntas em linguagem natural
4. **Nem todos os assistentes sao iguais** - experiencia varia entre ChatGPT/Claude/Manus
5. **Rate limits** - API tem limites de requisicao (nao documentados publicamente)
6. **Historico** - Conexao Bancaria traz apenas 90 dias de historico

---

## Exemplos de Requisicoes

### Listar Contas

```bash
curl https://api.organizze.com.br/rest/v2/accounts \
  -u "email:API_KEY" \
  -H "User-Agent: my-app (email)"
```

**Resposta:**
```json
[
  {
    "id": 123,
    "name": "Nubank",
    "type": "checking",
    "balance": "R$ 5.432,10"
  }
]
```

### Listar Transacoes do Mes

```bash
curl "https://api.organizze.com.br/rest/v2/transactions?start_date=2026-08-01&end_date=2026-08-31" \
  -u "email:API_KEY" \
  -H "User-Agent: my-app (email)"
```

### Criar Transacao

```bash
curl -X POST https://api.organizze.com.br/rest/v2/transactions \
  -u "email:API_KEY" \
  -H "User-Agent: my-app (email)" \
  -H "Content-Type: application/json" \
  -d '{
    "description": "Supermercado",
    "date": "2026-08-10",
    "amount_cents": 8500,
    "paid": true,
    "category_id": 456
  }'
```

### Usando CLI

```bash
npm i -g @organizze/cli
organizze login
organizze accounts list
organizze transactions list --since 2026-01-01 --json
```

### Python (Exemplo basico)

```python
import requests

EMAIL = "seu@email.com"
API_KEY = "sua-chave"
BASE = "https://api.organizze.com.br/rest/v2"

headers = {"User-Agent": "meu-app (seu@email.com)"}

# Listar contas
resp = requests.get(f"{BASE}/accounts", auth=(EMAIL, API_KEY), headers=headers)
contas = resp.json()

# Listar transacoes de agosto
resp = requests.get(
    f"{BASE}/transactions",
    params={"start_date": "2026-08-01", "end_date": "2026-08-31"},
    auth=(EMAIL, API_KEY),
    headers=headers
)
transacoes = resp.json()
```

---

## Integracao com Google Sheets

### Opcao 1: Script Apps Script (Google)

```javascript
// Google Apps Script para puxar dados do Organizze

const EMAIL = "seu@email.com";
const API_KEY = "sua-chave";
const BASE = "https://api.organizze.com.br/rest/v2";

function fetchOrganizzeData() {
  const options = {
    "headers": {
      "Authorization": "Basic " + Utilities.base64Encode(EMAIL + ":" + API_KEY),
      "User-Agent": "google-sheets-integration (seu@email.com)"
    }
  };

  // Buscar transacoes do mes atual
  const today = new Date();
  const start = today.getFullYear() + "-" + String(today.getMonth()+1).padStart(2,'0') + "-01";
  const end = today.getFullYear() + "-" + String(today.getMonth()+1).padStart(2,'0') + "-31";

  const url = `${BASE}/transactions?start_date=${start}&end_date=${end}`;
  const response = UrlFetchApp.fetch(url, options);
  const transactions = JSON.parse(response.getContentText());

  // Escrever na planilha
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  sheet.clear();

  // Cabecalhos
  sheet.appendRow(["Data", "Descricao", "Valor", "Categoria", "Pago"]);

  // Dados
  transactions.forEach(t => {
    sheet.appendRow([
      t.date,
      t.description,
      t.amount_cents / 100,
      t.category_id,
      t.paid ? "Sim" : "Nao"
    ]);
  });
}
```

### Opcao 2: Google Sheets + Organizze API via Python

```python
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests

# Configurar Google Sheets
scope = ["https://spreadsheets.google.com/feeds"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)

# Configurar Organizze
EMAIL = "seu@email.com"
API_KEY = "sua-chave"
headers = {"User-Agent": "sheets-integration"}

# Buscar dados
resp = requests.get(
    "https://api.organizze.com.br/rest/v2/transactions",
    params={"start_date": "2026-08-01", "end_date": "2026-08-31"},
    auth=(EMAIL, API_KEY),
    headers=headers
)

# Escrever na planilha
sheet = client.open("Financas").sheet1
sheet.clear()
sheet.append_row(["Data", "Descricao", "Valor"])

for t in resp.json():
    sheet.append_row([t["date"], t["description"], t["amount_cents"]/100])
```

---

## Integracao com Obsidian

### Nao existe plugin oficial do Organizze para Obsidian

**Opcoes possiveis:**

### Opcao 1: Script de Sincronizacao Periodica

Criar um script que busca dados do Organizze e cria/atualiza notas no Obsidian:

```python
import requests
import os
from datetime import datetime

# Config
EMAIL = os.getenv("ORGANIZZE_EMAIL")
API_KEY = os.getenv("ORGANIZZE_API_KEY")
VAULT_PATH = "C:/Users/lucas.martins/OneDrive - insidemedia.net/Documentos/Obsidian Vault/Financas"

headers = {"User-Agent": "obsidian-sync"}

# Buscar contas
accounts = requests.get(
    "https://api.organizze.com.br/rest/v2/accounts",
    auth=(EMAIL, API_KEY),
    headers=headers
).json()

# Criar nota de resumo
today = datetime.now().strftime("%Y-%m-%d")
filename = f"{VAULT_PATH}/Resumo-Financeiro-{today}.md"

with open(filename, "w", encoding="utf-8") as f:
    f.write(f"# Resumo Financeiro - {today}\n\n")
    f.write("## Contas\n\n")
    f.write("| Conta | Saldo |\n|-------|-------|\n")
    for acc in accounts:
        f.write(f"| {acc['name']} | {acc.get('balance', 'N/A')} |\n")
```

### Opcao 2: Usar MCP no Claude/Obsidian

Se o Obsidian tiver integracao com Claude (via plugins como "Copilot" ou "Smart Connections"), voce pode:
1. Conectar o Organizze ao Claude via MCP
2. Perguntar sobre financas pelo Claude dentro do Obsidian

### Opcao 3: Exportacao Manual + Templater

1. Exportar dados do Organizze (CSV/JSON)
2. Usar plugin Templater do Obsidian para gerar notas

---

## Ferramentas Disponiveis

| Ferramenta | Descricao | Como usar |
|------------|-----------|-----------|
| **REST API v2** | API classica | `curl`, scripts, apps |
| **MCP Remoto** | Para agentes de IA | ChatGPT, Claude, Manus |
| **CLI** | Linha de comando | `npm i -g @organizze/cli` |
| **Agent Skill** | Skill para AI agents | `@organizze/agent-tools` |
| **API Client** | Cliente TypeScript | `@organizze/api-client` |

### CLI - Exemplos

```bash
# Instalar
npm i -g @organizze/cli

# Login
organizze login

# Listar contas
organizze accounts list

# Listar transacoes
organizze transactions list --since 2026-01-01

# Output JSON
organizze transactions list --json
```

---

## Projetos Open Source

| Repositorio | Descricao | Linguagem |
|-------------|-----------|-----------|
| [organizze/agent-tools](https://github.com/organizze/agent-tools) | Oficial - API client, CLI, MCP, Skill | TypeScript |
| [arturovaine/telegram-bot-organizze](https://github.com/arturovaine/telegram-bot-organizze) | Bot Telegram + Gemini AI | Python |
| [tarcisiopgs/organizze-skill](https://github.com/tarcisiopgs/organizze-skill) | Agent Skill para AI assistants | - |
| [flyingluscas/organizze-cli](https://github.com/flyingluscas/organizze-cli) | CLI antigo | JavaScript |
| [graduenz/norganizze](https://github.com/graduenz/norganizze) | Cliente .NET | C# |

---

## Links Uteis

- **API Docs:** https://developers.organizze.com.br/
- **MCP Docs:** https://developers.organizze.com.br/remote-mcp.html
- **Planos:** https://organizze.com.br/planos
- **Agentes IA:** https://organizze.com.br/agentes
- **Ajuda:** https://ajuda.organizze.com.br/
- **GitHub:** https://github.com/organizze/agent-tools

---

## Proximos Passos Recomendados

1. **Criar conta no Organizze** (testar 7 dias gratis)
2. **Gerar API Key** em Configuracoes → Chaves de API
3. **Testar MCP** conectando ao ChatGPT ou Claude
4. **Criar script de sync** para Google Sheets (Apps Script)
5. **Avaliar integracao Obsidian** via script periodico ou MCP indireto

---

*Nota criada como parte da pesquisa de integracao financeira. Conecta com: [[Architect Architecture]], workflows de automacao.*
