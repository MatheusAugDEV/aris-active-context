# CONTEXT_INDEX

## Live pointers
- [CURRENT_STATE.md](CURRENT_STATE.md)
- [NEXT_ACTION.md](NEXT_ACTION.md)
- [DECISION_LOCKS.md](DECISION_LOCKS.md)
- [EXTERNAL_REFERENCES.md](EXTERNAL_REFERENCES.md)
- [MODEL_REASONING_POLICY.md](MODEL_REASONING_POLICY.md)
- [HANDOFF_RESPONSE_POLICY.md](HANDOFF_RESPONSE_POLICY.md)
- [ARIS_PHASE_LEDGER.md](ARIS_PHASE_LEDGER.md)
- [BEDROCK_GATE.md](BEDROCK_GATE.md)
- [NORTH_POLE.md](NORTH_POLE.md)
- [PHASE_SPECIFIC_GATES.md](PHASE_SPECIFIC_GATES.md)

## Recent phase references
- `F21-CTX-D2` completed the active-context OS reform design, kept apply blocked, and recommends `F21-CTX-D3` apply planning before any F21-A61 implementation.
- `F21-CTX-D1` completed the active-context OS full diagnostic with warnings, found a missing `HANDOFF_RESPONSE_POLICY.md`, and recommends `F21-CTX-D2` design-only reform before any F21-A61 implementation.
- `F21-A60` confirmed readiness for a future contract-only Prompt Kernel implementation and kept runtime integration blocked.
- `F21-A59` reviewed the Prompt Kernel implementation plan, repaired the live model-policy pointer, and kept implementation blocked pending readiness review.
- `F21-A58` planned the future Prompt Kernel v0.1 implementation boundary and kept runtime implementation blocked.
- `F21-A57` reviewed the Prompt Kernel v0.1 plan and kept implementation blocked.
- `F21-A56` created the Prompt Kernel v0.1 plan only and keeps implementation blocked until review.
- `F21-A55` post-sync closure reconciles the root commit divergence and keeps unrelated dirty work visible.
- `F21-A54C` remote sync verification confirmed both `origin/main` refs matched local HEAD.
- `F21-A54B` hygiene repair compacted the active-context and kept the root push debt visible.
- `F21-A54` lean runner review passed locally and recorded stale duplicate blocks as a warning.

## External reference index
- `ext_ref_huw_prosser_fury_2026_05`: catalogued external architectural reference for future Prompt Kernel, Context Compression, Memory Kernel, Skill Kernel, Tool Harness, Voice Runtime, UI Observability, and Action Runtime decisions.
- status: `catalogued_external_reference`
- implementation_allowed_now: `false`
- roadmap_direct_insert_allowed_now: `false`
- phase_sequence_change_allowed_now: `false`
- macroblock_mapping_required: `true`
- decision_gate_required_before_use: `true`
- source_of_truth_rank: `reference_only_non_authoritative`

## Model/reasoning policy index
- policy_file: `MODEL_REASONING_POLICY.md`
- default_model: `5.4 mini`
- default_reasoning_level: `baixo`
- escalation_required_when_phase_risk_increases: `true`
- active_context_touch_default: `5.4 normal / alto`
- critical_recovery_security_roadmap_default: `5.5 / altissimo`
- policy_is_advisory_not_authorization: `true`

## Handoff response policy index
- policy_file: `HANDOFF_RESPONSE_POLICY.md`
- default_handoff_style: `compact`
- artifact_detail_is_source_of_truth: `true`
- chat_handoff_should_not_duplicate_artifacts: `true`
- context_usage_report_in_chat_by_default: `false`
- full_validation_log_in_chat_by_default: `false`
- full_file_list_in_chat_by_default: `false`
- full_flags_list_in_chat_by_default: `false`

## Hygiene status
- latest_completed_phase: `F21-CTX-D2 - Active Context Operating System Reform Design Gate`
- next_recommended_phase: `F21-CTX-D3 - Active Context Operating System Reform Apply Plan Gate`
- active_context_os_diagnostic_completed: `True`
- active_context_os_reform_design_completed: `True`
- handoff_response_policy_available: `True`
- pass_warn_policy_reform_needed: `True`
- proposed_files_read_by_default: `4`
- current_default_boot_file_count: `10`
- estimated_boot_reduction_percent: `60.0`
- active_context_remote_sync_verified: `True`
- root_repo_push_verified: `True`
- root_repo_push_pending: `False`
- nested_active_context_push_verified: `True`
- root_worktree_dirty_unrelated: `True`
- model_reasoning_policy_available: `True`
- handoff_response_policy_available: `True`
- prompt_kernel_planning_allowed_now: `False`
- prompt_kernel_implementation_allowed_now: `False`
- controlled_contract_implementation_allowed_next: `False`
- f21_a61_allowed_next: `False`
- prompt_kernel_runtime_integration_allowed: `False`

## Notes
- This index is compact and intentionally excludes stale repeated blocks.
- F21-CTX-D2 is design-only; it does not apply the reform, compact, implement Prompt Kernel, mutate runtime, or authorize F21-A61.
- `HANDOFF_RESPONSE_POLICY.md` is present and defines compact handoff behavior; it is policy-only and not implementation authority.
- `MODEL_REASONING_POLICY.md` is live, advisory-only, and non-authoritative for implementation.
- `HANDOFF_RESPONSE_POLICY.md` is live and requires compact Codex phase handoffs by default.
- External references are catalogued and reference-only, never authoritative for implementation.
- `NORTH_POLE.md` remains the strategic north reference.
- `MODEL_REASONING_POLICY.md` must be consulted when generating future ARIS prompts so each prompt states model tier and reasoning level compactly.
- `HANDOFF_RESPONSE_POLICY.md` must be consulted before final phase handoff; detailed evidence belongs in artifacts/reports unless there is a failure or explicit request for full audit.
- The next gate may create only contract-only files and must not integrate with runtime.
- External references are advisory context only and do not authorize implementation, roadmap sequence changes, runtime mutation, MCP, product promotion, customer real use, or production release.
