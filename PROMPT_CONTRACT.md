# PROMPT_CONTRACT

`ARIS_PHASE_PROMPT_CONTRACT_V2` is the compact phase prompt contract for ARIS.

R0 governance foundation is materialized; future prompts still require the continuity fields and the active-context update.
It reduces repetition while preserving phase gates, safety, deterministic evidence, active-context precedence, and Bedrock Gate enforcement.

## Mandatory read-first rule

Every future ARIS phase prompt, Codex instruction, phase review, status review, roadmap decision, and next-step recommendation must read or explicitly reference:

1. CURRENT_STATE.md
2. NEXT_ACTION.md
3. DECISION_LOCKS.md
4. MANDATORY_READ_FIRST_RULES.md
5. LAB_OPERATING_CONTRACT.md
6. LAB_STATUS.md
7. LAB_VERDICTS.md
8. CONTEXT_INDEX.md
9. ARIS_PHASE_LEDGER.md
10. README.md
11. OPERATOR_PREFERENCES.md, if present
12. PROMPT_CONTRACT.md

If a required file is missing, stale, inaccessible, or contradictory, report drift before deciding.

## Required structure

Future phase prompts should follow this order:

1. Phase / objective
2. Read-first sources
3. Named standard guards
4. Bedrock Gate applicability and verdict requirement
5. Phase-specific evidence
6. Phase-specific scope
7. Required artifacts
8. Decision JSON fields
9. Tests
10. Validation
11. Active-context update
12. Commit/push/final report

## Preferred compact prompt skeleton

Use this compact form by default for future Codex prompts when active-context already contains the stable rules:

```text
PROMPT CODEX — <PHASE> <NAME>

Nível de raciocínio: alto / sênior / conservador / Bedrock-governed.

Leia primeiro:
CURRENT_STATE.md, NEXT_ACTION.md, DECISION_LOCKS.md, MANDATORY_READ_FIRST_RULES.md, LAB_OPERATING_CONTRACT.md, LAB_STATUS.md, LAB_VERDICTS.md, CONTEXT_INDEX.md, ARIS_PHASE_LEDGER.md, README.md, PROMPT_CONTRACT.md.

Use os guards:
AC-READ, BEDROCK-COMPLETE, NO-REAL-EXEC, NO-BULK, ARTIFACT-ONLY, TESTS-RUNNER-DOCS, ACTIVE-CONTEXT-UPDATE, COMMIT-PUSH-HASH.

Bedrock Gate:
<state whether this phase consumes an existing verdict, produces a verdict, or is an explicit Bedrock-preparation exception>

Contexto:
<phase-specific context only>

Objetivo:
<clear phase objective>

Escopo permitido:
<allowed work only>

Fora de escopo:
<phase-specific forbidden additions only>

Entregáveis:
<src, script, test, doc, artifacts, active-context updates>

Validações:
<py_compile, unittest, runner, json.tool, defensive grep>

Atualização final:
<active-context update, LAB_STATUS/LAB_VERDICTS update when applicable, commit, push, final hash>
```

## Preferred short guard aliases

- `AC-READ`: read active-context first and obey source-of-truth precedence.
- `BEDROCK-COMPLETE`: preserve Lab/Bedrock enforcement; every future phase/capability must have a Bedrock verdict or explicit Bedrock-preparation exception.
- `NO-REAL-EXEC`: no real runtime/product/db/schema/FTS5/ingestion/network/dependency/action execution unless the current valid gate explicitly authorizes it by evidence.
- `NO-BULK`: no bulk Obsidian/archive read; query-first only when specifically needed.
- `ARTIFACT-ONLY`: phase decisions are artifact/evidence decisions unless explicitly promoted by a valid Bedrock/Product gate.
- `TESTS-RUNNER-DOCS`: create/update runner, tests, docs, artifacts, and validations for the phase.
- `ACTIVE-CONTEXT-UPDATE`: update CURRENT_STATE.md, NEXT_ACTION.md, ARIS_PHASE_LEDGER.md, CONTEXT_INDEX.md, MANDATORY_READ_FIRST_RULES.md if needed, Lab files, and decision files when applicable.
- `COMMIT-PUSH-HASH`: commit, push, and report final hash.

## Legacy named guards

The following legacy names remain valid and map to the compact guard aliases above:

- `READ_FIRST_ACTIVE_CONTEXT`
- `SIMILAR_PROJECTS_ADVISORY_ONLY`
- `NO_NETWORK_NO_DEPS_NO_SECRETS`
- `NO_RUNTIME_MUTATION`
- `NO_REAL_DB_SCHEMA_FTS5_INGESTION`
- `NO_OBSIDIAN_BULK_READ`
- `NO_MCP_ACTIVATION`
- `NO_EXTERNAL_RESEARCH_AS_AUTHORITY`
- `DETERMINISTIC_ARTIFACTS_REQUIRED`
- `TESTS_AND_RUNNER_REQUIRED`
- `ACTIVE_CONTEXT_UPDATE_REQUIRED`
- `COMMIT_PUSH_HASH_REQUIRED`

