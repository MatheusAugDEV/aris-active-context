# aris-active-context

## Leia Primeiro

- `BOOT.md` — página única gerada para boot rápido; se o carimbo divergir do ref atual, rode `python3 scripts/render_boot.py`.
- `ACTIVE_CONTEXT_STATE.json` continua sendo a fonte de verdade; `BOOT.md` é derivado e deve permanecer sincronizado.

Memória externa do GPT/Codex para o projeto ARIS entre sessões.

## Propósito

Este repositório responde três perguntas:
1. Onde estamos?        → ACTIVE_CONTEXT_STATE.json
2. O que fazemos agora? → ACTIVE_CONTEXT_STATE.json > next_phase
3. Quais são as regras? → ARIS_BOOT.md

## Boot obrigatório (nesta ordem)

1. `ACTIVE_CONTEXT_STATE.json` — estado canônico e fonte de verdade
2. `ARIS_BOOT.md` — identidade, regras, padrões de prompt

## Roadmap macro canônico

`ROADMAP_CANONICAL.md` é a única autoridade de roadmap macro ativa ("ARIS ROADMAP CANONICAL — CAMADAS E OBJETIVOS"), baseada no documento do operador `operator_inputs/roadmap_aris_camadas_objetivos.md`. Roadmaps de fase/subsistema (ex.: `project_mirror/docs/purgatorium_full/purgatorium_roadmapcanon.md`) são subordinados e nunca vencem `ACTIVE_CONTEXT_STATE.json` nem `ROADMAP_CANONICAL.md`. Roadmaps macro concorrentes devem estar em `excludent/` (ver `EXCLUDENT_POLICY.md`).

A canonicalização do roadmap macro foi registrada e validada no commit `dcf1e7cfd7473e3d83fd7d50a9a27f33dc798a09` (ver `DECISION_LOCKS.md` § "Active-Context Post-Roadmap Canonical Sync" e `artifacts/roadmap/post_roadmap_canonical_sync_decision.json`). `ACTIVE_CONTEXT_STATE.json` permanece inalterado (sem novos campos, `additionalProperties: false` no schema); a Macro Transition Table futura permanece documental, não consumida pelo validador. HISTORICAL_ONLY / NOT_CURRENT_STATE: no momento desse commit, a rota viva era `active_next_phase=PURG-01`; o estado vivo atual está em `ACTIVE_CONTEXT_STATE.json` e na seção "Estado canônico atual" abaixo (`active_next_phase=null`).

## Referência sob demanda

| Arquivo | Quando ler |
|---|---|
| `ROADMAP_CANONICAL.md` | Ao mudar fase (Transition Table) |
| `DECISION_LOCKS.md` | Ao questionar locks de execução |
| `LAB_OPERATING_CONTRACT.md` | Ao tocar lab ou Bedrock |
| `INFERNUS_STANDING_AUTHORIZATION.md` | Fases infernus_full |
| `EXCLUDENT_POLICY.md` | Ao tocar excludent/ |
| `BEDROCK_GATE.md` | Ao abordar produto ou Bedrock |

## Estrutura do repositório

```
raiz/
  ACTIVE_CONTEXT_STATE.json        ← fonte de verdade
  ACTIVE_CONTEXT_SCHEMA.json       ← contrato de validação
  ARIS_BOOT.md                     ← boot obrigatório
  ROADMAP_CANONICAL.md             ← Transition Table
  DECISION_LOCKS.md                ← locks de autorização
  LAB_OPERATING_CONTRACT.md        ← regras lab/Bedrock
  INFERNUS_STANDING_AUTHORIZATION.md
  EXCLUDENT_POLICY.md
  BEDROCK_GATE.md
  scripts/                         ← validate_active_context_state.py
  artifacts/                       ← evidence chain
  project_mirror/                  ← espelho do projeto principal
  excludent/                       ← quarentena (nunca lido por padrão)
  archive/                         ← histórico (nunca lido por padrão)
    gate_history/                  ← gates fechados
    superseded/                    ← arquivos absorvidos pelo ARIS_BOOT.md
    derived_mirrors/               ← mirrors e planos históricos
  fixtures/                        ← cenários do lab
  tests/
  .github/workflows/               ← CI
```

## Regra de ouro

