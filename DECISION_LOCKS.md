current live locks are derived from ACTIVE_CONTEXT_STATE.json. If this file conflicts with ACTIVE_CONTEXT_STATE.json, ACTIVE_CONTEXT_STATE.json wins.

# Decision Locks

## Current Live Locks

- Latest completed phase: `ARIS Infernus Lab FULL Scenario Manifest Dataset Planning Gate`
- Last transition from: `ARIS Infernus Lab FULL Schema Pack Closure Review Gate`
- Status: `aris_infernus_lab_full_scenario_manifest_dataset_planning_gate_pass`
- Current status: `ready_for_aris_infernus_lab_full_scenario_manifest_dataset_review_gate`
- Active next phase: `ARIS Infernus Lab FULL Scenario Manifest Dataset Review Gate`
- Active next phase class: `review_gate_only`

## Roadmap Authority Locks

- `ROADMAP_CANONICAL.md` remains the only roadmap authority file.
- The canonical macrochain is: `Infernus FULL -> Purgatorium FULL -> Infernus Revalidation -> Crisol FULL -> Bedrock Gate -> Productization only if Bedrock permits`.
- `WRN-VERDICT-REF-NORMALIZATION`, `WRN-SIGNAL-REF-NORMALIZATION`, and `WRN-SCENARIO-MANIFEST-DATASET-LAYER-PENDING` are now materialized or resolved and must not be reintroduced silently.
- Old R0/F120, F21/F33/C6/C14, Lab Simulation, and Contract Schema Enforcement routes remain historical or superseded only.

## Canonical Macrochain

```text
Infernus revela.
Purgatorium corrige.
Infernus revalida.
Crisol refina.
Bedrock decide.
```

## Non-Authorization Locks

- Scenario manifest dataset planning does not authorize implementation or execution.
- No Bedrock authorization by schema planning.
- No product promotion authorization.
- No bot execution authorization.
- No attack execution authorization.
- No harness creation or execution authorization.
- No Purgatorium execution authorization.
- No real dry-run authorization.
- No real apply authorization.
- No production authorization.
- Bedrock remains non-executable and product promotion remains blocked.
