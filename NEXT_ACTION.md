# NEXT_ACTION

> Fonte primária: `ACTIVE_CONTEXT_STATE.json`. Este arquivo é mirror derivado.
> JSON é autoridade máxima. Markdown contraditório é drift.
> Última atualização: LAPIDARIUM_FASE_5_CLEANUP_EXECUTION_REMAINING_LOW_SCOPE_SET (2026-06-30)

---

## CURRENT CANONICAL NEXT ACTION

- **Source of truth:** `ACTIVE_CONTEXT_STATE.json`
- **phase_id:** `LAPIDARIUM`
- **sha_lido:** `0a64f632bd25e50c29112a4468298b72ee31af73`

### Status Atual

**Cleanup de baixo escopo atualizado em 2026-06-30.**

F5-004 e F5-005 já estavam ausentes do current HEAD/index do Project_ARIS e, por isso, não exigiram nova remoção.
F5-006 foi removido com `git rm -- legacy/wake/tts.py.backup`.
F5-013/F5-014/F5-015 permanecem fora do escopo e sem intervenção nesta execução.

---

### Próximas Ações (por prioridade)

**1. OPERADOR — Decisões de itens BLOQUEADOS (separadas, por finding):**
- **F4-FIND-002** (`F5-015`): Nested Git repo em `external/mcp_candidates/` —
  escolher estratégia: submodule / vendor / remove / quarantine
- **F4-FIND-003** (`F5-013`, `F5-014`): PostScript binários em `legacy/experiments/` —
  confirmar origem e intenção antes de qualquer remoção (ação irreversível)

**2. OPERADOR — Rotação de Segredos (independente de fase):**
Ver `artifacts/lapidarium/lapidarium_f4_find001_rotation_checklist.md`.
`.env` está corretamente gitignored — avaliação de risco é responsabilidade do operador.

---

### Aguardando Instrução

Todos os locks de runtime, produto e Bedrock permanecem `false`. Nenhuma ação
não autorizada explicitamente pelo operador será iniciada.

---

## Historical Appendix

`HISTORICAL_ONLY`
`SUPERSEDED_BY_LAPIDARIUM_FASE4_AND_F4_FIND001_CONTAINMENT`
`NOT_CURRENT_STATE`

Referências a IF09/next_phase=null e P15–P19 são históricas e superseded.
