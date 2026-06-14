# ARIS ROADMAP CANONICAL — CAMADAS E OBJETIVOS

Status: MACRO_ROADMAP_CANONICAL_ACTIVE
Authority: macro roadmap authority
Live-state authority: ACTIVE_CONTEXT_STATE.json
Conflict rule: ACTIVE_CONTEXT_STATE.json > ARIS_BOOT.md > ROADMAP_CANONICAL.md > DECISION_LOCKS.md > phase-specific roadmaps > artifacts/docs > archive > excludent
Real execution authorized by this document: false
Product/Bedrock/real_apply/secrets/runtime real authorized by this document: false

This file is the canonical macro roadmap authority for active direction.
Live routing still comes from `ACTIVE_CONTEXT_STATE.json`; if this file conflicts with `ACTIVE_CONTEXT_STATE.json`, `ACTIVE_CONTEXT_STATE.json` wins and the drift is blocking.

Operator source for this macro chain: `operator_inputs/roadmap_aris_camadas_objetivos.md` (ROADMAP ARIS — CAMADAS E OBJETIVOS).

## Macro Chain — Camadas e Objetivos

```text
Infernus FULL
  ↓
Purgatorium FULL
  ↓
Infernus Revalidation
  ↓
BenchUX
  ↓
Crisol
  ↓
Polimento
  ↓
EXT-SEC 00→04
  ↓
Cinzel
  ↓
EXT-SEC 05→06
  ↓
Bedrock Gate
  ↓
Produto Parte 2 / Design Partner
  ↓
EXT-SEC 07→08 contínuo
```

### 1. Infernus FULL

- Natureza: adversarial ofensivo-controlado.
- Objetivo: revelar falhas reais do sistema sob condições adversariais controladas.
- Escopo principal: waves sintéticas isoladas, evidence bundle, vulnerability register, handoff graph e Minos verdict.
- Entrega esperada: evidence bundle, vulnerability register, handoff graph e Minos verdict.
- Gate de saída: Minos final verdict + closure pass, com handoff Purgatorium pronto.
- Limites explícitos: não promete segurança absoluta; não autoriza produto, Bedrock, real_apply, secrets ou runtime real.

### 2. Purgatorium FULL

- Natureza: corretiva/mitigadora.
- Objetivo: corrigir, mitigar ou colocar em quarentena os findings do Infernus.
- Escopo principal / sequência interna: PURG-PRE → PURG-00 → PURG-01 → PURG-02 → PURG-03 → PURG-Sx → PURG-04 → PURG-05 → PURG-RES → PURG-EXIT. `PURG-Sx` é track condicional, não fila obrigatória.
- Entrega esperada: findings corrigidos, mitigados ou quarentenados, com evidência registrada.
- Gate de saída: PURG-EXIT com evidência completa e sem reset pendente.
- Limites explícitos: Purgatorium não fecha finding; GREEN sem reset é inválido; residual não vira resolved.

### 3. Infernus Revalidation

- Natureza: validação adversarial pós-correção.
- Objetivo: revalidar os findings tratados pelo Purgatorium.
- Escopo principal: única camada que pode declarar `finding_closed`, `finding_regressed`, `finding_partially_mitigated`, `finding_still_open`, `new_regression_found`.
- Entrega esperada: veredito de revalidação por finding.
- Gate de saída: veredito de revalidação registrado para todos os findings em escopo.
- Limites explícitos: nenhuma outra camada pode declarar esses status de finding.

### 4. BenchUX

- Natureza: validação de produto/experiência.
- Objetivo: validar posicionamento competitivo e experiência.
- Escopo principal: comparação com alternativas reais no momento da execução.
- Entrega esperada: relatório de benchmark comparativo de UX/posicionamento.
- Gate de saída: comparação registrada com evidência, não apenas narrativa.
- Limites explícitos: não é marketing.

### 5. Crisol

- Natureza: consolidação.
- Objetivo: consolidar o sistema completo.
- Escopo principal: remoção de contradições internas.
- Entrega esperada: sistema transformado em produto técnico coeso.
- Gate de saída: ausência de contradições internas relevantes registradas.
- Limites explícitos: não introduz capacidade nova além de consolidação.

