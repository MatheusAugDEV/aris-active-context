Derived mirror from ACTIVE_CONTEXT_STATE.json. If this file conflicts with ACTIVE_CONTEXT_STATE.json, ACTIVE_CONTEXT_STATE.json wins.

# Current State

## Live Snapshot
- Status: `lab_real_simulation_pack_controlled_apply_operator_approval_packet_review_pass`
- Decision: `pass`
- Latest completed phase: `Lab Real Simulation Pack Controlled Apply Operator Approval Packet Review`
- Current status: `ready_for_controlled_apply_dry_run_harness_planning`
- Active next phase: `Lab Real Simulation Pack Controlled Apply Dry-Run Harness Planning`
- Active next phase class: `planning_gate`
- Next phase execution authorization: `False`
- Operator approval packet review is execution approval: `False`
- H4/H5/Hx active current route: `False`
- H4/H5/Hx not active current route.
- Markdown files are derived mirrors or history, not authoritative live state.

## Review-Only Completion
- Controlled Apply Operator Approval Packet Review passed as review-only and did not execute approval or authorize execution.
- The next phase is planning-only for controlled apply dry-run harness and does not authorize real dry-run execution.
- Operator Approval Packet Review is review-only, not execution approval.
- No real apply, no real dry-run execution, no approval execution, no runtime refactor, no host filesystem mutation, no Debian harness execution, no container/image/VM creation, no package-manager execution, no product/pilot/customer activation, no secrets, no external LLM/API, no dependency change, no frontend/backend/action-runtime/audio mutation.

## Canonicality
- GitHub active-context is the only canonical active-context source.
- ACTIVE_CONTEXT_STATE.json is the only canonical live-state file.
- ACTIVE_CONTEXT_SCHEMA.json is the canonical validation contract.
- No GitHub active-context sync = no canonical PASS.

## Historical / Proof-Only
- The prior multi-Markdown live-state pattern has been replaced by `ACTIVE_CONTEXT_STATE.json`.
- Prior route proofs are historical/proof-only/non-active.
