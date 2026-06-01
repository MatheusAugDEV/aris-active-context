# ARIS Infernus Lab FULL Entry Gate

## Phase Name

`ARIS Infernus Lab FULL Macroblock Entry Gate`

## Status

`aris_infernus_lab_full_macroblock_entry_gate_pass`

## Decision

`pass`

## Macrochain Position

Macroblock `1` in the canonical chain:

```text
Infernus revela.
Purgatorium corrige.
Infernus revalida.
Crisol refina.
Bedrock decide.
```

This gate opens `ARIS Infernus Lab FULL` cleanly and hands the route to the next planning gate. It does not execute Infernus.

## Purpose

Define the macroblock entry contract for `ARIS Infernus Lab FULL` so future Infernus phases can discover failures conservatively, record findings deterministically, and prepare downstream correction flow without confusing planning with execution.

## Entry Criteria

- `ACTIVE_CONTEXT_STATE.json` and `ACTIVE_CONTEXT_SCHEMA.json` validate cleanly.
- `ARIS Macro Roadmap Canonical Chain` remains the live roadmap authority.
- The canonical macrochain remains exactly:
  `Infernus revela. / Purgatorium corrige. / Infernus revalida. / Crisol refina. / Bedrock decide.`
- Old `R0/F120`, `F21/F33/C6/C14`, `Lab Simulation`, and `Contract Schema Enforcement` routes remain historical or superseded only.
- Execution authorization, real dry-run authorization, real apply authorization, Bedrock execution, and product promotion all remain `false`.

## Non-Execution Boundary

This phase authorizes only macroblock entry planning.

It does not authorize:

- bot execution
- attacks
- real Infernus execution
- runtime, frontend, backend, action-runtime, or audio mutation
- dependency installation
- secret use
- external API or external LLM use
- real dry-run
- real apply
- Bedrock execution
- product promotion
- pilot, customer readiness, commercial launch, or production

## Discovery Taxonomy

Future `ARIS Infernus Lab FULL` work must classify findings at macro level across:

- governance and authorization bypass
- context, anti-corruption, routing, and ledger drift
- determinism, rollback, auditability, and regression gaps
- runtime, backend, frontend, action-runtime, and audio failure surfaces
- false PASS, false readiness, unsafe automation, and operator-misleading behavior
- product-direction blockers that matter for future quality, while remaining non-authorizing until Bedrock

## Evidence Requirements

Every future Infernus finding must include:

- a stable finding id
- discovery taxonomy classification
- affected surface and impact statement
- bounded reproduction or observation evidence
- explicit indication of whether the evidence is planning, simulation, review, or future controlled-execution candidate
- severity or decision consequence
- residual-risk note
- expected downstream handling in `Purgatorium FULL`

No future Infernus phase may claim PASS without evidence. Any request to move from planning into controlled execution requires a separate future gate.

## Purgatorium Handoff Contract

Findings discovered in future Infernus phases must hand off to `Purgatorium FULL` with:

- finding id and taxonomy
- supporting evidence bundle
- impacted subsystem or governance surface
- expected correction class: `fix`, `accepted_residual`, or `blocked`
- revalidation target for future `Infernus Revalidation`
- explicit carry-forward notes if unresolved

`Purgatorium FULL` is the required correction macroblock for anything Infernus reveals. Infernus does not self-correct inside this entry gate.

## Bedrock Non-Authorization

`Bedrock Gate` remains a future maximum decision gate only. This phase does not authorize Bedrock execution, Bedrock PASS, or any product-direction advancement beyond planning.

## Productization Non-Authorization

`Productization / Controlled Pilot` remains blocked unless Bedrock explicitly permits it. This phase does not authorize pilot, customer readiness, commercial launch, market release, or production.

## Next Recommended Phase

`ARIS Infernus Lab FULL Scope & Attack Taxonomy Planning Gate`
