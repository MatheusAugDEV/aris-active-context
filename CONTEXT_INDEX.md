# CONTEXT_INDEX

Read in this order:

1. [CURRENT_STATE.md](CURRENT_STATE.md)
2. [NEXT_ACTION.md](NEXT_ACTION.md)
3. [DECISION_LOCKS.md](DECISION_LOCKS.md)
4. [ARIS_PHASE_LEDGER.md](ARIS_PHASE_LEDGER.md)
5. [OPERATOR_PREFERENCES.md](OPERATOR_PREFERENCES.md)
6. [README.md](README.md)
7. [docs/fase31/f31b_hash_signature_metadata_index.md](../docs/fase31/f31b_hash_signature_metadata_index.md) for the current metadata index baseline
8. [docs/fase31/f31c_source_of_truth_consistency_gate.md](../docs/fase31/f31c_source_of_truth_consistency_gate.md) for the consistency gate
9. [docs/fase31/f31d_source_of_truth_drift_repair_plan.md](../docs/fase31/f31d_source_of_truth_drift_repair_plan.md) for the repair plan
9. [docs/fase31/f31d_source_of_truth_drift_repair_plan.md](../docs/fase31/f31d_source_of_truth_drift_repair_plan.md) for the repair plan
9. [ROADMAP_F30_F50.md](ROADMAP_F30_F50.md) for the formal post-V6 operational roadmap
10. [docs/context/ctxe1_token_economy_visibility_audit.md](../docs/context/ctxe1_token_economy_visibility_audit.md) for the token economy audit
11. [docs/context/ctxe2_prompt_template_compression_contract.md](../docs/context/ctxe2_prompt_template_compression_contract.md) for the prompt template compression contract
10. Obsidian only after the repair and only query-first
11. `archive/` only when history is needed
12. [docs/context/ctxe3_prompt_budget_gate.md](../docs/context/ctxe3_prompt_budget_gate.md) for the prompt budget gate
13. [docs/context/ctxe4_prompt_budget_threshold_calibration.md](../docs/context/ctxe4_prompt_budget_threshold_calibration.md) for the prompt budget threshold calibration
14. [docs/context/aris_prompt_budget_policy.md](../docs/context/aris_prompt_budget_policy.md) for the published prompt budget policy
15. [docs/context/ctxe5_prompt_budget_policy_publication.md](../docs/context/ctxe5_prompt_budget_policy_publication.md) for the prompt budget policy publication
16. `Project_ARIS` artifacts/docs only when cited

