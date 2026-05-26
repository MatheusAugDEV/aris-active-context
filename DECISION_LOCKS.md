# Decision Locks

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
