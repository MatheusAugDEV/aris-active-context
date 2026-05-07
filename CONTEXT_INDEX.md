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
20. Obsidian only after the repair and only query-first
21. `archive/` only when history is needed
22. `Project_ARIS` artifacts/docs only when cited

- Do not bulk-read `archive/`.
- Do not bulk-read Obsidian.
- Do not rely on old memory against `CURRENT_STATE`.
- Do not advance phase without checking `NEXT_ACTION`.
- Do not declare token savings without evidence.
- Keep this repo compact.
