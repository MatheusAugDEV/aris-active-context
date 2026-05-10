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

89. [docs/fase32/f32m_future_mcp_readonly_disable_rollback_rehearsal_gate.md](../docs/fase32/f32m_future_mcp_readonly_disable_rollback_rehearsal_gate.md) for the F32.M disable/rollback rehearsal gate doc
90. [artifacts/f32/f32_future_mcp_readonly_disable_rollback_rehearsal_gate_decision.json](../artifacts/f32/f32_future_mcp_readonly_disable_rollback_rehearsal_gate_decision.json) for the F32.M decision
91. [artifacts/f32/f32_future_mcp_readonly_disable_rollback_rehearsal_gate_summary.json](../artifacts/f32/f32_future_mcp_readonly_disable_rollback_rehearsal_gate_summary.json) for the F32.M summary
92. [artifacts/f32/f32_future_mcp_readonly_disable_rollback_rehearsal_gate_report.md](../artifacts/f32/f32_future_mcp_readonly_disable_rollback_rehearsal_gate_report.md) for the F32.M report
93. [artifacts/f32/f32_future_mcp_readonly_disable_rollback_rehearsal_gate_disable_plan.json](../artifacts/f32/f32_future_mcp_readonly_disable_rollback_rehearsal_gate_disable_plan.json) for the F32.M disable plan
94. [artifacts/f32/f32_future_mcp_readonly_disable_rollback_rehearsal_gate_rollback_plan.json](../artifacts/f32/f32_future_mcp_readonly_disable_rollback_rehearsal_gate_rollback_plan.json) for the F32.M rollback plan
95. [artifacts/f32/f32_future_mcp_readonly_disable_rollback_rehearsal_gate_rehearsal_matrix.json](../artifacts/f32/f32_future_mcp_readonly_disable_rollback_rehearsal_gate_rehearsal_matrix.json) for the F32.M rehearsal matrix

96. [docs/fase32/f32n_future_mcp_readonly_reenable_preconditions_gate.md](../docs/fase32/f32n_future_mcp_readonly_reenable_preconditions_gate.md) for the F32.N re-enable preconditions gate doc
97. [artifacts/f32/f32_future_mcp_readonly_reenable_preconditions_gate_decision.json](../artifacts/f32/f32_future_mcp_readonly_reenable_preconditions_gate_decision.json) for the F32.N decision
98. [artifacts/f32/f32_future_mcp_readonly_reenable_preconditions_gate_summary.json](../artifacts/f32/f32_future_mcp_readonly_reenable_preconditions_gate_summary.json) for the F32.N summary
99. [artifacts/f32/f32_future_mcp_readonly_reenable_preconditions_gate_report.md](../artifacts/f32/f32_future_mcp_readonly_reenable_preconditions_gate_report.md) for the F32.N report
100. [artifacts/f32/f32_future_mcp_readonly_reenable_preconditions_gate_requirements.json](../artifacts/f32/f32_future_mcp_readonly_reenable_preconditions_gate_requirements.json) for the F32.N requirements
101. [artifacts/f32/f32_future_mcp_readonly_reenable_preconditions_gate_preconditions.json](../artifacts/f32/f32_future_mcp_readonly_reenable_preconditions_gate_preconditions.json) for the F32.N preconditions contract
102. [artifacts/f32/f32_future_mcp_readonly_reenable_preconditions_gate_validation_matrix.json](../artifacts/f32/f32_future_mcp_readonly_reenable_preconditions_gate_validation_matrix.json) for the F32.N validation matrix

103. [docs/fase32/f32o_future_mcp_readonly_final_readiness_consolidation_gate.md](../docs/fase32/f32o_future_mcp_readonly_final_readiness_consolidation_gate.md) for the F32.O final readiness consolidation gate doc
104. [artifacts/f32/f32_future_mcp_readonly_final_readiness_consolidation_gate_decision.json](../artifacts/f32/f32_future_mcp_readonly_final_readiness_consolidation_gate_decision.json) for the F32.O decision
105. [artifacts/f32/f32_future_mcp_readonly_final_readiness_consolidation_gate_summary.json](../artifacts/f32/f32_future_mcp_readonly_final_readiness_consolidation_gate_summary.json) for the F32.O summary
106. [artifacts/f32/f32_future_mcp_readonly_final_readiness_consolidation_gate_report.md](../artifacts/f32/f32_future_mcp_readonly_final_readiness_consolidation_gate_report.md) for the F32.O report
107. [artifacts/f32/f32_future_mcp_readonly_final_readiness_consolidation_gate_requirements.json](../artifacts/f32/f32_future_mcp_readonly_final_readiness_consolidation_gate_requirements.json) for the F32.O requirements
108. [artifacts/f32/f32_future_mcp_readonly_final_readiness_consolidation_gate_evidence_map.json](../artifacts/f32/f32_future_mcp_readonly_final_readiness_consolidation_gate_evidence_map.json) for the F32.O evidence map
109. [artifacts/f32/f32_future_mcp_readonly_final_readiness_consolidation_gate_readiness_matrix.json](../artifacts/f32/f32_future_mcp_readonly_final_readiness_consolidation_gate_readiness_matrix.json) for the F32.O readiness matrix
110. [artifacts/f32/f32_future_mcp_readonly_final_readiness_consolidation_gate_next_phase_contract.json](../artifacts/f32/f32_future_mcp_readonly_final_readiness_consolidation_gate_next_phase_contract.json) for the F32.O next phase contract

