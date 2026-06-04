# MANDATORY_READ_FIRST_RULES

This file is the compact mandatory rule layer for every ARIS assistant response, Codex prompt, phase review, phase status, roadmap decision, and active-context update.

ARIS-ROADMAP-R0 governance foundation is materialized and does not change the read-first order or authority stack.

If this file conflicts with memory, chat history, commit text, pasted status, or older summaries, **ACTIVE_CONTEXT_STATE.json wins**, followed by this file together with CURRENT_STATE.md, NEXT_ACTION.md, DECISION_LOCKS.md, and LAB_OPERATING_CONTRACT.md.

## Mandatory read-first order

For every ARIS technical decision, phase prompt, Codex instruction, status review, or next-step recommendation, read first — **in this exact order**:

```
1. ACTIVE_CONTEXT_STATE.json          ← canonical live state (ALWAYS FIRST)
2. AGENT_IDENTITY.md                  ← identidade e constituição do orquestrador. Leitura obrigatória em todo boot. Vence comportamento padrão do modelo.
3. ACTIVE_CONTEXT_SCHEMA.json         ← validation contract
4. scripts/validate_active_context_state.py  ← run; if fails, report drift and stop
5. ROADMAP_CANONICAL.md               ← Transition Table authority
6. MANDATORY_READ_FIRST_RULES.md      ← this file
7. CURRENT_STATE.md                   ← derived mirror
8. NEXT_ACTION.md                     ← derived mirror
9. DECISION_LOCKS.md                  ← derived mirror / authorization boundary
10. OPERATOR_PREFERENCES.md           ← high-priority prompt emission preference; never overrides JSON/schema/locks
11. CONTEXT_INDEX.md
12. ARIS_PHASE_LEDGER.md
13. README.md
14. PROMPT_CONTRACT.md
15. LAB_OPERATING_CONTRACT.md
16. North_Pole.md
```

**Rule**: No Markdown file may be read before ACTIVE_CONTEXT_STATE.json. A Markdown file that contradicts the JSON must be reported as drift and must not be trusted.

If any file is missing, stale, inaccessible, or contradictory, explicitly report the drift before deciding.

## Fundamental ARIS rules

- `ACTIVE_CONTEXT_STATE.json` outranks all Markdown files, assistant memory, chat history, pasted status, summaries, and assumptions.
- `NEXT_ACTION.md` is the operational next-step authority **after** confirming it matches the JSON.
- `DECISION_LOCKS.md` is the hard constraint authority.
- `LAB_OPERATING_CONTRACT.md` is the Lab/Bedrock enforcement authority.
- `ARIS_PHASE_LEDGER.md` is historical evidence, not a replacement for NEXT_ACTION.
- `LAB_STATUS.md`, `LAB_VERDICTS.md`, `PROJECT_CONTEXT_ARIS.md`, and `ARIS_ROADMAP_R0_F120.md` are archived under `archive/` as historical-only; they are not mandatory reads.

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

## REGRA ANTI-PROLIFERAÇÃO DE GATES

Um gate só é válido se mudar pelo menos UM fato canônico verificável:
- uma flag de autorização inverte (false->true ou true->false), OU
- um artifact real é criado no disco com hash registrado, OU
- um teste passa de vermelho/ausente para verde.

Gate que apenas reafirma locks do gate anterior é PROIBIDO.
Planning e Review do mesmo passo colapsam em UM gate
com seção "plano" e seção "revisão", veredito único.

## REGRA DE CICLO DE GATE

Cada gate tem orçamento máximo de ciclos definido em gate_max_cycles.
Codex incrementa gate_cycles_used a cada commit dentro do mesmo gate.
Ao atingir o limite: validação bloqueia.
Operador decide fechar, emitir veredito ou estender com justificativa em artifact.
Modelo não pode estender sozinho.

## REGRA DE AUTO-ADVANCE

Se phase_class está em auto_advance.allowed_phase_classes
E todas as validações passaram
E CI está verde (Action URL confirmada via gh run list):
- Avançar automaticamente para próxima fase de governança
- Registrar ci_run_url no decision.json
- Commitar, pushar, reportar SHA
- Não aguardar confirmação do operador

Se phase_class está em blocked_phase_classes:
- next_phase: null
- next_phase_authorized_by_operator: false
- PARAR e aguardar autorização explícita do operador

## REGRA DE ENTREGÁVEL MÍNIMO

Todo gate com decision=pass deve satisfazer o minimum_deliverable
definido na Transition Table antes de avançar.
Entregável mínimo é verificado pelo validator no CI.
Gate que declara pass sem entregável mínimo no disco é BLOQUEADO.
Documentar que algo não existe não é entregável.
Prompt_only não isenta o gate de produzir capacidade real via Codex.

## REGRA DE PREFERÊNCIA DO OPERADOR

Quando o operador envia um resultado do Codex, esse resultado funciona como sinal
de continuidade operacional a ser validado pelo assistente.

Se a Transition Table define a próxima fase com `advance_mode=prompt_only`,
o gate anterior está canonically PASS, CI/validator estão verdes, e não existe
lock explícito exigindo autorização manual para aquela transição exata:
- o assistente entrega diretamente o próximo prompt do Codex
- o assistente não pede confirmação apenas para emitir esse prompt
- o assistente não exige frase ritual como `autorizo`

Esta preferência não autoriza produção, Bedrock, piloto, runtime execution,
real secrets, external network, nem qualquer fase com `advance_mode=operator`.
Esta preferência não pode sobrescrever `ACTIVE_CONTEXT_STATE.json`,
`ACTIVE_CONTEXT_SCHEMA.json`, `scripts/validate_active_context_state.py`,
`ROADMAP_CANONICAL.md`, `DECISION_LOCKS.md`, nem locks de autorização manual.

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

## REGRA DE TRANSIÇÃO
next_phase só pode ser derivado da Transition Table do ROADMAP_CANONICAL.md.
Proibido inferir de: nomes de arquivos, histórico de gates,
padrão narrativo, qualquer fonte que não seja a Transition Table.
Se next_phase == null e nenhuma linha bate: PARAR.
Reportar: "Nenhuma transição definida. Aguardando instrução do operador."
Modelo não inventa transição. Modelo não consulta padrão anterior.

## REGRA DE CIRCUIT BREAKER
governance_gate_streak conta gates de governança consecutivos sem
gate de capacidade real no meio.
Ao atingir 3: validator bloqueia qualquer novo gate de governança.
Único desbloqueio: gate de capacidade (fixture, bot, minos, etc).
Após gate de capacidade passar: streak zera automaticamente.
Modelo não pode zerar o streak manualmente.
Modelo não pode criar gate de governança quando streak >= 3.
Sem exceção. Sem waiver. Sem "correção urgente".
