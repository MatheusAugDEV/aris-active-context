# ARIS Active Context

## Canonical Architecture
- GitHub repository MatheusAugDEV/aris-active-context on branch main is the canonical active-context source.
- ACTIVE_CONTEXT_STATE.json is the only canonical live state file inside this repository.
- ACTIVE_CONTEXT_SCHEMA.json is the canonical validation contract for that live state.
- Markdown files are derived mirrors, explanatory docs, or historical ledger entries and are not authoritative live state.
- Markdown drift against `ACTIVE_CONTEXT_STATE.json` is a blocking error.
- Future agents must read `ACTIVE_CONTEXT_STATE.json` first, then validate mirrors and history.

## Live State Summary
- Latest completed phase: `Lab Real Simulation Pack Plan-Only Dry-Run Commit Rehearsal Review`
- Current status: `ready_for_controlled_apply_operator_approval_packet_review`
- Active next phase: `Lab Real Simulation Pack Controlled Apply Operator Approval Packet Review`
- Active next phase class: `review_gate_only`
- Operator Approval Packet Review is review-only and does not authorize execution.

## Safety Boundaries
- No real apply, no real dry-run execution, no approval execution, no runtime refactor, no host filesystem mutation, no Debian disposable harness execution, no container/image/VM creation, no apt/dpkg/package-manager execution, no package installation, no secrets access, no external LLM/API, no dependency change, no frontend/backend/action-runtime/audio mutation.
- GitHub active-context governance read, push, and verification are the only allowed network scope.

## Validation
- Validate ACTIVE_CONTEXT_STATE.json against ACTIVE_CONTEXT_SCHEMA.json before trusting any mirror.
- Markdown drift against JSON is a blocking error.
- Treat any Markdown live-looking text as non-authoritative if it conflicts with ACTIVE_CONTEXT_STATE.json.
