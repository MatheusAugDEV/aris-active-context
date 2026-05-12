# aris-active-context

Compact, read-first ARIS context entrypoint.

Read order:

1. `CURRENT_STATE.md`
2. `NEXT_ACTION.md`
3. `DECISION_LOCKS.md`
4. `ARIS_PHASE_LEDGER.md`
5. `CONTEXT_INDEX.md`
6. `OPERATOR_PREFERENCES.md`

Current snapshot:

- Official V6 is closed.
- F32 owns MCP read-only configuration, controlled apply planning, activation planning, smoke validation, zero-write/no-bulk-read validation, and closure.
- Latest completed phase: `F33.B — Governed Local Memory Charter Review Gate`
- Next principal phase: `F33.C — Governed Local Memory Technical Planning Gate`
- F33 now advances through Governed Local Memory charter/review-only work; F32 closure is complete.
- F32.RESEARCH-P0 created an artifact-only research intake program; it does not alter the operational next action.

Rules:

- Query-first, no bulk-read, no network, no dependency installs, no real MCP activation, no secret reads.
- `CURRENT_STATE.md`, `NEXT_ACTION.md`, and `DECISION_LOCKS.md` are the operational sources of truth.
- Historical depth belongs in `ARIS_PHASE_LEDGER.md`.
- F32.RESEARCH-P3 created a candidate roadmap impact delta; canonical roadmap and operational next action unchanged.