111. [docs/fase32/f32p_future_mcp_readonly_configuration_candidate_gate.md](../docs/fase32/f32p_future_mcp_readonly_configuration_candidate_gate.md) for the F32.P configuration candidate gate doc
112. [artifacts/f32/f32_future_mcp_readonly_configuration_candidate_gate_decision.json](../artifacts/f32/f32_future_mcp_readonly_configuration_candidate_gate_decision.json) for the F32.P decision
113. [artifacts/f32/f32_future_mcp_readonly_configuration_candidate_gate_summary.json](../artifacts/f32/f32_future_mcp_readonly_configuration_candidate_gate_summary.json) for the F32.P summary
114. [artifacts/f32/f32_future_mcp_readonly_configuration_candidate_gate_report.md](../artifacts/f32/f32_future_mcp_readonly_configuration_candidate_gate_report.md) for the F32.P report
115. [artifacts/f32/f32_future_mcp_readonly_configuration_candidate_gate_requirements.json](../artifacts/f32/f32_future_mcp_readonly_configuration_candidate_gate_requirements.json) for the F32.P requirements
116. [artifacts/f32/f32_future_mcp_readonly_configuration_candidate_gate_candidate_config.json](../artifacts/f32/f32_future_mcp_readonly_configuration_candidate_gate_candidate_config.json) for the F32.P candidate config
117. [artifacts/f32/f32_future_mcp_readonly_configuration_candidate_gate_validation_matrix.json](../artifacts/f32/f32_future_mcp_readonly_configuration_candidate_gate_validation_matrix.json) for the F32.P validation matrix
118. [artifacts/f32/f32_future_mcp_readonly_configuration_candidate_gate_safety_matrix.json](../artifacts/f32/f32_future_mcp_readonly_configuration_candidate_gate_safety_matrix.json) for the F32.P safety matrix

119. [docs/fase32/f32q_future_mcp_readonly_configuration_candidate_review_gate.md](../docs/fase32/f32q_future_mcp_readonly_configuration_candidate_review_gate.md) for the F32.Q configuration candidate review gate doc
120. [artifacts/f32/f32_future_mcp_readonly_configuration_candidate_review_gate_decision.json](../artifacts/f32/f32_future_mcp_readonly_configuration_candidate_review_gate_decision.json) for the F32.Q decision
121. [artifacts/f32/f32_future_mcp_readonly_configuration_candidate_review_gate_summary.json](../artifacts/f32/f32_future_mcp_readonly_configuration_candidate_review_gate_summary.json) for the F32.Q summary
122. [artifacts/f32/f32_future_mcp_readonly_configuration_candidate_review_gate_report.md](../artifacts/f32/f32_future_mcp_readonly_configuration_candidate_review_gate_report.md) for the F32.Q report
123. [artifacts/f32/f32_future_mcp_readonly_configuration_candidate_review_gate_requirements.json](../artifacts/f32/f32_future_mcp_readonly_configuration_candidate_review_gate_requirements.json) for the F32.Q requirements
124. [artifacts/f32/f32_future_mcp_readonly_configuration_candidate_review_gate_review_matrix.json](../artifacts/f32/f32_future_mcp_readonly_configuration_candidate_review_gate_review_matrix.json) for the F32.Q review matrix
125. [artifacts/f32/f32_future_mcp_readonly_configuration_candidate_review_gate_risk_matrix.json](../artifacts/f32/f32_future_mcp_readonly_configuration_candidate_review_gate_risk_matrix.json) for the F32.Q risk matrix
126. [artifacts/f32/f32_future_mcp_readonly_configuration_candidate_review_gate_next_phase_contract.json](../artifacts/f32/f32_future_mcp_readonly_configuration_candidate_review_gate_next_phase_contract.json) for the F32.Q next phase contract

127. [docs/fase32/f32r_future_mcp_readonly_configuration_planning_gate.md](../docs/fase32/f32r_future_mcp_readonly_configuration_planning_gate.md) for the F32.R configuration planning gate doc
128. [artifacts/f32/f32_future_mcp_readonly_configuration_planning_gate_decision.json](../artifacts/f32/f32_future_mcp_readonly_configuration_planning_gate_decision.json) for the F32.R decision
129. [artifacts/f32/f32_future_mcp_readonly_configuration_planning_gate_summary.json](../artifacts/f32/f32_future_mcp_readonly_configuration_planning_gate_summary.json) for the F32.R summary
130. [artifacts/f32/f32_future_mcp_readonly_configuration_planning_gate_report.md](../artifacts/f32/f32_future_mcp_readonly_configuration_planning_gate_report.md) for the F32.R report
131. [artifacts/f32/f32_future_mcp_readonly_configuration_planning_gate_requirements.json](../artifacts/f32/f32_future_mcp_readonly_configuration_planning_gate_requirements.json) for the F32.R requirements
132. [artifacts/f32/f32_future_mcp_readonly_configuration_planning_gate_configuration_plan.json](../artifacts/f32/f32_future_mcp_readonly_configuration_planning_gate_configuration_plan.json) for the F32.R configuration plan
133. [artifacts/f32/f32_future_mcp_readonly_configuration_planning_gate_planning_matrix.json](../artifacts/f32/f32_future_mcp_readonly_configuration_planning_gate_planning_matrix.json) for the F32.R planning matrix
134. [artifacts/f32/f32_future_mcp_readonly_configuration_planning_gate_safety_matrix.json](../artifacts/f32/f32_future_mcp_readonly_configuration_planning_gate_safety_matrix.json) for the F32.R safety matrix

