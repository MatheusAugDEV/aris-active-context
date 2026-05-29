Derived mirror from ACTIVE_CONTEXT_STATE.json. If this file conflicts with ACTIVE_CONTEXT_STATE.json, ACTIVE_CONTEXT_STATE.json wins.

# Current State

## Live Snapshot
- Status: `lab_real_simulation_pack_controlled_apply_dry_run_harness_planning_pass`
- Decision: `pass`
- Latest completed phase: `Lab Real Simulation Pack Controlled Apply Dry-Run Harness Planning`
- Current status: `ready_for_controlled_apply_dry_run_harness_readiness_review`
- Active next phase: `Lab Real Simulation Pack Controlled Apply Dry-Run Harness Readiness Review`
- Active next phase class: `readiness_gate`
- Next phase execution authorization: `False`
- Real dry-run execution authorized: `False`
- Real apply authorized: `False`
- Approval execution authorized: `False`
- H4/H5/Hx active current route: `False`
- H4/H5/Hx not active current route.
- Schema version: `2.1` (structural evolutionary schema; JSON-first anti-corruption model preserved)
- Markdown files are derived mirrors or history, not authoritative live state.

## Planning-Only Completion
- Anti-Corruption Hardening Gate remains carried forward as the latest governance repair before this planning gate.
- Controlled Apply Dry-Run Harness Planning passed as planning-only and did not execute a real dry-run, real apply, or approval execution.
- The phase consumed existing Lab/Bedrock verdicts, produced planning artifacts only, and recorded a Bedrock-preparation exception while keeping Bedrock non-executable.
- The next phase is readiness-review only and does not authorize real dry-run execution or real apply.
- No real apply, no real dry-run execution, no approval execution, no runtime refactor, no host filesystem mutation, no Debian harness execution, no container/image/VM creation, no package-manager execution, no product/pilot/customer activation, no secrets, no external LLM/API, no dependency change, no frontend/backend/action-runtime/audio mutation.

## Canonical Evidence
- Controlled apply dry-run harness planning summary: `artifacts/lab_simulation/lab_real_simulation_pack_controlled_apply_dry_run_harness_planning_summary.json`
- Controlled apply dry-run harness planning gate: `artifacts/lab_simulation/lab_real_simulation_pack_controlled_apply_dry_run_harness_planning.json`
- Controlled apply dry-run harness planning report: `artifacts/lab_simulation/lab_real_simulation_pack_controlled_apply_dry_run_harness_planning_report.md`

## Canonicality
- GitHub active-context is the only canonical active-context source.
- ACTIVE_CONTEXT_STATE.json is the only canonical live-state file.
- ACTIVE_CONTEXT_SCHEMA.json is the canonical validation contract.
- No GitHub active-context sync = no canonical PASS.

## Historical / Proof-Only
- The prior multi-Markdown live-state pattern has been replaced by `ACTIVE_CONTEXT_STATE.json`.
- Prior route proofs are historical/proof-only/non-active.
