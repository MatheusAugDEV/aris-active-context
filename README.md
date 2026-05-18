# aris-active-context

Compact, read-first ARIS context entrypoint.

## Read order

1. `CURRENT_STATE.md`
2. `NEXT_ACTION.md`
3. `DECISION_LOCKS.md`
4. `ARIS_PHASE_LEDGER.md`
5. `CONTEXT_INDEX.md`
6. `ARIS_ROADMAP_R0_F120.md`
7. `OPERATOR_PREFERENCES.md`
8. `PROMPT_CONTRACT.md`

## Current snapshot

- Latest completed phase: `ARIS-BEDROCK-C6 — Read-First & Source-of-Truth Compliance Evaluator`.
- Canonical roadmap: `ARIS_ROADMAP_R0_F120.md`.
- Roadmap status: `PASS by conservative review`.
- Next authorized phase: `ARIS-ROADMAP-R0 — Governance Foundation`.
- `ARIS-BEDROCK-C7` is blocked until `R0 = PASS`.
- Bedrock executable engine readiness: `45/100`.
- Bedrock Gate remains declared but non-executable.
- F33 remains paused under Lab governance.
- F51+ remains advisory-only.
- Product promotion remains false.
- Runtime mutation, SQLite schema apply, SQLite connect, FTS5 creation, network, dependency install, MCP activation, Obsidian bulk-read, and Vault write remain blocked.

## Roadmap rule

F120 closes Lab Mastery only. F120 does not authorize production. Any real productization requires future `F121+ Controlled Productization Gate`.

## Rules

- Query-first, no bulk-read, no network, no dependency installs, no real MCP activation, no secret reads.