Markdown que contradiz o JSON = drift. O JSON vence sempre.
PASS só existe com: CI terminal green + validator pass + artifact no disco.
Resposta sem SHA no topo = INVALID.

## Estado canônico atual

phase_id: IF09_CLOSURE_MILESTONE_MIRROR_SANITY_PACKET
status: if09_closure_milestone_mirror_sanity_pass
latest_completed_phase: IF09 Closure Milestone Mirror Sanity Packet
latest_completed_status: if09_closure_milestone_mirror_sanity_pass
next_phase: null
next_recommended_step: Nenhuma transição definida. Aguardando instrução do operador.
technical_roadmap_post_infernus: project_mirror/docs/purgatorium_full/purgatorium_roadmapcanon.md
Todos execution_locks: false
Selected branch: `TRACK_REVALIDATION_FIRST`
Track A patch: branch `codex/purg04-track-a-pointer-residual-repair-20260612`, patch commit `1e9a04a02846f3261ae72d0c95fbee6b0163b45b`
Merge to Project_ARIS main: executed at `7883af5a32c629026bfc6dc15ebee4ebbcadd295` with `CI_GREEN_CONFIRMED`
IF09-FIND-001 closed
BENCHUX_ROUTE_OPENING_PACKET
Project_ARIS main workspace: não alterado por este IF09 closure milestone mirror sanity packet

O packet canônico de mirror sanity está registrado em `artifacts/active_context/if09_closure_milestone_sanity_packet.json`. Ele consome a row viva `INF_REVALIDATION_ADJUDICATION_OR_CLOSURE_PACKET -> IF09_CLOSURE_MILESTONE_MIRROR_SANITY_PACKET`, preserva `next_phase=null` e `active_next_phase=null`, reafirma `finding_closed=true`, `remediation_proven=true` e `closure_basis=deterministic_oracle_pass_plus_no_regression_plus_no_forbidden_surface`, saneia mirrors derivados e emite `artifacts/benchux/benchux_route_opening_candidate.json` apenas como candidato documental.

Como artifact family desta fase viva, o repositório agora registra `artifacts/active_context/if09_closure_milestone_sanity_packet.json`, `if09_closure_milestone_mirror_drift_matrix.json`, `if09_closure_milestone_superseded_notes_manifest.json`, `if09_closure_milestone_no_real_execution_attestation.json`, `if09_closure_milestone_validation_evidence.json`, `artifacts/benchux/benchux_route_opening_candidate.json` e `benchux_pre_route_scope_note.json`. Esses artifacts mantêm `Project_ARIS` intocado, preservam runtime/real_apply/product/Bedrock/secrets fechados, rotulam stale notes como `HISTORICAL_ONLY`, `SUPERSEDED_BY_INF_REVALIDATION_ADJUDICATION_OR_CLOSURE_PACKET` e `NOT_CURRENT_STATE`, e deixam BenchUX estritamente fora da rota viva.

## Historical Appendix

HISTORICAL_ONLY
SUPERSEDED_BY_INF_REVALIDATION_ADJUDICATION_OR_CLOSURE_PACKET
NOT_CURRENT_STATE

As seções abaixo preservam trilhas e locks anteriores para auditoria. Qualquer menção abaixo deste ponto a `IF09-FIND-001 remains open`, `finding_closed=false`, `remediation_proven=false`, `INF_REVALIDATION_EXECUTION_PACKET` candidate-only ou `revalidation not executed` é histórica e não descreve o estado vivo atual.

## PURG-04 proof-loop corpus materialization

O packet `artifacts/purgatorium/purg04_proof_loop_corpus_materialization_readiness_packet.json` abriu apenas a readiness documental para materializar o corpus proof-loop ausente da linhagem aceita de Track A. Na execução seguinte, `artifacts/purgatorium/purg04_proof_loop_corpus_materialization_artifact_only_packet.json` registrou `blocked` porque o manifest `artifacts/purgatorium/purg04_proof_loop_corpus_materialization_source_hashes.json` já não bate com `DECISION_LOCKS.md` na `main` canônica. Por contrato, isso impede materializar os cinco artifacts de RED->RESET->GREEN, reset, benign-flow, kill-switch e rollback sem antes corrigir ou substituir o source manifest.

