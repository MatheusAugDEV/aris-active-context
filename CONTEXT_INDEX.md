artifact routes are derived from ACTIVE_CONTEXT_STATE.json. If this file conflicts with ACTIVE_CONTEXT_STATE.json, ACTIVE_CONTEXT_STATE.json wins.

# Context Index

## Canonical Live State
- `ACTIVE_CONTEXT_STATE.json`
- `ACTIVE_CONTEXT_SCHEMA.json`
- Latest completed phase: `ARIS Active-Context Anti-Corruption Hardening Gate`
- Current status: `ready_for_controlled_apply_dry_run_harness_planning`
- Active next phase: `Lab Real Simulation Pack Controlled Apply Dry-Run Harness Planning`
- Active next phase class: `planning_gate`
- Planning-only: `true`
- Operator Approval Packet Review is review-only, not execution approval.
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

## Phase Artifact Routes (external_to_active_context_repo)
These artifact paths are reference routes to files in the ARIS project workspace.
They are **not** local to this governance repository. Classification: `external_to_active_context_repo`.
Do not treat their absence from this repo as a blocking error — see `artifact_integrity_policy` in the JSON state.

- Controlled apply operator approval packet review summary: `artifacts/lab_simulation/lab_real_simulation_pack_controlled_apply_operator_approval_packet_review_summary.json` [external_to_active_context_repo]
- Controlled apply operator approval packet review gate: `artifacts/lab_simulation/lab_real_simulation_pack_controlled_apply_operator_approval_packet_review.json` [external_to_active_context_repo]
- Controlled apply operator approval packet review report: `artifacts/lab_simulation/lab_real_simulation_pack_controlled_apply_operator_approval_packet_review_report.md` [external_to_active_context_repo]
- Controlled apply operator approval packet contract: `artifacts/lab_simulation/lab_real_simulation_pack_controlled_apply_operator_approval_packet_contract.json` [external_to_active_context_repo]
- Controlled apply operator approval packet schema: `artifacts/lab_simulation/lab_real_simulation_pack_controlled_apply_operator_approval_packet_schema.json` [external_to_active_context_repo]
- Controlled apply operator approval packet risk register: `artifacts/lab_simulation/lab_real_simulation_pack_controlled_apply_operator_approval_packet_risk_register.json` [external_to_active_context_repo]
- Controlled apply operator approval packet route verification: `artifacts/lab_simulation/lab_real_simulation_pack_controlled_apply_operator_approval_packet_route_verification.json` [external_to_active_context_repo]

## Historical / Evidence Only
- Earlier filesystem isolation, shadow workspace, Debian planning, Debian readiness, and plan-only rehearsal artifacts remain evidence only.
- Older routes must not be read as active current routing.
