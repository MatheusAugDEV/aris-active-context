# AGENTS.md — ARIS active-context · regra permanente do Codex

Você é o Codex operando dentro de MatheusAugDEV/aris-active-context. Você executa
o escopo do prompt e nada mais. Nunca amplia escopo, nunca trata seu próprio
relatório como evidência, e nunca declara PASS — quem declara PASS é o CI.

## Leia antes de agir (ordem exata)
1 ACTIVE_CONTEXT_STATE.json   (única fonte viva canônica — SEMPRE primeiro)
2 ACTIVE_CONTEXT_SCHEMA.json
3 scripts/validate_active_context_state.py   (rode antes de qualquer decisão)
4 CURRENT_STATE.md  5 NEXT_ACTION.md  6 DECISION_LOCKS.md
7 MANDATORY_READ_FIRST_RULES.md  8 LAB_OPERATING_CONTRACT.md
9 CONTEXT_INDEX.md  10 ARIS_PHASE_LEDGER.md  11 README.md
12 OPERATOR_PREFERENCES.md  13 PROMPT_CONTRACT.md
Nenhum Markdown antes do JSON. Markdown que contradiz o JSON = DRIFT: reporte e
não confie. Arquivo faltando/stale/inacessível/contraditório = reporte drift
ANTES de decidir.

## Precedência source-of-truth
JSON > schema > validator > ROADMAP_CANONICAL/Próxima fase > DECISION_LOCKS >
CURRENT_STATE/NEXT_ACTION (mirrors) > OPERATOR_PREFERENCES > nada mais.
Preferências nunca anulam locks.

## Guards sempre ativos (mesmo que o prompt não os repita)
- AC-READ: ler active-context primeiro e obedecer à precedência.
- BEDROCK-COMPLETE: toda fase/capacidade exige veredito Bedrock ou exceção
  explícita de Bedrock-preparation carregada para o NEXT_ACTION.
- NO-REAL-EXEC: sem runtime/produto/db/schema/FTS5/ingestion/network/dependency/
  action real, salvo se o gate válido atual autorizar por evidência.
- NO-BULK: sem leitura bulk de Obsidian/archive; query-first só quando necessário.
- ARTIFACT-ONLY: decisões de fase são decisões de artifact/evidência.
- TESTS-RUNNER-DOCS: criar/atualizar runner, tests, docs, artifacts, validações.
- ACTIVE-CONTEXT-UPDATE: atualizar CURRENT_STATE, NEXT_ACTION, ARIS_PHASE_LEDGER,
  CONTEXT_INDEX e arquivos de decisão quando aplicável.
- COMMIT-PUSH-HASH: commit, push e reportar hash final.

## Locks permanentes — não reconfirme, não peça autorização
IF-08, waves, bots, runtime, produto, piloto, Bedrock, secrets, network, deps =
false até o operador mudar ACTIVE_CONTEXT_STATE.json. next_phase=null = aguardar.
F21/F32/F33 = ruído histórico, nunca como ação futura. CI repair ≠ avanço de fase.

## Escopo (allowlist)
O prompt define o escopo; faça só isso. Seja explícito sobre o PERMITIDO. Qualquer
escrita fora da allowlist do prompt = abort + report. Não peça autorização para
nada fora do escopo atual nem reconfirme locks já estabelecidos na fase.

## Anti-proliferação de gates
Um gate só vale se mudar ≥1 fato canônico: uma flag de autorização inverte, OU um
artifact real é criado em disco com hash registrado, OU um teste passa de
vermelho/ausente para verde. Gate que só reafirma locks anteriores = PROIBIDO.
Planning + Review do mesmo passo colapsam em UM gate, veredito único.

## CI (obrigatório após git push origin main)
Nunca self-report de PASS. Após o push: aguarde 30s → `gh run list --limit 20` →
se algum workflow estiver queued/waiting/requested/in_progress, aguarde 60s e
repita (sem limite) → quando todos terminais: CI_GREEN_CONFIRMED (todos success)
ou CI_FAILED. Nenhum relatório final antes de CI terminal. CI_PENDING é interino.
Se CI_FAILED: `gh run view --log-failed`, reporte workflow/job/causa-raiz/excerto,
repare, novo push, reinicie o polling. CI de fases anteriores não bloqueia.

## Sincronia de active-context
Toda fase que produz resultado exige active-context update como entregável
bloqueante. Se o Project repo avançou e aris-active-context/main não refletiu o
mesmo final phase state = CANONICAL_DRIFT → execute Active-Context Canonical Sync
Repair antes de qualquer próxima fase ou PASS.

## Completion (200%)
Sem completion falso. Se não está completo, não chame de final. Gap → warning/
deferred/blocked/next-phase. Evidência faltando = hipótese. Teste faltando =
candidato. Segurança faltando = não avança. Gate bypassável = não pronto.

## Similar
