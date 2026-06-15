# PURGATORIUM — Remaining Roadmap Canon (Technical Trail)

> **Subordinate technical trail.** This roadmap is the canonical *remaining* technical
> trail of the Purgatorium layer. It is subordinate to `ACTIVE_CONTEXT_STATE.json` and
> `ROADMAP_CANONICAL.md`. **It does not activate a successor row by itself.** The live
> Transition Table only changes through a separate, operator-authorized gate.

- artifact_id source: `artifacts/purgatorium/purgatorium_remaining_roadmap_canonicalization_packet.json`
- roadmap_status: `canonical_technical_trail_pending_active_transition_activation`
- generated_from: `purgatorium_remaining_roadmap_phase_graph.json` + `purgatorium_remaining_roadmap_transition_table_candidate.json`

## Boot Receipt

```text
SHA lido (ACTIVE_CONTEXT_STATE.json): 0e7acd4d81707502e1970bed56d2d7660e37ff0b21183ff82152f378aba385a4
git HEAD / origin/main: a8cd1416b81e0c29f4d94f28c17f673b9462556a (clean at generation)
phase_id = current_phase_id: PURG_RESIDUAL_RISK_CARRY_FORWARD_PACKET
status: purg_residual_risk_carry_forward_route_opening_pass
decision: pass
next_phase: null
active_next_phase: null
governance_gate_streak: 0
execution_locks todos false: SIM
IF09-FIND-001: open
remediation_proven: false
finding_closed: false
Project_ARIS latest_completed_project_commit_sha: 7883af5a32c629026bfc6dc15ebee4ebbcadd295
```

## Status Atual

O Purgatorium **não está fechado**. A rota residual `PURG_RESIDUAL_RISK_CARRY_FORWARD_PACKET`
foi aberta artifact-only por autorização explícita do operador e é **terminal** na live
Transition Table (sem sucessor). `IF09-FIND-001` permanece `open`; `remediation_proven=false`
é preservado; nenhum lock de execução real foi aberto; `Project_ARIS` permanece no commit
aceito `7883af5a...`. O fechamento do finding é exclusivo da camada **Infernus Revalidation**.

## Premissas

- O estado atual não fecha Purgatorium.
- `PURG_RESIDUAL_RISK_CARRY_FORWARD_PACKET` é terminal até o operador aprovar amendment/route opening.
- A rota restante não pode pular revalidação.
- `PURG-EXIT` não fecha finding por si só.
- Infernus Revalidation é a única camada habilitada a provar closure para `IF09-FIND-001`.
- Antes de qualquer closure: revalidação passa, evidência é adjudicada, `remediation_proven=true`
  tem gate próprio, finding close tem gate próprio, e o state update é separado e validado.
- Produto/Bedrock ficam bloqueados até gates próprios pós-revalidação/exit.
- O baseline global vermelho do `Project_ARIS` é tratado explicitamente (defer ou repair).

## Limites (este gate de canonicalização)

- Não altera `ACTIVE_CONTEXT_STATE.json`.
- Não altera a live Transition Table de `ROADMAP_CANONICAL.md`.
- Não executa `PURG-EXIT`, Infernus Revalidation, runtime, proof-loop, testes do `Project_ARIS` ou real_apply.
- Não fecha `IF09-FIND-001` e não marca `remediation_proven=true`.
- CI verde do GitHub **não** é tratado como prova de que a suite local global do `Project_ARIS` está verde.

## Tabela de Fases (R0–R14 + loopbacks + sentinels)