### 6. Polimento

- Natureza: limpeza cirúrgica.
- Objetivo: preparar o repositório para EXT-SEC/SAST/SCA/secret scanning com menos ruído.
- Escopo principal: limpeza sem capacidade nova.
- Entrega esperada: repositório limpo, pronto para varreduras de segurança.
- Gate de saída: limpeza concluída sem introdução de capacidade nova.
- Limites explícitos: sem capacidade nova; sem mudança funcional.

### 7. EXT-SEC 00→04

- Natureza: programa defensivo pré-Bedrock.
- Objetivo: preparar o sistema defensivamente antes do Bedrock Gate.
- Escopo principal / sequência interna: artifact-first, sem sistema vivo. Source ledger primário, threat model, hardening, fixtures sintéticas, closeout.
- Entrega esperada: artifacts de segurança defensiva (ledger, threat model, hardening plan, fixtures, closeout).
- Gate de saída: closeout EXT-SEC-04 com todos os artifacts presentes.
- Limites explícitos: artifact-first; sem sistema vivo; sem runtime real.

### 8. Cinzel

- Natureza: validação de automação aplicada.
- Objetivo: validar automação útil em SMB brasileiro simulado.
- Escopo principal: mínimo 5 cenários/workflows.
- Entrega esperada: métricas de tempo, custo, aprovação, rollback, retry e artifacts.
- Gate de saída: métricas completas registradas para todos os cenários mínimos.
- Limites explícitos: ambiente simulado; sem cliente real.

### 9. EXT-SEC 05→06

- Natureza: segurança ofensiva autorizada externa.
- Objetivo: DAST autorizado / pentest externo / retest.
- Escopo principal: staging-prod isolado.
- Entrega esperada: relatório de DAST/pentest e retest.
- Gate de saída: autorização, escopo, janela, contas de teste, dados sintéticos, rollback e legal authorization todos documentados e atendidos.
- Limites explícitos: exige autorização, escopo, janela, contas de teste, dados sintéticos, rollback e legal authorization.

### 10. Bedrock Gate

- Natureza: gate máximo de decisão.
- Objetivo: decidir produto real.
- Escopo principal: não é fase de construção.
- Entrega esperada: decisão explícita de Bedrock (PASS/WARN/BLOCK/NEEDS_REVIEW/REGRESSION/OBSOLETE).
- Gate de saída: decisão explícita do operador.
- Limites explícitos: só ocorre depois de Infernus, Purgatorium, Revalidation, BenchUX, Crisol, Polimento, EXT-SEC 00→04, Cinzel e EXT-SEC 05→06.

### 11. Produto Parte 2 / Design Partner

- Natureza: comercialização controlada.
- Objetivo: primeiro uso real.
- Escopo principal: vertical, ICP, prospects, contrato, pricing, onboarding, suporte e feedback.
- Entrega esperada: design partner ativo com feedback estruturado.
- Gate de saída: onboarding e ciclo de feedback inicial documentados.
- Limites explícitos: somente após Bedrock Gate explícito.

### 12. EXT-SEC 07→08 contínuo

- Natureza: segurança contínua pós-produto.
- Objetivo: manter segurança contínua após o início de produto.
- Escopo principal: vulnerability management, retest, adversarial emulation, incident response, backup/restore drills, tenant isolation review.
- Entrega esperada: ciclo contínuo de segurança operacional documentado.
- Gate de saída: não aplicável (contínuo).
- Limites explícitos: contínuo; depende da existência de produto ativo (camada 11).

## Princípio final

O ARIS não vira produto porque parece pronto.
O ARIS vira produto quando sobreviveu a ataque,
corrigiu o que foi encontrado,
foi revalidado,
foi comparado,
foi consolidado,
foi limpo,
foi auditado,
foi demonstrado,
foi testado externamente,
e passou por decisão explícita de Bedrock.

## Active Route