135. [docs/fase32/f32s_future_mcp_readonly_configuration_planning_review_gate.md](../docs/fase32/f32s_future_mcp_readonly_configuration_planning_review_gate.md) for the F32.S configuration planning review gate doc
136. [artifacts/f32/f32_future_mcp_readonly_configuration_planning_review_gate_decision.json](../artifacts/f32/f32_future_mcp_readonly_configuration_planning_review_gate_decision.json) for the F32.S decision
137. [artifacts/f32/f32_future_mcp_readonly_configuration_planning_review_gate_summary.json](../artifacts/f32/f32_future_mcp_readonly_configuration_planning_review_gate_summary.json) for the F32.S summary
138. [artifacts/f32/f32_future_mcp_readonly_configuration_planning_review_gate_report.md](../artifacts/f32/f32_future_mcp_readonly_configuration_planning_review_gate_report.md) for the F32.S report
139. [artifacts/f32/f32_future_mcp_readonly_configuration_planning_review_gate_requirements.json](../artifacts/f32/f32_future_mcp_readonly_configuration_planning_review_gate_requirements.json) for the F32.S requirements
140. [artifacts/f32/f32_future_mcp_readonly_configuration_planning_review_gate_review_matrix.json](../artifacts/f32/f32_future_mcp_readonly_configuration_planning_review_gate_review_matrix.json) for the F32.S review matrix
141. [artifacts/f32/f32_future_mcp_readonly_configuration_planning_review_gate_risk_matrix.json](../artifacts/f32/f32_future_mcp_readonly_configuration_planning_review_gate_risk_matrix.json) for the F32.S risk matrix
142. [artifacts/f32/f32_future_mcp_readonly_configuration_planning_review_gate_next_phase_contract.json](../artifacts/f32/f32_future_mcp_readonly_configuration_planning_review_gate_next_phase_contract.json) for the F32.S next phase contract

143. [docs/fase32/f32t_future_mcp_readonly_configuration_apply_dry_run_plan_gate.md](../docs/fase32/f32t_future_mcp_readonly_configuration_apply_dry_run_plan_gate.md) for the F32.T apply dry-run plan gate doc
144. [artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_plan_gate_decision.json](../artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_plan_gate_decision.json) for the F32.T decision
145. [artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_plan_gate_summary.json](../artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_plan_gate_summary.json) for the F32.T summary
146. [artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_plan_gate_report.md](../artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_plan_gate_report.md) for the F32.T report
147. [artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_plan_gate_requirements.json](../artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_plan_gate_requirements.json) for the F32.T requirements
148. [artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_plan_gate_apply_dry_run_plan.json](../artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_plan_gate_apply_dry_run_plan.json) for the F32.T apply dry-run plan
149. [artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_plan_gate_dry_run_matrix.json](../artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_plan_gate_dry_run_matrix.json) for the F32.T dry-run matrix
150. [artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_plan_gate_safety_matrix.json](../artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_plan_gate_safety_matrix.json) for the F32.T safety matrix
151. [artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_plan_gate_next_phase_contract.json](../artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_plan_gate_next_phase_contract.json) for the F32.T next phase contract

152. [docs/fase32/f32u_future_mcp_readonly_configuration_apply_dry_run_plan_review_gate.md](../docs/fase32/f32u_future_mcp_readonly_configuration_apply_dry_run_plan_review_gate.md) for the F32.U apply dry-run plan review gate doc
153. [artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_plan_review_gate_decision.json](../artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_plan_review_gate_decision.json) for the F32.U decision
154. [artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_plan_review_gate_summary.json](../artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_plan_review_gate_summary.json) for the F32.U summary
155. [artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_plan_review_gate_report.md](../artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_plan_review_gate_report.md) for the F32.U report
156. [artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_plan_review_gate_requirements.json](../artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_plan_review_gate_requirements.json) for the F32.U requirements
157. [artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_plan_review_gate_review_matrix.json](../artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_plan_review_gate_review_matrix.json) for the F32.U review matrix
158. [artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_plan_review_gate_risk_matrix.json](../artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_plan_review_gate_risk_matrix.json) for the F32.U risk matrix
159. [artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_plan_review_gate_next_phase_contract.json](../artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_plan_review_gate_next_phase_contract.json) for the F32.U next phase contract
160. [docs/fase32/f32v_future_mcp_readonly_configuration_apply_dry_run_execution_plan_gate.md](../docs/fase32/f32v_future_mcp_readonly_configuration_apply_dry_run_execution_plan_gate.md) for the F32.V execution plan gate doc
161. [artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_execution_plan_gate_decision.json](../artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_execution_plan_gate_decision.json) for the F32.V decision
162. [artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_execution_plan_gate_summary.json](../artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_execution_plan_gate_summary.json) for the F32.V summary
163. [artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_execution_plan_gate_report.md](../artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_execution_plan_gate_report.md) for the F32.V report
164. [artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_execution_plan_gate_requirements.json](../artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_execution_plan_gate_requirements.json) for the F32.V requirements
165. [artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_execution_plan_gate_execution_plan.json](../artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_execution_plan_gate_execution_plan.json) for the F32.V execution plan
166. [artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_execution_plan_gate_execution_matrix.json](../artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_execution_plan_gate_execution_matrix.json) for the F32.V execution matrix
167. [artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_execution_plan_gate_safety_matrix.json](../artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_execution_plan_gate_safety_matrix.json) for the F32.V safety matrix
168. [artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_execution_plan_gate_next_phase_contract.json](../artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_execution_plan_gate_next_phase_contract.json) for the F32.V next phase contract