- Do not bulk-read `archive/`.
- Do not bulk-read Obsidian.
- Do not rely on old memory against `CURRENT_STATE`.
- Do not advance phase without checking `NEXT_ACTION`.
- Do not declare token savings without evidence.
- Keep this repo compact.
17. [docs/context/ctxe6_prompt_budget_skill_script_implementation_plan.md](../docs/context/ctxe6_prompt_budget_skill_script_implementation_plan.md) for the prompt budget skill and script implementation plan
18. [docs/context/ctxe7_prompt_budget_skill_scaffold_materialization.md](../docs/context/ctxe7_prompt_budget_skill_scaffold_materialization.md) for the prompt budget skill scaffold materialization
19. [.agents/skills/](../.agents/skills/) and [.claude/skills/](../.claude/skills/) for the prompt budget skill scaffolds
20. [docs/context/ctxe8_prompt_budget_script_scaffold_materialization.md](../docs/context/ctxe8_prompt_budget_script_scaffold_materialization.md) for the prompt budget script scaffold materialization
21. [scripts/check_*.py](../scripts/check_active_context_first.py) and [scripts/run_standard_validation_pack.py](../scripts/run_standard_validation_pack.py) for local prompt-budget checks
22. [docs/context/ctxe9_prompt_budget_script_scaffold_validation_review.md](../docs/context/ctxe9_prompt_budget_script_scaffold_validation_review.md) for the prompt budget script scaffold validation review
23. [artifacts/context/ctxe9_prompt_budget_script_scaffold_validation_review_matrix.json](../artifacts/context/ctxe9_prompt_budget_script_scaffold_validation_review_matrix.json) for the script review matrix
24. [docs/context/ctxe10_prompt_budget_script_scaffold_repair_plan.md](../docs/context/ctxe10_prompt_budget_script_scaffold_repair_plan.md) for the prompt budget script scaffold repair plan
25. [artifacts/context/ctxe10_prompt_budget_script_scaffold_repair_plan_plan.json](../artifacts/context/ctxe10_prompt_budget_script_scaffold_repair_plan_plan.json) for the prompt budget script scaffold repair plan
26. [artifacts/context/ctxe10_prompt_budget_script_scaffold_repair_plan_findings.json](../artifacts/context/ctxe10_prompt_budget_script_scaffold_repair_plan_findings.json) for the prompt budget script scaffold repair findings
27. [docs/context/ctxe11_real_token_usage_baseline_plan.md](../docs/context/ctxe11_real_token_usage_baseline_plan.md) for the real token usage baseline plan
28. [artifacts/context/ctxe11_real_token_usage_baseline_plan_manual_evidence_template.json](../artifacts/context/ctxe11_real_token_usage_baseline_plan_manual_evidence_template.json) for the manual evidence template
29. [docs/context/ctxe12_real_token_usage_baseline_manual_evidence_runbook.md](../docs/context/ctxe12_real_token_usage_baseline_manual_evidence_runbook.md) for the manual evidence runbook
30. [docs/context/aris_real_token_usage_manual_evidence_runbook.md](../docs/context/aris_real_token_usage_manual_evidence_runbook.md) for the reusable manual evidence policy note
31. [docs/context/ctxe13_real_token_usage_baseline_manual_evidence_dry_run.md](../docs/context/ctxe13_real_token_usage_baseline_manual_evidence_dry_run.md) for the synthetic dry run report
32. [artifacts/context/ctxe13_real_token_usage_baseline_manual_evidence_dry_run_results.json](../artifacts/context/ctxe13_real_token_usage_baseline_manual_evidence_dry_run_results.json) for the dry-run validation results
33. [artifacts/context/ctxe13_real_token_usage_baseline_manual_evidence_dry_run_samples.json](../artifacts/context/ctxe13_real_token_usage_baseline_manual_evidence_dry_run_samples.json) for the synthetic sample set
34. [docs/context/ctxe14_real_token_usage_baseline_manual_evidence_collection_prep.md](../docs/context/ctxe14_real_token_usage_baseline_manual_evidence_collection_prep.md) for the evidence collection prep report
35. [docs/context/aris_real_token_usage_evidence_prep.md](../docs/context/aris_real_token_usage_evidence_prep.md) for the reusable evidence prep policy note
36. [artifacts/context/ctxe14_real_token_usage_baseline_manual_evidence_collection_prep_blank_sample_template.json](../artifacts/context/ctxe14_real_token_usage_baseline_manual_evidence_collection_prep_blank_sample_template.json) for the blank future evidence template
37. [artifacts/context/ctxe14_real_token_usage_baseline_manual_evidence_collection_prep_operator_checklist.json](../artifacts/context/ctxe14_real_token_usage_baseline_manual_evidence_collection_prep_operator_checklist.json) for the operator checklist
38. [artifacts/context/manual_token_usage_evidence/README.md](../artifacts/context/manual_token_usage_evidence/README.md) for the reserved future evidence directory
39. [docs/context/ctxe15_real_token_usage_baseline_manual_evidence_collection_readiness_review.md](../docs/context/ctxe15_real_token_usage_baseline_manual_evidence_collection_readiness_review.md) for the readiness review summary
40. [artifacts/context/ctxe15_real_token_usage_baseline_manual_evidence_collection_readiness_review_findings.json](../artifacts/context/ctxe15_real_token_usage_baseline_manual_evidence_collection_readiness_review_findings.json) for the readiness review findings
41. [docs/context/ctxe16_real_token_usage_baseline_manual_evidence_collection_authorization_gate.md](../docs/context/ctxe16_real_token_usage_baseline_manual_evidence_collection_authorization_gate.md) for the authorization gate summary
42. [artifacts/context/ctxe16_real_token_usage_baseline_manual_evidence_collection_authorization_gate_authorization.json](../artifacts/context/ctxe16_real_token_usage_baseline_manual_evidence_collection_authorization_gate_authorization.json) for the authorization payload
43. [artifacts/context/ctxe16_real_token_usage_baseline_manual_evidence_collection_authorization_gate_requirements.json](../artifacts/context/ctxe16_real_token_usage_baseline_manual_evidence_collection_authorization_gate_requirements.json) for the authorization requirements
44. [docs/context/ctxe17_real_token_usage_baseline_manual_evidence_intake_controlled_apply.md](../docs/context/ctxe17_real_token_usage_baseline_manual_evidence_intake_controlled_apply.md) for the manual evidence intake gate
45. [artifacts/context/ctxe17_real_token_usage_baseline_manual_evidence_intake_controlled_apply_decision.json](../artifacts/context/ctxe17_real_token_usage_baseline_manual_evidence_intake_controlled_apply_decision.json) for the intake decision
46. [artifacts/context/ctxe17_real_token_usage_baseline_manual_evidence_intake_controlled_apply_summary.json](../artifacts/context/ctxe17_real_token_usage_baseline_manual_evidence_intake_controlled_apply_summary.json) for the intake summary
47. [artifacts/context/ctxe17_real_token_usage_baseline_manual_evidence_intake_controlled_apply_intake_results.json](../artifacts/context/ctxe17_real_token_usage_baseline_manual_evidence_intake_controlled_apply_intake_results.json) for the intake results
48. [artifacts/context/ctxe17_real_token_usage_baseline_manual_evidence_intake_controlled_apply_requirements.json](../artifacts/context/ctxe17_real_token_usage_baseline_manual_evidence_intake_controlled_apply_requirements.json) for the intake requirements
49. [artifacts/context/ctxe17_real_token_usage_baseline_manual_evidence_intake_controlled_apply_pool_index.json](../artifacts/context/ctxe17_real_token_usage_baseline_manual_evidence_intake_controlled_apply_pool_index.json) for the future pool index
50. [artifacts/context/ctxe17_real_token_usage_baseline_manual_evidence_intake_controlled_apply_rejections.json](../artifacts/context/ctxe17_real_token_usage_baseline_manual_evidence_intake_controlled_apply_rejections.json) for the rejected evidence records
51. [docs/context/ctxe18_real_token_usage_baseline_manual_evidence_validation_review.md](../docs/context/ctxe18_real_token_usage_baseline_manual_evidence_validation_review.md) for the CTX-E18 validation review
52. [artifacts/context/ctxe18_real_token_usage_baseline_manual_evidence_validation_review_decision.json](../artifacts/context/ctxe18_real_token_usage_baseline_manual_evidence_validation_review_decision.json) for the CTX-E18 review decision
53. [artifacts/context/ctxe18_real_token_usage_baseline_manual_evidence_validation_review_summary.json](../artifacts/context/ctxe18_real_token_usage_baseline_manual_evidence_validation_review_summary.json) for the CTX-E18 review summary
54. [artifacts/context/ctxe18_real_token_usage_baseline_manual_evidence_validation_review_matrix.json](../artifacts/context/ctxe18_real_token_usage_baseline_manual_evidence_validation_review_matrix.json) for the CTX-E18 review matrix
55. [artifacts/context/ctxe18_real_token_usage_baseline_manual_evidence_validation_review_requirements.json](../artifacts/context/ctxe18_real_token_usage_baseline_manual_evidence_validation_review_requirements.json) for the CTX-E18 review requirements
56. [artifacts/context/ctxe18_real_token_usage_baseline_manual_evidence_validation_review_findings.json](../artifacts/context/ctxe18_real_token_usage_baseline_manual_evidence_validation_review_findings.json) for the CTX-E18 review findings
57. [docs/context/ctxe19_real_token_usage_baseline_manual_evidence_submission_window.md](../docs/context/ctxe19_real_token_usage_baseline_manual_evidence_submission_window.md) for the CTX-E19 submission window
58. [artifacts/context/ctxe19_real_token_usage_baseline_manual_evidence_submission_window_decision.json](../artifacts/context/ctxe19_real_token_usage_baseline_manual_evidence_submission_window_decision.json) for the CTX-E19 window decision
59. [artifacts/context/ctxe19_real_token_usage_baseline_manual_evidence_submission_window_summary.json](../artifacts/context/ctxe19_real_token_usage_baseline_manual_evidence_submission_window_summary.json) for the CTX-E19 window summary
60. [artifacts/context/ctxe19_real_token_usage_baseline_manual_evidence_submission_window_window.json](../artifacts/context/ctxe19_real_token_usage_baseline_manual_evidence_submission_window_window.json) for the CTX-E19 window artifact
61. [artifacts/context/ctxe19_real_token_usage_baseline_manual_evidence_submission_window_requirements.json](../artifacts/context/ctxe19_real_token_usage_baseline_manual_evidence_submission_window_requirements.json) for the CTX-E19 window requirements
62. [artifacts/context/ctxe19_real_token_usage_baseline_manual_evidence_submission_window_findings.json](../artifacts/context/ctxe19_real_token_usage_baseline_manual_evidence_submission_window_findings.json) for the CTX-E19 window findings
63. [docs/context/ctxe20_token_economy_track_closure_integration_readiness_gate.md](../docs/context/ctxe20_token_economy_track_closure_integration_readiness_gate.md) for the CTX-E20 closure gate
64. [docs/context/aris_token_economy_track_closure.md](../docs/context/aris_token_economy_track_closure.md) for the reusable token-economy track closure note
65. [artifacts/context/ctxe20_token_economy_track_closure_integration_readiness_gate_decision.json](../artifacts/context/ctxe20_token_economy_track_closure_integration_readiness_gate_decision.json) for the CTX-E20 closure decision
66. [artifacts/context/ctxe20_token_economy_track_closure_integration_readiness_gate_summary.json](../artifacts/context/ctxe20_token_economy_track_closure_integration_readiness_gate_summary.json) for the CTX-E20 closure summary
67. [artifacts/context/ctxe20_token_economy_track_closure_integration_readiness_gate_report.md](../artifacts/context/ctxe20_token_economy_track_closure_integration_readiness_gate_report.md) for the CTX-E20 closure report
68. [artifacts/context/ctxe20_token_economy_track_closure_integration_readiness_gate_readiness.json](../artifacts/context/ctxe20_token_economy_track_closure_integration_readiness_gate_readiness.json) for the CTX-E20 readiness artifact
69. [artifacts/context/ctxe20_token_economy_track_closure_integration_readiness_gate_requirements.json](../artifacts/context/ctxe20_token_economy_track_closure_integration_readiness_gate_requirements.json) for the CTX-E20 requirements
70. [artifacts/context/ctxe20_token_economy_track_closure_integration_readiness_gate_component_index.json](../artifacts/context/ctxe20_token_economy_track_closure_integration_readiness_gate_component_index.json) for the CTX-E20 component index
