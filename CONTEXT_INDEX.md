artifact routes are derived from ACTIVE_CONTEXT_STATE.json. If this file conflicts with ACTIVE_CONTEXT_STATE.json, ACTIVE_CONTEXT_STATE.json wins.

# Context Index

## Canonical Live State
- `ACTIVE_CONTEXT_STATE.json`
- `ACTIVE_CONTEXT_SCHEMA.json`
- Latest completed phase: `Lab Real Simulation Pack Controlled Apply Dry-Run Harness Readiness Review`
- Current status: `blocked_for_controlled_apply_dry_run_harness_planning_correction`
- Active next phase: `Lab Real Simulation Pack Controlled Apply Dry-Run Harness Planning Correction Gate`
- Active next phase class: `planning_gate`
- Planning-only: `true`
- Review-only: `false`
- Controlled Apply Dry-Run Harness Readiness Review completed with decision `blocked`.
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
- Readiness review decision: `artifacts/lab_simulation/lab_real_simulation_pack_controlled_apply_dry_run_harness_readiness_review.json`
- Readiness review summary: `artifacts/lab_simulation/lab_real_simulation_pack_controlled_apply_dry_run_harness_readiness_review_summary.json`
- Readiness review report: `artifacts/lab_simulation/lab_real_simulation_pack_controlled_apply_dry_run_harness_readiness_review_report.md`
- Planning decision reviewed: `artifacts/lab_simulation/lab_real_simulation_pack_controlled_apply_dry_run_harness_planning.json`
- Planning summary reviewed: `artifacts/lab_simulation/lab_real_simulation_pack_controlled_apply_dry_run_harness_planning_summary.json`
- Planning report reviewed: `artifacts/lab_simulation/lab_real_simulation_pack_controlled_apply_dry_run_harness_planning_report.md`
