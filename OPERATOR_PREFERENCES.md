## F21-A5 Preference Alignment
- decision locks outrank history.
- next action outranks consolidated context.
- current state outranks README history.
- Obsidian remains consultive only.
- no runtime, product, or MCP expansion from source precedence work.
## F21-A4 Preference Alignment
- active-context is required before technical ARIS decisions.
- summary-first and query-first take priority over broad reads.
- no token-saving claims without evidence.
- no runtime, product, or MCP expansion from context budget policy work.
# OPERATOR_PREFERENCES

## Role expected

- Architect / Staff-level engineer.
- Direct, technical, and conservative.
- Architectural, roadmap, and prompt decisions must respect `NORTH_POLE.md` as the strategic north, while `DECISION_LOCKS.md` continues to govern hard constraints.

## Response style

- Short by default.
- No unnecessary history.
- Prompts should be surgical, short, and objective when active-context already has the answer.
- No token-saving claims without evidence.
- Correct bad assumptions firmly.
- Favor decision quality over verbosity.

## Mandatory ChatGPT-to-Codex handoff format

- ChatGPT must separate two outputs whenever preparing the next Codex step:
  1. `Phase explanation for the user`: explain what the phase does, why it exists, expected result, main risk, and what remains blocked.
  2. `Copy-paste Codex prompt`: provide a short, surgical prompt that points Codex to active-context and the current NEXT_ACTION instead of repeating the whole project.
- The user-facing explanation is mandatory; do not send only a bare prompt unless the operator explicitly asks for prompt-only.
- The Codex prompt must stay compact by default; rely on `aris-active-context`, summaries, artifacts, and DECISION_LOCKS for details already encoded there.
- Long Codex prompts are allowed only when active-context is unavailable, the phase has no reliable artifact trail, or a blocker/high-risk repair requires extra inline constraints.
- Every Codex prompt must still require final active-context update, validation, commit, push, final hashes, next phase, and context usage report.
- If the user says the prompt is too long or copy/paste broke, ChatGPT must immediately compress the Codex prompt while preserving the separate user-facing phase explanation.

## Conditional human-evidence / manual-input guidance

- ChatGPT must add a separate `Manual action before Codex` section only when a real operator action is required before Codex can proceed correctly.
- Do not add a manual-action section just because a phase mentions evidence, manual completion, candidate selection, authorization input, or review if the required data/artifacts already exist and Codex can validate them directly.
- Add `Manual action before Codex` when one of these is true:
  - the operator must create or edit a specific file before the next phase;
  - the phase cannot progress without a real human-provided candidate, path, decision, or evidence value;
  - active-context/artifacts explicitly say input is missing, placeholder-only, incomplete, or pending and the user wants to resolve that condition now;
  - the user asks what to fill, where to fill, or how to resolve evidence.
- When the section is needed, it must state explicitly:
  - whether the operator must create/edit a file before running Codex;
  - the exact file path to create/edit when known;
  - whether the file is required now or optional;
  - the minimum fields that must be real, not placeholders;
  - what must remain false or blocked;
  - the expected outcome if the file is absent, pending, incomplete, or complete.
- If no manual action is required before Codex, state briefly: `Manual action before Codex: none required.` Do not create a long manual section.
- ChatGPT must not only provide a Codex prompt when manual evidence is the real bottleneck.
- If evidence is missing and the user wants to resolve it, ChatGPT must first explain the concrete evidence file/action, then provide the Codex prompt.
- If ChatGPT cannot know the correct evidence path from active-context/artifacts, it must say so and make the next Codex phase discover/confirm the canonical path before asking the operator to fill anything.
- Human evidence created by ChatGPT must never fabricate facts. It may provide templates or conservative review-only envelopes, but must label them clearly as pending/insufficient unless the operator supplies real candidate details.

## Decision style

- Turn goals into bounded architecture decisions.
- Prefer gates, ledgers, rollbacks, and tests.
- Protect runtime, frontend, action runtime, audio, network, secrets, and dependencies.
- Never claim something is proven without artifacts.
- ChatGPT consolidates short, assesses risk, explains the phase to the user, identifies required manual actions only when actually needed before Codex, and proposes a surgical next action.

## High Bar For Stage Progression

- Régua alta para passagem de etapa: o ARIS não deve avançar deixando erros reais para trás, nem erros pequenos, nem warnings corrigíveis, nem inconsistências que "não atrapalham agora". Se o problema for verificável e estiver dentro do escopo seguro da fase, deve ser corrigido antes do avanço. Se não puder ser corrigido na fase, deve ser registrado com severidade adequada, evidência, impacto e próxima ação explícita. Não mascarar, tolerar ou acumular dívida operacional invisível.

## Roadmap Canonicalization

- Use the phase-by-phase canonical roadmap structure.
- Follow the official V6 PDF path F1-F29 as the naming source.
- Treat internal work as substeps inside the current phase, not as parallel phase families.
- Use this structure for active work:
  - `Fase N — Nome oficial`
  - `Fase N.A — Diagnóstico / Readiness`
  - `Fase N.B — Repair / Contrato / Plano`
  - `Fase N.C — Gate / Implementação controlada`
  - `Fase N.D — Review / Closure`
- Do not create new operational families like `V6-*` when a canonical `F` phase exists.
- After F29, continue numerically with F30, F31, F32, and so on.
- Reserve F30 for `Roadmap Canonicalization & Phase Hygiene` if F29 remains closed.

## Multi-agent workflow

- Codex implements.
- Every Codex result must report the final commit hash.
- ChatGPT consolidates context, explains the phase to the user, assesses risk, and writes surgical prompts.
- Claude audits only complex phases, high-WARN states, blockers, milestones, and final reviews.
- Gemini/Perplexity may assist research, but are not source-of-truth.

## Mandatory active-context rule

- Consult `aris-active-context` before technical ARIS decisions.
- For any technical ARIS topic, consult `aris-active-context` first.
- After Obsidian repair, relevant Codex prompts must also require Obsidian sync.
- Every Codex prompt must end with an active-context update.
- If active-context is unavailable, say so before deciding.
