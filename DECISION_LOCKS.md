# ARIS Active-Context Live-State Normalization and Stale Routing Eradication Gate

## Current Live Locks
- Lock id: `ARIS_ACTIVE_CONTEXT_LIVE_STATE_NORMALIZATION_AND_STALE_ROUTING_ERADICATION`
- Status: `active_context_live_state_normalization_pass`
- Decision: `pass`
- Latest completed phase: `Lab Real Simulation Pack Debian Disposable Harness Readiness Review`
- Current status: `ready_for_plan_only_dry_run_commit_rehearsal_review`
- Active next phase: `Lab Real Simulation Pack Plan-Only Dry-Run Commit Rehearsal Review`
- Deferred phase: `Lab Real Simulation Pack Controlled Apply Operator Approval Packet Review`
- Deferred phase reason: `Operator Approval Packet Review remains deferred until Plan-Only Dry-Run Commit Rehearsal Review and remaining Tier-1 runtime-safety prerequisites are completed.`
- H4/H5/Hx: `not active current route`
- GitHub active-context is the only canonical active-context source.
- No GitHub active-context sync = no canonical PASS.
- Every ARIS phase/gate/status transition must update GitHub active-context.
- Every ARIS phase/gate/status transition must commit, push, and verify GitHub active-context.
- No real apply authorization.
- No real shadow workspace execution authorization.
- No Debian disposable harness execution authorization.
- No container/image/VM creation authorization.
- No Docker/Podman/Buildah/Nerdctl/containerd execution authorization.
- No apt/dpkg/package-manager execution authorization.
- No package installation authorization.
- No real dry-run execution authorization.
- No approval execution authorization.
- No runtime refactor authorization.
- No host filesystem mutation authorization.
- No product/pilot/customer activation authorization.
- No secrets access authorization.
- No external LLM/API authorization.
- No dependency change authorization.
- No frontend/backend/action-runtime/audio mutation authorization.
- GitHub active-context read/push/verification allowed only.

# GitHub Active-Context Canonicality Rule Gate

- Lock id: `GITHUB_ACTIVE_CONTEXT_CANONICALITY_V1_0`
- Status: `active_context_canonicality_rule_materialized_and_enforced`
- Decision: `pass`
- Canonical active-context source: `GitHub repository MatheusAugDEV/aris-active-context main branch`
- Canonical active-context remote: `https://github.com/MatheusAugDEV/aris-active-context`
- Canonical active-context branch: `main`

## Rule 1: Source-of-Truth Precedence

- GitHub active-context is the only canonical active-context source.
- Local active-context checkout is non-canonical until pushed and remote-verified.
- No local-only active-context update is canonical.
- No unpushed active-context commit is canonical.
- No GitHub active-context sync = no canonical PASS.

## Rule 2: Governance Enforcement

- Every ARIS phase/gate/status transition must update GitHub active-context.
- Every ARIS phase/gate/status transition must commit, push, and verify GitHub active-context.
- This includes:
  - phase pass
  - phase blocked
  - phase deferred
  - route correction
  - lock update
  - artifact creation
  - roadmap remediation
  - ledger correction
  - source-of-truth clarification
  - GitHub/local drift repair
  - any change to current status, next action, decision locks, ledger, context index, or canonical routing

## Rule 3: Agent Consultation

- ChatGPT and Codex must consult GitHub active-context before ARIS routing decisions.
- ChatGPT and Codex must prefer GitHub active-context over:
  - old chat memory
  - local-only active-context commits
  - unpushed Codex reports
  - uploaded local summaries
  - stale roadmap snippets
  - historical artifacts
  - assumptions
  - Obsidian notes
  - archive files

## Rule 4: Blocked and Drift Signals

- If GitHub active-context is unavailable, report: `BLOCKED_FOR_GITHUB_ACTIVE_CONTEXT_ACCESS`
- If local and GitHub active-context differ, report: `ACTIVE_CONTEXT_DRIFT_DETECTED`
- Do not treat local files as canonical until the drift is repaired, pushed, and remote-verified.

## Rule 5: Network Boundary