169. [docs/fase32/f32w_future_mcp_readonly_configuration_apply_dry_run_execution_plan_review_gate.md](../docs/fase32/f32w_future_mcp_readonly_configuration_apply_dry_run_execution_plan_review_gate.md) for the F32.W execution plan review gate doc
170. [artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_execution_plan_review_gate_decision.json](../artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_execution_plan_review_gate_decision.json) for the F32.W decision
171. [artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_execution_plan_review_gate_summary.json](../artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_execution_plan_review_gate_summary.json) for the F32.W summary
172. [artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_execution_plan_review_gate_report.md](../artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_execution_plan_review_gate_report.md) for the F32.W report
173. [artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_execution_plan_review_gate_requirements.json](../artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_execution_plan_review_gate_requirements.json) for the F32.W requirements
174. [artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_execution_plan_review_gate_review_matrix.json](../artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_execution_plan_review_gate_review_matrix.json) for the F32.W review matrix
175. [artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_execution_plan_review_gate_risk_matrix.json](../artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_execution_plan_review_gate_risk_matrix.json) for the F32.W risk matrix
176. [artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_execution_plan_review_gate_next_phase_contract.json](../artifacts/f32/f32_future_mcp_readonly_configuration_apply_dry_run_execution_plan_review_gate_next_phase_contract.json) for the F32.W next phase contract

177. [docs/fase32/f32x_future_mcp_readonly_configuration_dry_run_execution_authorization_gate.md](../docs/fase32/f32x_future_mcp_readonly_configuration_dry_run_execution_authorization_gate.md) for the F32.X dry-run execution authorization gate doc
178. [artifacts/f32/f32_future_mcp_readonly_configuration_dry_run_execution_authorization_gate_decision.json](../artifacts/f32/f32_future_mcp_readonly_configuration_dry_run_execution_authorization_gate_decision.json) for the F32.X decision
179. [artifacts/f32/f32_future_mcp_readonly_configuration_dry_run_execution_authorization_gate_summary.json](../artifacts/f32/f32_future_mcp_readonly_configuration_dry_run_execution_authorization_gate_summary.json) for the F32.X summary
180. [artifacts/f32/f32_future_mcp_readonly_configuration_dry_run_execution_authorization_gate_report.md](../artifacts/f32/f32_future_mcp_readonly_configuration_dry_run_execution_authorization_gate_report.md) for the F32.X report
181. [artifacts/f32/f32_future_mcp_readonly_configuration_dry_run_execution_authorization_gate_requirements.json](../artifacts/f32/f32_future_mcp_readonly_configuration_dry_run_execution_authorization_gate_requirements.json) for the F32.X requirements
182. [artifacts/f32/f32_future_mcp_readonly_configuration_dry_run_execution_authorization_gate_authorization_contract.json](../artifacts/f32/f32_future_mcp_readonly_configuration_dry_run_execution_authorization_gate_authorization_contract.json) for the F32.X authorization contract
183. [artifacts/f32/f32_future_mcp_readonly_configuration_dry_run_execution_authorization_gate_authorization_matrix.json](../artifacts/f32/f32_future_mcp_readonly_configuration_dry_run_execution_authorization_gate_authorization_matrix.json) for the F32.X authorization matrix
184. [artifacts/f32/f32_future_mcp_readonly_configuration_dry_run_execution_authorization_gate_safety_matrix.json](../artifacts/f32/f32_future_mcp_readonly_configuration_dry_run_execution_authorization_gate_safety_matrix.json) for the F32.X safety matrix
185. [artifacts/f32/f32_future_mcp_readonly_configuration_dry_run_execution_authorization_gate_next_phase_contract.json](../artifacts/f32/f32_future_mcp_readonly_configuration_dry_run_execution_authorization_gate_next_phase_contract.json) for the F32.X next phase contract
186. [docs/reference/brand_identity_meaning.md](../docs/reference/brand_identity_meaning.md) for the ARIS brand identity meaning reference

