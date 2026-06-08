# IF-08 W4 Validator Sync Repair

- repair_type: `active_context_validator_sync_repair`
- does_not_advance_phase: `true`
- latest_completed_phase_preserved: `IF-08 W4 Replay/Rollback/Concurrency/Cost Controlled Execution`
- latest_completed_status_preserved: `if08_w4_replay_rollback_concurrency_cost_controlled_execution_pass`
- latest_completed_project_commit_sha_preserved: `c65888a2f587c35b4e38b16b50b917233bac8fa3`
- latest_completed_ci_state_preserved: `CI_GREEN_CONFIRMED`
- next_recommended_step_preserved: `post_sync_review_if08_w4_replay_rollback_concurrency_cost_controlled_execution`

## Scope

- Sync `scripts/validate_active_context_state.py` with the already canonical W4 controlled execution packet.
- Keep the validator checking `synthetic_attack_cases_total=14`, `rollback_honesty_checks=6/6`, `duplicate_detection_checks=5/5`, `cost_enforcement_checks=3/3`, and `RHR=DDR=CER=1.0`.
- Preserve `w4_execution_performed=true`, `execution_scope=synthetic_isolated_lab_only`, and all forbidden execution surfaces as `false`.

## Non-Goals

- No new wave execution.
- No phase advance.
- No route change.
- No lock relaxation for runtime, real apply, product, Bedrock, secrets, MCP, RAG, memory write, socket, shell, filesystem escape, network, cost, or quota.