Latest completed phase: PURG-04 Track A Pointer Residual Repair Patch Packet
Current phase_id/current_phase_id: PURG-04
Current status/status: purg04_track_a_pointer_residual_repair_patch_pass
Decision: pass
Active next phase: PURG04_TRACK_A_PATCH_REVIEW_AND_MERGE_DECISION
Active next phase class: purgatorium_route_admission
next_phase_authorized_by_operator: false
next_phase_execution_authorization: false
operator_approval_packet_review_is_execution_approval: false
real_apply_authorized: false
runtime_integration_allowed: false
production_authorized: false
product_ready: false
secrets_access_authorized: false
Track A patch applied in cleanroom branch only.
Patch branch: `codex/purg04-track-a-pointer-residual-repair-20260612`
Patch commit: `1e9a04a02846f3261ae72d0c95fbee6b0163b45b`
Latest completed project commit SHA: `6312302ea45b72ddc310b2b33f56245be65b99dc`
Latest completed CI state: `CI_GREEN_CONFIRMED`
Merge to Project_ARIS main: `NOT AUTHORIZED`
IF09-FIND-001 remains open; closure only via Infernus Revalidation.
Project_ARIS main workspace remains untouched.
Next canonical step: `PURG04_TRACK_A_PATCH_REVIEW_AND_MERGE_DECISION`
Historical stale mirror appendix preserved only for validator compatibility; non-authoritative:
Latest completed phase: IF-11 Minos Final Verdict + Closure
Active next phase: PURG-01
Standing authorization: canonroadmap approved by operator — see INFERNUS_STANDING_AUTHORIZATION.md
Post-Infernus technical direction document: `project_mirror/docs/purgatorium_full/purgatorium_roadmapcanon.md`
PURG-PRE route opening candidate: `artifacts/purgatorium/purg_pre_route_opening_candidate.json`
Live route terminalized by: `purg00_route_amendment_terminal_wait_state_operator_source_required`
PURG-PRE canonical authority execution verified by: `purg_pre_canonical_authority_execution_pass`
PURG-00 operator review packet prepared by: `purg00_operator_review_packet_pass`
PURG-00 route admitted by: `purg00_route_admission_pass`
PURG-00 handoff intake / authority lock status: `purg00_handoff_intake_authority_lock_blocked`
PURG-00 route amendment terminal wait-state status: `purg00_route_amendment_terminal_wait_state_operator_source_required`
PURG-00 operator source packet intake: `purg00_operator_source_packet_intake_pass`
PURG-01 route admission review: `purg01_route_admission_review_pass`
PURG-01 route admitted by: `purg01_route_admission_pass`
PURG-01 triage readiness review: `purg01_triage_readiness_review_pass`
PURG-01 triage planning gate: `purg01_triage_planning_gate_pass`
PURG-01 triage authorization gate: `purg01_triage_authorization_gate_pass`
PURG-01 controlled triage execution gate: `purg01_controlled_triage_execution_gate_pass`
PURG-00 execution: false
PURG-00 intake executed: true
Future PURG-01 triage readiness: CONTROLLED_EXECUTION_GATE_PASS
PURG-01 triage authorized: true
Operator primary source packet supplied and validated: true
Next non-execution step: `execute_purg01_controlled_triage_artifact_only`
Real execution (waves against real systems, runtime, apply): false — requires operator execution command
W4 post-sync review remains historical and preserved the controlled execution closure with w4_execution_performed=true, execution_scope=synthetic_isolated_lab_only, synthetic_attack_cases_total=14, rollback_honesty_checks=6/6, duplicate_detection_checks=5/5, cost_enforcement_checks=3/3, and RHR=DDR=CER=1.0.
IF10 purgatorium handoff graph remains the canonical source packet for this sync with source_project_sha_verified_by_packet=57106d9780af7a807bd58ea6039af3a7b1b23701, source_active_context_sync_sha_verified_by_packet=7755a1506e6981d3f1c5b3534c7217112a12b960, source_root_manifest_sha256=3f750d814afbd4465a3abf4ee5a18ca563980619b887f0ad074ed2f8c1108660, source_graph_sha256=c786d5ba366a64c1ebf69daf7586721cfc8cddee9c4c54235f1f14c644292dd1, validated_handoff_ids=[IF09-FIND-001], contextual_candidate_ids=[IF09-FIND-002], excluded_invalid_ids=[IF09-FIND-003], and supporting_observation_ids=[IF09-OBS-001].
IF11 minos final verdict closure is canonical as pass; this PURG sync keeps the validated operator source packet from project commit ff9ade875ebf47bad8c4fde0311f576d958c1625 with packet sha256=6f616556d0a31ebba8e0bd647ccfd014f1955127856cc20d2deee2f6d7111e72 and CI_GREEN_CONFIRMED, keeps PURG-01 admitted through route-admission-only authority, records explicit operator authorization for PURG-01 triage using the planning-gate project commit 2bfefac900c6c3e7c3f016b7a790570587e57fbb and active-context commit c8ee8c8225e74ffa8ba56aae916343fcd3d55b0d, records the controlled triage execution gate as pass from the operator packet plus IF10 handoff graph evidence, keeps triage execution unopened, and limits the next move to execute_purg01_controlled_triage_artifact_only without authorizing any real execution surface.

