# ARIS Active Context

## Canonical Architecture

- GitHub repository MatheusAugDEV/aris-active-context on branch main is the canonical active-context source.
- **ACTIVE_CONTEXT_STATE.json is the only canonical live state file inside this repository.**
- ACTIVE_CONTEXT_SCHEMA.json is the canonical validation contract for that live state.
- Markdown files are derived mirrors, explanatory docs, or historical ledger entries and are not authoritative live state.
- Markdown drift against `ACTIVE_CONTEXT_STATE.json` is a blocking error.
- **Read ACTIVE_CONTEXT_STATE.json first**, then validate mirrors and history. Never read Markdown before the JSON.
- GitHub active-context is the only canonical active-context source.
- No GitHub active-context sync = no canonical PASS.

## Mandatory Read Order (for any agent or human)

```
1. ACTIVE_CONTEXT_STATE.json          ← canonical live state
2. ACTIVE_CONTEXT_SCHEMA.json         ← validation contract
3. scripts/validate_active_context_state.py  ← run before any decision
4. Markdown mirrors (read-only confirmation):
   CURRENT_STATE.md, NEXT_ACTION.md, DECISION_LOCKS.md,
   CONTEXT_INDEX.md, ARIS_PHASE_LEDGER.md, ROADMAP_CANONICAL.md
5. Governance contracts when required:
   BOOT_PROFILE.md, MANDATORY_READ_FIRST_RULES.md, PROMPT_CONTRACT.md
6. Lab files when required:
   LAB_OPERATING_CONTRACT.md, LAB_STATUS.md, LAB_VERDICTS.md
```

A Markdown file that contradicts ACTIVE_CONTEXT_STATE.json **must not be trusted**. Report the drift and block the decision.

## Live State Summary

- ACTIVE_CONTEXT_STATE.json wins. If this file conflicts with ACTIVE_CONTEXT_STATE.json, ACTIVE_CONTEXT_STATE.json wins.
- Latest completed phase: `ARIS Active-Context Anti-Corruption Hardening Gate`
- Current status: `ready_for_controlled_apply_dry_run_harness_planning`
- Active next phase: `Lab Real Simulation Pack Controlled Apply Dry-Run Harness Planning`
- Active next phase class: `planning_gate`
- Planning-only: `true` — produces a plan artifact, does not authorize any execution.
- H4/H5/Hx not active current route.

## Safety Boundaries

- No real apply, no real dry-run execution, no approval execution, no runtime refactor, no host filesystem mutation, no Debian disposable harness execution, no container/image/VM creation, no apt/dpkg/package-manager execution, no package installation, no secrets access, no external LLM/API, no dependency change, no frontend/backend/action-runtime/audio mutation.
- GitHub active-context governance read, push, and verification are the only allowed network scope.

## Validation

- Always run: `python3 scripts/validate_active_context_state.py` before trusting any state.
- Validate ACTIVE_CONTEXT_STATE.json against ACTIVE_CONTEXT_SCHEMA.json before trusting any mirror.
- Markdown drift against JSON is a blocking error.
- Treat any Markdown live-looking text as non-authoritative if it conflicts with ACTIVE_CONTEXT_STATE.json.

## Anti-Corruption Contract

See `ACTIVE_CONTEXT_ANTI_CORRUPTION_CONTRACT.md` for the full anti-corruption protocol for agents and humans.
