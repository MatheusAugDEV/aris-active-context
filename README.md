# aris-active-context

Compact, read-first ARIS context entrypoint.

Read order:

1. `CURRENT_STATE.md`
2. `NEXT_ACTION.md`
3. `DECISION_LOCKS.md`
4. `ARIS_PHASE_LEDGER.md`
5. `CONTEXT_INDEX.md`
6. `OPERATOR_PREFERENCES.md`
7. `PROMPT_CONTRACT.md`

Current snapshot:

- Official V6 is closed.
- F32 owns MCP read-only configuration, controlled apply planning, activation planning, smoke validation, zero-write/no-bulk-read validation, and closure.
- Latest completed phase: `F33.F — Governed Local Memory Schema Contract Review Gate`
- Next principal phase: `F33.G — Governed Local Memory SQLite Dry-Run Plan Gate`
- F33 now advances through Governed Local Memory technical planning/review-only work; Similar Projects remains advisory-only at phase start; F32 closure is complete.
- F32.RESEARCH-P0 created an artifact-only research intake program; it does not alter the operational next action.

Rules:

- Query-first, no bulk-read, no network, no dependency installs, no real MCP activation, no secret reads.
- `CURRENT_STATE.md`, `NEXT_ACTION.md`, and `DECISION_LOCKS.md` are the operational sources of truth.
- Historical depth belongs in `ARIS_PHASE_LEDGER.md`.
- F32.RESEARCH-P3 created a candidate roadmap impact delta; canonical roadmap and operational next action unchanged.

- F33.F — Governed Local Memory Schema Contract Review Gate completed; status `f33_governed_local_memory_schema_contract_review_gate_passed`; anchor phase `F33.E — Governed Local Memory Schema Contract Gate`; schema contract reviewed; field catalog reviewed; constraints matrix reviewed; migration safety contract reviewed; FTS5 planned only; next phase recommendation `F33.G — Governed Local Memory SQLite Dry-Run Plan Gate`.
