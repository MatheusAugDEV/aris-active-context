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
status: purg00_route_amendment_terminal_wait_state_blocked
latest_completed_phase: IF-11 Minos Final Verdict + Closure
latest_completed_status: if11_minos_final_verdict_closure_pass
next_phase: null
next_recommended_step: prepare_purg01_route_admission_review
technical_roadmap_post_infernus: project_mirror/docs/purgatorium_full/purgatorium_roadmapcanon.md
Todos execution_locks: false
PURG-01 continua fechado: true
Pacote primario do operador validado: true
