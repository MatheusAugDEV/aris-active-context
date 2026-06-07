# OPERATOR_PREFERENCES

This file is a high-priority operator preference layer for prompt emission behavior.
If this file conflicts with `ACTIVE_CONTEXT_STATE.json`, `ACTIVE_CONTEXT_SCHEMA.json`,
`scripts/validate_active_context_state.py`, `ROADMAP_CANONICAL.md`, the Transition
Table, or any explicit lock/manual authorization requirement, the higher canonical
authority wins and this file must not be used to justify action.

## SCOPE DISCIPLINE — Regras para Codex e ChatGPT

- O Codex não deve sair do escopo explícito do prompt. Se o prompt diz X, faça X e nada mais.
- Não solicite autorização para coisas que não estão no escopo do prompt atual.
- Não confirme locks que já estão confirmados na fase atual. INF-FULL-07 tem todos os locks de execução como `false` — isso não precisa ser reconfirmado a cada ciclo.
- Não peça autorização para produto, piloto, Bedrock, runtime, bots ou waves. Esses locks são permanentes até instrução explícita do operador que muda o estado.
- Não referencie F21, F32, F33 em nenhum contexto de ação futura. São ruído histórico.
- O `next_phase=null` significa aguardar. Não avance autonomamente.
- CI em progress só bloqueia se o CI pertence à fase ATUAL. CI de fases anteriores não bloqueia o loop.

## IF-08 Synthetic Wave Standing Authorization

For IF-08, synthetic isolated lab waves defined by the approved Infernus canonroadmap do not require a new per-wave operator permission prompt after their preflight/readiness gates pass.

The operator has explicitly authorized W0 and has instructed the system to stop requesting repeated permissions for synthetic IF-08 waves.

The assistant and Codex must not ask for ritual authorization before each synthetic isolated IF-08 wave when:
- the wave is listed in the approved canonroadmap;
- the wave preflight/readiness gate passed;
- all required contracts, oracles, controls, evidence outputs and stop conditions are present;
- CI is terminal green;
- no hard lock is violated;
- scope remains synthetic isolated lab only.

This standing authorization does not authorize:
- production or staging real systems;
- real_apply;
- product/pilot promotion;
- Bedrock final gate;
- secrets access;
- external network;
- dependency/package-manager mutation;
- irreversible real-world actions;
- any wave or action outside the approved canonroadmap.

### CI POLLING — REGRA PERMANENTE

Após qualquer push, não emita relatório final até o CI estar terminal. Execute:

Passo 1 — aguarde 30 segundos após o push.
Passo 2 — execute: `gh run list --limit 20`
Passo 3 — se qualquer workflow estiver `queued`, `waiting`, `requested` ou `in_progress`: aguarde 60 segundos e repita o Passo 2. Sem limite de iterações.
Passo 4 — somente quando todos os workflows estiverem em status terminal: classifique como `CI_GREEN_CONFIRMED` (todos `success`) ou `CI_FAILED` (qualquer `failure`).

Nunca emita relatório com CI pendente. Nunca entregue resultado pela metade. O relatório só existe quando o CI é terminal.

Se `CI_FAILED`: identifique o erro com `gh run view --log-failed`, repare, faça novo push, reinicie o polling do Passo 1.

## Prompt emission preference

When the operator sends a Codex result, that result is a continuity signal for the
assistant to validate. If the result is canonically PASS, the Transition Table
defines the next phase with `advance_mode=prompt_only`, CI/validator evidence is
green, and no explicit lock says operator/manual authorization is required for that
exact transition, the assistant should directly provide the next Codex prompt.

The assistant must not ask for confirmation just to send the next Codex prompt in
those cases, and must not require any ritual phrase such as `autorizo`.

When the operator has already explicitly authorized a gated chain, the assistant and
Codex must not ask for repeated confirmation for the next pre-execution gates in that
same chain. They should advance with prompt emission, Transition Table updates, and
phase patches while execution locks remain false.

## Safety boundary

This preference does not authorize production, Bedrock, pilot, runtime execution,
real secrets, external network, or any phase whose `advance_mode=operator`.

It also does not authorize bot execution, runtime start, Bedrock execution, product
promotion, secret access, dependency installation, real dry-run, or real apply for a
pre-execution gated chain. Those still require separate explicit authorization.

This preference cannot override:
- `ACTIVE_CONTEXT_STATE.json`
- `ACTIVE_CONTEXT_SCHEMA.json`
- `scripts/validate_active_context_state.py`
- `ROADMAP_CANONICAL.md`
- the Transition Table
- `DECISION_LOCKS.md`
- `next_phase_authorized_by_operator=false`
- any explicit manual/operator authorization requirement for the exact transition

## Non-authorization consequences

- next_phase remains `null` after a phase closes unless an explicit state transition is canonically recorded.
- `ACB-CAP-05` or any later phase is not auto-opened by this preference alone.
- `advance_mode=operator` still requires explicit operator authorization.
