# Hygiene Report — Weekly Canonical Review 2026-08-03

> Gerado por rotina semanal automática. Revisão humana obrigatória antes de qualquer ação.
> Data: 2026-08-03 | Branch: `claude/beautiful-noether-e49csx`

---

## Resultado

**HYGIENE_ISSUES_FOUND** — dois achados documentados abaixo.

---

## Achado 1 — CRÍTICO: Acúmulo de 25 PRs abertos sem merge

### Descrição

A rotina diária "active-context doctor" e a rotina semanal de higiene (esta mesma) estão abrindo PRs continuamente desde 2026-06-24, mas nenhum PR foi mergeado ou fechado.

**Estado atual:**
- 25 PRs abertos em `MatheusAugDEV/aris-active-context`
- Mais antigo: PR #1 — `active-context doctor: daily mirror/drift cleanup 2026-06-24` (2026-06-24)
- Mais recente antes deste: PR #26 — `active-context doctor: daily mirror/drift cleanup 2026-08-03` (hoje)
- Nenhum commit em `main` desde 2026-07-01 (>1 mês)
- Todos os PRs têm base em `main @ 3129f71`

### Risco

O acúmulo de PRs sem revisão:
- Cria ruído severo na interface do repositório
- Impede identificar rapidamente qual PR é relevante
- Sugere que o loop de automação e o loop de revisão humana estão desconectados
- PRs mais antigos (julho) podem conter diagnósticos que já perderam relevância

### Recomendação para o operador

1. **Revisar e fechar/mergear** PRs antigos da série "active-context doctor" que não contêm mudanças ativas (a maioria provavelmente só tem relatórios sem commits de código).
2. **Avaliar a frequência** da rotina diária: se nenhum PR é mergeado, abrir um por dia não adiciona valor e só aumenta o ruído.
3. **Definir política de expiração**: PRs de higiene sem ação após N dias podem ser fechados automaticamente, ou a rotina pode atualizar um PR existente em vez de abrir um novo.

> Esta rotina semanal NÃO fecha PRs por conta própria — isso requer ação explícita do operador.

---

## Achado 2 — MENOR: README.md com duplo `## Current snapshot` stale

### Descrição

O `README.md` possui **duas seções com o cabeçalho `## Current snapshot`**, sendo a segunda obsoleta (era IF09):

- **Linhas 1–10** (atual e correto): referencia `LAPIDARIUM_FASE_6_GUARDA_TRUE`, SHA correto, locks corretos.
- **Linhas 11–17** (stale): referencia `IF09_CLOSURE_MILESTONE_MIRROR_SANITY_PACKET` — fase encerrada há meses.

Além disso, a seção `## Estado canônico atual` (linhas 88–108) também exibe conteúdo IF09-era antes do separador `## Historical Appendix` (linha 109), sem marcação explícita de que é histórico.

### Risco

Ambiguidade para qualquer leitor que abra o README — o segundo snapshot pode ser confundido com estado atual.

### Correção incluída neste PR

Este PR renomeia e marca as seções stale como `HISTORICAL_ONLY` (ver diff em `README.md`).

---

## Verificados sem achados

| Arquivo | Status |
|---|---|
| `CURRENT_STATE.md` | Limpo — atualizado 2026-07-01, alinhado com JSON |
| `NEXT_ACTION.md` | Limpo — aguardando instrução do operador conforme esperado |
| `ROADMAP_CANONICAL.md` | Limpo — fases CLOSED/CANDIDATE corretas |
| `DECISION_LOCKS.md` | Legível (251 kB) — nenhum lock modificado; conteúdo append-only esperado |
| `artifacts/active_context/` | 21 arquivos, todos da família lapidarium/if09 — sem orphans recentes |
| Commits em `main` (última semana) | 0 — esperado; projeto aguarda autorização de operador |

---

## Resumo

| # | Achado | Severidade | Ação necessária |
|---|---|---|---|
| 1 | 25 PRs abertos sem merge acumulados desde 2026-06-24 | CRÍTICO | Revisão e triagem pelo operador |
| 2 | README.md com segundo `## Current snapshot` stale (IF09) | MENOR | Corrigido neste PR |

---

_Rotina: `beautiful-noether` (higiene canônica semanal, segundas 09:00)_