187. [docs/fase32/f32y_future_mcp_readonly_configuration_dry_run_execution_authorization_review_gate.md](../docs/fase32/f32y_future_mcp_readonly_configuration_dry_run_execution_authorization_review_gate.md) for the F32.Y authorization review gate doc
188. [artifacts/f32/f32_future_mcp_readonly_configuration_dry_run_execution_authorization_review_gate_decision.json](../artifacts/f32/f32_future_mcp_readonly_configuration_dry_run_execution_authorization_review_gate_decision.json) for the F32.Y decision
189. [artifacts/f32/f32_future_mcp_readonly_configuration_dry_run_execution_authorization_review_gate_summary.json](../artifacts/f32/f32_future_mcp_readonly_configuration_dry_run_execution_authorization_review_gate_summary.json) for the F32.Y summary
190. [artifacts/f32/f32_future_mcp_readonly_configuration_dry_run_execution_authorization_review_gate_report.md](../artifacts/f32/f32_future_mcp_readonly_configuration_dry_run_execution_authorization_review_gate_report.md) for the F32.Y report
191. [artifacts/f32/f32_future_mcp_readonly_configuration_dry_run_execution_authorization_review_gate_requirements.json](../artifacts/f32/f32_future_mcp_readonly_configuration_dry_run_execution_authorization_review_gate_requirements.json) for the F32.Y requirements
192. [artifacts/f32/f32_future_mcp_readonly_configuration_dry_run_execution_authorization_review_gate_review_matrix.json](../artifacts/f32/f32_future_mcp_readonly_configuration_dry_run_execution_authorization_review_gate_review_matrix.json) for the F32.Y review matrix
193. [artifacts/f32/f32_future_mcp_readonly_configuration_dry_run_execution_authorization_review_gate_safety_matrix.json](../artifacts/f32/f32_future_mcp_readonly_configuration_dry_run_execution_authorization_review_gate_safety_matrix.json) for the F32.Y safety matrix
194. [artifacts/f32/f32_future_mcp_readonly_configuration_dry_run_execution_authorization_review_gate_next_phase_contract.json](../artifacts/f32/f32_future_mcp_readonly_configuration_dry_run_execution_authorization_review_gate_next_phase_contract.json) for the F32.Y next phase contract

195. [docs/fase32/f32z_future_mcp_readonly_configuration_controlled_dry_run_execution_gate.md](../docs/fase32/f32z_future_mcp_readonly_configuration_controlled_dry_run_execution_gate.md) for the F32.Z controlled dry-run execution doc
196. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_dry_run_execution_decision.json](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_dry_run_execution_decision.json) for the F32.Z decision
197. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_dry_run_execution_summary.json](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_dry_run_execution_summary.json) for the F32.Z summary
198. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_dry_run_execution_report.md](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_dry_run_execution_report.md) for the F32.Z report
199. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_dry_run_execution_simulated_config.json](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_dry_run_execution_simulated_config.json) for the F32.Z simulated config
200. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_dry_run_execution_execution_matrix.json](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_dry_run_execution_execution_matrix.json) for the F32.Z execution matrix
201. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_dry_run_execution_safety_matrix.json](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_dry_run_execution_safety_matrix.json) for the F32.Z safety matrix
202. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_dry_run_execution_noop_proof.json](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_dry_run_execution_noop_proof.json) for the F32.Z noop proof
203. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_dry_run_execution_next_phase_contract.json](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_dry_run_execution_next_phase_contract.json) for the F32.Z next phase contract
204. [docs/fase32/f32z1_future_mcp_readonly_configuration_controlled_dry_run_execution_review_gate.md](../docs/fase32/f32z1_future_mcp_readonly_configuration_controlled_dry_run_execution_review_gate.md) for the F32.Z1 controlled dry-run execution review gate doc
205. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_dry_run_execution_review_gate_decision.json](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_dry_run_execution_review_gate_decision.json) for the F32.Z1 decision
206. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_dry_run_execution_review_gate_summary.json](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_dry_run_execution_review_gate_summary.json) for the F32.Z1 summary
207. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_dry_run_execution_review_gate_report.md](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_dry_run_execution_review_gate_report.md) for the F32.Z1 report
208. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_dry_run_execution_review_gate_review_matrix.json](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_dry_run_execution_review_gate_review_matrix.json) for the F32.Z1 review matrix
209. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_dry_run_execution_review_gate_safety_matrix.json](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_dry_run_execution_review_gate_safety_matrix.json) for the F32.Z1 safety matrix
210. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_dry_run_execution_review_gate_noop_review.json](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_dry_run_execution_review_gate_noop_review.json) for the F32.Z1 noop review
211. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_dry_run_execution_review_gate_next_phase_contract.json](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_dry_run_execution_review_gate_next_phase_contract.json) for the F32.Z1 next phase contract

212. [docs/fase32/f32z2_future_mcp_readonly_configuration_controlled_apply_preparation_plan.md](../docs/fase32/f32z2_future_mcp_readonly_configuration_controlled_apply_preparation_plan.md) for the F32.Z2 apply-preparation plan doc
213. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_preparation_plan_decision.json](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_preparation_plan_decision.json) for the F32.Z2 decision
214. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_preparation_plan_summary.json](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_preparation_plan_summary.json) for the F32.Z2 summary
215. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_preparation_plan_report.md](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_preparation_plan_report.md) for the F32.Z2 report
216. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_preparation_plan_preconditions.json](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_preparation_plan_preconditions.json) for the F32.Z2 preconditions
217. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_preparation_plan_human_checklist.json](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_preparation_plan_human_checklist.json) for the F32.Z2 human checklist
218. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_preparation_plan_technical_checklist.json](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_preparation_plan_technical_checklist.json) for the F32.Z2 technical checklist
219. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_preparation_plan_permission_matrix.json](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_preparation_plan_permission_matrix.json) for the F32.Z2 permission matrix
220. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_preparation_plan_rollback_plan.json](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_preparation_plan_rollback_plan.json) for the F32.Z2 rollback plan
221. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_preparation_plan_audit_ledger_plan.json](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_preparation_plan_audit_ledger_plan.json) for the F32.Z2 audit ledger plan
222. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_preparation_plan_failure_modes.json](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_preparation_plan_failure_modes.json) for the F32.Z2 failure modes
223. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_preparation_plan_next_phase_contract.json](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_preparation_plan_next_phase_contract.json) for the F32.Z2 next phase contract