| R | phase_id | type | operator | exec | state_change | next_on_pass | next_on_block |
|---|----------|------|----------|------|--------------|--------------|---------------|
| R0 | `PURG_CURRENT_TERMINAL_STATE_LOCK` | artifact_only_governance_lock | no | no | no | PURG_REMAINING_ROADMAP_ACTIVATION_DECISION_PACKET | BLOCKED_OPERATOR_DIRECTION_REQUIRED |
| R1 | `PURG_REMAINING_ROADMAP_ACTIVATION_DECISION_PACKET` | operator_route_governance_decision | yes | no | no | `TRACK_EXIT_FIRST` → PURG_EXIT_READINESS_PACKET<br>`TRACK_REVALIDATION_FIRST` → INF_REVALIDATION_ROUTE_ADMISSION_PACKET<br>`TRACK_BASELINE_STABILIZATION_FIRST` → PURG_PROJECT_ARIS_GLOBAL_BASELINE_STABILIZATION_DECISION_PACKET | BLOCKED_OPERATOR_DIRECTION_REQUIRED |
| R2 | `PURG_EXIT_READINESS_PACKET` | artifact_only_exit_readiness | no | no | no | PURG_EXIT_HANDOFF_PACKAGE_PACKET | BLOCKED_OPERATOR_DIRECTION_REQUIRED |
| R3 | `PURG_EXIT_HANDOFF_PACKAGE_PACKET` | artifact_only_handoff | no | no | no | INF_REVALIDATION_ROUTE_ADMISSION_PACKET | BLOCKED_OPERATOR_DIRECTION_REQUIRED |
| R4 | `PURG_PROJECT_ARIS_GLOBAL_BASELINE_STABILIZATION_DECISION_PACKET` | artifact_only_decision | yes | no | no | `REPAIR_BASELINE_BEFORE_REVALIDATION` → PURG_PROJECT_ARIS_BASELINE_REPAIR_READINESS_PACKET<br>`DEFER_TO_INFERNUS_REVALIDATION` → INF_REVALIDATION_ROUTE_ADMISSION_PACKET | BLOCKED_OPERATOR_DIRECTION_REQUIRED |
| R4A | `PURG_PROJECT_ARIS_BASELINE_REPAIR_READINESS_PACKET` | artifact_only_readiness | no | no | no | PURG_PROJECT_ARIS_BASELINE_REPAIR_OPERATOR_AUTHORIZATION_PACKET | BLOCKED_OPERATOR_DIRECTION_REQUIRED |
| R4B | `PURG_PROJECT_ARIS_BASELINE_REPAIR_OPERATOR_AUTHORIZATION_PACKET` | operator_gate | yes | no | no | PURG_PROJECT_ARIS_BASELINE_REPAIR_EXECUTION_PACKET | BLOCKED_OPERATOR_DIRECTION_REQUIRED |
| R4C | `PURG_PROJECT_ARIS_BASELINE_REPAIR_EXECUTION_PACKET` | controlled_execution_project_aris_baseline_repair | yes | yes | no | INF_REVALIDATION_ROUTE_ADMISSION_PACKET | BLOCKED_OPERATOR_DIRECTION_REQUIRED |
| R5 | `INF_REVALIDATION_ROUTE_ADMISSION_PACKET` | route_admission_artifact_only | yes | no | no | INF_REVALIDATION_READINESS_PACKET | BLOCKED_OPERATOR_DIRECTION_REQUIRED |
| R6 | `INF_REVALIDATION_READINESS_PACKET` | artifact_only_readiness | no | no | no | INF_REVALIDATION_OPERATOR_AUTHORIZATION_PACKET | BLOCKED_OPERATOR_DIRECTION_REQUIRED |
| R7 | `INF_REVALIDATION_OPERATOR_AUTHORIZATION_PACKET` | operator_gate | yes | no | no | INF_REVALIDATION_EXECUTION_PACKET | BLOCKED_OPERATOR_DIRECTION_REQUIRED |
| R8 | `INF_REVALIDATION_EXECUTION_PACKET` | controlled_execution_only_after_R7_pass | yes | yes | no | INF_REVALIDATION_RESULT_ADJUDICATION_PACKET | INF_REVALIDATION_FAILURE_LOOPBACK_TRIAGE_PACKET |
| R8F | `INF_REVALIDATION_FAILURE_LOOPBACK_TRIAGE_PACKET` | artifact_only_failure_triage | no | no | no | `PLAN_REVISION` → PURG03_REMEDIATION_PLAN_REVISION_PACKET<br>`PATCH_REVISION` → PURG04_TRACK_A_PATCH_REVISION_PACKET<br>`BASELINE_REPAIR` → PURG_PROJECT_ARIS_BASELINE_REPAIR_READINESS_PACKET<br>`OPERATOR_DIRECTION` → BLOCKED_OPERATOR_DIRECTION_REQUIRED | BLOCKED_OPERATOR_DIRECTION_REQUIRED |
| R9 | `INF_REVALIDATION_RESULT_ADJUDICATION_PACKET` | artifact_only_adjudication | no | no | no | PURG_REMEDIATION_PROVEN_DECISION_PACKET | BLOCKED_OPERATOR_DIRECTION_REQUIRED |
| R10 | `PURG_REMEDIATION_PROVEN_DECISION_PACKET` | decision_gate | no | no | no | PURG_FINDING_CLOSURE_ELIGIBILITY_PACKET | BLOCKED_OPERATOR_DIRECTION_REQUIRED |
| R11 | `PURG_FINDING_CLOSURE_ELIGIBILITY_PACKET` | artifact_only_eligibility | no | no | no | PURG_FINDING_CLOSE_OPERATOR_PACKET | BLOCKED_OPERATOR_DIRECTION_REQUIRED |
| R12 | `PURG_FINDING_CLOSE_OPERATOR_PACKET` | operator_gate | yes | no | no | PURG_FINDING_CLOSE_CANONICAL_STATE_UPDATE_PACKET | BLOCKED_OPERATOR_DIRECTION_REQUIRED |
| R13 | `PURG_FINDING_CLOSE_CANONICAL_STATE_UPDATE_PACKET` | canonical_state_update | yes | no | yes | PURG_FINAL_EXIT_PACKET | BLOCKED_OPERATOR_DIRECTION_REQUIRED |
| R14 | `PURG_FINAL_EXIT_PACKET` | exit_gate | yes | no | yes | BENCHUX_OR_MACRO_HANDOFF_ADMISSION_PACKET | BLOCKED_OPERATOR_DIRECTION_REQUIRED |
| LB-PLAN | `PURG03_REMEDIATION_PLAN_REVISION_PACKET` | artifact_only_loopback_revision | no | no | no | PURG04_TRACK_A_PATCH_REVISION_PACKET | BLOCKED_OPERATOR_DIRECTION_REQUIRED |
| LB-PATCH | `PURG04_TRACK_A_PATCH_REVISION_PACKET` | artifact_only_loopback_revision | no | no | no | INF_REVALIDATION_ROUTE_ADMISSION_PACKET | BLOCKED_OPERATOR_DIRECTION_REQUIRED |
| SENTINEL | `BLOCKED_OPERATOR_DIRECTION_REQUIRED` | terminal_block_sentinel | yes | no | no | — | — |
| SENTINEL | `BENCHUX_OR_MACRO_HANDOFF_ADMISSION_PACKET` | external_macro_handoff_sentinel | yes | no | no | — | — |