Esse bloqueio é estritamente documental: `ACTIVE_CONTEXT_STATE.json` continua terminal em `PURG04_TRACK_A_POST_MERGE_VALIDATION_PACKET`, `next_phase=null`, `active_next_phase=null`, `IF09-FIND-001` permanece open, `remediation_proven=false`, `Project_ARIS` não foi mutado e nenhum teste de `Project_ARIS` ou proof-loop foi executado nesta fase.

O repair `artifacts/purgatorium/purg04_proof_loop_corpus_source_hash_manifest_divergence_diagnostic.json` verificou que a divergência veio de `DECISION_LOCKS.md` tratado como se fosse fonte imutável, embora o hash esperado no manifest correspondesse ao estado pré-append do próprio cycle de readiness. O resync `artifacts/purgatorium/purg04_proof_loop_corpus_source_hash_manifest_resync.json` separa fontes imutáveis de derivação, autoridades canônicas, ledger mutável e mirrors não autoritativos, e emite `artifacts/purgatorium/purg04_proof_loop_corpus_materialization_retry_candidate.json` apenas como candidate gate documental para um retry futuro ainda artifact-only.

A finalização `artifacts/purgatorium/purg04_proof_loop_corpus_retry_epoch_finalization_diagnostic.json` reancora esse retry no epoch `6a7b861523a818ecacb3c180585c2b5a585ddea7` e emite `artifacts/purgatorium/purg04_proof_loop_corpus_source_hash_manifest_resync_v2.json` junto com `artifacts/purgatorium/purg04_proof_loop_corpus_materialization_retry_candidate_v2.json`. O `resync_v2` mantém exact-hash blocking para autoridades e fontes imutáveis, trata `DECISION_LOCKS.md` como ledger append-only com pre-retry drift conhecido e preserva os hashes atuais dos cinco blocked stubs antes de qualquer overwrite futuro, sem alterar o estado canônico JSON e sem executar proof-loop.

O retry `artifacts/purgatorium/purg04_proof_loop_corpus_materialization_retry_packet.json` consumiu esse `resync_v2`, revalidou authorities, sources imutáveis, custody hashes e a política append-only do ledger, e então substituiu os cinco blocked stubs por artifacts PASS derivados apenas de evidência já registrada. O resultado criou também `artifacts/purgatorium/purg04_proof_loop_corpus_materialization_retry_output_hashes.json`, `...retry_custody_map.json`, `...retry_lineage_matrix.json`, `...retry_no_real_execution_attestation.json` e `...retry_next_route_candidate.json`, emitindo somente `PURGATORIUM_POST_PURG04_ROUTE_DECISION_RECHECK_ARTIFACT_ONLY` como candidate gate documental, ainda sem alterar `ACTIVE_CONTEXT_STATE.json`.

O recheck `artifacts/purgatorium/purgatorium_post_purg04_route_decision_recheck_packet.json` reavaliou a decisão de rota pós-PURG04 usando apenas esses cinco artifacts PASS e confirmou que os blockers documentais originais foram removidos. O resultado emite somente `PURG05_EVIDENCE_LEDGER_SIGNING_CUSTODY_PACKET` como `candidate_next_gate`, com `candidate_only=true`, `can_open_purg05_now=false`, `next_phase=null`, `active_next_phase=null`, `IF09-FIND-001` ainda open e `remediation_proven=false`.

O admission packet `artifacts/purgatorium/purg05_evidence_ledger_signing_custody_admission_packet.json` transforma esse candidate em contrato verificável para uma abertura futura, sem abrir `PURG05` agora. Ele fixa os inputs obrigatórios, o escopo permitido, os critérios de aceitação e os bloqueios futuros, emitindo somente `PURG05_EVIDENCE_LEDGER_SIGNING_CUSTODY_PACKET_OPERATOR_OR_ROUTE_OPENING_PACKET` como próximo candidate gate, ainda com `candidate_only=true`, `purg05_opened=false`, `next_phase=null` e `remediation_proven=false`.

O opening packet `artifacts/purgatorium/purg05_evidence_ledger_signing_custody_opening_packet.json` verificou que a admissão continua íntegra, que todos os required inputs seguem presentes e que a futura abertura de `PURG05_EVIDENCE_LEDGER_SIGNING_CUSTODY_PACKET` pode ser proposta sem ativar o gate agora. O resultado emite novamente `PURG05_EVIDENCE_LEDGER_SIGNING_CUSTODY_PACKET` apenas como candidate gate, com `candidate_only=true`, `requires_operator_or_explicit_route_activation=true`, `purg05_opened=false`, `next_phase=null` e `remediation_proven=false`.

