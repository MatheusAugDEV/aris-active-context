# Active-Context Schema/State Drift Repair

- Decision: `pass`
- Status: `active_context_schema_state_drift_repair_pass`
- Scope: schema/state/validator coherence repair only
- Project_ARIS touched: `false`

## Repaired drift

- `ACTIVE_CONTEXT_SCHEMA.json` now accepts `active_context_version=3.0`.
- `artifact_routes` now reflects the live state shape with `boot_rules` and `history_archive`, and no longer requires `decision_locks_mirror`.
- Stale live-state requirements absent from `ACTIVE_CONTEXT_STATE.json` were removed from the schema contract.
- Missing live-state keys used by the current PURG04 route are now declared in the schema.
- `scripts/validate_active_context_state.py` now checks schema/state coherence directly and reports `governance_gate_streak=0` exactly as stored.
- Historical tests pinned to IF-08 were updated to the current PURG04 live route while preserving the historical `INF-FULL-07 -> PURG-PRE` Próxima fase truth.

## Preserved live route

- `phase_id=current_phase_id=PURG04_TRACK_A_POST_MERGE_VALIDATION_PACKET`
- `status=purg04_track_a_post_merge_validation_packet_pass`
- `next_phase=null`
- `active_next_phase=null`
- `governance_gate_streak=0`
- `IF09-FIND-001` remains open
- `finding_closed=false`
- `remediation_proven=false`

## Local validation evidence

- `python3 -m json.tool ACTIVE_CONTEXT_STATE.json` -> `0`
- `python3 -m json.tool ACTIVE_CONTEXT_SCHEMA.json` -> `0`
- `python3 scripts/validate_active_context_state.py` -> `0`
- `python3 -m pytest -q tests/test_validate_active_context.py tests/test_purg04_validator_scope_repair.py tests/test_active_context_route_sync_unittest.py` -> `0` (`79 passed`)

## Real-lock attestation

- `real_apply_authorized=false`
- `production_authorized=false`
- `product_ready=false`
- `secrets_access_authorized=false`
- `runtime_integration_allowed=false`
- no `finding_closed=true` introduced
- no `Project_ARIS` mutation performed