Entry: the live phase `PURG_RESIDUAL_RISK_CARRY_FORWARD_PACKET` is frozen by **R0**
(`PURG_CURRENT_TERMINAL_STATE_LOCK`); the first activation transition is `live → R1`,
gated by the R0 lock artifact.

## Branch Logic

- **R1** (activation decision) branches:
  - `TRACK_EXIT_FIRST` → R2 (exit readiness)
  - `TRACK_REVALIDATION_FIRST` → R5 (revalidation route admission)
  - `TRACK_BASELINE_STABILIZATION_FIRST` → R4 (baseline stabilization decision)
- **R4** branches: `REPAIR_BASELINE_BEFORE_REVALIDATION` → R4A→R4B→R4C→R5; `DEFER_TO_INFERNUS_REVALIDATION` → R5.
- **R8** (revalidation execution): pass → R9; fail/block → R8F (failure loopback triage).
- **R8F** loopback targets: `PLAN_REVISION` → PURG03 plan revision → patch revision → R5;
  `PATCH_REVISION` → PURG04 patch revision → R5; `BASELINE_REPAIR` → R4A; `OPERATOR_DIRECTION` → blocked.
- Closure path: R8 → R9 → R10 → R11 → R12 → **R13 (canonical state update — only finding-closure state change)** → R14 → macro handoff.

## Critérios PASS/BLOCK e Artifacts por Fase

### R0 — `PURG_CURRENT_TERMINAL_STATE_LOCK`
- name: Terminal State Lock
- type: `artifact_only_governance_lock` · requires_operator: `False` · allows_execution: `False` · allows_state_change: `False`
- artifacts: `purg_current_terminal_state_lock.json`
- PASS: next_phase=null; active_next_phase=null; IF09-FIND-001 remains open; remediation_proven stays false; all execution locks remain false
- BLOCK: critical JSON/mirror conflict; any closure claim; any remediation_proven=true claim
- notes: Materializes a governance lock over the current live terminal phase; does not advance the live route. Activation of the trail is the live->R1 transition gated by this lock artifact.

