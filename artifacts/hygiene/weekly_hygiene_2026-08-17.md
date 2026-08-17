# Rotina semanal de higiene canônica — 2026-08-17

Data: 2026-08-17 (segunda-feira, 09:00)
Rotina: weekly canonical hygiene
Base analisada: `main` @ `3129f71556367bccde3e83e507556d66723a9260`

---

## Veredicto geral

**RUÍDO ACUMULADO — AÇÃO DO OPERADOR NECESSÁRIA**

O repositório está funcionalmente íntegro (JSON canônico limpo, locks `false`, fases fechadas), mas o backlog de PRs automatizados não revisados continua crescendo sem intervenção humana. Esta é a sexta semana consecutiva com `main` congelado.

---

## Achados

### [CRÍTICO] PR accumulation — 30 PRs abertos, main frozen 42 dias

| Métrica | Valor |
|---|---|
| Último commit em `main` | 2026-07-06 (`3129f71`) |
| PRs abertos | 30 (#9–#38) |
| PRs de daily doctor | ~25 (criados diariamente) |
| PRs de weekly hygiene | 5 (#11, #16, #20, #27, #32) |
| Ramos remotos estagnados | 30+ |

A rotina `active-context doctor` cria um PR por dia independentemente de haver diff real ou não. O resultado é uma fila ilegível que dificulta a identificação de PRs com conteúdo acionável.

**PRs com conteúdo relevante que o operador deveria avaliar primeiro:**

- **PR #38** (2026-08-16) — `claude/great-bell-7s78ct` — `mergeable_state: clean`
  - Corrige drift em `README.md` (remove bloco `## Current snapshot` duplicado da era IF09)
  - Corrige drift em `CURRENT_STATE.md` (seção `### next_phase` ainda mostrava `LAPIDARIUM_FASE_4_REVISAO_CODIGO_GENUINO` / `next_phase_authorized_by_operator: true`, divergindo do JSON canônico que tem `null` / `false`)
  - 12 adições, 18 deleções, 2 arquivos, 1 commit — pequeno e revisável

- **PR #32** (2026-08-10) — `claude/beautiful-noether-jlhcqp` — relatório de higiene da semana passada
  - Documenta os mesmos achados; sem alteração de arquivo canônico

Os demais PRs daily doctor (#9–#37, exceto #32) propõem variações mínimas dos mesmos drifts e podem ser fechados em lote sem perda de informação.

---

### [MÉDIO] README.md — duplo `## Current snapshot` (drift não corrigido)

O `README.md` em `main` ainda contém dois blocos `## Current snapshot`:

1. **Bloco atual (correto):** Lapidarium Fase 6, candidata `DIAGNOSTICO_AUTOMACAO_GATE`
2. **Bloco histórico (stale):** IF09_CLOSURE_MILESTONE_MIRROR_SANITY_PACKET — superseded, deve estar sob `## Historical Appendix`

Correção proposta: PR #38 (pronto para merge).

---

### [MÉDIO] CURRENT_STATE.md — seção `### next_phase` com drift

A seção `### next_phase` de `CURRENT_STATE.md` em `main` mostra:
- `next_phase: LAPIDARIUM_FASE_4_REVISAO_CODIGO_GENUINO`
- `next_phase_authorized_by_operator: true`

O `ACTIVE_CONTEXT_STATE.json` canônico tem:
- `next_phase: null`
- `active_next_phase: null`
- `next_phase_authorized_by_operator: false` (implícito)

Markdown contradizendo JSON = drift conforme a regra de ouro do repositório.
Correção proposta: PR #38 (pronto para merge).

---

### [BAIXO] DECISION_LOCKS.md — 251K caracteres

O arquivo excede o limite de leitura inline do MCP (251.924 chars). Agentes automatizados não conseguem ler o arquivo na íntegra numa única chamada. Eventual movimentação de seções `CLOSED` para `archive/gate_history/` aliviaria o tamanho — requer decisão explícita do operador, não é escopo desta rotina.

---

## Estado dos arquivos canônicos em `main`

| Arquivo | Estado | Observação |
|---|---|---|
| `ACTIVE_CONTEXT_STATE.json` | ✅ OK | Fonte de verdade íntegra, `phase_id: LAPIDARIUM_FASE_6_GUARDA_TRUE` |
| `CURRENT_STATE.md` | ⚠️ DRIFT | Seção `### next_phase` diverge do JSON (corrigida no PR #38) |
| `NEXT_ACTION.md` | ✅ OK | Consistente com JSON |
| `ROADMAP_CANONICAL.md` | ✅ OK | LAPIDARIUM CLOSED, DIAGNOSTICO_AUTOMACAO_GATE CANDIDATE |
| `README.md` | ⚠️ DRIFT | Bloco `## Current snapshot` duplicado (corrigido no PR #38) |
| `DECISION_LOCKS.md` | ⚠️ ATENÇÃO | Arquivo de 251K chars, leitura por agentes comprometida |
| `artifacts/active_context/` | ✅ OK | 20 artefatos estáveis, fases encerradas |

---

## Ações recomendadas (por prioridade)

1. **Mesclar PR #38** — correção documental segura, `mergeable_state: clean`, 2 arquivos
2. **Fechar em lote PRs daily doctor stale** — #9 a #37 (exceto #32 se quiser manter o relatório da semana passada)
3. **Fechar ou mesclar PR #32** — relatório de higiene 2026-08-10, conteúdo superseded por este
4. **Avaliar a rotina daily doctor** — considerar criar PR somente quando houver diff real vs main, para evitar acumulação futura

---

## O que esta rotina não faz

- Não alterou `ACTIVE_CONTEXT_STATE.json`, `ACTIVE_CONTEXT_SCHEMA.json`, `DECISION_LOCKS.md`, `ROADMAP_CANONICAL.md`, `NEXT_ACTION.md`, `LAB_OPERATING_CONTRACT.md`, `BOOT.md`
- Não tocou `archive/`, `excludent/`, `Project_ARIS`
- Não abriu `next_phase`
- Não alterou locks reais
- Não fez push em `main`
- Não fechou nem mesclou nenhum PR existente

---

## Checksums de referência

- `ACTIVE_CONTEXT_STATE.json` SHA256: `8cae9cb33beb4d5eb9cb4dfdfc308f58bd195bf3371e1caf87b4d966a220fb58`
- `ACTIVE_CONTEXT_STATE.json` git blob: `f3de455c8f686bde7c7a66e0ef36b52b6bd24e27`
- Base commit analisado: `3129f71556367bccde3e83e507556d66723a9260`
- `phase_id`: `LAPIDARIUM_FASE_6_GUARDA_TRUE`
- `next_phase`: `null`
- `active_next_phase`: `null`
- Execution locks all `false`: **sim**
