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
- Latest completed phase: `Lab Real Simulation Pack Controlled Apply Dry-Run Harness Readiness Review`
- Status: `lab_real_simulation_pack_controlled_apply_dry_run_harness_readiness_review_blocked`
- Current status: `blocked_for_controlled_apply_dry_run_harness_planning_correction`
- Active next phase: `Lab Real Simulation Pack Controlled Apply Dry-Run Harness Planning Correction Gate`
- Active next phase class: `planning_gate`
- H4/H5/Hx: `not active current route`
- Bedrock gate executable now: `False`
- Product promotion allowed: `False`
- False readiness blocked: `True`
- Dangerous flags verified false: `True`
- Roadmap amendment required: `True`
- No real apply authorization.
- No real dry-run execution authorization.
- No approval execution authorization.
- No runtime refactor authorization.
- No host filesystem mutation authorization.
- No Debian disposable harness execution authorization.
- No container/image/VM creation authorization.
- No apt/dpkg/package-manager execution authorization.
- No package installation authorization.
- No product/pilot/customer activation authorization.
- No secrets access authorization.
- No external LLM/API authorization.
- No dependency change authorization.
- No frontend/backend/action-runtime/audio mutation authorization.
