# ARIS Active Context

## Canonical Architecture
- GitHub repository MatheusAugDEV/aris-active-context on branch main is the canonical active-context source.
- ACTIVE_CONTEXT_STATE.json is the only canonical live state file inside this repository.
- ACTIVE_CONTEXT_STATE.json is the only canonical live-state file.
- ACTIVE_CONTEXT_SCHEMA.json is the canonical validation contract for that live state.
- Markdown files are derived mirrors, explanatory docs, or historical ledger entries and are not authoritative live state.
- Markdown drift against `ACTIVE_CONTEXT_STATE.json` is a blocking error.
- Markdown drift against JSON is a blocking error.
- Read ACTIVE_CONTEXT_STATE.json first, then validate mirrors and history.
- GitHub active-context is the only canonical active-context source.
- No GitHub active-context sync = no canonical PASS.

## Live State Summary
- Latest completed phase: `Lab Real Simulation Pack Controlled Apply Dry-Run Operator Approval Response Evidence Packaging Planning`
- Current status: `ready_for_controlled_apply_dry_run_operator_approval_response_evidence_packaging_readiness_review`
- Active next phase: `Lab Real Simulation Pack Controlled Apply Dry-Run Operator Approval Response Evidence Packaging Readiness Review`
- Active next phase class: `readiness_gate`
- Operator Approval Response Evidence Packaging Planning completed with decision `pass`.
- The prior readiness review remains historical `blocked` evidence and was not rewritten.
- Roadmap amendment required: `True`
- Bedrock preparation exception recorded in `LAB_VERDICTS.md`; Bedrock gate remains non-executable.
- H4/H5/Hx not active current route.

## Safety Boundaries
- No real apply, no real dry-run execution, no approval execution, no runtime refactor, no host filesystem mutation, no Debian disposable harness execution, no container/image/VM creation, no apt/dpkg/package-manager execution, no package installation, no secrets access, no external LLM/API, no dependency change, no frontend/backend/action-runtime/audio mutation.
- GitHub active-context governance read, push, and verification are the only allowed network scope.