224. [docs/fase32/f32z3_future_mcp_readonly_configuration_controlled_apply_preparation_plan_review_gate.md](../docs/fase32/f32z3_future_mcp_readonly_configuration_controlled_apply_preparation_plan_review_gate.md) for the F32.Z3 apply-preparation plan review gate doc
225. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_preparation_plan_review_gate_decision.json](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_preparation_plan_review_gate_decision.json) for the F32.Z3 decision
226. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_preparation_plan_review_gate_summary.json](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_preparation_plan_review_gate_summary.json) for the F32.Z3 summary
227. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_preparation_plan_review_gate_report.md](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_preparation_plan_review_gate_report.md) for the F32.Z3 report
228. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_preparation_plan_review_gate_review_matrix.json](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_preparation_plan_review_gate_review_matrix.json) for the F32.Z3 review matrix
229. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_preparation_plan_review_gate_human_checklist_review.json](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_preparation_plan_review_gate_human_checklist_review.json) for the F32.Z3 human checklist review
230. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_preparation_plan_review_gate_technical_checklist_review.json](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_preparation_plan_review_gate_technical_checklist_review.json) for the F32.Z3 technical checklist review
231. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_preparation_plan_review_gate_permission_matrix_review.json](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_preparation_plan_review_gate_permission_matrix_review.json) for the F32.Z3 permission matrix review
232. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_preparation_plan_review_gate_rollback_review.json](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_preparation_plan_review_gate_rollback_review.json) for the F32.Z3 rollback review
233. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_preparation_plan_review_gate_audit_ledger_review.json](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_preparation_plan_review_gate_audit_ledger_review.json) for the F32.Z3 audit ledger review
234. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_preparation_plan_review_gate_failure_modes_review.json](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_preparation_plan_review_gate_failure_modes_review.json) for the F32.Z3 failure modes review
235. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_preparation_plan_review_gate_safety_matrix.json](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_preparation_plan_review_gate_safety_matrix.json) for the F32.Z3 safety matrix
236. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_preparation_plan_review_gate_next_phase_contract.json](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_preparation_plan_review_gate_next_phase_contract.json) for the F32.Z3 next phase contract
247. [docs/fase32/f32z4_future_mcp_readonly_configuration_controlled_apply_authorization_gate.md](../docs/fase32/f32z4_future_mcp_readonly_configuration_controlled_apply_authorization_gate.md) for the F32.Z4 authorization gate doc
248. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_authorization_gate_decision.json](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_authorization_gate_decision.json) for the F32.Z4 decision
249. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_authorization_gate_summary.json](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_authorization_gate_summary.json) for the F32.Z4 summary
250. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_authorization_gate_report.md](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_authorization_gate_report.md) for the F32.Z4 report
251. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_authorization_gate_requirements.json](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_authorization_gate_requirements.json) for the F32.Z4 requirements
252. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_authorization_gate_authorization_contract.json](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_authorization_gate_authorization_contract.json) for the F32.Z4 authorization contract
253. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_authorization_gate_authorization_matrix.json](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_authorization_gate_authorization_matrix.json) for the F32.Z4 authorization matrix
254. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_authorization_gate_human_confirmation_contract.json](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_authorization_gate_human_confirmation_contract.json) for the F32.Z4 human confirmation contract
255. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_authorization_gate_safety_matrix.json](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_authorization_gate_safety_matrix.json) for the F32.Z4 safety matrix
256. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_authorization_gate_next_phase_contract.json](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_authorization_gate_next_phase_contract.json) for the F32.Z4 next phase contract
257. [docs/fase32/f32z5_future_mcp_readonly_configuration_controlled_apply_authorization_review_gate.md](../docs/fase32/f32z5_future_mcp_readonly_configuration_controlled_apply_authorization_review_gate.md) for the F32.Z5 authorization review gate doc
258. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_authorization_review_gate_decision.json](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_authorization_review_gate_decision.json) for the F32.Z5 decision
259. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_authorization_review_gate_summary.json](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_authorization_review_gate_summary.json) for the F32.Z5 summary
260. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_authorization_review_gate_report.md](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_authorization_review_gate_report.md) for the F32.Z5 report
261. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_authorization_review_gate_review_matrix.json](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_authorization_review_gate_review_matrix.json) for the F32.Z5 review matrix
262. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_authorization_review_gate_authorization_contract_review.json](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_authorization_review_gate_authorization_contract_review.json) for the F32.Z5 authorization contract review
263. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_authorization_review_gate_authorization_matrix_review.json](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_authorization_review_gate_authorization_matrix_review.json) for the F32.Z5 authorization matrix review
264. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_authorization_review_gate_human_confirmation_review.json](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_authorization_review_gate_human_confirmation_review.json) for the F32.Z5 human confirmation review
265. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_authorization_review_gate_safety_matrix.json](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_authorization_review_gate_safety_matrix.json) for the F32.Z5 safety matrix
266. [artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_authorization_review_gate_next_phase_contract.json](../artifacts/f32/f32_future_mcp_readonly_configuration_controlled_apply_authorization_review_gate_next_phase_contract.json) for the F32.Z5 next phase contract

