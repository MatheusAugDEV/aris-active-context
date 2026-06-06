# INF-FULL-02 Baseline Freeze Planning

## Verdict

- Phase: `ARIS Infernus FULL Baseline Freeze Planning`
- Phase ID: `INF-FULL-02`
- Decision: `pass`
- Status: `inf_full_02_baseline_freeze_planning_pass`
- Operator authorization source: `chat_operator_said_vamos_continuar_2026_06_06`
- baseline_freeze_planned: `true`
- baseline_freeze_applied: `false`
- next_phase: `null`

## Frozen Baseline Answer

The frozen reference baseline is the observed Project_ARIS scoped code tree defined by INF-FULL-01, plus the 13 materialized fixture scenarios under `aris-active-context/fixtures/lab_simulation/aris_infernus_lab_full`, anchored to:

- Project repository HEAD observed: `9e6194d9a97dfc4040bc3abffba61ec2136c1e5b`
- Active-context repository HEAD observed: `c922967bd8e23c8e35b3c3316f2cface4de66a60`

This phase does not apply a clean-tree baseline assertion. It records a deterministic hash reference package because both repositories already have local drift.

## Baseline Contents

Included in the baseline candidate set:

- `artifacts/decisions/acb_cap_05_project_evidence_2026_06_05.json`
- `artifacts/acb_cap_05/advanced_supply_chain_decision.json`
- `artifacts/infernus/inf_full_01_scope_charter_decision_2026_06_06.json`
- `artifacts/infernus/inf_full_01_scope_matrix_2026_06_06.json`
- `artifacts/infernus/inf_full_01_module_scope_manifest_2026_06_06.json`
- `docs/infernus_full/inf_full_01_scope_charter_2026_06_06.md`
- all scoped `src/aris` module trees
- all 13 materialized scenario directories

Historical-only reference set:

- `aris-active-context/artifacts/inf_bot_01/nemesis_execution_log.json`
- `aris-active-context/artifacts/inf_minos_01/minos_verdict.json`
- `aris-active-context/artifacts/purg_01/finding_nemesis_validator_bypass.json`

Quarantine hash-only modules:

- `src/aris/diagnostics`
- `src/aris/packaging`

Excluded from the authoritative frozen baseline:

- `src/aris/__pycache__`
- `docs/infernus_full/infernus_full_roadmap_v1.md`
- `docs/infernus_full/infernus_full_execution_spec.md`
- legacy planning JSONs under `artifacts/infernus/` that are advisory but not authoritative for the freeze set

## Hash Strategy

- Artifact files use `SHA-256` over file bytes.
- Module trees use `directory_tree_sha256` = `SHA-256` over sorted `<relative_path>:<file_sha256>` lines.
- Fixture scenario directories use the same `directory_tree_sha256` algorithm.
- The resulting manifest is recorded in `artifacts/infernus/inf_full_02_baseline_freeze_hash_manifest_2026_06_06.json`.

## Prohibitions Until Review

- No bot execution.
- No runtime start.
- No real dry-run.
- No real apply.
- No new Purgatorium expansion.
- No product or pilot authorization.
- No Bedrock execution.
- No secrets access.
- No external network execution.
- Historical bot/Minos/Purgatorium artifacts must not be treated as current execution evidence.

## Successor Assessment

No canonical successor is currently defined for INF-FULL-02 in ROADMAP_CANONICAL.md.

Advisory-only note: `docs/infernus_full/infernus_full_roadmap_v1.md` suggests F5 Bot Materialization after baseline freeze, but this is not canonical until `ROADMAP_CANONICAL.md` gains an explicit successor row.
