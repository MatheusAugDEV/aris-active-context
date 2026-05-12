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
- Latest completed phase: `F33.KS/R1 — Human Authorization Evidence Submission Recovery`
- Next principal phase: `F33.KR2 — Governed Local Memory SQLite Controlled Dry-Run Human Authorization Evidence Review Recheck Gate`
- F33 now advances through Governed Local Memory human authorization recovery/review-only work; Similar Projects remains advisory-only at phase start; F32 closure is complete.
- F32.RESEARCH-P0 created an artifact-only research intake program; it does not alter the operational next action.

Rules:

- Query-first, no bulk-read, no network, no dependency installs, no real MCP activation, no secret reads.
- `CURRENT_STATE.md`, `NEXT_ACTION.md`, and `DECISION_LOCKS.md` are the operational sources of truth.
- Historical depth belongs in `ARIS_PHASE_LEDGER.md`.
- F32.RESEARCH-P3 created a candidate roadmap impact delta; canonical roadmap and operational next action unchanged.

- F33.J — Governed Local Memory SQLite Controlled Dry-Run Preparation Review Gate completed; status `f33_governed_local_memory_sqlite_controlled_dry_run_preparation_review_gate_passed`; anchor phase `F33.I — Governed Local Memory SQLite Controlled Dry-Run Preparation Gate`; source phase F33.I reviewed; preparation contract reviewed; preconditions reviewed; permission contract reviewed; execution boundary reviewed; abort matrix reviewed; ledger entry shape reviewed; operator explanation rule verified; no DB file created; next phase recommendation `F33.K — Governed Local Memory SQLite Controlled Dry-Run Authorization Gate`.

- Operator-facing phase explanation rule: saved in PROMPT_CONTRACT.md.

- F33.K — Governed Local Memory SQLite Controlled Dry-Run Authorization Gate completed; status `f33_governed_local_memory_sqlite_controlled_dry_run_authorization_required`; anchor phase `F33.J — Governed Local Memory SQLite Controlled Dry-Run Preparation Review Gate`; source phase F33.J reviewed; preparation package reviewed; dedicated authorization evidence path checked; human authorization granted `False`; operator explanation rule verified; no DB file created; next phase recommendation `F33.KH — Governed Local Memory SQLite Controlled Dry-Run Human Authorization Evidence Intake`.