### R1 — `PURG_REMAINING_ROADMAP_ACTIVATION_DECISION_PACKET`
- name: Roadmap Activation Decision Packet
- type: `operator_route_governance_decision` · requires_operator: `True` · allows_execution: `False` · allows_state_change: `False`
- artifacts: `purg_remaining_roadmap_activation_decision_packet.json`, `purg_remaining_roadmap_activation_amendment_candidate.json`
- PASS: operator selects exactly one route; amendment candidate created; active Transition Table NOT changed in this phase
- BLOCK: ambiguous decision; attempt to execute revalidation; attempt to close finding
- notes: Branch gate. Activates the candidate roadmap and picks the initial branch. Does not mutate the live Transition Table.

### R2 — `PURG_EXIT_READINESS_PACKET`
- name: PURG Exit Readiness Packet
- type: `artifact_only_exit_readiness` · requires_operator: `False` · allows_execution: `False` · allows_state_change: `False`
- artifacts: `purg_exit_readiness_packet.json`, `purg_exit_findings_matrix.json`, `purg_exit_residual_risk_matrix.json`, `purg_exit_forbidden_claim_scan.json`, `purg_exit_next_route_candidate.json`
- PASS: residual risk formalized; open finding preserved; closure delegated to Infernus Revalidation; no safe/resolved claim
- BLOCK: any closure/safe/resolved claim; missing residual matrix
- notes: Exit readiness never closes the finding; it only formalizes residual risk and delegates closure.

### R3 — `PURG_EXIT_HANDOFF_PACKAGE_PACKET`
- name: PURG Exit Handoff Package
- type: `artifact_only_handoff` · requires_operator: `False` · allows_execution: `False` · allows_state_change: `False`
- artifacts: `purg_exit_handoff_package.json`, `purg_exit_handoff_custody_table.json`, `purg_exit_handoff_open_findings.json`, `purg_exit_handoff_required_revalidation.json`, `purg_exit_handoff_no_real_execution_attestation.json`, `purg_exit_handoff_next_route_candidate.json`
- PASS: handoff ready; IF09-FIND-001 open preserved; remediation_proven stays false; revalidation required
- BLOCK: any closure claim; missing open-findings ledger
- notes: Packages the Purgatorium exit without ending the finding; routes to Infernus Revalidation admission.

### R4 — `PURG_PROJECT_ARIS_GLOBAL_BASELINE_STABILIZATION_DECISION_PACKET`
- name: Project_ARIS Global Baseline Stabilization Decision
- type: `artifact_only_decision` · requires_operator: `True` · allows_execution: `False` · allows_state_change: `False`
- artifacts: `purg_project_aris_global_baseline_stabilization_decision.json`, `purg_project_aris_global_baseline_risk_matrix.json`, `purg_project_aris_global_baseline_defer_or_repair_candidate.json`
- PASS: explicit defer-or-repair decision recorded; global baseline red state acknowledged (not hidden)
- BLOCK: decision omits the red global baseline; decision claims baseline green without evidence
- notes: Explicitly handles the globally-red local suite (231 failures/1519 errors at merge); GitHub CI green is not treated as local-suite green.

### R4A — `PURG_PROJECT_ARIS_BASELINE_REPAIR_READINESS_PACKET`
- name: Project_ARIS Baseline Repair Readiness
- type: `artifact_only_readiness` · requires_operator: `False` · allows_execution: `False` · allows_state_change: `False`
- artifacts: `purg_project_aris_baseline_repair_readiness_packet.json`, `purg_project_aris_baseline_repair_scope_matrix.json`, `purg_project_aris_baseline_repair_forbidden_actions.json`, `purg_project_aris_baseline_repair_operator_authorization_needed.json`
- PASS: repair scope defined; Project_ARIS mutation NOT yet authorized
- BLOCK: any Project_ARIS mutation attempted; scope undefined
- notes: Readiness only; explicitly requires a separate operator approval (R4B) before any Project_ARIS mutation.

### R4B — `PURG_PROJECT_ARIS_BASELINE_REPAIR_OPERATOR_AUTHORIZATION_PACKET`
- name: Project_ARIS Baseline Repair Operator Authorization
- type: `operator_gate` · requires_operator: `True` · allows_execution: `False` · allows_state_change: `False`
- artifacts: `purg_project_aris_baseline_repair_operator_authorization_packet.json`, `purg_project_aris_baseline_repair_execution_contract.json`, `purg_project_aris_baseline_repair_safety_lock_matrix.json`
- PASS: explicit operator authorization captured; scope closed; no product/Bedrock/secrets/real_apply included
- BLOCK: no explicit authorization; scope creep beyond baseline repair
- notes: Added for graph completeness: R4A names this operator-authorization packet as its candidate next. Authorizes but does not execute.