## Bedrock Gate rule

ARIS Lab is the active validation control plane. Bedrock Gate is mandatory for every future phase/capability advancement.

Allowed verdicts:

- PASS
- WARN
- BLOCK
- NEEDS_REVIEW
- REGRESSION
- OBSOLETE

A phase/capability is not complete unless it records a Bedrock verdict or explicitly states that it is a Bedrock-preparation exception. The exception must be carried into NEXT_ACTION.

## Similar Projects rule

At the start of every new ARIS phase, Codex must consult the Similar Projects Reference Library as advisory-only research for relevant risks, patterns, antipatterns, and future verification candidates.
It must never use Similar Projects as source-of-truth, implementation authority, dependency authority, roadmap authority, or replacement for active-context.

Required fields:

- `similar_projects_consulted=true`
- `similar_projects_advisory_only=true`
- `similar_projects_used_for_decision=false`
- `similar_projects_primary_source_verification_required=true`

Notes:

- maximum 5 phase-relevant notes
- no web/primary-source validation unless a later phase explicitly authorizes it

## Operator-facing phase explanation rule

Before every Codex prompt and after every Codex result, the assistant must give a brief operator-facing explanation outside the prompt that states:

- what the phase is
- what it does
- what it does not do
- why it matters
- one-sentence summary

This rule is operator-facing only. It must not bloat Codex prompts, weaken guards, replace active-context evidence, or authorize implementation.

## Compactness rule

- Default to the preferred compact prompt skeleton above.
- Use short guard aliases instead of restating full prohibition blocks.
- Include only phase-specific deltas and phase-specific forbidden additions.
- Keep stable repeated content in this file, MANDATORY_READ_FIRST_RULES.md, LAB_OPERATING_CONTRACT.md, and docs/runbooks.
- Do not repeat long safety constitutions in every Codex prompt unless a new subsystem, new risk class, or explicit recovery condition requires it.

## Phase narrative continuity rule

Starting with ARIS-LAB-B14, every future ARIS phase prompt, Codex instruction, phase review, status review, roadmap decision, and next-step recommendation must include both compact continuity fields:

- `previous_phase_short_summary`: a short, operator-facing summary of the immediately previous phase.
- `next_phase_short_explanation`: a short, operator-facing explanation of what the next phase will do.

The fields must stay brief and continuity-focused. They do not replace active-context evidence, source-of-truth files, or full phase documentation.
Future next-phase contracts must require both fields.

## ARIS Completion Doctrine / 200% Standard

Every future ARIS phase prompt, Codex instruction, phase review, status review, roadmap decision, and next-step recommendation must avoid false completion language unless the evidence package is complete, validated, and non-bypassable.

Completion claims are only allowed when the current gate can support all of the following without known blockers:

- no false completion
- no hidden TODO
- evidence-backed completion
- safe completion
- efficient completion
- non-bypassable gate
- operator clarity

Operational interpretation:

- If it is not complete, do not call it final.
- If it has a gap, convert it to warning, deferred, blocked, or next-phase requirement.
- If evidence is missing, it is a hypothesis.
- If a test is missing, it is a candidate.
- If safety is missing, do not advance.
- If operator clarity is insufficient, it is not final.
- If a known risk lacks classification, do not close.
- If the gate can be bypassed without detection, the gate is not ready.
- If efficiency is poor because of repetition, noise, bulk-read, or prompt bloat, record a required improvement.
- "100%" means complete, validated, safe, and free of known blockers.
- "200%" means complete plus efficient, operator-clear, evidence-backed, non-bypassable, and without false done.

## Quality rule

Compact prompts must preserve:

- source-of-truth precedence
- deterministic gates
- Bedrock verdict or explicit Bedrock-preparation exception
- tests
- runner artifacts
- defensive grep
- active-context updates
- commit/push/hash reporting
- explicit no-implementation flags

## Size guidance

- Default prompt target: copy/paste friendly, short, surgical, and objective.
- Prefer compact prompts over long prompts when active-context and this contract already contain the stable rules.
- Longer prompts are allowed only for new subsystems, first implementation of a new pattern, high-risk recovery, or unresolved blockers.
- Move repeated stable content into PROMPT_CONTRACT.md, MANDATORY_READ_FIRST_RULES.md, and LAB_OPERATING_CONTRACT.md rather than copying it into each prompt.

## How to reference

Use this file as the stable meta-contract.
Use docs/runbooks/codex_compact_prompt_template.md as the prompt skeleton for new phases when available.
