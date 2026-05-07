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
10. [docs/fase31/f31e_source_of_truth_drift_repair_controlled_apply.md](../docs/fase31/f31e_source_of_truth_drift_repair_controlled_apply.md) for the F31.E controlled apply summary
11. [artifacts/f31/f31_source_of_truth_drift_repair_controlled_apply_decision.json](../artifacts/f31/f31_source_of_truth_drift_repair_controlled_apply_decision.json) for the F31.E apply decision
12. [artifacts/f31/f31_source_of_truth_drift_repair_controlled_apply_summary.json](../artifacts/f31/f31_source_of_truth_drift_repair_controlled_apply_summary.json) for the F31.E apply summary
13. [artifacts/f31/f31_source_of_truth_drift_repair_controlled_apply_diff_summary.json](../artifacts/f31/f31_source_of_truth_drift_repair_controlled_apply_diff_summary.json) for the F31.E apply diff summary
14. [artifacts/f31/f31_source_of_truth_drift_repair_controlled_apply_requirements.json](../artifacts/f31/f31_source_of_truth_drift_repair_controlled_apply_requirements.json) for the F31.E apply requirements
15. [ROADMAP_F30_F50.md](ROADMAP_F30_F50.md) for the formal post-V6 operational roadmap
16. [docs/fase32/f32a_context_boundary_trust_firewall_bootstrap_gate.md](../docs/fase32/f32a_context_boundary_trust_firewall_bootstrap_gate.md) for the F32.A bootstrap gate doc
17. [artifacts/f32/f32_context_boundary_trust_firewall_bootstrap_gate_decision.json](../artifacts/f32/f32_context_boundary_trust_firewall_bootstrap_gate_decision.json) for the F32.A decision
18. [artifacts/f32/f32_context_boundary_trust_firewall_bootstrap_gate_boundary_matrix.json](../artifacts/f32/f32_context_boundary_trust_firewall_bootstrap_gate_boundary_matrix.json) for the context boundary matrix
19. [artifacts/f32/f32_context_boundary_trust_firewall_bootstrap_gate_threat_model.json](../artifacts/f32/f32_context_boundary_trust_firewall_bootstrap_gate_threat_model.json) for the trust firewall threat model
20. [docs/fase32/f32b_context_boundary_trust_firewall_implementation_gate.md](../docs/fase32/f32b_context_boundary_trust_firewall_implementation_gate.md) for the F32.B implementation gate doc
21. [artifacts/f32/f32_context_boundary_trust_firewall_implementation_gate_decision.json](../artifacts/f32/f32_context_boundary_trust_firewall_implementation_gate_decision.json) for the F32.B decision
22. [artifacts/f32/f32_context_boundary_trust_firewall_implementation_gate_validation_matrix.json](../artifacts/f32/f32_context_boundary_trust_firewall_implementation_gate_validation_matrix.json) for the F32.B validation matrix
23. [artifacts/f32/f32_context_boundary_trust_firewall_implementation_gate_rule_results.json](../artifacts/f32/f32_context_boundary_trust_firewall_implementation_gate_rule_results.json) for the F32.B rule results
24. [docs/fase32/f32c_structured_obsidian_query_contract_gate.md](../docs/fase32/f32c_structured_obsidian_query_contract_gate.md) for the F32.C contract gate doc
25. [artifacts/f32/f32_structured_obsidian_query_contract_gate_contract.json](../artifacts/f32/f32_structured_obsidian_query_contract_gate_contract.json) for the F32.C structured query contract
26. [artifacts/f32/f32_structured_obsidian_query_contract_gate_decision.json](../artifacts/f32/f32_structured_obsidian_query_contract_gate_decision.json) for the F32.C decision
27. [artifacts/f32/f32_structured_obsidian_query_contract_gate_summary.json](../artifacts/f32/f32_structured_obsidian_query_contract_gate_summary.json) for the F32.C summary
28. [artifacts/f32/f32_structured_obsidian_query_contract_gate_validation_matrix.json](../artifacts/f32/f32_structured_obsidian_query_contract_gate_validation_matrix.json) for the F32.C validation matrix
29. [docs/fase32/f32d_structured_obsidian_query_contract_review_gate.md](../docs/fase32/f32d_structured_obsidian_query_contract_review_gate.md) for the F32.D review gate doc
30. [artifacts/f32/f32_structured_obsidian_query_contract_review_gate_decision.json](../artifacts/f32/f32_structured_obsidian_query_contract_review_gate_decision.json) for the F32.D decision
31. [artifacts/f32/f32_structured_obsidian_query_contract_review_gate_summary.json](../artifacts/f32/f32_structured_obsidian_query_contract_review_gate_summary.json) for the F32.D summary
32. [artifacts/f32/f32_structured_obsidian_query_contract_review_gate_review_matrix.json](../artifacts/f32/f32_structured_obsidian_query_contract_review_gate_review_matrix.json) for the F32.D review matrix
33. Obsidian only after the repair and only query-first
34. `archive/` only when history is needed
35. `Project_ARIS` artifacts/docs only when cited

