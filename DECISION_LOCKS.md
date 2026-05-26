# Decision Locks

# Product Loop L1.4 Controlled Apply Plan Gate Lock
- Lock id: `PRODUCT_LOOP_L1_4_CONTROLLED_APPLY_PLAN`
- Status: `pass`
- Decision: `pass`
- Macrostructure phase: `Product Loop Demonstrável`
- Selected task: `notes.create.local`
- Source plan hash: `sha256:41d232e3515acd8720948776e956f07190ecfeb133602365f47a0795e3a8e1a3`
- Source envelope hash: `sha256:bdee490afddde25056f1e9833512ba713971cf27c6ace0c3f954fc5d7e4eea05`
- Apply plan hash: `sha256:8c30c9cc8e4bb3f00ee0ac8818e80c0c748a49fe202fbc8e38fae8c1eb3808d5`
- Execution mode: `controlled_apply_plan_only`
- Human permission required: `True`
- Human permission granted: `False`
- Permission envelope verified: `True`
- Controlled apply plan created: `True`
- Controlled apply allowed: `False`
- Controlled apply executed: `False`
- Write operation allowed: `False`
- Action runtime activation allowed: `False`
- Runtime integration allowed: `False`
- Product Loop implemented: `False`
- Target path planned: `data/aris_notes/aris_created_note_preview.md`
- Target path allowed by policy: `True`
- Payload schema valid: `True`
- Rollback plan required: `True`
- Rollback plan attached: `True`
- Idempotency key required: `True`
- Idempotency key attached: `True`
- Ledger entry required: `True`
- Ledger entry planned: `True`
- Verification required: `True`
- Verification plan attached: `True`
- Cost/time measurement required: `True`
- Cost/time measurement plan attached: `True`
- Apply blockers count: `0`
- Unsafe payloads blocked: `True`
- Next phase can prepare pre-apply review: `True`
- Blocking gaps before real apply:
  - `L1.5 pre-apply authorization review has not executed yet.`
  - `Human permission remains ungranted in L1.4.`
  - `Controlled apply remains plan-only and not authorized in L1.4.`
  - `Action runtime activation remains blocked-by-default.`
  - `Runtime integration remains false.`
  - `No real write path under data/aris_notes is authorized yet.`
  - `Rollback, idempotency, ledger, verification, and cost/time stay mandatory before any future apply.`
- All applicable Core Priority Invariants passed for L1.4.
- WARN does not unlock critical advancement.
- Next phase is `Product Loop L1.5 - Pre-Apply Authorization Review Gate`.
- L1.4 is controlled apply planning only, not real write/apply.

# Product Loop L1.3 Permissioned Dry-Run Envelope Gate Lock
- Lock id: `PRODUCT_LOOP_L1_3_PERMISSIONED_DRY_RUN_ENVELOPE`
- Status: `pass`
- Decision: `pass`
- Macrostructure phase: `Product Loop Demonstrável`
- Selected task: `notes.create.local`
- Source plan hash: `sha256:41d232e3515acd8720948776e956f07190ecfeb133602365f47a0795e3a8e1a3`
- Envelope hash: `sha256:bdee490afddde25056f1e9833512ba713971cf27c6ace0c3f954fc5d7e4eea05`
- Execution mode: `permissioned_dry_run_envelope_only`
- Human permission required: `True`
- Human permission granted: `False`
- Permission request created: `True`
- Permission request presentable: `True`
- Dry-run preview created: `True`
- Dry-run has no side effects: `True`
- Write operation allowed: `False`
- Controlled apply allowed: `False`
- Controlled apply executed: `False`
- Action runtime activation allowed: `False`
- Runtime integration allowed: `False`
- Real note creation allowed: `False`
- Rollback plan attached: `True`
- Idempotency key attached: `True`
- Ledger entry planned: `True`
- Verification plan attached: `True`
- Cost/time measurement plan attached: `True`
- Authorization blockers count: `0`
- Unsafe payloads blocked: `True`
- Next phase can prepare controlled apply plan: `True`
- Next phase is `Product Loop L1.4 - Controlled Apply Plan Gate`.
- L1.4 is controlled apply planning only, not real write/apply.
- Product Loop remains not implemented.
- All applicable Core Priority Invariants passed for L1.3.
- WARN does not unlock critical advancement.

## Product Loop L1.2 Single Task E2E Plan Lock
- Lock id: `PRODUCT_LOOP_L1_2_SINGLE_TASK_E2E_PLAN`
- Status: `pass`
- Decision: `pass`
- Macrostructure phase: `Product Loop Demonstrável`
- Selected task: `notes.create.local`
- Execution mode: `dry_run_plan_only`
- Plan hash: `sha256:41d232e3515acd8720948776e956f07190ecfeb133602365f47a0795e3a8e1a3`
- Product Loop 12-step envelope is required and ordered:
  - `intent`
  - `context_binding`
  - `typed_plan`
  - `risk_classifier`
  - `permission_gate`
  - `dry_run`
  - `controlled_apply`
  - `ledger`
  - `verification`
  - `cost_time_measurement`
  - `response`
  - `rollback_compensation`
