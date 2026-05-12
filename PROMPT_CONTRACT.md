# PROMPT_CONTRACT

`ARIS_PHASE_PROMPT_CONTRACT_V2` is the compact phase prompt contract for ARIS.
It reduces repetition while preserving phase gates, safety, deterministic evidence, and active-context precedence.

## Required structure

Future phase prompts should follow this order:

1. Phase / objective
2. Read-first sources
3. Named standard guards
4. Phase-specific evidence
5. Phase-specific scope
6. Required artifacts
7. Decision JSON fields
8. Tests
9. Validation
10. Active-context update
11. Commit/push/final report

## Named guards

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

- Use guard names instead of restating full prohibition blocks.
- Include only phase-specific deltas and phase-specific forbidden additions.
- Keep stable repeated content in this file and in `docs/runbooks/`.

## Quality rule

Compact prompts must preserve:

- source-of-truth precedence
- deterministic gates
- tests
- runner artifacts
- defensive grep
- active-context updates
- commit/push/hash reporting
- explicit no-implementation flags

## Size guidance

- Default prompt target: copy/paste friendly, ideally under about 250 lines.
- Longer prompts are allowed for new subsystems or the first implementation of a new pattern.
- Move repeated stable content into `PROMPT_CONTRACT.md` rather than copying it into each prompt.

## How to reference

Use this file as the stable meta-contract.
Use `docs/runbooks/codex_compact_prompt_template.md` as the prompt skeleton for new phases.
