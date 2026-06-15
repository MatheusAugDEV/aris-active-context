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

A canonicalização do roadmap macro foi registrada e validada no commit `dcf1e7cfd7473e3d83fd7d50a9a27f33dc798a09` (ver `DECISION_LOCKS.md` § "Active-Context Post-Roadmap Canonical Sync" e `artifacts/roadmap/post_roadmap_canonical_sync_decision.json`). `ACTIVE_CONTEXT_STATE.json` permanece inalterado (sem novos campos, `additionalProperties: false` no schema); a Macro Transition Table futura permanece documental, não consumida pelo validador, e a rota viva (`active_next_phase=PURG-01`) permanece preservada.

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

phase_id: PURG04_TRACK_A_POST_MERGE_VALIDATION_PACKET
status: purg04_track_a_post_merge_validation_packet_pass
latest_completed_phase: PURG04 Track A Post-Merge Validation Packet
latest_completed_status: purg04_track_a_post_merge_validation_packet_pass
next_phase: null
next_recommended_step: Nenhuma transição definida. Aguardando instrução do operador.
technical_roadmap_post_infernus: project_mirror/docs/purgatorium_full/purgatorium_roadmapcanon.md
Todos execution_locks: false
Track A patch: branch `codex/purg04-track-a-pointer-residual-repair-20260612`, patch commit `1e9a04a02846f3261ae72d0c95fbee6b0163b45b`
Merge to Project_ARIS main: executed at `7883af5a32c629026bfc6dc15ebee4ebbcadd295` with `CI_GREEN_CONFIRMED`
IF09-FIND-001 remains open
Project_ARIS main workspace: não alterado por este post-merge validation packet

O packet canônico de validação pós-merge está registrado em `artifacts/purgatorium/purg04_track_a_post_merge_validation_packet.json`, com autorização explícita em `artifacts/purgatorium/purg04_track_a_post_merge_validation_operator_authorization.json`. Ele confirma que o merge Track A permaneceu dentro do escopo autorizado, que `forbidden_paths_touched=[]`, que `remediation_proven=false`, que `IF09-FIND-001` continua open e que a Transition Table não define sucessor após esta fase.

## PURG-04 proof-loop corpus materialization

O packet `artifacts/purgatorium/purg04_proof_loop_corpus_materialization_readiness_packet.json` abriu apenas a readiness documental para materializar o corpus proof-loop ausente da linhagem aceita de Track A. Na execução seguinte, `artifacts/purgatorium/purg04_proof_loop_corpus_materialization_artifact_only_packet.json` registrou `blocked` porque o manifest `artifacts/purgatorium/purg04_proof_loop_corpus_materialization_source_hashes.json` já não bate com `DECISION_LOCKS.md` na `main` canônica. Por contrato, isso impede materializar os cinco artifacts de RED->RESET->GREEN, reset, benign-flow, kill-switch e rollback sem antes corrigir ou substituir o source manifest.

Esse bloqueio é estritamente documental: `ACTIVE_CONTEXT_STATE.json` continua terminal em `PURG04_TRACK_A_POST_MERGE_VALIDATION_PACKET`, `next_phase=null`, `active_next_phase=null`, `IF09-FIND-001` permanece open, `remediation_proven=false`, `Project_ARIS` não foi mutado e nenhum teste de `Project_ARIS` ou proof-loop foi executado nesta fase.

O repair `artifacts/purgatorium/purg04_proof_loop_corpus_source_hash_manifest_divergence_diagnostic.json` verificou que a divergência veio de `DECISION_LOCKS.md` tratado como se fosse fonte imutável, embora o hash esperado no manifest correspondesse ao estado pré-append do próprio cycle de readiness. O resync `artifacts/purgatorium/purg04_proof_loop_corpus_source_hash_manifest_resync.json` separa fontes imutáveis de derivação, autoridades canônicas, ledger mutável e mirrors não autoritativos, e emite `artifacts/purgatorium/purg04_proof_loop_corpus_materialization_retry_candidate.json` apenas como candidate gate documental para um retry futuro ainda artifact-only.

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
