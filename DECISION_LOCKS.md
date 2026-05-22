# DECISION_LOCKS

## F21-A54B — Active Context Hygiene Repair Lock
- latest_completed_phase: `F21-A54B — Active Context Hygiene Repair for Lean Runner Review`
- status: `active_context_hygiene_repair_warn`
- decision: `warn`
- reviewed_phase_id: `F21-A54`
- stale_duplicate_blocks_detected: `True`
- stale_duplicate_blocks_cleaned: `True`
- root_repo_push_verified: `False`
- root_repo_push_pending: `True`
- active_context_remote_sync_verified: `False`
- nested_active_context_push_verified: `False`
- prompt_kernel_allowed: `False`
- template_library_allowed: `False`
- batch_runner_allowed: `False`
- mcp_activation_allowed: `False`
- mcp_config_write_allowed: `False`
- vault_write_allowed: `False`
- network_allowed: `False`
- dependency_install_allowed: `False`
- runtime_mutation_allowed: `False`
- product_promotion_allowed: `False`
- customer_real_use_allowed: `False`
- production_release_allowed: `False`
- next_real_action: `F21-A54C — Active Context Remote Sync Verification Gate`

This lock keeps the post-repair state explicit and preserves the root push debt.

## Recent immutable antecedents
- `F21-A54`: lean minimal acceptance runner review passed locally, detected stale duplicate blocks, and left the root push pending.
- `F21-A51`: validator review kept acceptance runner work blocked until the implementation gate.
- `F21-A50`: validator implementation remained review-only and did not authorize acceptance runner work.
- `F21-A49`: schema review allowed the validator implementation next and kept acceptance runner work blocked.
