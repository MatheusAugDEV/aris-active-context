Derived mirror from ACTIVE_CONTEXT_STATE.json. If this file conflicts with ACTIVE_CONTEXT_STATE.json, ACTIVE_CONTEXT_STATE.json wins.

# Current State

## Live Snapshot
- Status: `active_context_anti_corruption_hardening_gate_pass`
- Decision: `pass`
- Latest completed phase: `ARIS Active-Context Anti-Corruption Hardening Gate`
- Current status: `ready_for_controlled_apply_dry_run_harness_planning`
- Active next phase: `Lab Real Simulation Pack Controlled Apply Dry-Run Harness Planning`
- Active next phase class: `planning_gate`
- Planning-only: `true`
- Next phase execution authorization: `false`
- Operator approval packet review is execution approval: `false`
- H4/H5/Hx active current route: `false`
- H4/H5/Hx not active current route.
- Schema version: `2.1` (structural evolutionary schema — const only for permanent invariants)
- Markdown files are derived mirrors or history, not authoritative live state.

## Anti-Corruption Hardening Gate — Completed
- ARIS Active-Context Anti-Corruption Hardening Gate passed as a governance repair gate.
- Schema refactored to v2.1: structural and evolutionary, not phase-snapshot.
- Validator enforces cross-field consistency, additionalProperties, artifact existence, and JSON-first governance contracts.
- BOOT_PROFILE, MANDATORY_READ_FIRST_RULES, and PROMPT_CONTRACT now declare ACTIVE_CONTEXT_STATE.json as step 1.
- required_files_for_transition expanded to 18 files.
- Versioning contract and anti-corruption contract added to state.
- artifact_integrity_policy classifies external artifact routes explicitly.
- cross_field_consistency_policy documents all enforced field redundancy checks.
- Controlled Apply Operator Approval Packet Review passed as review-only and did not execute approval or authorize execution.
- The next phase is planning-only for controlled apply dry-run harness and does not authorize real dry-run execution.

## Canonicality
- GitHub active-context is the only canonical active-context source.
- ACTIVE_CONTEXT_STATE.json is the only canonical live-state file.
- ACTIVE_CONTEXT_SCHEMA.json is the canonical validation contract.
- No GitHub active-context sync = no canonical PASS.

## Historical / Proof-Only
- The prior multi-Markdown live-state pattern has been replaced by `ACTIVE_CONTEXT_STATE.json`.
- Prior route proofs are historical/proof-only/non-active.
