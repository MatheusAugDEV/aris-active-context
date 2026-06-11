# aris-active-context

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

phase_id: INF-FULL-07
status: purg01_route_admission_pass
latest_completed_phase: IF-11 Minos Final Verdict + Closure
latest_completed_status: if11_minos_final_verdict_closure_pass
next_phase: PURG-01
next_recommended_step: execute_purg01_controlled_triage_artifact_only
technical_roadmap_post_infernus: project_mirror/docs/purgatorium_full/purgatorium_roadmapcanon.md
Todos execution_locks: false
PURG-01 admitido como rota: true
PURG-01 triage autorizada para etapa futura controlada: true
Pacote primario do operador validado: true
Review formal de admissao PURG-01: pass
Review de prontidao para triage PURG-01: pass
Gate de planejamento de triage PURG-01: pass
Gate de autorizacao de triage PURG-01: pass
Gate de execucao controlada de triage PURG-01: pass

## PURG-01.1 triage classification

O pacote canônico `artifacts/purgatorium/purg01_1_if09_find_001_triage_classification_packet.json` registra a classificação de triagem de `IF09-FIND-001` usando apenas o handoff IF09/IF10 e o roadmap Purgatorium. O packet fixa `selected_track=S3` com `classification_confidence=medium`, preserva todos os locks de execução em `false` e mantém `next_recommended_step=BLOCKED_NEEDS_OPERATOR_DIRECTION` para evitar abrir `PURG-02` ou inventar um sucessor `PURG-01.2` fora da rota viva.

## PURG-01.2 S3 successor candidate

O artifact `artifacts/purgatorium/purg01_2_s3_track_successor_candidate.json` define `PURG-01.2` como um gate artifact-only de escopo e readiness para a trilha `S3` de `IF09-FIND-001`. Ele não abre `PURG-02`, não autoriza remediação, runtime, real_apply ou finding close, e só registra os critérios mínimos que uma etapa futura precisaria satisfazer antes de qualquer avanço roadmap-defined.