### R4C — `PURG_PROJECT_ARIS_BASELINE_REPAIR_EXECUTION_PACKET`
- name: Project_ARIS Baseline Repair Execution
- type: `controlled_execution_project_aris_baseline_repair` · requires_operator: `True` · allows_execution: `True` · allows_state_change: `False`
- artifacts: `purg_project_aris_baseline_repair_execution_result.json`, `purg_project_aris_baseline_repair_test_evidence.json`, `purg_project_aris_baseline_repair_regression_matrix.json`, `purg_project_aris_baseline_repair_no_forbidden_surface_attestation.json`
- PASS: authorized baseline surface stabilized; no forbidden surface touched; no new regression
- BLOCK: repair failure; regression introduced; scope/forbidden-surface violation
- notes: Only baseline-repair Project_ARIS mutation node; gated by R4B operator authorization. Does NOT close the finding or prove remediation.

### R5 — `INF_REVALIDATION_ROUTE_ADMISSION_PACKET`
- name: Infernus Revalidation Route Admission
- type: `route_admission_artifact_only` · requires_operator: `True` · allows_execution: `False` · allows_state_change: `False`
- artifacts: `inf_revalidation_route_admission_packet.json`, `inf_revalidation_required_inputs.json`, `inf_revalidation_scope_matrix.json`, `inf_revalidation_forbidden_actions.json`, `inf_revalidation_next_route_candidate.json`
- PASS: macro route admission defined; revalidation NOT executed; finding still open
- BLOCK: attempt to execute revalidation in this phase; attempt to close finding
- notes: Admits the macro transition Purgatorium FULL -> Infernus Revalidation. Infernus Revalidation is the only layer that can declare finding_closed.

### R6 — `INF_REVALIDATION_READINESS_PACKET`
- name: Infernus Revalidation Readiness
- type: `artifact_only_readiness` · requires_operator: `False` · allows_execution: `False` · allows_state_change: `False`
- artifacts: `inf_revalidation_readiness_packet.json`, `inf_revalidation_scenario_scope.json`, `inf_revalidation_oracle_contract.json`, `inf_revalidation_abort_criteria.json`, `inf_revalidation_no_real_execution_attestation.json`
- PASS: scenario and oracle defined; abort criteria defined; execution authorization still absent
- BLOCK: execution attempted without authorization; oracle undefined
- notes: Prepares scope/scenarios/oracles/abort criteria for revalidating IF09-FIND-001; no execution.

### R7 — `INF_REVALIDATION_OPERATOR_AUTHORIZATION_PACKET`
- name: Infernus Revalidation Operator Authorization
- type: `operator_gate` · requires_operator: `True` · allows_execution: `False` · allows_state_change: `False`
- artifacts: `inf_revalidation_operator_authorization_packet.json`, `inf_revalidation_execution_contract.json`, `inf_revalidation_safety_lock_matrix.json`
- PASS: explicit authorization, closed scope; does not include product/Bedrock/real_apply/secrets
- BLOCK: no explicit authorization; scope includes forbidden surfaces
- notes: Captures explicit operator authorization to run controlled revalidation.

### R8 — `INF_REVALIDATION_EXECUTION_PACKET`
- name: Infernus Revalidation Execution
- type: `controlled_execution_only_after_R7_pass` · requires_operator: `True` · allows_execution: `True` · allows_state_change: `False`
- artifacts: `inf_revalidation_execution_result.json`, `inf_revalidation_oracle_result.json`, `inf_revalidation_test_evidence.json`, `inf_revalidation_regression_matrix.json`, `inf_revalidation_no_forbidden_surface_attestation.json`
- PASS: oracle passes; no regression; evidence sufficient
- BLOCK: oracle failure; regression; scope violation
- notes: Controlled revalidation execution; read-only against accepted Track A lineage. Does not itself close the finding or set remediation_proven.

### R8F — `INF_REVALIDATION_FAILURE_LOOPBACK_TRIAGE_PACKET`
- name: Revalidation Failure Loopback Triage
- type: `artifact_only_failure_triage` · requires_operator: `False` · allows_execution: `False` · allows_state_change: `False`
- artifacts: `inf_revalidation_failure_loopback_triage.json`, `inf_revalidation_failure_root_cause_matrix.json`, `inf_revalidation_failure_next_candidate.json`
- PASS: failure classified; loopback target selected
- BLOCK: root cause undetermined and no operator direction
- notes: Classifies a failed revalidation and routes a loopback. Never closes the finding.

