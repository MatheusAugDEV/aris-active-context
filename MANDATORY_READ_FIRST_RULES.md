# MANDATORY_READ_FIRST_RULES

This file is the compact mandatory rule layer for every ARIS assistant response, Codex prompt, phase review, phase status, roadmap decision, and active-context update.

ARIS-ROADMAP-R0 governance foundation is materialized and does not change the read-first order or authority stack.

If this file conflicts with memory, chat history, commit text, pasted status, or older summaries, **ACTIVE_CONTEXT_STATE.json wins**, followed by this file together with CURRENT_STATE.md, NEXT_ACTION.md, DECISION_LOCKS.md, LAB_OPERATING_CONTRACT.md, LAB_STATUS.md, and LAB_VERDICTS.md.

## Mandatory read-first order

For every ARIS technical decision, phase prompt, Codex instruction, status review, or next-step recommendation, read first — **in this exact order**:

```
1. ACTIVE_CONTEXT_STATE.json          ← canonical live state (ALWAYS FIRST)
2. ACTIVE_CONTEXT_SCHEMA.json         ← validation contract
3. scripts/validate_active_context_state.py  ← run; if fails, report drift and stop
4. CURRENT_STATE.md                   ← derived mirror
5. NEXT_ACTION.md                     ← derived mirror
6. DECISION_LOCKS.md                  ← derived mirror / authorization boundary
7. MANDATORY_READ_FIRST_RULES.md      ← this file
8. LAB_OPERATING_CONTRACT.md
9. LAB_STATUS.md
10. LAB_VERDICTS.md
11. CONTEXT_INDEX.md
12. ARIS_PHASE_LEDGER.md
13. README.md
14. OPERATOR_PREFERENCES.md, if present
15. PROMPT_CONTRACT.md
16. North_Pole.md
```

**Rule**: No Markdown file may be read before ACTIVE_CONTEXT_STATE.json. A Markdown file that contradicts the JSON must be reported as drift and must not be trusted.

If any file is missing, stale, inaccessible, or contradictory, explicitly report the drift before deciding.

## Fundamental ARIS rules

- `ACTIVE_CONTEXT_STATE.json` outranks all Markdown files, assistant memory, chat history, pasted status, summaries, and assumptions.
- `NEXT_ACTION.md` is the operational next-step authority **after** confirming it matches the JSON.
- `DECISION_LOCKS.md` is the hard constraint authority.
- `LAB_OPERATING_CONTRACT.md` is the Lab/Bedrock enforcement authority.
- `LAB_STATUS.md` is the current Lab state authority.
- `LAB_VERDICTS.md` is the Lab verdict ledger authority.
- `ARIS_PHASE_LEDGER.md` is historical evidence, not a replacement for NEXT_ACTION.

## Lab and Bedrock rules

- ARIS Lab is active as the operational validation control plane.
- Bedrock Gate is mandatory for future phase/capability advancement.
- A future phase is not complete unless it has a Bedrock Gate verdict or an explicit Bedrock-preparation exception recorded in its phase contract.
- Bedrock Gate verdicts are PASS, WARN, BLOCK, NEEDS_REVIEW, REGRESSION, and OBSOLETE.
- PASS means evidence is sufficient to advance.
- WARN means the next phase must carry forward warnings explicitly.
- BLOCK means the phase cannot advance.
- NEEDS_REVIEW means evidence is incomplete or ambiguous.
- REGRESSION means baseline worsened and advancement is blocked.
- OBSOLETE means superseded by a later approved decision.

## Safety and execution rules

- No real execution is allowed unless the current phase explicitly authorizes it through the required evidence chain.
- No runtime mutation is allowed unless explicitly authorized.
- No schema apply, SQLite persistence, DDL, CREATE TABLE, CREATE VIRTUAL TABLE, FTS5 creation, memory ingestion, connector use, network, dependency install, MCP activation, vault write, or bulk read is allowed unless explicitly authorized by the current valid gate.
- Chat context, Codex status, commit text, placeholder, template, checklist, marker, or narrative claim does not count as authorization.
- External research is advisory until primary-source verified and accepted through gates.
- F51+ is preserved as advisory research only; it does not authorize implementation, roadmap mutation, productization, real connectors, or pilot execution.
- F44 is Lab hardening, red-team expansion, benchmark maturity, and audit maturity.
- F33 is paused under Lab governance, not cancelled.

## Prompt and Codex rules

Every Codex prompt must:

- include the mandatory read-first list or reference this file explicitly;
- declare ACTIVE_CONTEXT_STATE.json as step 1;
- state the expected reasoning level;
- include named guards;
- define allowed scope and forbidden scope;
- require decision JSON, summary/report artifacts, tests or deterministic validation evidence, safety attestation, drift check, next-phase contract, and active-context update;
- require commit, push, and final hash;
- preserve Lab/Bedrock verdict requirements when the phase advances a capability.

## Response rule for the assistant

Before giving a phase prompt or next technical recommendation, the assistant must:

- read `ACTIVE_CONTEXT_STATE.json` first when accessible;
- run or reference `scripts/validate_active_context_state.py`;
- state if the repo or required files cannot be read;
- avoid treating memory as source-of-truth;
- keep F51+ advisory-only unless a future gate changes it;
- keep Bedrock Gate mandatory for future phase/capability advancement.
