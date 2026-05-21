# CONTEXT_INDEX

## Active live sources

### `CURRENT_STATE.md`
- role: Live operational state surface.
- current_macroblock: `MB1 — Context Governance & Input Trust Boundary`
- latest_completed_phase: `F21-A52 — ARIS Lean Development Protocol v0.1 Minimal Acceptance Runner Planning Gate`
- next_real_action: `F21-A53 — ARIS Lean Development Protocol v0.1 Minimal Acceptance Runner Implementation Gate`
- status: `lean_minimal_acceptance_runner_plan_warn`

### `NEXT_ACTION.md`
- role: Sole authoritative next operational gate pointer.
- next_gate: `F21-A53 — ARIS Lean Development Protocol v0.1 Minimal Acceptance Runner Implementation Gate`
- next_action_changed_by_governance_repair: `false`

### `DECISION_LOCKS.md`
- role: Hard constraints and non-authorization locks.
- includes: `Triple Gate Approval Lock`, `Bedrock Non-Bypass Lock`, `North Pole Alignment Lock`, `F21-A53 Scope Lock`, `Global Non-Authorization Lock`.

### `BEDROCK_GATE.md`
- role: First approval layer and inviolable foundation gate.
- blocks: false claims, unauthorized runtime/product/network/MCP/vault/dependency actions, source-of-truth bypass, unsafe evidence handling, control removal without equivalent safety.

### `NORTH_POLE.md`
- role: Strategic excellence target.
- governs: maximum market excellence, two victories, minimum necessary mechanism, confidence/capacity/value, technical victory, future product victory.

### `PHASE_SPECIFIC_GATES.md`
- role: Third approval layer for local technical proof.
- requires: objective phase-specific evidence, allowed/prohibited scope, artifacts, tests, active-context update, commit hash, and category classification.

### `ARIS_PHASE_LEDGER.md`
- role: Historical phase ledger and governance repair record.
- status: evidence/history, not live authorization.

## Mandatory approval stack index
Every future phase, prompt Codex, architecture change, feature, refactor, roadmap update, or operational decision must pass:

1. `BEDROCK_GATE.md`
2. `NORTH_POLE.md`
3. `PHASE_SPECIFIC_GATES.md`
4. `ACTIVE_CONTEXT_UPDATE`
5. `COMMIT_PUSH_HASH_FINAL`

## Current phase reference
- phase_id: `F21-A52`
- status: `lean_minimal_acceptance_runner_plan_warn`
- decision: `warn`
- minimal_acceptance_runner_plan_created: `true`
- acceptance_runner_implementation_allowed_next: `true`
- acceptance_runner_allowed_now: `false`
- prompt_kernel_allowed_now: `false`
- template_library_allowed_now: `false`
- batch_runner_allowed_now: `false`
- next_real_action: `F21-A53 — ARIS Lean Development Protocol v0.1 Minimal Acceptance Runner Implementation Gate`
- future_acceptance_runner_path: `scripts/run_lean_phase_acceptance_v0_1.py`
- machine_result_hash: `sha256:533f429365cef8ae3f2e2e168f062607e4f015f8ac2fa7f94e31230afd723bcc`
- summary_hash: `sha256:8ffa21cbcd7c32dbecb642dc4582dec043901d971b0875f6b93c04bc8a7d034d`
- report_hash: `sha256:81a7bc9a4f61684f61caba3fd9263b005c6233e4951c06136e2dad245040e25a`
- next_prompt_seed_hash: `sha256:dfeb17499c0ad26397e1d796b1b7ff63ffcebecf2f7d2ad0e51257587c5ad27a`
- plan_hash: `sha256:8befe1234757c9d36059afed8f1d806abd5cf6306b2ea88d036c699a459f0ce7`

## Governance repair record
- repair_id: `ACTIVE-CONTEXT-GOV-TRIPLE-GATE-01`
- created_files:
  - `BEDROCK_GATE.md`
  - `PHASE_SPECIFIC_GATES.md`
- compressed_files:
  - `CURRENT_STATE.md`
  - `DECISION_LOCKS.md`
  - `CONTEXT_INDEX.md`
  - `ARIS_PHASE_LEDGER.md`
- updated_files:
  - `NEXT_ACTION.md`
- purpose: `Remove duplicated live-context noise, fix approval-stack ambiguity, and materialize Bedrock + North Pole + Phase-Specific gates as mandatory approval layers.`
- next_action_changed: `false`
- blocked_capabilities_changed: `false`
- runtime_or_product_authorization_changed: `false`

## Blocked capabilities index
The following remain blocked unless a future explicit gate changes them:

- candidate approval;
- automatic activation;
- controlled apply;
- MCP activation;
- MCP config write;
- vault write;
- Obsidian bulk-read;
- network access;
- dependency installation;
- runtime mutation;
- product promotion;
- customer-real use;
- production release.

## Stale/noise prevention
- `NEXT_ACTION.md` must contain exactly one live next gate.
- `CURRENT_STATE.md` must prioritize live state over historical accumulation.
- `DECISION_LOCKS.md` must contain canonical locks, not repeated phase blocks.
- `CONTEXT_INDEX.md` must index active sources, not duplicate entire histories.
- `ARIS_PHASE_LEDGER.md` may record history, but history does not authorize action.
- Chat, memory, prompts, roadmap discussion, and advisory research are not authorization unless materialized into approved active-context/artifacts.
