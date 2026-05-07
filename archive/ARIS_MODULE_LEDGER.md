# ARIS_MODULE_LEDGER

## 1. Early root modules

- Purpose: the original bootstrap stack of ARIS.
- Known modules / paths: `main.py`, `brain.py`, `actions.py`, memory JSON files.
- Known artifacts: early session notes, memory files, UI prototypes.
- Status: legacy / partially verified.
- Risks / open items: naming drift, mixed-era code, unverified paths.
- Verification level: `REQUIRES_VERIFICATION` in many details.

## 2. `src/aris/understanding`

- Purpose: intent, ambiguity, semantic routing.
- Known modules / paths: `REQUIRES_VERIFICATION`.
- Known artifacts: F14/F21 related summaries and docs.
- Status: active conceptually.
- Risks / open items: path drift, overlap with response logic.
- Verification level: partial.

## 3. `src/aris/response`

- Purpose: response planning, composition, reliability.
- Known modules / paths: `REQUIRES_VERIFICATION`.
- Known artifacts: F20/F22/F24/F25/F26 proof artifacts.
- Status: active and growing.
- Risks / open items: overclaiming quality, fallback mismatch.

## 4. `src/aris/response/evaluation`

- Purpose: evaluation, benchmark/golden gates, traceability.
- Known modules / paths: `REQUIRES_VERIFICATION`.
- Known artifacts: F24/F25/F26 matrices and reports.
- Status: active.
- Risks / open items: fake coverage, missing provenance.

## 5. `src/aris/action_runtime_contracts`

- Purpose: action gating, dry-run, rollback, permission policy.
- Known modules / paths: `REQUIRES_VERIFICATION`.
- Known artifacts: F19 materials.
- Status: active conceptually.
- Risks / open items: mutation safety, ledger completeness.

## 6. `src/aris/audio`

- Purpose: voice safety and audio policy.
- Known modules / paths: `REQUIRES_VERIFICATION`.
- Known artifacts: F18/F23/F24 evidence.
- Status: active but heavily gated.
- Risks / open items: unsafe voice execution, network dependency.

## 7. `src/aris/cockpit`

- Purpose: evidence browsing, readiness, controlled expansion.
- Known modules / paths: `REQUIRES_VERIFICATION`.
- Known artifacts: Pre-V6 cockpit/evidence foundation.
- Status: active foundation.
- Risks / open items: canonical mapping, false certainty.

## 8. `src/aris/context`

- Purpose: active context, source-of-truth, navigation.
- Known modules / paths: `REQUIRES_VERIFICATION`.
- Known artifacts: active-context repo, context policies.
- Status: critical.
- Risks / open items: stale context, drift.

## 9. `src/aris/diagnostics`

- Purpose: healthcheck, dependency diagnostics, risk reports.
- Known modules / paths: `REQUIRES_VERIFICATION`.
- Known artifacts: F27/F28 diagnostics.
- Status: active.
- Risks / open items: hidden dependency failures.

## 10. `src/aris/packaging`

- Purpose: local packaging and recovery planning.
- Known modules / paths: `REQUIRES_VERIFICATION`.
- Known artifacts: F27 profiles and maintenance plans.
- Status: active.
- Risks / open items: unsafe install assumptions.

## 11. Frontend/UI/orb

- Purpose: visual shell and interaction.
- Known modules / paths: `REQUIRES_VERIFICATION`.
- Known artifacts: orb prototypes, GUI iterations.
- Status: present but gated.
- Risks / open items: rendering safety, runtime coupling.

## 12. Obsidian/active-context

- Purpose: compact navigation and evidence access.
- Known modules / paths: active-context repo.
- Known artifacts: context policy docs.
- Status: critical and still under repair.
- Risks / open items: bulk-read, stale context, false closure.

## 13. Docs/artifacts

- Purpose: canonical summaries, decisions, reports, and docs.
- Known modules / paths: `docs/`, `artifacts/`.
- Known artifacts: phase summaries and proof gates.
- Status: primary evidence layer.
- Risks / open items: stale docs if not reconciled.

## 14. Product/roadmap/research references

- Purpose: external inspirations and strategic framing.
- Known modules / paths: `REQUIRES_VERIFICATION`.
- Known artifacts: roadmap docs, research notes, references.
- Status: reference only.
- Risks / open items: mixing inspiration with source-of-truth.