- Do not bulk-read `archive/`.
- Do not bulk-read Obsidian.
- Do not rely on old memory against `CURRENT_STATE`.
- Do not advance phase without checking `NEXT_ACTION`.
- Do not declare token savings without evidence.
- Keep this repo compact.

36. [docs/fase32/f32e_future_mcp_readonly_candidate_contract_gate.md](../docs/fase32/f32e_future_mcp_readonly_candidate_contract_gate.md) for the F32.E candidate contract gate doc
37. [artifacts/f32/f32_future_mcp_readonly_candidate_contract_gate_contract.json](../artifacts/f32/f32_future_mcp_readonly_candidate_contract_gate_contract.json) for the F32.E candidate contract
38. [artifacts/f32/f32_future_mcp_readonly_candidate_contract_gate_decision.json](../artifacts/f32/f32_future_mcp_readonly_candidate_contract_gate_decision.json) for the F32.E decision
39. [artifacts/f32/f32_future_mcp_readonly_candidate_contract_gate_summary.json](../artifacts/f32/f32_future_mcp_readonly_candidate_contract_gate_summary.json) for the F32.E summary
40. [artifacts/f32/f32_future_mcp_readonly_candidate_contract_gate_validation_matrix.json](../artifacts/f32/f32_future_mcp_readonly_candidate_contract_gate_validation_matrix.json) for the F32.E validation matrix
41. [artifacts/f32/f32_future_mcp_readonly_candidate_contract_gate_requirements.json](../artifacts/f32/f32_future_mcp_readonly_candidate_contract_gate_requirements.json) for the F32.E requirements
42. `Project_ARIS` artifacts/docs only when cited

43. [docs/fase32/f32f_future_mcp_readonly_candidate_contract_review_gate.md](../docs/fase32/f32f_future_mcp_readonly_candidate_contract_review_gate.md) for the F32.F review gate doc
44. [artifacts/f32/f32_future_mcp_readonly_candidate_contract_review_gate_decision.json](../artifacts/f32/f32_future_mcp_readonly_candidate_contract_review_gate_decision.json) for the F32.F decision
45. [artifacts/f32/f32_future_mcp_readonly_candidate_contract_review_gate_summary.json](../artifacts/f32/f32_future_mcp_readonly_candidate_contract_review_gate_summary.json) for the F32.F summary
46. [artifacts/f32/f32_future_mcp_readonly_candidate_contract_review_gate_report.md](../artifacts/f32/f32_future_mcp_readonly_candidate_contract_review_gate_report.md) for the F32.F report
47. [artifacts/f32/f32_future_mcp_readonly_candidate_contract_review_gate_requirements.json](../artifacts/f32/f32_future_mcp_readonly_candidate_contract_review_gate_requirements.json) for the F32.F requirements
48. [artifacts/f32/f32_future_mcp_readonly_candidate_contract_review_gate_review_matrix.json](../artifacts/f32/f32_future_mcp_readonly_candidate_contract_review_gate_review_matrix.json) for the F32.F review matrix
49. `Project_ARIS` artifacts/docs only when cited

