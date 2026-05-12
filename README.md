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
- ARIS-LAB-B0/R1 is complete and F33.KR2 is temporarily deferred for operational completion.
- Latest completed phase: `ARIS-LAB-B0/R1 — Lab Operational Completion Supersession Gate`
- Next principal phase: `ARIS-LAB-B1 — Lab Impact Summary Template`
- F33.KR2 remains preserved and the Lab phase-to-phase contract still blocks product promotion.
- F44 interpretation: `ARIS Lab Hardening, Red-Team Expansion & Benchmark Maturity`

Rules:

- Query-first, no bulk-read, no network, no dependency installs, no real MCP activation, no secret reads.
- `CURRENT_STATE.md`, `NEXT_ACTION.md`, and `DECISION_LOCKS.md` are the operational sources of truth.
- Historical depth belongs in `ARIS_PHASE_LEDGER.md`.