O gate `artifacts/purgatorium/purg05_evidence_ledger_hash_inventory.json` e seus artifacts irmãos materializam a custódia documental do corpus já admitido: inventário de hashes, metadados de signing sem assinatura real, cadeia de custódia, tabela de lineage, locks carry-forward e attestation de não execução real. Esse candidate foi consumido pelo novo packet `artifacts/purgatorium/purg_residual_risk_carry_forward_route_opening_packet.json`, que abriu a rota residual apenas no active-context e preservou todos os locks reais em `false`.

O admission backfill `artifacts/purgatorium/purg_residual_risk_carry_forward_admission_packet.json` fixa retrospectivamente os inputs obrigatórios, o scope matrix, os acceptance criteria e a attestation de não execução real para esse candidate residual, mantendo `candidate_only=true`, `admission_only=true`, `residual_packet_opened=false` e `finding_closed=false`.

## PURG-01.1 triage classification

O pacote canônico `artifacts/purgatorium/purg01_1_if09_find_001_triage_classification_packet.json` registra a classificação de triagem de `IF09-FIND-001` usando apenas o handoff IF09/IF10 e o roadmap Purgatorium. O packet fixa `selected_track=S3` com `classification_confidence=medium`, preserva todos os locks de execução em `false` e mantém `next_recommended_step=BLOCKED_NEEDS_OPERATOR_DIRECTION` para evitar abrir `PURG-02` ou inventar um sucessor `PURG-01.2` fora da rota viva.

## PURG-01.2 S3 successor candidate

O artifact `artifacts/purgatorium/purg01_2_s3_track_successor_candidate.json` define `PURG-01.2` como um gate artifact-only de escopo e readiness para a trilha `S3` de `IF09-FIND-001`. Ele não abre `PURG-02`, não autoriza remediação, runtime, real_apply ou finding close, e só registra os critérios mínimos que uma etapa futura precisaria satisfazer antes de qualquer avanço roadmap-defined.

## PURG-01.2 S3 readiness gate

O artifact `artifacts/purgatorium/purg01_2_s3_scope_and_remediation_planning_readiness.json` materializa o gate de readiness do `PURG-01.2` para `IF09-FIND-001/S3`. Ele fixa o escopo S3, define critérios e evidências mínimas para uma futura decisão do operador sobre `PURG-02`, mantém `PURG-02` e `PURG-03` fechados e preserva todos os locks reais em `false`.

## PURG-02 IF09-FIND-001 S3 RED baseline

O artifact `artifacts/purgatorium/purg02_if09_find_001_s3_red_baseline.json` abre `PURG-02` apenas no plano artifact-only e synthetic-only para `IF09-FIND-001/S3`. Ele materializa a hipótese RED, a matriz de evidência, o oracle documental e o plano de reprodução segura sem runtime, sem scanner/DAST/pentest, sem patch, sem remediação e sem fechamento do finding; `PURG-03` continua fechado e não autorizado.

## PURG-03 IF09-FIND-001 S3 remediation plan review

O artifact `artifacts/purgatorium/purg03_if09_find_001_s3_remediation_plan_compiler_review_packet.json` compila o pacote de revisão do plano de remediação para `IF09-FIND-001/S3` em modo artifact-only e planning-only. Ele define objetivos, estratégia proposta, superfície candidata, critérios de aceitação, evidência obrigatória, critérios de abort e requisitos futuros de revalidação sem aplicar patch, sem executar remediação e sem fechar o finding.

## PURG-03 IF09-FIND-001 S3 operator approval packet

O artifact `artifacts/purgatorium/purg03_if09_find_001_s3_remediation_plan_operator_approval_packet.json` transforma o plano compilado em um packet objetivo de aprovação/rejeição. Ele fixa critérios de approve/block, requisitos mínimos para uma futura remediação local, evidência anti-teatro, limites de blast radius e rollback documental, deixando explícito que esta decisão não autoriza apply, patch, runtime ou finding close.

## PURG-04 IF09-FIND-001 S3 local remediation readiness

