# Roadmap Canônico ARIS V1.2

## Purpose
This file is the active roadmap authority for ARIS after active-context canonicalization. It defines the canonical macrostructure, the non-negotiable locks, the invariants, the pre-pilot gaps, and the distinction between active direction, preserved history, and future amendments.

## Official Phrase
ARIS não promete automação. ARIS prova automação.

## Canonical Macrostructure
0. Strategic Reset
1. Product Loop Demonstrável
2. Hardening Base H0-H7
   - H0 — Invariants by Layer Numeric Contract Gate
   - H1 — Golden Tasks Baseline Gate
   - H2 — Ledger Chain + Replay Baseline Gate
   - H3 — Context Engineering Baseline Gate
   - H4 — Observability + Cost/Time + Quota Gate
   - H5 — Degraded Mode + Failure UX Gate
   - H6 — Eval Harness Baseline Gate
   - H7 — Hardening Base Closure Gate
2.5. Lab Real Simulation Pack
3. ARIS Infernus Lab FULL
4. ARIS Final Crisol FULL
5. Productatization Gate
6. Primeiro Piloto Controlado
7. SIP — Sistema Imunológico Permanente

## Current Canonical Position
- Strategic Reset: `PASS`
- Product Loop Demonstrável: `PASS`
- Product Loop L1.15 closure hash: `sha256:bd2974c9caf880dc3869eaa5696988d28f54a2f1c37a20d8295ce9b59270a5f0`
- H0 exists as a materialized design brief and must be reviewed against this roadmap before any later Hardening Base advancement.
- The active next phase is `H0 Design Brief Alignment / Hardening Base H0 Roadmap V1.2 Review Gate`.

## Absolute Pre-Pilot Lock
Nenhum piloto, cliente, design partner operacional ou uso externo do ARIS é autorizado antes de:

1. `Product Loop Demonstrável = PASS`
2. `Hardening Base = PASS`
3. `Lab Real Simulation Pack = PASS`
4. `ARIS Infernus Lab FULL = PASS`
5. `ARIS Final Crisol FULL = PASS`
6. `Productatization Gate = PASS`

`Primeiro Piloto Controlado` exists only after all prior locks above are materially passed.

## 16 Core Priority Invariants
Every next phase, artifact, gate, design decision, implementation decision, and roadmap advancement must be evaluated against these 16 Core Priority Invariants:

1. Determinismo — mesmo input, mesmo output; sem variação aleatória em decisões críticas.
2. Tipagem / Type-Safety — todo dado tem schema declarado e validado; sem coerção silenciosa.
3. Isolamento — camadas, processos e contextos não vazam estado entre si.
4. Governança — toda ação passa por gate autorizado; nada executa fora de plano aprovado.
5. Compressão de Contexto — contexto entregue ao LLM é o mínimo necessário, não o máximo possível.
6. Sincronismo — ordem de eventos é preservada e verificável; sem race conditions silenciosas.
7. Densidade Cognitiva — cada token de contexto carrega informação relevante; sem ruído ou redundância.
8. Autoavaliação — o sistema sabe quando não sabe; produz confiança calibrada, não certeza falsa.
9. Regressão / Testes — toda mudança é validada contra suite de golden tasks antes de merge.
10. Rastreabilidade — toda operação tem origem, autor, hora e hash registrados no ledger.
11. Roteamento — cada request vai para o componente correto baseado em risk class, não em heurística.
12. Idempotência — executar a mesma operação N vezes produz o mesmo efeito que executar 1 vez.
13. Resiliência — falha de dependência tem comportamento especificado, nunca undefined behavior.
14. Modularidade — componentes têm fronteiras claras; substituição não quebra contrato de camada.
15. Autonomia — sistema decide dentro do envelope autorizado; nunca fora dele.
16. Eficiência — custo e tempo por operação são medidos, orçados e auditáveis.

Nothing passes without real PASS on applicable priorities. WARN does not unlock critical advancement.

## 9 lacunas pré-piloto
Roadmap V1.2 incorporates the following 9 lacunas pré-piloto:

1. Determinism Verification Suite
2. Chaos Engineering Interno
3. Property-Based Testing
4. Performance Regression Detection
5. Reproducibility Beyond Replay
6. Static Analysis + Type Coverage
7. Audit Log Tamper Detection
8. Capability Handle Lifecycle Hardening
9. Documentation as Contract

## Efficiency Rule
Eficiência não será otimizada removendo governança.

Efficiency may be optimized through:
- context budget
- risk-based execution
- observability
- quota
- replay
- evidence-based cache
- harness profiles
- governed fast path
- SIP

Governed fast path can only exist after:
- invariants are materially enforced
- golden tasks baseline exists
- ledger or replay baseline exists
- cost or time baseline exists

## Active vs Historical vs Amendments
Active direction:
- `CURRENT_STATE.md`
- `NEXT_ACTION.md`
- `DECISION_LOCKS.md`
- `CONTEXT_INDEX.md`
- `ARIS_PHASE_LEDGER.md`
- this file
- `ROADMAP_AMENDMENT_PROTOCOL.md`

Historical preserved material:
- legacy Bedrock files
- Lab files
- roadmap overlays
- superseded roadmap tombstones
- historical ledger notes

Historical preserved material is not active roadmap authority unless a later canonical gate explicitly reactivates it.

Future amendments:
- must follow `ROADMAP_AMENDMENT_PROTOCOL.md`
- must not be applied silently
- must preserve historical audit trail

## Non-Authorization
This roadmap does not authorize:
- runtime mutation by itself
- frontend mutation by itself
- voice or audio mutation by itself
- action runtime mutation by itself
- backend mutation by itself
- network use by itself
- dependency installation by itself
- pilot, customer, or commercial use by itself
