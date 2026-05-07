# aris-active-context

Compact, read-first ARIS context entrypoint for ChatGPT, Codex, and Claude.

This repo is intentionally small and operational. It is not the full ARIS
project context dump.

Read order:

1. `CURRENT_STATE.md`
2. `NEXT_ACTION.md`
3. `DECISION_LOCKS.md`
4. `ARIS_PHASE_LEDGER.md`
5. `CONTEXT_INDEX.md`
6. `OPERATOR_PREFERENCES.md`

Official V6 naming follows the PDF roadmap F1-F29.
Consult this repo before ARIS technical decisions.
Update it at the end of every Codex phase.
Current repair status: Obsidian Context Law / Context Control repair passed; F29 readiness review is warn-passed, F29 readiness warnings repair is repaired, F29 final execution plan is ready, and F29 final practical closure execution has passed. F30.A historical-to-canonical baseline is warn-passed, F30.B official phase naming cleanup and roadmap save are complete, F30.C artifact, warning & residual risk index is warn-passed, F30.D roadmap publication gate is warn-passed, F31.A source inventory is warn-passed, F31.B hash/signature/metadata index is warn-passed with 35 entries indexed, and F31.C source-of-truth consistency gate is warn-passed. F31.E source-of-truth drift repair controlled apply is complete, F32.A/F32.B are the active context-boundary trust-firewall gates, F32.C structured Obsidian query contract gate is warn-passed, F32.D structured Obsidian query contract review gate is warn-passed, F32.E future MCP read-only candidate contract gate is warn-passed, F32.F future MCP read-only candidate contract review gate is warn-passed, and F32.G future MCP read-only implementation plan gate is warn-passed.
Canonical roadmap preference: phase-by-phase organization with subtracks inside each phase (`F29.A`, `F29.B`, `F29.C`, `F29.D`), then continue numerically with `F30`, `F31`, `F32`, and so on. F31.C remains warn-passed historically, F32.A is ready, F32.B now points to F32.C — Structured Obsidian Query Contract Gate, F32.C now points to F32.D — Structured Obsidian Query Contract Review Gate, F32.D now points to F32.E — Future MCP Read-Only Candidate Contract Gate, F32.E now points to F32.F — Future MCP Read-Only Candidate Contract Review Gate, F32.F now points to F32.G — Future MCP Read-Only Implementation Plan Gate, F32.G now points to F32.H — Future MCP Read-Only Implementation Plan Review Gate, F32.H now points to F32.I — Future MCP Read-Only Dry-Run Gate, F32.I now points to F32.J — Future MCP Read-Only Dry-Run Review Gate, F32.J now points to F32.K — Future MCP Read-Only Security Review Gate, F32.K now points to F32.L — Future MCP Read-Only Provenance Gate, and F32.L now points to F32.M — Future MCP Read-Only Disable and Rollback Rehearsal Gate, F32.M now points to F32.N — Future MCP Read-Only Re-Enable Preconditions Gate, F32.N now points to F32.O — Future MCP Read-Only Final Readiness Consolidation Gate, F32.O now points to F32.P — Future MCP Read-Only Configuration Candidate Gate, and F32.P now points to F32.Q — Future MCP Read-Only Configuration Candidate Review Gate.
Avoid new parallel `V6-*` operational families.
If the closed state remains stable, reserve `F30` for `Roadmap Canonicalization & Phase Hygiene`.
Formal post-V6 roadmap reference: [ROADMAP_F30_F50.md](ROADMAP_F30_F50.md).
The full history is in `archive/`, and `Project_ARIS` remains the detailed
technical source-of-truth.

GitHub: https://github.com/MatheusAugDEV/aris-active-context