O artifact `artifacts/purgatorium/purg04_if09_find_001_s3_local_remediation_plan_readiness.json` converte o approval packet em pré-condições concretas para uma futura remediação local controlada. Ele define superfície candidata, módulos prováveis em escopo, regressões obrigatórias, evidência before/after, rollback documental, blast radius e bloqueios, mantendo `future_apply_gate_required=true` e sem autorizar apply, patch, runtime ou finding close.

## PURG-04 IF09-FIND-001 S3 apply approval packet

O artifact `artifacts/purgatorium/purg04_if09_find_001_s3_local_remediation_apply_approval_packet.json` consolida o pacote formal que poderá embasar um pedido futuro de apply local para `IF09-FIND-001/S3`. Ele fixa checklist, preconditions, testes, evidência, rollback e blast radius para um apply futuro, deixando explícito que este gate não autoriza apply agora e exige comando explícito futuro do operador.

## PURG-04 IF09-FIND-001 S3 local remediation apply result

O artifact `artifacts/purgatorium/purg04_if09_find_001_s3_local_remediation_apply_result.json` canoniza a tentativa FAILED de apply local controlado para `IF09-FIND-001/S3` como failure-ledger após rollback. O patch temporário passou nos testes focados, mas não pôde ser aceito canonicamente porque `python3 -m unittest discover -s tests` falhou fora da superfície autorizada, com evidência terminal `fatal: path 'CURRENT_STATE.md' exists on disk, but not in 'HEAD'`. O resultado mantém `finding_closed=false`, `remediation_proven=false` e fixa `next_recommended_step=PURG04_GLOBAL_TEST_BASELINE_TRIAGE_ARTIFACT_ONLY`.

## PURGATORIUM Remaining Roadmap Canon (trilha técnica subordinada)

`purgatorium_remaining_roadmapcanon.md` é a trilha técnica canônica restante do Purgatorium, subordinada ao ACTIVE_CONTEXT_STATE.json e ao ROADMAP_CANONICAL.md. Ela não ativa successor row sozinha.

O gate artifact-only `PURGATORIUM_REMAINING_ROADMAP_CANONICALIZATION_PACKET_ARTIFACT_ONLY` materializou `project_mirror/docs/purgatorium_full/purgatorium_remaining_roadmapcanon.md` e os artifacts `purgatorium_remaining_roadmap_diagnostic_reconciliation.json`, `...canonicalization_packet.json`, `...phase_graph.json`, `...transition_table_candidate.json`, `...no_deviation_policy.json`, `...post_save_self_review.json` e `...no_real_execution_attestation.json` em `artifacts/purgatorium/`. A trilha cobre R0–R14 (mais loopbacks de revalidação e uma fase explícita de estabilização do baseline global do `Project_ARIS`). Fechamento de finding e `remediation_proven=true` só ocorrem em gates próprios estritamente a jusante da Infernus Revalidation. Este gate não alterou `ACTIVE_CONTEXT_STATE.json`, não alterou a live Transition Table, manteve `next_phase: null`, `IF09-FIND-001 remains open` e `remediation_proven=false`.

## PURG Remaining Roadmap Activation Decision Packet (R1) — Blocked, Aguardando Operador

O gate `PURG_REMAINING_ROADMAP_ACTIVATION_DECISION_PACKET` (R1 da trilha técnica restante do Purgatorium) finalizou como `decision=blocked` / `blocked_reason=operator_branch_selection_required`, pois nenhuma linha `operator_selected_branch=TRACK_EXIT_FIRST|TRACK_REVALIDATION_FIRST|TRACK_BASELINE_STABILIZATION_FIRST` foi fornecida pelo operador. Os artifacts `purg_remaining_roadmap_activation_decision_packet.json`, `purg_remaining_roadmap_activation_branch_matrix.json`, `purg_remaining_roadmap_activation_amendment_candidate.json`, `purg_remaining_roadmap_activation_no_real_execution_attestation.json` e `purg_remaining_roadmap_activation_next_route_candidate.json` foram materializados em `artifacts/purgatorium/`, todos com `candidate_next_gate=BLOCKED_OPERATOR_DIRECTION_REQUIRED` (sentinel candidate, não ativo). Este gate não alterou `ACTIVE_CONTEXT_STATE.json`, não alterou a live Transition Table, manteve `next_phase: null`, `IF09-FIND-001 remains open` e `remediation_proven=false`. Para destravar, o operador deve fornecer exatamente um `operator_selected_branch`.

