# CI Terminal-State Reporting Rule

- Rule name: `CI Terminal-State Reporting Rule`
- Decision: `pass`
- Status: `ci_terminal_reporting_rule_materialized`

## Allowed terminal outcomes

1. `CI_GREEN_CONFIRMED`
2. `CI_FAILED`
3. `CI_PENDING`

## Enforcement

- Final PASS reports are forbidden while any relevant workflow is `queued`, `waiting`, `requested`, or `in_progress`.
- `CI_PENDING` is interim-only and blocks final decision, next prompt emission, and phase advance.
- `CI_GREEN_CONFIRMED` requires every relevant workflow to be terminal with `success`.
- `CI_FAILED` requires terminal failure evidence, failed workflow URL, failed job, root cause, and log excerpt.

## Safety

- `if08_execution_authorized=false`
- `waves_execution_authorized=false`
- `bot_execution_authorized=false`
- `runtime_execution_authorized=false`
- `real_dry_run_authorized=false`
- `real_apply_authorized=false`
- `product_promotion_authorized=false`
- `pilot_authorized=false`
- `bedrock_authorized=false`
- `secrets_access_authorized=false`
- `dependency_mutation_authorized=false`
