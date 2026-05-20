## F21-A5 Source-of-Truth Precedence Gate References
- phase_id: `F21-A5`
- phase_doc: `docs/fase21/f21a_a5_source_of_truth_precedence_gate.md`
- summary_artifact: `artifacts/f21/source_of_truth_precedence_gate_v2_summary.json`
- decision_artifact: `artifacts/f21/source_of_truth_precedence_gate_v2.json`
- report_artifact: `artifacts/f21/source_of_truth_precedence_gate_v2_report.md`
- next_recommended_phase: `F21-A6 — Obsidian MCP Human Evidence Intake`

## F21-A5 Active Track Notes
- Hard locks are first, next action is second, and live state is third.
- Phase artifacts outrank historical docs; README and project context remain non-authoritative.
- Obsidian stays consultive only.
- Chat history and memory stay non-authoritative.
## F21-A4 Context Budget Policy Gate References
- phase_id: `F21-A4`
- phase_doc: `docs/fase21/f21a_a4_context_budget_policy_gate.md`
- summary_artifact: `artifacts/f21/context_budget_policy_gate_summary.json`
- decision_artifact: `artifacts/f21/context_budget_policy_gate.json`
- report_artifact: `artifacts/f21/context_budget_policy_gate_report.md`
- usage_report_artifact: `artifacts/f21/context_budget_usage_report.json`
- next_recommended_phase: `F21-A5 — Source-of-Truth Precedence Gate`

## F21-A4 Active Track Notes
- The budget policy is summary-first, query-first, and bounded by active-context tiers.
- Token-saving remains unclaimed unless measured and recorded in artifact form.
- Obsidian stays read-only and query-first.
- Bulk reads remain blocked.
## F21-A3 Claude Code Instruction Alignment References
- phase_id: `F21-A3`
- phase_doc: `docs/fase21/f21a_a3_claude_code_instruction_alignment.md`
- summary_artifact: `artifacts/f21/claude_code_instruction_alignment_summary.json`
- decision_artifact: `artifacts/f21/claude_code_instruction_alignment.json`
- report_artifact: `artifacts/f21/claude_code_instruction_alignment_report.md`
- source_boundary_doc: `docs/fase21/f21a_a1_context_source_access_policy_untrusted_input_boundary.md`
- codex_skill_alignment_doc: `docs/fase21/f21a_a2_codex_skill_alignment_review.md`
- next_recommended_phase: `F21-A4 — Context Budget Policy Gate`

## F21-A3 Active Track Notes
- The Claude Code alignment gate is read-first, summary-first, query-first, and final-handoff aware.
- Active-context update, commit hash, and push reporting are explicit.
- Obsidian remains query-first and read-only.
- Bulk reads remain blocked.

## F21-A2 Codex Skill Alignment Review References
- phase_id: `F21-A2`
- phase_doc: `docs/fase21/f21a_a2_codex_skill_alignment_review.md`
- summary_artifact: `artifacts/f21/codex_skill_alignment_review_summary.json`
- decision_artifact: `artifacts/f21/codex_skill_alignment_review.json`
- report_artifact: `artifacts/f21/codex_skill_alignment_review_report.md`
- source_boundary_doc: `docs/fase21/f21a_a1_context_source_access_policy_untrusted_input_boundary.md`
- next_recommended_phase: `F21-A3 — Claude Code Instruction Alignment`

## F21-A2 Active Track Notes
- The Codex skill review is read-first, summary-first, and query-first.
- Obsidian remains query-first and read-only.
- Bulk reads remain blocked.
- Prompt handoff requires the final active-context update and commit hash reporting.
## F21-A1 Context Source Access Policy & Untrusted Input Boundary References
- phase_id: `F21-A1`
- macroblock_id: `MB1`
- gate_summary_artifact: `artifacts/f21/context_source_access_policy_gate_summary.json`
- gate_decision_artifact: `artifacts/f21/context_source_access_policy_gate_decision.json`
- gate_report_artifact: `artifacts/f21/context_source_access_policy_gate_report.md`
- policy_doc: `docs/fase21/f21a_a1_context_source_access_policy_untrusted_input_boundary.md`
- source_of_truth_policy: `docs/architecture/source_of_truth_policy.md`
- obsidian_query_first_summary: `artifacts/f21/obsidian_query_first_access_contract_summary.json`
- obsidian_bulk_read_summary: `artifacts/f21/obsidian_bulk_read_prevention_gate_summary.json`
- source_precedence_summary: `artifacts/f21/source_of_truth_precedence_gate_summary.json`
- next_recommended_phase: `F21-A2 — Codex Skill Alignment Review`
- legacy_noise_sources: `src/aris/context/context_source_access_policy.py, docs/fase21/f21_context_source_access_policy.md, artifacts/f21/context_source_access_policy_summary.json, artifacts/f21/context_source_access_policy_report.md, artifacts/f21/context_source_access_policy_decision.json`

## Roadmap Canonical State References
- canonical_current_state: `MB1 active; F21-A1 materialized; active track continues at F21-A2.`
- next_action_single_forward_pointer: `True`
- manual_selection_required: `False`

## Roadmap Canonical State References
- roadmap_canonical_state_gate_summary_artifact: `artifacts/context/roadmap_canonical_state_gate_summary.json`
- roadmap_canonical_state_gate_decision_artifact: `artifacts/context/roadmap_canonical_state_gate_decision.json`
- roadmap_canonical_phase_matrix_artifact: `artifacts/context/roadmap_canonical_phase_matrix.json`
- roadmap_next_action_sanitization_plan_artifact: `artifacts/context/roadmap_next_action_sanitization_plan.json`
- roadmap_next_action_recommendation_artifact: `artifacts/context/roadmap_next_action_recommendation.json`
- p29r8_closure_summary_artifact: `artifacts/context/active_context_compaction_closure_gate_summary.json`
- active_track_resume_summary_artifact: `artifacts/context/active_track_resume_gate_summary.json`
- active_track_phase_reconciliation_summary_artifact: `artifacts/context/active_track_phase_reconciliation_summary.json`
- pre_f21_summary_artifact: `artifacts/v5/token_economy_context_discipline_summary.json`
- f32_closure_artifact: `docs/fase32/f32z13t_r1_final_f32_closure_gate.md`
- f33_hold_summary_artifact: `artifacts/f33/f33z5_schema_materialization_controlled_pre_apply_authorization_gate_summary.json`

## ARIS-CONTEXT-ROADMAP-CANONICAL-STATE — Roadmap Canonical State & Next Action Sanitization Gate
- roadmap_class: `f21_canonical_f33_blocked_under_lab_governance`
- canonical_current_state: `P29 closed; PRE-F21 materialized; active track resumes at F21; F32 closed; F33 blocked under Lab governance.`
- canonical_next_phase: `F21 — Context Source Access Policy & Untrusted Input Boundary`
- canonical_next_phase_title: `Context Source Access Policy & Untrusted Input Boundary`
- manual_selection_required: `False`
- next_action_single_forward_pointer: `True`
- next_action_repair_required: `True`
- ledger_history_preserved: `True`
- preexisting_untracked_noise: `True`

## Roadmap Macroblocks
- `docs/roadmap/roadmap_macroblocks.md`
- `docs/roadmap/roadmap_macroblocks_r0_f120.md`
- `artifacts/context/active_context_macroblock_cleanup_summary.json`
- `artifacts/context/active_context_macroblock_cleanup_report.md`