267. [docs/fase32/f32z6_future_mcp_readonly_configuration_final_pre_apply_dry_run_simulation.md](../docs/fase32/f32z6_future_mcp_readonly_configuration_final_pre_apply_dry_run_simulation.md) for the F32.Z6 final pre-apply dry-run simulation doc
268. [artifacts/f32/f32_future_mcp_readonly_configuration_final_pre_apply_dry_run_simulation_decision.json](../artifacts/f32/f32_future_mcp_readonly_configuration_final_pre_apply_dry_run_simulation_decision.json) for the F32.Z6 decision
269. [artifacts/f32/f32_future_mcp_readonly_configuration_final_pre_apply_dry_run_simulation_summary.json](../artifacts/f32/f32_future_mcp_readonly_configuration_final_pre_apply_dry_run_simulation_summary.json) for the F32.Z6 summary
270. [artifacts/f32/f32_future_mcp_readonly_configuration_final_pre_apply_dry_run_simulation_report.md](../artifacts/f32/f32_future_mcp_readonly_configuration_final_pre_apply_dry_run_simulation_report.md) for the F32.Z6 report
271. [artifacts/f32/f32_future_mcp_readonly_configuration_final_pre_apply_dry_run_simulation_planned_config_content.json](../artifacts/f32/f32_future_mcp_readonly_configuration_final_pre_apply_dry_run_simulation_planned_config_content.json) for the F32.Z6 planned config content
272. [artifacts/f32/f32_future_mcp_readonly_configuration_final_pre_apply_dry_run_simulation_planned_config_hash.json](../artifacts/f32/f32_future_mcp_readonly_configuration_final_pre_apply_dry_run_simulation_planned_config_hash.json) for the F32.Z6 planned config hash
273. [artifacts/f32/f32_future_mcp_readonly_configuration_final_pre_apply_dry_run_simulation_pre_state.json](../artifacts/f32/f32_future_mcp_readonly_configuration_final_pre_apply_dry_run_simulation_pre_state.json) for the F32.Z6 pre-state
274. [artifacts/f32/f32_future_mcp_readonly_configuration_final_pre_apply_dry_run_simulation_post_state.json](../artifacts/f32/f32_future_mcp_readonly_configuration_final_pre_apply_dry_run_simulation_post_state.json) for the F32.Z6 post-state
275. [artifacts/f32/f32_future_mcp_readonly_configuration_final_pre_apply_dry_run_simulation_rollback_handle.json](../artifacts/f32/f32_future_mcp_readonly_configuration_final_pre_apply_dry_run_simulation_rollback_handle.json) for the F32.Z6 rollback handle
276. [artifacts/f32/f32_future_mcp_readonly_configuration_final_pre_apply_dry_run_simulation_ledger_entry_plan.json](../artifacts/f32/f32_future_mcp_readonly_configuration_final_pre_apply_dry_run_simulation_ledger_entry_plan.json) for the F32.Z6 ledger entry plan
277. [artifacts/f32/f32_future_mcp_readonly_configuration_final_pre_apply_dry_run_simulation_final_denylist.json](../artifacts/f32/f32_future_mcp_readonly_configuration_final_pre_apply_dry_run_simulation_final_denylist.json) for the F32.Z6 final denylist
278. [artifacts/f32/f32_future_mcp_readonly_configuration_final_pre_apply_dry_run_simulation_safety_matrix.json](../artifacts/f32/f32_future_mcp_readonly_configuration_final_pre_apply_dry_run_simulation_safety_matrix.json) for the F32.Z6 safety matrix
279. [artifacts/f32/f32_future_mcp_readonly_configuration_final_pre_apply_dry_run_simulation_next_phase_contract.json](../artifacts/f32/f32_future_mcp_readonly_configuration_final_pre_apply_dry_run_simulation_next_phase_contract.json) for the F32.Z6 next phase contract

280. [docs/fase32/f32z7_future_mcp_readonly_configuration_final_human_authorization_gate.md](../docs/fase32/f32z7_future_mcp_readonly_configuration_final_human_authorization_gate.md) for the F32.Z7 human authorization gate doc
281. [artifacts/f32/f32_future_mcp_readonly_configuration_final_human_authorization_gate_decision.json](../artifacts/f32/f32_future_mcp_readonly_configuration_final_human_authorization_gate_decision.json) for the F32.Z7 decision
282. [artifacts/f32/f32_future_mcp_readonly_configuration_final_human_authorization_gate_summary.json](../artifacts/f32/f32_future_mcp_readonly_configuration_final_human_authorization_gate_summary.json) for the F32.Z7 summary
283. [artifacts/f32/f32_future_mcp_readonly_configuration_final_human_authorization_gate_report.md](../artifacts/f32/f32_future_mcp_readonly_configuration_final_human_authorization_gate_report.md) for the F32.Z7 report
284. [artifacts/f32/f32_future_mcp_readonly_configuration_final_human_authorization_statement_template.json](../artifacts/f32/f32_future_mcp_readonly_configuration_final_human_authorization_statement_template.json) for the F32.Z7 authorization template
285. [artifacts/f32/f32_future_mcp_readonly_configuration_final_human_authorization_request.md](../artifacts/f32/f32_future_mcp_readonly_configuration_final_human_authorization_request.md) for the F32.Z7 authorization request
286. [artifacts/f32/f32_future_mcp_readonly_configuration_final_human_authorization_next_phase_contract.json](../artifacts/f32/f32_future_mcp_readonly_configuration_final_human_authorization_next_phase_contract.json) for the F32.Z7 next phase contract