### R9 — `INF_REVALIDATION_RESULT_ADJUDICATION_PACKET`
- name: Revalidation Result Adjudication
- type: `artifact_only_adjudication` · requires_operator: `False` · allows_execution: `False` · allows_state_change: `False`
- artifacts: `inf_revalidation_result_adjudication_packet.json`, `inf_revalidation_evidence_sufficiency_matrix.json`, `inf_revalidation_regression_check.json`, `inf_revalidation_remediation_proven_candidate.json`
- PASS: evidence sufficient; regressions absent; lineage consistent
- BLOCK: insufficient evidence; regression present; lineage mismatch
- notes: Adjudicates whether revalidation evidence can support a remediation_proven candidate. Emits a candidate only, not a state change.

### R10 — `PURG_REMEDIATION_PROVEN_DECISION_PACKET`
- name: Remediation Proven Decision
- type: `decision_gate` · requires_operator: `False` · allows_execution: `False` · allows_state_change: `False`
- artifacts: `purg_remediation_proven_decision_packet.json`, `purg_remediation_proven_evidence_bundle.json`, `purg_remediation_proven_state_change_candidate.json`, `purg_remediation_proven_no_real_execution_attestation.json`
- PASS: reachable only if R8 and R9 passed; does not change state without the separate state-update gate
- BLOCK: R8/R9 not passed; attempt to mutate state in this phase
- notes: Decides whether remediation_proven may become true; emits a state-change CANDIDATE only. State is changed later at R13.

### R11 — `PURG_FINDING_CLOSURE_ELIGIBILITY_PACKET`
- name: Finding Closure Eligibility
- type: `artifact_only_eligibility` · requires_operator: `False` · allows_execution: `False` · allows_state_change: `False`
- artifacts: `purg_finding_closure_eligibility_packet.json`, `purg_finding_closure_evidence_matrix.json`, `purg_finding_closure_policy_check.json`, `purg_finding_closure_forbidden_claim_scan.json`
- PASS: valid remediation_proven candidate present; revalidation pass present; no residual blocker
- BLOCK: missing revalidation pass; residual blocker present
- notes: Eligibility only; does not close the finding.

### R12 — `PURG_FINDING_CLOSE_OPERATOR_PACKET`
- name: Finding Close Operator Packet
- type: `operator_gate` · requires_operator: `True` · allows_execution: `False` · allows_state_change: `False`
- artifacts: `purg_finding_close_operator_packet.json`, `purg_finding_close_state_change_manifest.json`, `purg_finding_close_rollback_plan.json`
- PASS: explicit operator authorization; state change manifest prepared; validator/schema support planned
- BLOCK: no explicit authorization; no rollback plan
- notes: Captures explicit operator authorization for closure; prepares but does not apply the state change.

### R13 — `PURG_FINDING_CLOSE_CANONICAL_STATE_UPDATE_PACKET`
- name: Finding Close Canonical State Update
- type: `canonical_state_update` · requires_operator: `True` · allows_execution: `False` · allows_state_change: `True`
- artifacts: `purg_finding_close_canonical_state_update_packet.json`, `purg_finding_close_validator_evidence.json`, `purg_finding_close_ci_evidence.json`
- PASS: IF09-FIND-001 transitions to closed ONLY at this gate after R8 revalidation; remediation_proven candidate promoted to true under operator authorization; validator pass; CI green
- BLOCK: any prior gate (R8/R9/R10/R12) not passed; validator fail; CI not green
- notes: The ONLY phase that mutates ACTIVE_CONTEXT_STATE.json for finding closure / remediation_proven. Strictly downstream of Infernus Revalidation execution (R8).

### R14 — `PURG_FINAL_EXIT_PACKET`
- name: Purgatorium Final Exit Packet
- type: `exit_gate` · requires_operator: `True` · allows_execution: `False` · allows_state_change: `True`
- artifacts: `purg_final_exit_packet.json`, `purg_final_exit_evidence_bundle.json`, `purg_final_exit_residual_risk_matrix.json`, `purg_final_exit_next_macro_candidate.json`
- PASS: evidence bundle complete; closure/handoff policy satisfied; product/Bedrock still NOT implied
- BLOCK: incomplete evidence bundle; any product/Bedrock implication
- notes: Layer-exit live-route advance only (does not re-touch finding/remediation flags, which R13 set). Hands off to a separate macro gate.