Standing Authorization Policy
Historical note: the operator-approved `infernus_full_canonroadmap.md` granted standing authorization for Infernus FULL while that program was active. After IF-11, that document is superseded and forensic-only. The post-Infernus technical direction document is `project_mirror/docs/purgatorium_full/purgatorium_roadmapcanon.md`, but it does not open a live route by itself and does not authorize real execution.
Exception: execution of waves against real system, real apply, product promotion, Bedrock require explicit operator execution command.

## Transition Table

| current_phase_id | decision | next_phase_id | next_phase_class | advance_mode | minimum_deliverable |
|------------------|----------|---------------|------------------|--------------|---------------------|
| AC-REPAIR-01 | pass | AC-OBS-02 | observability | auto | anti_proliferation_rule_active=true in JSON |
| AC-OBS-02 | pass | AC-TRANS-03 | transition_engine | auto | assert_mirror_sync.py exists and passes |
| AC-TRANS-03 | pass | AC-CONTRACT-04 | contract | auto | minimum_deliverable enforcement in validator for all pass transitions |
| AC-CONTRACT-04 | pass | AC-BREAK-05 | circuit_breaker | auto | governance_gate_streak field in state with validator enforcement |
| AC-BREAK-05 | pass | ACB-CORE-01 | capability_build | prompt_only | acb_decision artifact exists |
| INF-MAT-01 | pass | INF-BOT-01 | bot_execution | prompt_only | at least 1 bot execution log with hash in artifacts/ |
| INF-BOT-01 | pass | INF-MINOS-01 | minos_verdict | prompt_only | minos verdict JSON with deterministic threshold results |
| INF-MINOS-01 | pass | PURG-01 | purgatorium | prompt_only | at least 1 finding record with severity and status |
| PURG-01 | pass | ACB-CORE-01 | capability_build | prompt_only | acb_decision artifact exists |
| ACB-CORE-01 | pass | ACB-CORE-02 | capability_build | prompt_only | uv.lock + pip-audit CI gate + SBOM exists |
| ACB-CORE-02 | pass | ACB-CAP-01 | capability_build | prompt_only | __all__ snapshot committed |
| ACB-CAP-01 | pass | ACB-CAP-02 | capability_build | prompt_only | FastAPI health check + auth passing |
| ACB-CAP-02 | pass | ACB-CAP-03 | capability_build | prompt_only | MCP sandbox running + STDIO banned |
| ACB-CAP-03 | pass | ACB-CAP-04 | capability_build | prompt_only | runtime public API documented |
| ACB-CAP-04 | pass | ACB-CAP-05 | capability_build | prompt_only | pilot gates defined |
| ACB-CAP-05 | pass | INF-FULL-01 | infernus_full | operator | all ACB complete + Infernus spec exists |
| INF-FULL-01 | pass | INF-FULL-02 | infernus_full | canonroadmap | scope charter decision + scope matrix + module scope manifest + charter markdown |
| INF-FULL-02 | pass | INF-FULL-03 | infernus_full | canonroadmap | historical infernus_full_canonroadmap.md + if00 transition/hermeticity + if01 ledger + if02 ontology/coverage + if03 oracle pack + if04 bot/permission pack |
| INF-FULL-03 | pass | INF-FULL-04 | infernus_full | canonroadmap | scenario pack + controls design + harness readiness + sandbox/cost/quota/replay/kill-switch contracts |
| INF-FULL-04 | pass | INF-FULL-05 | infernus_full | canonroadmap | if07 pre-execution review decision artifact + no bot/runtime execution attestation + scenario-count normalization evidence + validator evidence |
| INF-FULL-05 | pass | INF-FULL-06 | infernus_full_excludent_cleanup | canonroadmap | excludent policy + move manifest + only-canonroadmap-visible evidence + validator evidence |
| INF-FULL-06 | pass | INF-FULL-07 | infernus_full_execution_authorization | canonroadmap | IF-08 authorization decision artifact + no execution attestation + successor validation matrix + validator evidence |
| INF-FULL-07 | pass | PURG-PRE | purgatorium_full_authority_materialization | operator | purg_pre_route_admission_decision.json + operator review packet + schema/validator admission + no-real-exec attestation |
| PURG-PRE | pass | PURG-00 | purgatorium_full_intake | operator | purg00_route_admission_decision.json + purg00_operator_review_packet + schema/validator admission + no-real-exec attestation |
| PURG-00 | pass | PURG-01 | purgatorium_route_admission | operator | purg01_route_admission_decision.json + operator authorization + no-real-exec attestation + validator evidence |
| BENCH-01 | pass | CRISOL-01 | crisol | prompt_only | crisol refinement artifact with evidence |
| CRISOL-01 | pass | BEDROCK-01 | bedrock | operator | operator sign-off artifact |
| BEDROCK-01 | pass | null | product | operator | product promotion artifact |

