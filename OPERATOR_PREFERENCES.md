# OPERATOR_PREFERENCES

This file is a high-priority operator preference layer for prompt emission behavior.
If this file conflicts with `ACTIVE_CONTEXT_STATE.json`, `ACTIVE_CONTEXT_SCHEMA.json`,
`scripts/validate_active_context_state.py`, `ROADMAP_CANONICAL.md`, the Transition
Table, or any explicit lock/manual authorization requirement, the higher canonical
authority wins and this file must not be used to justify action.

## Prompt emission preference

The assistant must not ask for confirmation just to send the next Codex prompt when
the Transition Table defines the next phase with `advance_mode=prompt_only`, the
previous phase is canonically PASS, CI/validator evidence is green, and no explicit
lock says operator/manual authorization is required for that exact transition.
In those cases, the assistant should directly provide the next Codex prompt.

## Safety boundary

This preference does not authorize production, Bedrock, pilot, runtime execution,
real secrets, external network, or any phase whose `advance_mode=operator`.

This preference cannot override:
- `ACTIVE_CONTEXT_STATE.json`
- `ACTIVE_CONTEXT_SCHEMA.json`
- `scripts/validate_active_context_state.py`
- `ROADMAP_CANONICAL.md`
- the Transition Table
- `DECISION_LOCKS.md`
- `next_phase_authorized_by_operator=false`
- any explicit manual/operator authorization requirement for the exact transition

## Non-authorization consequences

- next_phase remains `null` after a phase closes unless an explicit state transition is canonically recorded.
- `ACB-CAP-02` or any later phase is not auto-opened by this preference alone.
- `advance_mode=operator` still requires explicit operator authorization.
