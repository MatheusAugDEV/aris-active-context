# PROMPT_CONTRACT

`ARIS_PHASE_PROMPT_CONTRACT_V2` is the compact phase prompt contract for ARIS.

R0 governance foundation is materialized; future prompts still require the continuity fields and the active-context update.
It reduces repetition while preserving phase gates, safety, deterministic evidence, active-context precedence, and Bedrock Gate enforcement.

## Mandatory read-first rule

Every future ARIS phase prompt, Codex instruction, phase review, status review, roadmap decision, and next-step recommendation must read or explicitly reference — **in this exact order**:

```
1. ACTIVE_CONTEXT_STATE.json          ← canonical live state (ALWAYS FIRST)
2. ACTIVE_CONTEXT_SCHEMA.json         ← validation contract
3. scripts/validate_active_context_state.py  ← run before any decision
4. CURRENT_STATE.md                   ← derived mirror
5. NEXT_ACTION.md                     ← derived mirror
6. DECISION_LOCKS.md                  ← derived mirror / authorization boundary
7. MANDATORY_READ_FIRST_RULES.md
8. LAB_OPERATING_CONTRACT.md
9. CONTEXT_INDEX.md
10. ARIS_PHASE_LEDGER.md
11. README.md
12. OPERATOR_PREFERENCES.md, if present
13. PROMPT_CONTRACT.md
```

**Rule**: ACTIVE_CONTEXT_STATE.json is always step 1. No Markdown file may be consulted before the JSON. A Markdown file that contradicts the JSON must be reported as drift and must not be trusted.

If a required file is missing, stale, inaccessible, or contradictory, report drift before deciding.

## Reviewer SHA rule

Toda resposta do revisor abre com SHA resolvido de origin/main lido naquele turno.
Sem SHA citado: resposta é INVALID por construção.

## POST-COMMIT VERIFICATION (obrigatório em todo gate)

After `git push origin main`:

1. Wait 30 seconds.
2. Run:
   `gh run list --limit 20`
3. If any relevant workflow for the current commit/push is `queued`, `waiting`, `requested`, or `in_progress`, wait 60 seconds and repeat step 2.
4. Continue polling until every relevant workflow for the current commit/push is terminal.
5. If every relevant workflow conclusion is `success`, classify:
   `CI_GREEN_CONFIRMED`
6. If any relevant workflow conclusion is `failure`, `cancelled`, `timed_out`, `action_required`, or any non-success terminal conclusion, classify:
   `CI_FAILED`
7. If `CI_FAILED`, run:
   `gh run view --log-failed`
   Then report failed workflow, failed job, root cause, and relevant log excerpt before any repair.
8. Embed Action run URL(s) in the decision artifact when the phase writes decision artifacts.

The model never self-reports PASS. The CI reports PASS.
`CI_PENDING` is an interim state only; it is not a valid final report.
No final report may be emitted before terminal CI.
No prompt, phase, or local instruction may reduce this polling requirement.

## Required CI output discipline

Every final Codex report after push must include terminal CI state.

Forbidden final combinations:
- `Decision: pass` + any workflow `in_progress`
- `Status final` + any workflow `queued`
- `CI_GREEN_CONFIRMED` + missing required workflow
- next phase request while required workflows are not terminal

Allowed interim report:
`CI_PENDING`, with list of still-running workflows and URLs.

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

Leia primeiro (nesta ordem):
ACTIVE_CONTEXT_STATE.json, ACTIVE_CONTEXT_SCHEMA.json, scripts/validate_active_context_state.py, CURRENT_STATE.md, NEXT_ACTION.md, DECISION_LOCKS.md, MANDATORY_READ_FIRST_RULES.md, LAB_OPERATING_CONTRACT.md, CONTEXT_INDEX.md, ARIS_PHASE_LEDGER.md, README.md, PROMPT_CONTRACT.md.

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

## REGRA ANTI-PROLIFERAÇÃO DE GATES

Um gate só é válido se mudar pelo menos UM fato canônico verificável:
- uma flag de autorização inverte (false->true ou true->false), OU
- um artifact real é criado no disco com hash registrado, OU
- um teste passa de vermelho/ausente para verde.

Gate que apenas reafirma locks do gate anterior é PROIBIDO.
Planning e Review do mesmo passo colapsam em UM gate
com seção "plano" e seção "revisão", veredito único.

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

## Regras de Scope para Prompts Codex

- O prompt define o escopo. Codex executa o escopo. Nada além.
- Prompts não devem pedir confirmação de locks globais já estabelecidos no active-context.
- Prompts devem ser explícitos sobre o que é PERMITIDO, não apenas sobre o que é proibido.
- Locks de execução (IF-08, waves, bots, runtime, produto, piloto, Bedrock, secrets) são permanentes até instrução explícita do operador que atualiza `ACTIVE_CONTEXT_STATE.json`.
- Um prompt de CI repair é diferente de um prompt de fase. CI repair não avança fase.
- Se o CI falhou por path antigo movido para excludent, corrija o path no script. Não restaure o arquivo.
- Resultados de CI de fases anteriores não são bloqueantes para o estado atual.
- `CI POLLING` é obrigatório em todo prompt que inclua push para `origin/main`. A regra está em `OPERATOR_PREFERENCES.md` seção `SCOPE DISCIPLINE`. Todo prompt herda essa regra automaticamente e não precisa repeti-la individualmente. O Codex deve aplicá-la mesmo que o prompt individual não a mencione explicitamente.
- Every Codex prompt that can produce a phase result must require active-context update as a blocking deliverable. Final report must include both Project repo SHA and active-context repo SHA verified on `origin/main`.
- If Project repo result exists but `aris-active-context/main` does not reflect it yet, the prompt must block on `Active-Context Canonical Sync Repair` before any next phase prompt or canonical PASS claim.