### LB-PLAN — `PURG03_REMEDIATION_PLAN_REVISION_PACKET`
- name: Remediation Plan Revision (loopback)
- type: `artifact_only_loopback_revision` · requires_operator: `False` · allows_execution: `False` · allows_state_change: `False`
- artifacts: `purg03_remediation_plan_revision_packet.json`, `purg03_remediation_plan_revision_scope_matrix.json`, `purg03_remediation_plan_revision_no_real_execution_attestation.json`
- PASS: revised remediation plan recorded; no apply/patch executed
- BLOCK: apply/patch executed; scope undefined
- notes: Loopback target after a failed revalidation classified as a plan defect. Re-enters the trail toward patch revision then revalidation re-admission.

### LB-PATCH — `PURG04_TRACK_A_PATCH_REVISION_PACKET`
- name: Track A Patch Revision (loopback)
- type: `artifact_only_loopback_revision` · requires_operator: `False` · allows_execution: `False` · allows_state_change: `False`
- artifacts: `purg04_track_a_patch_revision_packet.json`, `purg04_track_a_patch_revision_scope_matrix.json`, `purg04_track_a_patch_revision_no_real_execution_attestation.json`
- PASS: revised patch plan recorded; actual apply/merge deferred to its own operator-gated mutation phase
- BLOCK: apply/merge executed in this artifact-only phase
- notes: Loopback target; records a revised patch plan and re-admits Infernus Revalidation. Actual patch apply remains a separate operator-gated mutation outside this artifact-only node.

## Locks Carregados (carry-forward)

Carregados de `purg05_carry_forward_locks.json` e preservados por toda a trilha até os gates próprios:

- `IF09-FIND-001 = open`
- `remediation_proven = false`
- `finding_closed = false`
- `purgatorium_can_close_finding = false`
- `infernus_revalidation_required_for_closure = true`
- `product_ready = false` · `bedrock_ready = false`
- `runtime / real_apply / secrets / dependency-package-manager = false`
- `proof_loop_execution_allowed = false` (até R8 sob autorização do operador)

## No-Deviation Policy

Fonte: `artifacts/purgatorium/purgatorium_remaining_roadmap_no_deviation_policy.json`.

- The remaining roadmap (R0-R14 + loopbacks) is followed to the letter once activated.
- Deviations are permitted only through an amendment artifact.
- An amendment requires explicit operator approval.
- An amendment requires validator pass + CI terminal green.
- A candidate gate is not an active gate.
- Route-opening is not execution.
- Residual carry-forward does not close the finding.
- Infernus Revalidation (R5-R9) is mandatory before any closure.
- The closure state update (R13) is a separate, independently validated gate.
- Product and Bedrock require their own separate gates after exit/closure.

## Amendment Policy

- Qualquer desvio da trilha exige um **amendment artifact** explícito.
- O amendment exige **aprovação explícita do operador**.
- O amendment exige **validator pass + CI terminal green**.
- Ativar qualquer row da `purgatorium_remaining_roadmap_transition_table_candidate.json` exige:
  gate explícito do operador, suporte de schema/validator para os novos `phase_id`/`phase_class`,
  um artifact de admissão análogo ao padrão PURG-PRE/PURG-00/PURG-01, e CI verde.

## Relação com ROADMAP_CANONICAL.md

- `ROADMAP_CANONICAL.md` é a única autoridade de roadmap macro; sua live Transition Table
  permanece **inalterada** e terminal em `PURG_RESIDUAL_RISK_CARRY_FORWARD_PACKET` (`next_phase=null`).
- Este documento é uma trilha técnica **subordinada**: não vence `ACTIVE_CONTEXT_STATE.json`
  nem `ROADMAP_CANONICAL.md`, e não autoriza execução real, produto, Bedrock, secrets,
  real_apply ou runtime por si só.
- A sequência macro de saída (Purgatorium FULL → Infernus Revalidation → BenchUX → …)
  permanece definida em `ROADMAP_CANONICAL.md`; esta trilha apenas detalha o interior
  restante do Purgatorium e o handoff para a próxima camada macro.

> **Nota explícita:** este roadmap é trilha técnica canônica subordinada; a live Transition
> Table só muda por gate separado.

