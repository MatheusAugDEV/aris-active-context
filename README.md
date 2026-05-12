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
- F33.KR2-BEDROCK passed and F33.L is the active next action under the Lab contract.
- Latest completed phase: `F33.KR2-BEDROCK — Governed Local Memory SQLite Human Authorization Evidence Recheck With Complete Bedrock Gate`
- Next principal phase: `F33.L — Governed Local Memory SQLite Controlled Dry-Run Execution Plan Gate`
- F33.KR2-BEDROCK passed on artifact/evidence only; F33.L is the active next action under the Lab contract and product promotion remains blocked.
- F44 interpretation: `hardening/maturity of existing Lab`

Rules:

- Query-first, no bulk-read, no network, no dependency installs, no real MCP activation, no secret reads.
- `CURRENT_STATE.md`, `NEXT_ACTION.md`, and `DECISION_LOCKS.md` are the operational sources of truth.
- Historical depth belongs in `ARIS_PHASE_LEDGER.md`.
