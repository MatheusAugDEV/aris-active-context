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
- ARIS-LAB-A1 is complete and F33 is temporarily paused for Lab foundation.
- Latest completed phase: `ARIS-LAB-A1 — Capability Taxonomy & Product Boundary Contract`
- Next principal phase: `ARIS-LAB-A2 — Lab Run, Evidence Package & Gate Ledger Contract`
- F33.KR2 is preserved as the paused resume point until an explicit active-context decision reopens F33 work.
- F44 interpretation: `ARIS Lab Hardening, Red-Team Expansion & Benchmark Maturity`

Rules:

- Query-first, no bulk-read, no network, no dependency installs, no real MCP activation, no secret reads.
- `CURRENT_STATE.md`, `NEXT_ACTION.md`, and `DECISION_LOCKS.md` are the operational sources of truth.
- Historical depth belongs in `ARIS_PHASE_LEDGER.md`.