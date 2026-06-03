# AC-REPAIR-01 Report

- Phase: `ARIS Active-Context Anti-Proliferation & CI Enforcement Repair Gate`
- Phase ID: `AC-REPAIR-01`
- Initial `origin/main` SHA read first: `b297f3d0a50bf8e5c6b1cbca7ca31145ca6c3a0c`
- Decision: `pass`
- Next phase: `null`
- next_phase_authorized_by_operator: `false`
- anti_proliferation_rule_active: `true`
- ci_enforcement_active: `true`

## Scope

Governance repair only. No real execution, no fixture materialization, no bot activation, and no runtime mutation.

## Materialized changes

- Added the anti-proliferation gate rule to `MANDATORY_READ_FIRST_RULES.md`.
- Added the anti-proliferation rule and mandatory reviewer SHA rule to `PROMPT_CONTRACT.md`.
- Added CI enforcement in `.github/workflows/validate_active_context.yml`.
- Added `scripts/assert_no_unauthorized_fixtures.py`.
- Updated `ACTIVE_CONTEXT_SCHEMA.json` and `ACTIVE_CONTEXT_STATE.json` for `phase_id`, `current_phase_id`, null next-phase routing, and new governance flags.
- Updated mirrors so the canonical route is closed pending manual operator authorization.
