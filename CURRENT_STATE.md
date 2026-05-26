# Product Loop L1.1 - Runtime Awake Discovery Gate

## Current Position
- Status: `product_loop_l1_1_runtime_awake_discovery_pass`
- Decision: `pass`
- Macrostructure phase: `Product Loop Demonstrável`
- Current state: `Product Loop L1.1 - Runtime Awake Discovery Gate`
- Strategic Reset verified: `True`
- Product Loop implemented: `False`
- L1.2 implemented: `False`
- Runtime changed: `False`
- Frontend changed: `False`
- Voice/audio changed: `False`
- Action runtime activated: `False`
- Network used: `False`
- Dependencies installed: `False`

## Runtime Entry Path Identified
1. `src/aris/app/orchestrator.py::processar_e_responder`
2. `src/aris/app/orchestrator.py::_submeter_texto_para_processamento`
3. `src/aris/app/orchestrator.py::_executar_processamento`
4. `src/aris/app/orchestrator.py::_resolve_turn_via_official_trail`
5. `src/aris/turn/pipeline.py::resolve_turn`
6. `src/aris/app/interaction_router.py::decidir_rota_interacao`
7. `src/aris/app/interaction_router.py::executar_rota_interacao`

## Recommended Insertion Strategy
- Do not patch orchestrator in L1.1.
- Use a sidecar Product Loop planner first.
- Future runtime insertion should happen only after `turn.pipeline.resolve_turn` has route evidence and before any `action_runtime` controlled dispatch.
- Any runtime patch must be authorized by a later gate.

## Recommended First E2E Task
- Candidate: `notes.create.local`
- Mode for L1.2: dry-run plan only.
- Evidence: F19 `notes.create.local` dry-run artifacts and `src/aris/action_runtime/local_notes_adapter.py` expose preview/blocked-apply behavior.
- Real note creation is not authorized by L1.1.

## Gaps Before L1.2
- No Product Loop task envelope is currently wired into the turn path.
- Action runtime scaffold remains blocked-by-default and not integrated with orchestrator.
- Human permission presentation for Product Loop E2E is not mapped to current UI/voice.
- Rollback and idempotency evidence must be attached before any write.
- No runtime smoke exists for a Product Loop sidecar handoff.

## Core Priority Invariants
- All applicable Core Priority Invariants: `PASS`
- N/A priorities: none.
- WARN does not unlock critical advancement.

## Evidence
- Diagnostic module: `src/aris/product_loop/product_loop_runtime_awake_discovery.py`
- Runner: `scripts/run_product_loop_l1_1_runtime_awake_discovery_gate.py`
- Test: `tests/test_product_loop_l1_1_runtime_awake_discovery_gate.py`
- Summary artifact: `artifacts/product_loop/product_loop_l1_1_runtime_awake_discovery_summary.json`
- Report artifact: `artifacts/product_loop/product_loop_l1_1_runtime_awake_discovery_report.md`
- Phase doc: `docs/fase_product_loop/product_loop_l1_1_runtime_awake_discovery.md`

## Next
- Next recommended phase: `Product Loop L1.2 - Single Task E2E Plan`
- L1.2 scope must remain plan/controlled dry-run design for the first E2E task, not broad runtime execution.
