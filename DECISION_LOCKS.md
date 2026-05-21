# DECISION_LOCKS

## Triple Gate Approval Lock

All future ARIS phases, prompts Codex, architecture changes, features, refactors, roadmap updates, or operational decisions must pass the approval stack in this order:

1. `BEDROCK_GATE.md`
2. `NORTH_POLE.md`
3. `PHASE_SPECIFIC_GATES`
4. `ACTIVE_CONTEXT_UPDATE`
5. `COMMIT_PUSH_HASH_FINAL`

A later gate cannot override a Bedrock failure. Passing local tests cannot override Bedrock or North Pole failure.

## Bedrock Non-Bypass Lock

A phase must be `BLOCKED` or `INVALID` if it violates any inviolable ARIS foundation, including but not limited to:

- false claims about capability, evidence, execution, production readiness, or authorization;
- product promotion, customer-real use, or production release without explicit future gate;
- runtime mutation, network access, dependency installation, MCP activation, MCP config write, vault write, Obsidian bulk-read, or controlled apply without explicit authorization;
- secret exposure or unsafe environment reading;
- bypass of `NEXT_ACTION.md`, `DECISION_LOCKS.md`, `BEDROCK_GATE.md`, `NORTH_POLE.md`, source-of-truth policy, or phase artifacts;
- treating chat, memory, roadmap discussion, prompt text, or advisory analysis as materialized authorization;
- removing critical controls merely to reduce friction.

## North Pole Alignment Lock

A phase must prove that it aligns with `NORTH_POLE.md` by answering whether it:

- strengthens the technical victory;
- preserves future product victory;
- increases confidence, capacity, or value;
- uses the minimum mechanism necessary;
- preserves locks while increasing real value;
- improves determinism, type-safety, isolation, governance, context compression, testing, traceability, routing, idempotency, resilience, modularity, controlled autonomy, efficiency, simplicity, usability, future UX/interface, real automation, deliverability, scalability, performance, implementability, auditability, security, and/or market value.

If the dominant answer is no, the phase must be revised, compressed, deferred, rejected, or blocked.

## Active Operational Track Lock

- current_macroblock: `MB1 — Context Governance & Input Trust Boundary`
- latest_completed_phase: `F21-A52 — ARIS Lean Development Protocol v0.1 Minimal Acceptance Runner Planning Gate`
- latest_status: `lean_minimal_acceptance_runner_plan_warn`
- next_operational_gate: `F21-A53 — ARIS Lean Development Protocol v0.1 Minimal Acceptance Runner Implementation Gate`
- next_action_authority: `NEXT_ACTION.md`
- f21_a52_implemented_runner: `false`
- f21_a53_allowed_next: `true`

## F21-A53 Scope Lock

F21-A53 may implement only the Lean v0.1 minimal acceptance runner, subject to Bedrock, North Pole, and phase-specific gates.

F21-A53 does not authorize:
- prompt kernel;
- template library;
- batch runner;
- MCP activation;
- MCP config write;
- Obsidian bulk-read;
- vault write;
- network access;
- dependency installation;
- runtime mutation;
- product promotion;
- customer-real use;
- production release.

## Global Non-Authorization Lock

- candidate_approval_allowed: `false`
- automatic_activation_allowed: `false`
- controlled_apply_allowed: `false`
- mcp_activation_allowed: `false`
- mcp_config_write_allowed: `false`
- vault_write_allowed: `false`
- obsidian_bulk_read_allowed: `false`
- network_allowed: `false`
- dependency_install_allowed: `false`
- runtime_mutation_allowed: `false`
- product_promotion_allowed: `false`
- customer_real_use_allowed: `false`
- production_release_allowed: `false`

## Source-of-Truth and Active-Context Lock

- `BEDROCK_GATE.md` governs inviolable foundations.
- `NORTH_POLE.md` governs excellence, two victories, and minimum necessary mechanism.
- `NEXT_ACTION.md` governs the next operational step.
- `DECISION_LOCKS.md` governs hard constraints.
- `CURRENT_STATE.md` is the live state surface.
- `CONTEXT_INDEX.md` is the active reference index.
- `ARIS_PHASE_LEDGER.md` is historical evidence, not live authorization.
- Phase artifacts/evidence outrank historical docs and chat memory.
- Chat memory and advisory discussion are non-authoritative unless materialized into approved artifacts/docs.
- Obsidian is consultive/query-first only unless a future gate changes that.

## R0–F120 Lab Governance Lock

- R0–F120 materialize lab/governance/internal-engine work only.
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

## Governance Repair Record

- repair_id: `ACTIVE-CONTEXT-GOV-TRIPLE-GATE-01`
- purpose: `Compress duplicated decision-lock noise and materialize Bedrock + North Pole + Phase-Specific gates as mandatory approval stack.`
- repeated_f21_a52_lock_blocks_removed: `true`
- next_action_changed: `false`
- blocked_capabilities_changed: `false`
- runtime_or_product_authorization_changed: `false`