50. [docs/fase32/f32g_future_mcp_readonly_implementation_plan_gate.md](../docs/fase32/f32g_future_mcp_readonly_implementation_plan_gate.md) for the F32.G plan gate doc
51. [artifacts/f32/f32_future_mcp_readonly_implementation_plan_gate_decision.json](../artifacts/f32/f32_future_mcp_readonly_implementation_plan_gate_decision.json) for the F32.G decision
52. [artifacts/f32/f32_future_mcp_readonly_implementation_plan_gate_summary.json](../artifacts/f32/f32_future_mcp_readonly_implementation_plan_gate_summary.json) for the F32.G summary
53. [artifacts/f32/f32_future_mcp_readonly_implementation_plan_gate_report.md](../artifacts/f32/f32_future_mcp_readonly_implementation_plan_gate_report.md) for the F32.G report
54. [artifacts/f32/f32_future_mcp_readonly_implementation_plan_gate_requirements.json](../artifacts/f32/f32_future_mcp_readonly_implementation_plan_gate_requirements.json) for the F32.G requirements
55. [artifacts/f32/f32_future_mcp_readonly_implementation_plan_gate_plan.json](../artifacts/f32/f32_future_mcp_readonly_implementation_plan_gate_plan.json) for the F32.G plan
56. [artifacts/f32/f32_future_mcp_readonly_implementation_plan_gate_validation_matrix.json](../artifacts/f32/f32_future_mcp_readonly_implementation_plan_gate_validation_matrix.json) for the F32.G validation matrix
57. `Project_ARIS` artifacts/docs only when cited

58. [docs/fase32/f32h_future_mcp_readonly_implementation_plan_review_gate.md](../docs/fase32/f32h_future_mcp_readonly_implementation_plan_review_gate.md) for the F32.H review gate doc
59. [artifacts/f32/f32_future_mcp_readonly_implementation_plan_review_gate_decision.json](../artifacts/f32/f32_future_mcp_readonly_implementation_plan_review_gate_decision.json) for the F32.H decision
60. [artifacts/f32/f32_future_mcp_readonly_implementation_plan_review_gate_summary.json](../artifacts/f32/f32_future_mcp_readonly_implementation_plan_review_gate_summary.json) for the F32.H summary
61. [artifacts/f32/f32_future_mcp_readonly_implementation_plan_review_gate_report.md](../artifacts/f32/f32_future_mcp_readonly_implementation_plan_review_gate_report.md) for the F32.H report
62. [artifacts/f32/f32_future_mcp_readonly_implementation_plan_review_gate_requirements.json](../artifacts/f32/f32_future_mcp_readonly_implementation_plan_review_gate_requirements.json) for the F32.H requirements
63. [artifacts/f32/f32_future_mcp_readonly_implementation_plan_review_gate_review_matrix.json](../artifacts/f32/f32_future_mcp_readonly_implementation_plan_review_gate_review_matrix.json) for the F32.H review matrix
64. `Project_ARIS` artifacts/docs only when cited

65. [docs/fase32/f32i_future_mcp_readonly_dry_run_gate.md](../docs/fase32/f32i_future_mcp_readonly_dry_run_gate.md) for the F32.I dry-run gate doc
66. [artifacts/f32/f32_future_mcp_readonly_dry_run_gate_decision.json](../artifacts/f32/f32_future_mcp_readonly_dry_run_gate_decision.json) for the F32.I decision
67. [artifacts/f32/f32_future_mcp_readonly_dry_run_gate_summary.json](../artifacts/f32/f32_future_mcp_readonly_dry_run_gate_summary.json) for the F32.I summary
68. [artifacts/f32/f32_future_mcp_readonly_dry_run_gate_report.md](../artifacts/f32/f32_future_mcp_readonly_dry_run_gate_report.md) for the F32.I report
69. [artifacts/f32/f32_future_mcp_readonly_dry_run_gate_requirements.json](../artifacts/f32/f32_future_mcp_readonly_dry_run_gate_requirements.json) for the F32.I requirements
70. [artifacts/f32/f32_future_mcp_readonly_dry_run_gate_dry_run_results.json](../artifacts/f32/f32_future_mcp_readonly_dry_run_gate_dry_run_results.json) for the F32.I dry-run results
71. [artifacts/f32/f32_future_mcp_readonly_dry_run_gate_validation_matrix.json](../artifacts/f32/f32_future_mcp_readonly_dry_run_gate_validation_matrix.json) for the F32.I validation matrix