- GitHub network access is allowed only for active-context governance read, push, and remote verification.
- GitHub network access applies only to `MatheusAugDEV/aris-active-context` governance synchronization.
- GitHub network access must not be generalized to arbitrary internet access.
- Runtime/product/pilot/customer network remains forbidden.
- External LLM/API calls, secrets access, dependency updates, telemetry runtime, product runtime, action runtime, frontend/backend/audio mutation, real apply, real dry-run execution, approval execution, runtime refactor, and host filesystem mutation remain forbidden.

## Rule 6: Proof of Sync

- A phase/gate PASS requires proof:
  1. local active-context commit hash
  2. GitHub origin/main before push
  3. GitHub origin/main after push
  4. Verification: local HEAD == origin/main

- No push/fetch success = no canonical PASS.
- No verification = no canonical PASS.

## Canonical Files Required

- `CURRENT_STATE.md`
- `NEXT_ACTION.md`
- `DECISION_LOCKS.md`
- `CONTEXT_INDEX.md`
- `ARIS_PHASE_LEDGER.md`
- `ROADMAP_CANONICAL.md`
- `README.md`

These files must be updated at every phase/gate/status transition and must be pushed to GitHub.

## Historical / Proof-Only Entries

- Historical snapshot only; not the active current route. Do not use this block for current routing.

### Historical Routing Proof From Canonicality Gate

- Latest completed routing/remediation phase: `Lab Real Simulation Pack Filesystem Isolation Readiness Review`
- Current status: `ready_for_shadow_workspace_dry_run_blueprint_review`
- Active next phase: `Lab Real Simulation Pack Shadow Workspace Dry-Run Blueprint Review`
- Deferred/premature phase: `Lab Real Simulation Pack Controlled Apply Operator Approval Packet Review`
- Deferred phase blocking statement: `Lab Real Simulation Pack Controlled Apply Operator Approval Packet Review remains deferred until Debian Disposable Harness Readiness Review, plan-only dry-run commit rehearsal, and related Tier-1 runtime-safety prerequisites are completed.`
- Anti-regression: `H4/H5/Hx not active current route`

### Historical Lock Snapshot From Prior Canonicality Gate

- Historical snapshot only; not the active current route. Do not use this block for current routing.
- Previous roadmap remediation status: `ready_for_debian_disposable_harness_planning`
- Previous allowed future decision values: `['approved_for_next_plan_only_dry_run_blueprint_review', 'rejected', 'needs_revision']`
- Previous forbidden future decision values: `['approved_for_real_apply', 'ready_for_real_apply', 'approved_for_runtime_change', 'approved_for_network_use', 'approved_for_secret_access', 'approved_for_dependency_change']`
- Previous root commit hash: `04c2c46b4ee99357912c08aa1947666812dc85fe`
- Previous active-context commit hash: `04c2c46b4ee99357912c08aa1947666812dc85fe`
- Previous push result: `push_succeeded_github_active_context_canonicality_gate_applied`

## Current Authorization (Immutable Until Next Gate)

- No real apply authorization.
- No real shadow workspace execution authorization.
- No Debian disposable harness execution authorization.
- No container/image/VM creation authorization.
- No apt/dpkg/package-manager execution authorization.
- No real dry-run execution authorization.
- No approval execution authorization.
- No runtime refactor authorization.
- No host filesystem mutation authorization.
- No product/pilot/customer activation authorization.
- No secrets access authorization.
- No external LLM/API authorization.
- No dependency change authorization.
- No frontend/backend/action-runtime/audio mutation authorization.
- GitHub active-context read/push/verification allowed only.

## Gate Validation Proof

- Gate executed: `ARIS GitHub Active-Context Canonicality Rule Gate`
- GitHub remote verified: `True`
- Local HEAD before gate: `04c2c46b4ee99357912c08aa1947666812dc85fe`
- GitHub origin/main before gate: `243963b7f1d105a4374ae488da0996b5e988cf30`
- GitHub origin/main after push: `04c2c46b4ee99357912c08aa1947666812dc85fe`
- Local HEAD == origin/main after push: `True`
- Push succeeded: `True`
- Drift detected before push: `True` (local HEAD 5 commits newer than origin/main)
- Drift repaired: `True`
- Governance gap closed: `True`
- Policy strings materialized: `True` (all 11 required strings present)
- Routing strings materialized: `True` (all 6 required strings present)
- Forbidden authorization strings not present: `True` (no affirmative forbidden authorizations found)
- Protected surfaces not modified: `True` (frontend/backend/audio/action_runtime/runtime/dependencies untouched)
