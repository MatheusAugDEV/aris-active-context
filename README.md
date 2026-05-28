# ARIS Active Context

## Canonical Architecture
- GitHub repository MatheusAugDEV/aris-active-context on branch main is the canonical active-context source.
- ACTIVE_CONTEXT_STATE.json is the only canonical live state file inside this repository.
- ACTIVE_CONTEXT_STATE.json is the only canonical live-state file.
- ACTIVE_CONTEXT_SCHEMA.json is the canonical validation contract for that live state.
- Markdown files are derived mirrors, explanatory docs, or historical ledger entries and are not authoritative live state.
- Markdown drift against `ACTIVE_CONTEXT_STATE.json` is a blocking error.
- Future agents must read `ACTIVE_CONTEXT_STATE.json` first, then validate mirrors and history.
- GitHub active-context is the only canonical active-context source.
- No GitHub active-context sync = no canonical PASS.

## Live State Summary
- Latest completed phase: `Lab Real Simulation Pack Controlled Apply Operator Approval Packet Review`
- Current status: `ready_for_controlled_apply_dry_run_harness_planning`
- Active next phase: `Lab Real Simulation Pack Controlled Apply Dry-Run Harness Planning`
- Active next phase class: `planning_gate`
- Operator Approval Packet Review is review-only, not execution approval.
- Controlled Apply Operator Approval Packet Review passed as review-only and did not execute approval or authorize execution.
- The next phase is planning-only for controlled apply dry-run harness and does not authorize real dry-run execution.
- H4/H5/Hx not active current route.

## Safety Boundaries
- No real apply, no real dry-run execution, no approval execution, no runtime refactor, no host filesystem mutation, no Debian disposable harness execution, no container/image/VM creation, no apt/dpkg/package-manager execution, no package installation, no secrets access, no external LLM/API, no dependency change, no frontend/backend/action-runtime/audio mutation.
- GitHub active-context governance read, push, and verification are the only allowed network scope.

## Validation
- Validate ACTIVE_CONTEXT_STATE.json against ACTIVE_CONTEXT_SCHEMA.json before trusting any mirror.
- Markdown drift against JSON is a blocking error.
- Treat any Markdown live-looking text as non-authoritative if it conflicts with ACTIVE_CONTEXT_STATE.json.
