# Context Index

## Active Source Routing
- Current state: `aris-active-context/CURRENT_STATE.md`
- Next action: `aris-active-context/NEXT_ACTION.md`
- Decision locks: `aris-active-context/DECISION_LOCKS.md`
- Phase ledger: `aris-active-context/ARIS_PHASE_LEDGER.md`
- Canonical roadmap: `aris-active-context/ROADMAP_CANONICAL.md`
- Roadmap amendment protocol: `aris-active-context/ROADMAP_AMENDMENT_PROTOCOL.md`
- Strategic Reset summary: `artifacts/roadmap/strategic_reset_macrostructure_lock_summary.json`
- Product Loop L1.15 summary: `artifacts/product_loop/product_loop_l1_15_product_loop_closure_summary.json`
- H1 baseline summary: `artifacts/hardening_base/hardening_base_h1_golden_tasks_baseline_gate_summary.json`
- H2 baseline decision: `artifacts/hardening_base/hardening_base_h2_ledger_chain_replay_baseline_gate.json`
- H2 baseline summary: `artifacts/hardening_base/hardening_base_h2_ledger_chain_replay_baseline_gate_summary.json`
- H2 baseline report: `artifacts/hardening_base/hardening_base_h2_ledger_chain_replay_baseline_gate_report.md`
- H2 ledger event schema: `artifacts/hardening_base/hardening_base_h2_ledger_event_schema.json`
- H2 replay policy: `artifacts/hardening_base/hardening_base_h2_replay_policy.json`
- H2 tamper matrix: `artifacts/hardening_base/hardening_base_h2_tamper_detection_matrix.json`
- H2 golden task ledger mapping: `artifacts/hardening_base/hardening_base_h2_golden_task_ledger_mapping.json`

## Indexed Topics
- Strategic Reset PASS: `artifacts/roadmap/strategic_reset_macrostructure_lock_summary.json`
- Product Loop L1.15 PASS: `artifacts/product_loop/product_loop_l1_15_product_loop_closure_summary.json`
- Product Loop closure hash: `sha256:bd2974c9caf880dc3869eaa5696988d28f54a2f1c37a20d8295ce9b59270a5f0`
- Product Loop layer closed: `True`
- H1 golden tasks baseline result: `pass`
- H2 ledger/replay baseline result: `pass`
- H2 event types count: `12`
- H2 P0 mapped count: `15`
- H2 tamper scenarios count: `10`
- H2 replay divergence scenarios count: `10`
- Active roadmap direction: `aris-active-context/ROADMAP_CANONICAL.md`
- Active roadmap amendment process: `aris-active-context/ROADMAP_AMENDMENT_PROTOCOL.md`
- Active next phase: `Hardening Base H3 — Context Engineering Baseline Gate`
- Pre-pilot lock and active restrictions: `aris-active-context/DECISION_LOCKS.md`
- Historical milestone ledger: `aris-active-context/ARIS_PHASE_LEDGER.md`

## Historical Preserved Sources
- `aris-active-context/BEDROCK_GATE.md`
- `aris-active-context/ARIS_ROADMAP_R0_F120.md`
- `aris-active-context/ARIS_ROADMAP_R1_CRITICAL_REALITY_GAPS_DELTA.md`
- `aris-active-context/ARIS_ROADMAP_R2_ACTIVE_HANDOFF.md`
- `aris-active-context/ARIS_ROADMAP_R2_LAB_SIMULATION_MASTERY.md`
- `aris-active-context/ARIS_LAB_MACROBLOCK_MATURITY_FRAMEWORK.md`
- `aris-active-context/ARIS_LAB_OPERATIONAL_LOAD_TEST_PLAN.md`
- `aris-active-context/ROADMAP_CANONICAL_F33_F50.md`
- `aris-active-context/ROADMAP_F30_F50.md`
- `aris-active-context/LAB_STATUS.md`
- `aris-active-context/LAB_VERDICTS.md`
- `aris-active-context/EXTERNAL_REFERENCES.md`

## Routing Rules
- Start with the active-context canonical files.
- Use `ROADMAP_CANONICAL.md` for active roadmap semantics.
- Use `ROADMAP_AMENDMENT_PROTOCOL.md` before proposing roadmap changes.
- Treat historical preserved sources as `historical_only`, `superseded`, or `removed_from_active_direction` unless a later canonical gate explicitly reactivates them.
- Do not reopen Product Loop L1.15 from active routing.
- Do not treat the H3 next-step entry as H3 execution.