72. [docs/fase32/f32j_future_mcp_readonly_dry_run_review_gate.md](../docs/fase32/f32j_future_mcp_readonly_dry_run_review_gate.md) for the F32.J review gate doc
73. [artifacts/f32/f32_future_mcp_readonly_dry_run_review_gate_decision.json](../artifacts/f32/f32_future_mcp_readonly_dry_run_review_gate_decision.json) for the F32.J decision
74. [artifacts/f32/f32_future_mcp_readonly_dry_run_review_gate_summary.json](../artifacts/f32/f32_future_mcp_readonly_dry_run_review_gate_summary.json) for the F32.J summary
75. [artifacts/f32/f32_future_mcp_readonly_dry_run_review_gate_report.md](../artifacts/f32/f32_future_mcp_readonly_dry_run_review_gate_report.md) for the F32.J report
76. [artifacts/f32/f32_future_mcp_readonly_dry_run_review_gate_requirements.json](../artifacts/f32/f32_future_mcp_readonly_dry_run_review_gate_requirements.json) for the F32.J requirements
77. [artifacts/f32/f32_future_mcp_readonly_dry_run_review_gate_review_matrix.json](../artifacts/f32/f32_future_mcp_readonly_dry_run_review_gate_review_matrix.json) for the F32.J review matrix

78. [docs/fase32/f32k_future_mcp_readonly_security_review_gate.md](../docs/fase32/f32k_future_mcp_readonly_security_review_gate.md) for the F32.K security review gate doc
79. [artifacts/f32/f32_future_mcp_readonly_security_review_gate_decision.json](../artifacts/f32/f32_future_mcp_readonly_security_review_gate_decision.json) for the F32.K decision
80. [artifacts/f32/f32_future_mcp_readonly_security_review_gate_summary.json](../artifacts/f32/f32_future_mcp_readonly_security_review_gate_summary.json) for the F32.K summary
81. [artifacts/f32/f32_future_mcp_readonly_security_review_gate_report.md](../artifacts/f32/f32_future_mcp_readonly_security_review_gate_report.md) for the F32.K report
82. [artifacts/f32/f32_future_mcp_readonly_security_review_gate_security_matrix.json](../artifacts/f32/f32_future_mcp_readonly_security_review_gate_security_matrix.json) for the F32.K security matrix

83. [docs/fase32/f32l_future_mcp_readonly_provenance_gate.md](../docs/fase32/f32l_future_mcp_readonly_provenance_gate.md) for the F32.L provenance gate doc
84. [artifacts/f32/f32_future_mcp_readonly_provenance_gate_decision.json](../artifacts/f32/f32_future_mcp_readonly_provenance_gate_decision.json) for the F32.L decision
85. [artifacts/f32/f32_future_mcp_readonly_provenance_gate_summary.json](../artifacts/f32/f32_future_mcp_readonly_provenance_gate_summary.json) for the F32.L summary
86. [artifacts/f32/f32_future_mcp_readonly_provenance_gate_report.md](../artifacts/f32/f32_future_mcp_readonly_provenance_gate_report.md) for the F32.L report
87. [artifacts/f32/f32_future_mcp_readonly_provenance_gate_provenance_contract.json](../artifacts/f32/f32_future_mcp_readonly_provenance_gate_provenance_contract.json) for the F32.L provenance contract
88. [artifacts/f32/f32_future_mcp_readonly_provenance_gate_validation_matrix.json](../artifacts/f32/f32_future_mcp_readonly_provenance_gate_validation_matrix.json) for the F32.L validation matrix
