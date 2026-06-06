# ARIS Active Context

- `ACTIVE_CONTEXT_STATE.json` is the only canonical live state.
- `ACTIVE_CONTEXT_SCHEMA.json` is the canonical validation contract.
- `ROADMAP_CANONICAL.md` is the canonical roadmap authority.
- `OPERATOR_PREFERENCES.md` is a priority-read prompt emission preference layer and never overrides JSON, schema, validator, Transition Table, or explicit safety locks.
- Markdown drift against JSON is a blocking error.

## Current Route

- Latest completed phase: `ARIS Infernus FULL Baseline Freeze Planning`
- Previous execution phase: `ARIS Infernus Full Scope Charter Gate`
- Active next phase: `null`
- Active next phase class: `null`
- governance_gate_streak: `0`
- fixture_materialization_executed: `true` (65 files / 13 scenarios on disk)
- bot_execution_executed: `true` (1 deterministic nemesis log on disk, historical only)
- current_phase_bots_executed: `false`
- minos_verdict_executed: `true` (1 deterministic Minos verdict on disk, historical only)
- purgatorium_finding_created: `true` (1 deterministic finding record on disk, historical only)
- baseline_freeze_planned: `true`
- baseline_freeze_applied: `false`
- runtime_execution_authorized: `false`
- product_promotion_allowed: `false`
- pilot_authorized: `false`
- bedrock_executed: `false`

## Active Artifacts

- `artifacts/decisions/acb_cap_05_project_evidence_2026_06_05.json`
- `../artifacts/infernus/inf_full_01_scope_charter_decision_2026_06_06.json`
- `../artifacts/infernus/inf_full_01_scope_matrix_2026_06_06.json`
- `../artifacts/infernus/inf_full_01_module_scope_manifest_2026_06_06.json`
- `../artifacts/infernus/inf_full_02_baseline_freeze_planning_decision_2026_06_06.json`
- `../artifacts/infernus/inf_full_02_baseline_freeze_inventory_2026_06_06.json`
- `../artifacts/infernus/inf_full_02_baseline_freeze_hash_manifest_2026_06_06.json`
- `../artifacts/infernus/inf_full_02_baseline_freeze_summary_2026_06_06.json`
- `../docs/infernus_full/inf_full_01_scope_charter_2026_06_06.md`
- `../docs/infernus_full/inf_full_02_baseline_freeze_planning_2026_06_06.md`
- `validate_active_context.yml`

## Non-Authorization

- INF-FULL-02 is planning-only and does not apply a baseline freeze.
- No bot execution, runtime start, product promotion, pilot authorization, Bedrock execution, or secret access is authorized.
- No canonical successor is defined after `INF-FULL-02`; no next phase is opened automatically.
