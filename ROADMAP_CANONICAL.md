# ARIS Macro Roadmap Canonical Chain

This file is the canonical roadmap authority for active direction.
Live routing still comes from `ACTIVE_CONTEXT_STATE.json`; if this file conflicts with `ACTIVE_CONTEXT_STATE.json`, `ACTIVE_CONTEXT_STATE.json` wins and the drift is blocking.

## Canonical Chain

```text
Infernus revela.
Purgatorium corrige.
Infernus revalida.
BenchUX valida produto real.
Crisol refina.
Bedrock decide.
```

## Active Route

Latest completed phase: IF-11 Minos Final Verdict + Closure
Active next phase: null
Active next phase class: null
Standing authorization: canonroadmap approved by operator — see INFERNUS_STANDING_AUTHORIZATION.md
next_phase_authorized_by_operator: false
Post-Infernus technical direction document: `project_mirror/docs/purgatorium_full/purgatorium_roadmapcanon.md`
Infernus canonroadmap status: superseded/excludent/forensic-only with stub retained at `project_mirror/docs/infernus_full/infernus_full_canonroadmap.md` and forensic copy at `excludent/infernus/roadmaps/infernus_full_canonroadmap.md`
PURG-PRE route opening candidate: `artifacts/purgatorium/purg_pre_route_opening_candidate.json`
Live route terminalized by: `purg00_route_amendment_terminal_wait_state_operator_source_required`
Live route admission artifacts: `artifacts/purgatorium/purg_pre_route_admission_decision.json`, `artifacts/purgatorium/purg_pre_route_admission_summary.json`, `artifacts/purgatorium/purg_pre_route_admission_no_real_execution_attestation.json`
PURG-PRE canonical authority execution verified by: `purg_pre_canonical_authority_execution_pass`
PURG-00 operator review packet prepared by: `purg00_operator_review_packet_pass`
PURG-00 route admitted by: `purg00_route_admission_pass`
PURG-00 handoff intake / authority lock status: `purg00_handoff_intake_authority_lock_blocked`
PURG-00 route amendment terminal wait-state status: `purg00_route_amendment_terminal_wait_state_operator_source_required`
PURG-00 operator source packet intake: `purg00_operator_source_packet_intake_pass`
PURG-01 route admission review: `purg01_route_admission_review_pass`
Future PURG-00 admission candidate: `artifacts/purgatorium/purg_pre_future_purg00_admission_candidate.json`
Previous live route preserved historically before admission: `IF-08` / `infernus_full_execution`
PURG-00 execution: false
PURG-00 intake executed: true
Future PURG-01 triage readiness: REVIEW_ONLY_CANDIDATE
PURG-01 triage authorized: false
Operator primary source packet supplied and validated: true
Next non-execution step: `request_operator_authorization_for_purg01_route_admission`
Real execution (waves against real systems, runtime, apply): false — requires operator execution command
Product/Bedrock/real_apply/secrets/runtime real: false
W4 post-sync review remains historical and preserved the controlled execution closure with w4_execution_performed=true, execution_scope=synthetic_isolated_lab_only, synthetic_attack_cases_total=14, rollback_honesty_checks=6/6, duplicate_detection_checks=5/5, cost_enforcement_checks=3/3, and RHR=DDR=CER=1.0.
IF10 purgatorium handoff graph remains the canonical source packet for this sync with source_project_sha_verified_by_packet=57106d9780af7a807bd58ea6039af3a7b1b23701, source_active_context_sync_sha_verified_by_packet=7755a1506e6981d3f1c5b3534c7217112a12b960, source_root_manifest_sha256=3f750d814afbd4465a3abf4ee5a18ca563980619b887f0ad074ed2f8c1108660, source_graph_sha256=c786d5ba366a64c1ebf69daf7586721cfc8cddee9c4c54235f1f14c644292dd1, validated_handoff_ids=[IF09-FIND-001], contextual_candidate_ids=[IF09-FIND-002], excluded_invalid_ids=[IF09-FIND-003], and supporting_observation_ids=[IF09-OBS-001].
IF11 minos final verdict closure is canonical as pass; this PURG-00 sync now preserves the closed live route, records the operator-supplied primary source packet as validated from project commit ff9ade875ebf47bad8c4fde0311f576d958c1625 with packet sha256=6f616556d0a31ebba8e0bd647ccfd014f1955127856cc20d2deee2f6d7111e72 and CI_GREEN_CONFIRMED, records a review-only PURG-01 route-admission candidate, keeps PURG-01 unopened, and limits the next move to request_operator_authorization_for_purg01_route_admission without authorizing any real execution surface.
excludent/ remains excluded_from_context with read_by_default=false, authority=none, forensic_only.

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
| BENCH-01 | pass | CRISOL-01 | crisol | prompt_only | crisol refinement artifact with evidence |
| CRISOL-01 | pass | BEDROCK-01 | bedrock | operator | operator sign-off artifact |
| BEDROCK-01 | pass | null | product | operator | product promotion artifact |