287. [docs/fase32/f32z7h_future_mcp_readonly_configuration_human_authorization_evidence_intake.md](../docs/fase32/f32z7h_future_mcp_readonly_configuration_human_authorization_evidence_intake.md) for the F32.Z7H intake doc
288. [artifacts/f32/f32_future_mcp_readonly_configuration_human_authorization_evidence_intake_decision.json](../artifacts/f32/f32_future_mcp_readonly_configuration_human_authorization_evidence_intake_decision.json) for the F32.Z7H decision
289. [artifacts/f32/f32_future_mcp_readonly_configuration_human_authorization_evidence_intake_summary.json](../artifacts/f32/f32_future_mcp_readonly_configuration_human_authorization_evidence_intake_summary.json) for the F32.Z7H summary
290. [artifacts/f32/f32_future_mcp_readonly_configuration_human_authorization_evidence_intake_report.md](../artifacts/f32/f32_future_mcp_readonly_configuration_human_authorization_evidence_intake_report.md) for the F32.Z7H report
291. [artifacts/f32/f32_future_mcp_readonly_configuration_human_authorization_statement_instructions.md](../artifacts/f32/f32_future_mcp_readonly_configuration_human_authorization_statement_instructions.md) for the F32.Z7H instructions
292. [artifacts/f32/f32_future_mcp_readonly_configuration_final_human_authorization_statement.placeholder.json](../artifacts/f32/f32_future_mcp_readonly_configuration_final_human_authorization_statement.placeholder.json) for the F32.Z7H placeholder
293. [artifacts/f32/f32_future_mcp_readonly_configuration_human_authorization_evidence_schema.json](../artifacts/f32/f32_future_mcp_readonly_configuration_human_authorization_evidence_schema.json) for the F32.Z7H evidence schema
294. [artifacts/f32/f32_future_mcp_readonly_configuration_human_authorization_next_phase_contract.json](../artifacts/f32/f32_future_mcp_readonly_configuration_human_authorization_next_phase_contract.json) for the F32.Z7H next phase contract

295. [docs/fase32/f32z7i_future_mcp_readonly_configuration_human_authorization_evidence_validation.md](../docs/fase32/f32z7i_future_mcp_readonly_configuration_human_authorization_evidence_validation.md) for the F32.Z7I validation doc
296. [artifacts/f32/f32_future_mcp_readonly_configuration_human_authorization_evidence_validation_decision.json](../artifacts/f32/f32_future_mcp_readonly_configuration_human_authorization_evidence_validation_decision.json) for the F32.Z7I decision
297. [artifacts/f32/f32_future_mcp_readonly_configuration_human_authorization_evidence_validation_summary.json](../artifacts/f32/f32_future_mcp_readonly_configuration_human_authorization_evidence_validation_summary.json) for the F32.Z7I summary
298. [artifacts/f32/f32_future_mcp_readonly_configuration_human_authorization_evidence_validation_report.md](../artifacts/f32/f32_future_mcp_readonly_configuration_human_authorization_evidence_validation_report.md) for the F32.Z7I report
299. [artifacts/f32/f32_future_mcp_readonly_configuration_human_authorization_evidence_validation_matrix.json](../artifacts/f32/f32_future_mcp_readonly_configuration_human_authorization_evidence_validation_matrix.json) for the F32.Z7I validation matrix
300. [artifacts/f32/f32_future_mcp_readonly_configuration_human_authorization_evidence_validation_next_phase_contract.json](../artifacts/f32/f32_future_mcp_readonly_configuration_human_authorization_evidence_validation_next_phase_contract.json) for the F32.Z7I next phase contract

301. [docs/fase32/f32z7j_future_mcp_readonly_configuration_manual_human_authorization_required.md](../docs/fase32/f32z7j_future_mcp_readonly_configuration_manual_human_authorization_required.md) for the F32.Z7J manual authorization doc
302. [artifacts/f32/f32_future_mcp_readonly_configuration_manual_human_authorization_required_decision.json](../artifacts/f32/f32_future_mcp_readonly_configuration_manual_human_authorization_required_decision.json) for the F32.Z7J decision
303. [artifacts/f32/f32_future_mcp_readonly_configuration_manual_human_authorization_required_summary.json](../artifacts/f32/f32_future_mcp_readonly_configuration_manual_human_authorization_required_summary.json) for the F32.Z7J summary
304. [artifacts/f32/f32_future_mcp_readonly_configuration_manual_human_authorization_required_report.md](../artifacts/f32/f32_future_mcp_readonly_configuration_manual_human_authorization_required_report.md) for the F32.Z7J report
305. [artifacts/f32/f32_future_mcp_readonly_configuration_manual_human_authorization_operator_checklist.md](../artifacts/f32/f32_future_mcp_readonly_configuration_manual_human_authorization_operator_checklist.md) for the F32.Z7J operator checklist
306. [artifacts/f32/f32_future_mcp_readonly_configuration_manual_human_authorization_exact_statement_template.json](../artifacts/f32/f32_future_mcp_readonly_configuration_manual_human_authorization_exact_statement_template.json) for the F32.Z7J exact statement template
307. [artifacts/f32/f32_future_mcp_readonly_configuration_manual_human_authorization_stop_marker.json](../artifacts/f32/f32_future_mcp_readonly_configuration_manual_human_authorization_stop_marker.json) for the F32.Z7J stop marker
308. [artifacts/f32/f32_future_mcp_readonly_configuration_manual_human_authorization_next_phase_contract.json](../artifacts/f32/f32_future_mcp_readonly_configuration_manual_human_authorization_next_phase_contract.json) for the F32.Z7J next phase contract
