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
- Latest completed phase: `Lab Real Simulation Pack Plan-Only Dry-Run Commit Rehearsal Review`
- Current status: `ready_for_controlled_apply_operator_approval_packet_review`
- Active next phase: `Lab Real Simulation Pack Controlled Apply Operator Approval Packet Review`
- Active next review gate: `Lab Real Simulation Pack Controlled Apply Operator Approval Packet Review`
- H4/H5/Hx: `not active current route`
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

## Historical / Proof-Only Entries
- Historical routing proof from the prior canonicality gate remains historical only.
- Do not use historical proof for current routing.
- Historical snapshot values may include earlier phases, but they are superseded by `ACTIVE_CONTEXT_STATE.json`.
