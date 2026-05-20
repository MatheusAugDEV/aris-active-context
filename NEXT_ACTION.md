## ARIS-CONTEXT-P29-R6 — Artifact Reference-Only Controlled Apply Rerun Gate
- status: `artifact_reference_only_controlled_apply_rerun_warn`
- execution_class: `controlled_apply_rerun_passed_with_reduction`
- baseline_refresh_verified: `True`
- current_context_valid_before_apply: `True`
- current_context_valid_after_apply: `True`
- hot_path_preserved: `True`
- artifact_reference_only_contract_preserved: `True`
- allowlist_respected: `True`
- deny_conditions_respected: `True`
- rollback_ready: `True`
- rollback_executed: `False`
- actual_token_reduction: `130742`
- minimum_planned_token_reduction: `19963`
- projected_token_reduction_from_p29r5: `53232`
- safe_to_continue_after_rerun: `True`
- recommended_next_phase: `ARIS-CONTEXT-P29-R4 — Active-Context Baseline Reconciliation Gate`

The rerun is complete and the next step is validation only if the compact apply passed every precondition.

## Compact references
- source_context_commit_ref: `c10253f1f6ad15b93b62981fcccc0ba02eb06237`
- root_repo_commit_ref: `b9a763d0f75deb94c64458fcfaabaa11b9018f7c`
- p29r5_refreshed_preflight_hashes_artifact: `artifacts/context/active_context_baseline_refresh_preflight_hashes.json`
- p29r5_snapshot_artifact: `artifacts/context/active_context_baseline_refresh_snapshot.json`
- p29r5_rollback_readiness_artifact: `artifacts/context/active_context_baseline_refresh_rollback_readiness.json`
- p29r5_recommendation_artifact: `artifacts/context/active_context_baseline_refresh_recommendation.json`
- p29r4_hash_matrix_artifact: `artifacts/context/active_context_baseline_reconciliation_hash_matrix.json`
- p29r4_drift_manifest_artifact: `artifacts/context/active_context_baseline_reconciliation_drift_manifest.json`
- p29r3_post_hashes_artifact: `artifacts/context/artifact_reference_only_controlled_apply_compaction_repair_execution_post_hashes.json`
- p29r3_diff_manifest_artifact: `artifacts/context/artifact_reference_only_controlled_apply_compaction_repair_execution_diff_manifest.json`
- p29r3_token_delta_artifact: `artifacts/context/artifact_reference_only_controlled_apply_compaction_repair_execution_token_delta.json`
- p29r2_allowlist_artifact: `artifacts/context/artifact_reference_only_controlled_apply_compaction_repair_preflight_allowlist.json`
- p29r2_rollback_package_artifact: `artifacts/context/artifact_reference_only_controlled_apply_compaction_repair_preflight_rollback_package.json`
- p29_r1_token_projection_artifact: `artifacts/context/artifact_reference_only_controlled_apply_compaction_repair_token_projection.json`
- p29_summary_artifact: `artifacts/context/artifact_reference_only_controlled_apply_post_apply_validation_gate_summary.json`
- p29r5_provenance_verified: `True`
- p29r4_provenance_verified: `True`
- p29r5_baseline_refresh_materialized: `True`
- p29r5_safe_to_rerun_p29r3_after_refresh: `True`
- p29r5_p29r3_rerun_allowed_next: `True`
- p29r4_current_context_commit_ref: `b89a5224fa5cb3b25624a5aae29cb440f015772b`
- p29r4_drift_classification: `expected_recovery_drift`
- p29r4_cause_category: `stale_p29r2_snapshot`