## Macro Transition Table — Future Extension (documental, not yet active)

The macro transitions below describe the high-level "Camadas e Objetivos" chain
(Infernus FULL → ... → EXT-SEC 07→08 contínuo). They are documental references only.
They do not appear in the live `## Transition Table` above, are not consumed by
`scripts/validate_active_context_state.py`, and do not change `active_next_phase`,
`next_phase`, `current_phase_id`, or any live-route field in `ACTIVE_CONTEXT_STATE.json`.

The full proposed mapping, including a `Phase ID Mapping` against existing
phase IDs (e.g. `PURG-01`..`PURG-EXIT`, `INF-FULL-*`, `BEDROCK-01`), is recorded in:

`artifacts/roadmap/macro_transition_table_extension_candidate.json`

```text
INF-FULL -> PURG-FULL
PURG-FULL -> INF-REVALIDATION
INF-REVALIDATION -> BENCHUX
BENCHUX -> CRISOL
CRISOL -> POLIMENTO
POLIMENTO -> EXT-SEC-00
EXT-SEC-00 -> EXT-SEC-01
EXT-SEC-01 -> EXT-SEC-02
EXT-SEC-02 -> EXT-SEC-03
EXT-SEC-03 -> EXT-SEC-04
EXT-SEC-04 -> CINZEL
CINZEL -> EXT-SEC-05
EXT-SEC-05 -> EXT-SEC-06
EXT-SEC-06 -> BEDROCK
BEDROCK -> PRODUCT-P2-DESIGN-PARTNER
PRODUCT-P2-DESIGN-PARTNER -> EXT-SEC-07
EXT-SEC-07 -> EXT-SEC-08-CONTINUOUS
```

Activation of any row in this candidate table requires: an explicit operator
gate, schema/validator support for the new phase_id/phase_class values, an
admission decision artifact analogous to the PURG-PRE/PURG-00/PURG-01 pattern,
and CI terminal green. None of these conditions are satisfied by this document
alone.