- `controlled_apply` must remain present but `not_executed` and `planned_only` until a later explicit apply gate.
- Human permission is required before any future dry-run envelope advances.
- Write operation allowed: `False`
- Runtime integration allowed: `False`
- Action runtime activation allowed: `False`
- Real note creation allowed: `False`
- Rollback required before apply: `True`
- Idempotency key required: `True`
- Ledger entry planned: `True`
- Verification planned: `True`
- Cost/time measurement planned: `True`
- Next phase is `Product Loop L1.3 - Permissioned Dry-Run Envelope Gate`.
- L1.3 is not real apply/write/runtime integration.
- Product Loop remains not implemented.
- All applicable Core Priority Invariants passed for L1.2.
- WARN does not unlock critical advancement.

## Product Loop L1.1 Runtime Awake Discovery Lock
- Lock id: `PRODUCT_LOOP_L1_1_RUNTIME_AWAKE_DISCOVERY`
- Status: `pass`
- Decision: `pass`
- Macrostructure phase: `Product Loop Demonstrável`
- Runtime entry path identified:
  - `orchestrator.processar_e_responder`
  - `orchestrator._submeter_texto_para_processamento`
  - `orchestrator._executar_processamento`
  - `orchestrator._resolve_turn_via_official_trail`
  - `turn.pipeline.resolve_turn`
  - `interaction_router.decidir_rota_interacao`
  - `interaction_router.executar_rota_interacao`
- Product Loop insertion is not authorized in runtime by L1.1.
- Future insertion strategy must start sidecar-first and only later consider a bounded handoff after `turn.pipeline.resolve_turn` route evidence and before action runtime controlled dispatch.
- First E2E task candidate is `notes.create.local` dry-run plan.
- Real note creation is not authorized by L1.1.
- Action runtime activation is not authorized by L1.1.
- L1.2 is authorized as `Product Loop L1.2 - Single Task E2E Plan`, not broad execution.
- Touching orchestrator, interaction_router, or turn.pipeline requires a later explicit runtime patch gate.
- Product Loop remains not implemented.
- All applicable Core Priority Invariants passed for L1.1.
- WARN does not unlock critical advancement.

## Strategic Reset / Macrostructure Lock
- Lock id: `STRATEGIC_RESET_MACROSTRUCTURE_LOCK`
- Status: `pass`
- Decision: `pass`
- The official ARIS macrostructure is:
  0. Strategic Reset
  1. Product Loop Demonstrável
  2. Hardening Base
  3. ARIS Infernus Lab
  4. ARIS Final Crisol
  5. Productatization Gate
  6. SIP
- SIP means `Sistema Imunológico Permanente`.
- Productatization Gate replaces the active name `F121+ Productization Gate`.
- ARIS Infernus Lab and ARIS Final Crisol are the main names; MB8/MB9 must not appear as primary names in the active roadmap.
- Product Loop Demonstrável is the next real proof.
- Core Priority Invariants are mandatory passage criteria.
- Nothing passes without real PASS on applicable priorities.
- WARN não destrava avanço crítico.
- Replay means replay of canonized ledger/artifacts, not free LLM requery expecting identical output.
- Ed25519 is signature, not hash.
- Active-context maintains five canonical files:
  - `CURRENT_STATE.md`
  - `NEXT_ACTION.md`
  - `DECISION_LOCKS.md`
  - `CONTEXT_INDEX.md`
  - `ARIS_PHASE_LEDGER.md`
- LLM-as-judge does not decide critical gates.
- Crisol does not rerun the whole Infernus; Crisol certifies evidence.
- Minos must be deterministic when implemented.
- Auditable history must not be deleted without its own gate.

## Historical Direction Policy
- Previous F21/Bedrock/Context continuation direction is `removed_from_active_direction` when incompatible with the official macrostructure 0-6.
- Historical docs, artifacts, summaries, ledger entries, and commits remain preserved as audit trail.
- Use `historical_only`, `superseded`, and `removed_from_active_direction` for material no longer serving active direction.
- The old direction is not equivalent to the new active macrostructure.

## Non-Authorization Locks
- Runtime productive mutation: `False`
- Frontend mutation: `False`
- Voice/audio mutation: `False`
- Action runtime activation: `False`
- Real MCP activation: `False`
- Network access: `False`
- Dependency installation: `False`
- Provider calls: `False`
- Production authorization: `False`
