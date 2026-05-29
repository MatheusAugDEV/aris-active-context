artifact routes are derived from ACTIVE_CONTEXT_STATE.json. If this file conflicts with ACTIVE_CONTEXT_STATE.json, ACTIVE_CONTEXT_STATE.json wins.

# Context Index

## Canonical Live State
- `ACTIVE_CONTEXT_STATE.json`
- `ACTIVE_CONTEXT_SCHEMA.json`
- Latest completed phase: `Lab Real Simulation Pack Controlled Apply Dry-Run Harness Planning Correction Gate`
- Current status: `ready_for_controlled_apply_dry_run_harness_correction_readiness_review`
- Active next phase: `Lab Real Simulation Pack Controlled Apply Dry-Run Harness Correction Readiness Review`
- Active next phase class: `readiness_gate`
- Controlled Apply Dry-Run Harness Readiness Review remains historically blocked and preserved.
- Bedrock preparation exception recorded in `LAB_VERDICTS.md`.
- Roadmap amendment required: `True`
- H4/H5/Hx not active current route.

## Governance Artifact Routes (local to this repo)
- State: `ACTIVE_CONTEXT_STATE.json`
- Schema: `ACTIVE_CONTEXT_SCHEMA.json`
- Validator: `scripts/validate_active_context_state.py`
- Anti-corruption contract: `ACTIVE_CONTEXT_ANTI_CORRUPTION_CONTRACT.md`
- Current state mirror: `CURRENT_STATE.md`
- Next action mirror: `NEXT_ACTION.md`
- Decision locks mirror: `DECISION_LOCKS.md`
- Context index mirror: `CONTEXT_INDEX.md`
- Phase ledger history: `ARIS_PHASE_LEDGER.md`
- Roadmap authority: `ROADMAP_CANONICAL.md`
- README: `README.md`

## Current Artifact Routes (external_to_active_context_repo)
- Readiness review decision reviewed: `artifacts/lab_simulation/lab_real_simulation_pack_controlled_apply_dry_run_harness_readiness_review.json`
- Readiness review summary reviewed: `artifacts/lab_simulation/lab_real_simulation_pack_controlled_apply_dry_run_harness_readiness_review_summary.json`
- Readiness review report reviewed: `artifacts/lab_simulation/lab_real_simulation_pack_controlled_apply_dry_run_harness_readiness_review_report.md`
- Correction gate decision: `artifacts/lab_simulation/lab_real_simulation_pack_controlled_apply_dry_run_harness_planning_correction_gate.json`
- Correction gate summary: `artifacts/lab_simulation/lab_real_simulation_pack_controlled_apply_dry_run_harness_planning_correction_gate_summary.json`
- Correction gate report: `artifacts/lab_simulation/lab_real_simulation_pack_controlled_apply_dry_run_harness_planning_correction_gate_report.md`
- Correction matrix: `artifacts/lab_simulation/lab_real_simulation_pack_controlled_apply_dry_run_harness_correction_matrix.json`
