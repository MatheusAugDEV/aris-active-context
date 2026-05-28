current live locks are derived from ACTIVE_CONTEXT_STATE.json. If this file conflicts with ACTIVE_CONTEXT_STATE.json, ACTIVE_CONTEXT_STATE.json wins.

# Decision Locks

## Current Live Locks
- GitHub active-context is the only canonical active-context source.
- `ACTIVE_CONTEXT_STATE.json` is the only canonical live-state file.
- ACTIVE_CONTEXT_STATE.json is the only canonical live state.
- `ACTIVE_CONTEXT_SCHEMA.json` is the canonical validation contract.
- Markdown files are non-authoritative mirrors/docs/history.
- No GitHub active-context sync = no canonical PASS.
- Every ARIS phase/gate/status transition must update GitHub active-context.
- Every ARIS phase/gate/status transition must commit, push, and verify GitHub active-context.
- Latest completed phase: `ARIS Active-Context Anti-Corruption Hardening Gate`
- Current status: `ready_for_controlled_apply_dry_run_harness_planning`
- Active next phase: `Lab Real Simulation Pack Controlled Apply Dry-Run Harness Planning`
- Active next phase class: `planning_gate`
- Planning-only: `true`
- H4/H5/Hx: `not active current route`
- Operator Approval Packet Review is review-only, not execution approval.
- Controlled Apply Operator Approval Packet Review passed as review-only and did not execute approval or authorize execution.
- The next phase is planning-only for controlled apply dry-run harness and does not authorize real dry-run execution.
- No real apply authorization.
- No real dry-run execution authorization.
- No approval execution authorization.
- No runtime refactor authorization.
- No host filesystem mutation authorization.
- No Debian disposable harness execution authorization.
- No container/image/VM creation authorization.
- No Docker/Podman/Buildah/Nerdctl/containerd execution authorization.
- No apt/dpkg/package-manager execution authorization.
- No package installation authorization.
- No product/pilot/customer activation authorization.
- No secrets access authorization.
- No external LLM/API authorization.
- No dependency change authorization.
- No frontend/backend/action-runtime/audio mutation authorization.

## Anti-Corruption Locks (added by Hardening Gate)
- ACTIVE_CONTEXT_STATE.json must be read before any Markdown mirror.
- scripts/validate_active_context_state.py must pass before any phase decision.
- Cross-field drift within the JSON is a blocking error.
- Extra properties in authorization or any closed object are a blocking error.
- governance contracts (BOOT_PROFILE, MANDATORY_READ_FIRST_RULES, PROMPT_CONTRACT) must declare JSON-first.

## Historical / Proof-Only Entries
- Historical routing proof from prior gates remains historical only.
- Do not use historical proof for current routing.
- Historical snapshot values may include earlier phases, but they are superseded by `ACTIVE_CONTEXT_STATE.json`.
