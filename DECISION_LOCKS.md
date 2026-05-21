# DECISION_LOCKS

## Global Non-Authorization Lock

- Product promotion remains `false`.
- Runtime mutation remains `false` unless an explicit future gate authorizes it.
- Customer-real use remains `false`.
- Production release remains `false`.
- Network access remains blocked for ARIS runtime work unless explicitly authorized by a future gate.
- Dependency installation remains blocked unless explicitly authorized by a future gate.
- MCP activation remains blocked.
- Obsidian bulk-read remains blocked.
- Vault write remains blocked.
- Chat context, prompt text, roadmap text, advisory research, placeholder files, summaries, or human discussion do not count as authorization.

## Source-of-Truth and Active-Context Lock

- Active-context is the authoritative live state surface.
- `NEXT_ACTION.md` governs the next operational step.
- `DECISION_LOCKS.md` governs hard constraints.
- Phase artifacts/evidence outrank historical docs and chat memory.
- Chat memory and advisory discussion are non-authoritative unless materialized into approved artifacts/docs.
- Obsidian is consultive/query-first only unless a future gate changes that.
- Historical ledger entries are evidence/history, not live authorization.

## Active Operational Track Lock

- Current operational macroblock remains `MB1 — Context Governance & Input Trust Boundary`.
- Next operational gate remains `F21-A45 — Real MCP Candidate Controlled Pre-Apply Dry-Run Plan`.
- `F21-A44 — Real MCP Candidate Controlled Authorization Decision Gate` completed the final controlled decision step and did not authorize activation.
- `F21-A11 — MCP Candidate Human Evidence Completion Review Gate` is a stale pointer that was repaired by `ACTIVE-CONTEXT-R1`.
- MB8/MB9 future roadmap discussion does not move `NEXT_ACTION`.
- F33 remains blocked under lab governance until explicitly reopened by a future gate.
## R0–F120 Lab Governance Lock

- R0–F120 materialize lab/governance planning only.
- F120 closes Lab Mastery only and does not authorize production.
- Any real release requires a future `F121+ Controlled Productization Gate` outside the current roadmap.
- No product claim may be made from macroblock maturity, load-test plans, product-shadow simulations, advisory market research, or conceptual roadmap discussion.

## MB8/MB9 Infernus Concept Lock

- MB8 final concept: `ARIS Infernus Lab — Os 13 Pecados Capitais do ARIS`.
- MB9 final concept: `ARIS Final Crisol — Evidence Certification, False-Completion Defense & Pre-Productization Gate`.
- Decision: `ADOTAR_COM_GATES`.
- Concept status: `PASS with documented WARNs`.
- Implementation allowed now: `false`.
- Runtime mutation allowed now: `false`.
- Bot implementation allowed now: `false`.
- Harness implementation allowed now: `false`.
- Scenario manifest creation allowed now: `false`.
- Productization allowed now: `false`.
- MB9 reexecutes MB8: `false`.
- MB9 authorizes production: `false`.

### Infernus bot-count lock

- `13 bots = núcleo necessário do Infernus`.
- `5 bots = smoke test inicial / harness validation only`.
- `20 bots = expansão futura, not required now`.
- Do not add `BOT-014` for concurrency, rollback, process chaos, permission abuse, or trajectory oracle unless a future gate proves a distinct uncovered failure class.

### Bot/component boundary lock

- Oracle is not a bot.
- Trajectory Oracle is not a bot.
- State Oracle is not a bot.
- Ledger Oracle is not a bot.
- Permission Oracle is not a bot.
- Rollback Oracle is not a bot.
- Policy Oracle is not a bot.
- Security Oracle is not a bot.
- Permission Abuser is not a separate necessary bot; it is covered by explicit scenarios/gates under `Elos`, `Taipan`, and `Labirinto`.
- Process Chaos is not a separate necessary bot; it is covered by explicit future subscenarios under `Vitium`.
- LLM-as-judge may assist UX/semantic diagnostics, but it cannot decide critical gates.

### Loop/Minos ordering lock

- `Loop` must run after `Quimera` through `Abzu`.
- `Minos` must run after `Loop`.
- `Minos` must audit Loop artifacts before MB8 closure.
- MB9 certifies the evidence package after MB8 closure; MB9 does not rerun the full MB8 suite.