## PURG Remaining Roadmap Branch Selection Diagnostic (R1 evidence) — Artifact-Only, Não-Vinculante

O gate artifact-only `PURG_REMAINING_ROADMAP_BRANCH_SELECTION_DIAGNOSTIC_PACKET_ARTIFACT_ONLY` mapeou a superfície de revalidação de `IF09-FIND-001` (linhagem Track A aceita: patch `1e9a04a02846f3261ae72d0c95fbee6b0163b45b`, merge `7883af5a32c629026bfc6dc15ebee4ebbcadd295`, 6 arquivos em `src/aris/context/`, `src/aris/product_loop/`, `scripts/` e `tests/`, todas as 5 validações focadas passaram) contra o baseline global vermelho local do `Project_ARIS` (`python3 -m unittest discover -s tests` falha com `fatal: path 'CURRENT_STATE.md' exists on disk, but not in 'HEAD'`, mais três falhas específicas de IF-08/W0.5). O resultado é `baseline_intersects_if09_revalidation_oracle=false` com `confidence=medium`, e a recomendação técnica não-vinculante é `recommended_branch=TRACK_REVALIDATION_FIRST` (`recommendation_is_binding=false`, `operator_still_must_select_branch=true`). Os artifacts `purg_remaining_roadmap_branch_selection_diagnostic_packet.json`, `purg_remaining_roadmap_branch_selection_surface_matrix.json`, `purg_remaining_roadmap_branch_selection_evidence_inventory.json`, `purg_remaining_roadmap_gate_compression_analysis.json`, `purg_remaining_roadmap_branch_selection_no_real_execution_attestation.json` e `purg_remaining_roadmap_branch_selection_next_route_candidate.json` foram materializados em `artifacts/purgatorium/`. A análise de compressão de gates (Task 5) concluiu que R5+R6 e R9+R10+R11 não são colapsáveis sem perder uma checagem distinta (`requires_amendment_to_apply=true`, `roadmap_changed_now=false`, recomendação `keep_as_is`). Este gate não alterou `ACTIVE_CONTEXT_STATE.json`, não alterou a live Transition Table, não escolheu branch, manteve `next_phase: null`, `IF09-FIND-001 remains open` e `remediation_proven=false`.

## PURG Remaining Roadmap Activation Decision Packet (R1) — Pass, Branch Selecionado

O gate `PURG_REMAINING_ROADMAP_ACTIVATION_DECISION_PACKET` (R1 da trilha técnica restante do Purgatorium) foi re-executado com `decision=pass`, após o operador fornecer explicitamente `operator_selected_branch=TRACK_REVALIDATION_FIRST`. A seleção é consistente com (mas não vinculada a) a recomendação não-vinculante do diagnóstico anterior (`purg_remaining_roadmap_branch_selection_diagnostic_packet.json`: `baseline_intersects_if09_revalidation_oracle=false`, `confidence=medium`, `recommended_branch=TRACK_REVALIDATION_FIRST`). A linha da Transition Table candidata (`purgatorium_remaining_roadmap_transition_table_candidate.json`) com `current_phase_id=PURG_REMAINING_ROADMAP_ACTIVATION_DECISION_PACKET`, `branch_choice=TRACK_REVALIDATION_FIRST` mapeia para `next_phase_id=INF_REVALIDATION_ROUTE_ADMISSION_PACKET`, `advance_mode=operator`. Os artifacts `purg_remaining_roadmap_activation_decision_packet.json`, `purg_remaining_roadmap_activation_branch_matrix.json`, `purg_remaining_roadmap_activation_amendment_candidate.json`, `purg_remaining_roadmap_activation_no_real_execution_attestation.json` e `purg_remaining_roadmap_activation_next_route_candidate.json` foram atualizados em `artifacts/purgatorium/`, todos com `candidate_next_gate=INF_REVALIDATION_ROUTE_ADMISSION_PACKET` (`candidate_only=true`, `state_advanced=false`). Este gate não alterou `ACTIVE_CONTEXT_STATE.json`, não alterou a live Transition Table, manteve `next_phase: null`, `active_next_phase: null`, `IF09-FIND-001 remains open` e `remediation_proven=false`. Ativar esta linha na Transition Table viva ainda requer um passo separado e explícito de amendment-activation do operador, com suporte de schema/validador e artifact de admissão dedicado.
