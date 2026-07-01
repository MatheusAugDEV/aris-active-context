PROMPT CODEX — LAPIDARIUM_TRUE_PHASES_ROUTE_AMENDMENT_PACKET

Modelo: codex-1 | reasoning=high

Autorização:
Executar somente análise governance/artifact de admissão da proposta "Lapidarium True Phases 2–6".

Não executar Fase 2.
Não reabrir Lapidarium automaticamente.
Não alterar arquitetura real.
Não mover arquivos.
Não remover arquivos.
Não tocar runtime.
Não tocar produto.
Não tocar Bedrock.
Não acessar secrets.

Contexto:
O operador forneceu um desenho novo e detalhado para cinco fases que ele chama de fases
faltantes do Lapidarium:

- Fase 2: LAPIDARIUM_FASE_2_ARQUITETURA_ALVO
- Fase 3: LAPIDARIUM_FASE_3_EXECUCAO_POR_FATIAS
- Fase 4: LAPIDARIUM_FASE_4_CANONIZACAO_TRUE
- Fase 5: LAPIDARIUM_FASE_5_SELO_TRUE
- Fase 6: LAPIDARIUM_FASE_6_GUARDA

O active-context atual (pós gates de hoje: "Roadmap Único" + "Limpeza de Referências
Residuais") registra Lapidarium como fechado depois de F5 residual safe resolution, com
stale pointers reconciliados. A próxima rota candidata registrada HOJE é
DIAGNOSTICO_AUTOMACAO_GATE — não BENCHUX_ROUTE_OPENING_PACKET (esse nome é obsoleto,
substituído no gate de hoje).

ROADMAP_CANONICAL.md hoje é a ÚNICA fonte de sequência viva — não existe mais Transition
Table separada. O bloco "## 0. Lapidarium" nesse arquivo diz:

  Status: CLOSED
  Próxima fase: DIAGNOSTICO_AUTOMACAO_GATE

Portanto, este pacote deve decidir como admitir a nova proposta sem corromper o estado
canônico E sem recriar uma segunda fonte de sequência fora do ROADMAP_CANONICAL.md.

Leia primeiro, nesta ordem:
1. ACTIVE_CONTEXT_STATE.json
2. ARIS_BOOT.md
3. ROADMAP_CANONICAL.md
4. DECISION_LOCKS.md
5. ACTIVE_CONTEXT_SCHEMA.json
6. scripts/validate_active_context_state.py
7. artifacts/lapidarium/lapidarium_final_route_reconciliation_packet.json
8. artifacts/lapidarium/lapidarium_final_handoff_decision.json
9. artifacts/lapidarium/lapidarium_final_stale_pointer_register.json
10. artifacts/lapidarium/lapidarium_final_residuals_carry_forward_register.json
11. artifacts/lapidarium/lapidarium_final_no_macro_execution_attestation.json
12. artifacts/lapidarium/lapidarium_final_route_reconciliation_validation_evidence.json
13. artifacts/lapidarium/lapidarium_fase5_residuals_safe_resolution_packet.json
14. artifacts/lapidarium/lapidarium_fase5_residuals_safe_resolution_validation_evidence.json

Também materialize como operator source, sem reinterpretar livremente:
- Criar operator_inputs/lapidarium_true_phases_2_to_6_operator_source.md
- Copiar integralmente o desenho fornecido pelo operador para esse arquivo.
- Não alterar conteúdo sem marcar como normalização separada.

Guards: AC-READ, OPERATOR-SOURCE-MATERIALIZATION, ROUTE-AMENDMENT-ONLY, GOVERNANCE-ONLY,
ARTIFACT-ONLY, NO-PHASE-2-EXECUTION, NO-LAPIDARIUM-REOPEN-BY-DEFAULT,
NO-ARCHITECTURE-MUTATION, NO-FILE-DELETION, NO-FILE-MOVE, NO-GIT-RM, NO-CLEANUP,
NO-RUNTIME, NO-REAL-APPLY, NO-PRODUCT, NO-BEDROCK, NO-SECRETS, NO-SECRET-PRINT,
NO-ENV-READ, NO-HISTORY-REWRITE, NO-FORCE-PUSH, NO-ROOT-MARKDOWN-MIRRORS, MAIN-ONLY,
COMMIT-PUSH-HASH

Objetivo:
Admitir formalmente a proposta "Lapidarium True Phases 2–6" como fonte do operador e
produzir uma decisão canônica de encaixe — que precisa ficar refletida tanto no
ACTIVE_CONTEXT_STATE.json quanto no ROADMAP_CANONICAL.md, nunca só em um dos dois.

A decisão deve responder:

1. A proposta contradiz o fechamento atual do Lapidarium?
2. A proposta deve reabrir Lapidarium?
3. A proposta deve virar uma nova trilha pós-Lapidarium?
4. A proposta deve substituir DIAGNOSTICO_AUTOMACAO_GATE como próxima rota candidata,
   ou precede ele?
5. Qual é a próxima fase segura depois desta admissão?
6. Fase 2 pode ser aberta como candidate-only?
7. Quais locks continuam fechados?
8. Como o bloco "## 0. Lapidarium" (ou blocos novos) do ROADMAP_CANONICAL.md precisa
   mudar para refletir essa decisão, no formato de fase única já estabelecido
   (Status / Objetivo / Resultado final esperado / Pesquisa-arquitetura-decisões /
   Entrega mínima / Próxima fase)?

Interpretação obrigatória:
- O fechamento atual do Lapidarium é canônico até que esta emenda seja validada.
- A proposta do operador é forte, mas ainda não é estado canônico.
- Nenhuma execução real pode ocorrer neste pacote.
- O pacote pode recomendar abrir LAPIDARIUM_FASE_2_ARQUITETURA_ALVO como candidate-only,
  mas não pode executá-la.
- Se houver conflito entre roadmap anterior e operador source novo, registrar conflito e
  decisão de precedência.
- Se for necessário reabrir Lapidarium, isso deve ser explícito, versionado e
  justificado como route amendment.
- ROADMAP_CANONICAL.md é a ÚNICA fonte de sequência. Qualquer decisão de rota tomada
  aqui que não seja refletida nele é inválida por construção — não crie uma segunda
  fonte de verdade dentro de ACTIVE_CONTEXT_STATE.json que não bata com o roadmap.

Escopo permitido:
1. Criar operator source:
   - operator_inputs/lapidarium_true_phases_2_to_6_operator_source.md

2. Criar análise comparativa:
   - fechamento canônico atual vs proposta nova
   - fases já fechadas vs fases que o operador diz faltar
   - diferenças entre "Fase 4 Revisão Genuína" (já executada) e
     "Fase 4 Canonização True" (proposta, não executada)
   - diferenças entre "Fase 5 Cleanup" (já executada) e "Fase 5 Selo True"
     (proposta, não executada)

3. Classificar a proposta:
   - route_reopen_candidate
   - post_lapidarium_candidate
   - diagnostico_automacao_precondition_candidate
   - supersedes_prior_lapidarium_labels_candidate

4. Produzir decisão recomendada conservadora:
   - preferir NÃO apagar o fechamento anterior;
   - preferir preservar histórico;
   - preferir abrir uma trilha nova explicitamente nomeada, se necessário;
   - não tratar fases antigas como erro sem evidência;
   - se os nomes antigos colidem, usar nomes *_TRUE para evitar colisão.

5. Definir próxima fase candidate-only:
   - se aprovado: LAPIDARIUM_FASE_2_ARQUITETURA_ALVO_CANDIDATE_OPENING
   - ou POST_LAPIDARIUM_ARCHITECTURE_TRACK_OPENING
   - escolher uma e justificar.

6. Atualizar active-context (arquivos vivos, não espelhos root):
   - ACTIVE_CONTEXT_STATE.json
   - ACTIVE_CONTEXT_SCHEMA.json — SE novo campo top-level for admitido, é
     OBRIGATÓRIO incrementar schema_version (ex.: 3.34 → 3.35) e adicionar a chave
     correspondente schema_3_35_change_summary em versioning_contract descrevendo
     exatamente o que mudou, seguindo o padrão de todas as entradas anteriores
     (schema_3_0 até schema_3_34) já presentes no arquivo. Não pular esse passo.
   - ROADMAP_CANONICAL.md — OBRIGATÓRIO. O bloco "## 0. Lapidarium" precisa ser
     atualizado para refletir a decisão desta emenda. Se a decisão for
     "post_lapidarium_candidate" ou "reopen": adicionar blocos novos no MESMO
     formato usado por todas as outras fases do arquivo (Status/Objetivo/Resultado
     final esperado/Pesquisa-arquitetura-decisões/Entrega mínima/Próxima fase),
     com Status=CANDIDATE, para Fase 2 a 6 (nomes *_TRUE se houver colisão),
     e ajustar "Próxima fase:" do bloco Lapidarium (ou do bloco que fechar essa
     cadeia) para apontar corretamente. NÃO deixar o roadmap e o
     ACTIVE_CONTEXT_STATE.json divergindo entre si — se divergirem, o pacote
     inteiro é INVALID.
   - DECISION_LOCKS.md
   - BOOT.md (via scripts/render_boot.py, gerado a partir do STATE.json atualizado
     — nunca editado à mão)
   - NÃO editar CURRENT_STATE.md nem NEXT_ACTION.md na raiz do repo — esses
     mirrors são noncanonical pela decisão de fronteira BOUNDARY_C já registrada
     em versioning_contract; editar eles reintroduziria drift de espelho.

7. Criar artifacts:
   - artifacts/lapidarium/lapidarium_true_phases_route_amendment_packet.json
   - artifacts/lapidarium/lapidarium_true_phases_operator_source_receipt.json
   - artifacts/lapidarium/lapidarium_true_phases_conflict_analysis.json
   - artifacts/lapidarium/lapidarium_true_phases_label_collision_register.json
   - artifacts/lapidarium/lapidarium_true_phases_route_options_matrix.json
   - artifacts/lapidarium/lapidarium_true_phases_admission_decision.json
   - artifacts/lapidarium/lapidarium_true_phases_roadmap_canonical_diff.json
     (diff explícito do que mudou em ROADMAP_CANONICAL.md — antes/depois do
     bloco "## 0. Lapidarium" e de qualquer bloco novo adicionado)
   - artifacts/lapidarium/lapidarium_true_phases_no_execution_attestation.json
   - artifacts/lapidarium/lapidarium_true_phases_validation_evidence.json
   - artifacts/lapidarium/lapidarium_true_phases_report.md

8. Commit direto em main.
9. Push para origin/main.
10. Polling CI até terminal.

Campos esperados no ACTIVE_CONTEXT_STATE.json:
- lapidarium_true_phases_operator_source_received: true
- lapidarium_true_phases_operator_source_path:
  operator_inputs/lapidarium_true_phases_2_to_6_operator_source.md
- lapidarium_true_phases_route_amendment_completed: true
- lapidarium_true_phases_route_amendment_decision: pass|blocked
- lapidarium_true_phases_conflicts_with_closed_lapidarium: true/false
- lapidarium_true_phases_label_collision_detected: true
- lapidarium_true_phases_label_collision_items: list
- lapidarium_true_phases_recommended_route_handling: one of:
  - REOPEN_LAPIDARIUM_AS_TRUE_PHASES
  - CREATE_POST_LAPIDARIUM_ARCHITECTURE_TRACK
  - KEEP_AS_DIAGNOSTICO_AUTOMACAO_PRECONDITION_CANDIDATE
  - BLOCK_PENDING_OPERATOR_CLARIFICATION
- lapidarium_true_phases_next_candidate_phase: chosen next candidate
- lapidarium_true_phases_execution_authorized: false
- lapidarium_true_phases_phase2_execution_authorized: false
- lapidarium_true_phases_roadmap_canonical_updated: true
- lapidarium_true_phases_roadmap_canonical_matches_state: true
  (campo de auto-verificação: precisa bater com o que o validator confirma)
- runtime_integration_allowed: false
- real_apply_authorized: false
- production_authorized: false
- product_ready: false
- secrets_access_authorized: false

Fora de escopo:
- Não executar LAPIDARIUM_FASE_2_ARQUITETURA_ALVO.
- Não criar TARGET_ARCHITECTURE.md ainda.
- Não criar ADRs fundadores ainda.
- Não mover arquivos.
- Não apagar arquivos.
- Não reescrever ACTIVE_CONTEXT_STATE.json do zero.
- Não alterar código funcional.
- Não tocar .env.
- Não acessar secrets.
- Não executar runtime.
- Não abrir produto.
- Não abrir Bedrock.
- Não abrir BenchUIX real.
- Não pesquisar concorrentes.
- Não instalar dependências.
- Não reescrever histórico.
- Não force push.
- Não editar CURRENT_STATE.md / NEXT_ACTION.md na raiz (mirrors noncanonical).

Entregáveis detalhados:

1. lapidarium_true_phases_route_amendment_packet.json
Deve conter: phase, decision, operator_source_received, closed_lapidarium_status,
conflict_detected, label_collision_detected, recommended_route_handling,
next_candidate_phase, execution_authorized=false, roadmap_canonical_updated=true

2. lapidarium_true_phases_operator_source_receipt.json
Deve conter: source path, received_at, phase list extracted, hash of operator source,
source treated as operator-provided, not inferred

3. lapidarium_true_phases_conflict_analysis.json
Deve comparar: current canonical Lapidarium closed status, new claim that phases 2–6
remain, current next candidate DIAGNOSTICO_AUTOMACAO_GATE (não BenchUX — corrigido),
proposed Fase 2–6 chain, risk of direct reopening, risk of ignoring proposal,
recommended safe handling

4. lapidarium_true_phases_label_collision_register.json
Deve listar: LAPIDARIUM_FASE_4_REVISAO_CODIGO_GENUINO vs
LAPIDARIUM_FASE_4_CANONIZACAO_TRUE; LAPIDARIUM_FASE_5_*CLEANUP* vs
LAPIDARIUM_FASE_5_SELO_TRUE; qualquer outro nome colidente; recommended naming rule

5. lapidarium_true_phases_route_options_matrix.json
Opções mínimas: direct reopen Lapidarium; create post-Lapidarium architecture track;
treat as DIAGNOSTICO_AUTOMACAO_GATE precondition; block pending operator clarification.
Para cada uma: pros, cons, risk, compatibility with current ROADMAP_CANONICAL.md,
recommended yes/no

6. lapidarium_true_phases_admission_decision.json
Deve conter: final decision, why this is safest, whether Fase 2 can be opened next as
candidate-only, whether DIAGNOSTICO_AUTOMACAO_GATE remains candidate or is superseded/
reordered, exact next candidate phase

7. lapidarium_true_phases_roadmap_canonical_diff.json
Deve conter: bloco "## 0. Lapidarium" antes e depois (texto completo dos dois), lista
de blocos novos adicionados (se houver) com seus phase_id, confirmação de que
"Próxima fase:" de cada bloco afetado está consistente com
active_next_phase/next_phase do ACTIVE_CONTEXT_STATE.json

8. lapidarium_true_phases_no_execution_attestation.json
Deve declarar: no Phase 2 execution, no architecture creation, no file movement,
no deletion, no runtime, no product, no Bedrock, no BenchUIX execution, no secrets,
no env read, no history rewrite, no force push, no root markdown mirror edits

Validações obrigatórias:
1. python3 -m json.tool ACTIVE_CONTEXT_STATE.json > /dev/null
2. python3 -m json.tool ACTIVE_CONTEXT_SCHEMA.json > /dev/null
3. test -s scripts/validate_active_context_state.py
4. python3 scripts/validate_active_context_state.py
5. Validar JSON de todos os artifacts novos.
6. Confirmar que o operator source foi gravado e hashado.
7. Confirmar que TARGET_ARCHITECTURE.md NÃO foi criado nesta fase.
8. Confirmar que Fase 2 NÃO foi executada.
9. Confirmar que nenhum arquivo de Project_ARIS foi removido/movido.
10. Confirmar que .env não foi lido.
11. Confirmar que CURRENT_STATE.md e NEXT_ACTION.md na raiz não foram tocados.
12. Confirmar que ROADMAP_CANONICAL.md foi atualizado E que o campo "Próxima fase:"
    de cada bloco afetado bate exatamente com active_next_phase/next_phase do
    ACTIVE_CONTEXT_STATE.json — rodar grep cruzado entre os dois arquivos como prova.
13. Se ACTIVE_CONTEXT_SCHEMA.json mudou: confirmar que schema_version foi
    incrementado e que existe schema_X_Y_change_summary correspondente.
14. Confirmar locks reais false: runtime, product, production, real_apply, secrets,
    Bedrock
15. git diff --stat
16. git status --short
17. Commit:
    git add ACTIVE_CONTEXT_STATE.json ACTIVE_CONTEXT_SCHEMA.json ROADMAP_CANONICAL.md \
      DECISION_LOCKS.md BOOT.md \
      operator_inputs/lapidarium_true_phases_2_to_6_operator_source.md \
      artifacts/lapidarium/
    git commit -m "LAPIDARIUM: admit true phases route amendment"
18. Push:
    git push origin main
19. CI polling:
    aguarde 30s
    gh run list --limit 20
    gh run watch <RUN_ID> --exit-status
20. Confirmar:
    git fetch origin main
    git rev-parse HEAD == git rev-parse origin/main

Critérios de sucesso:
- Proposta do operador materializada como fonte.
- Conflito com fechamento atual analisado.
- Colisão de labels analisada.
- Próximo candidate definido sem execução real.
- ROADMAP_CANONICAL.md e ACTIVE_CONTEXT_STATE.json consistentes entre si — mesma
  próxima fase nos dois, sem exceção.
- Fase 2 não executada.
- Todos os locks reais fechados.
- Validator pass.
- CI green.
- HEAD == origin/main.

Atualização final obrigatória:
- SHA/blob lido no início.
- SHA do commit final.
- HEAD == origin/main.
- CI terminal state + run id.
- Validator decision.
- Operator source path.
- Operator source hash.
- Conflict detected: true/false.
- Label collisions detected.
- Recommended route handling.
- Next candidate phase.
- Confirmação: ROADMAP_CANONICAL.md e ACTIVE_CONTEXT_STATE.json consistentes.
- Confirmação: Fase 2 execution authorized = false.
- Confirmação: TARGET_ARCHITECTURE.md não criado.
- Confirmação: nenhum runtime/produto/Bedrock/real_apply/secrets.
- Confirmação: nenhum cleanup/move/delete.
- Confirmação: CURRENT_STATE.md/NEXT_ACTION.md na raiz não tocados.
- Próximo passo recomendado:
  - se a decisão for abrir Fase 2: emitir
    LAPIDARIUM_FASE_2_ARQUITETURA_ALVO_CANDIDATE_OPENING;
  - se a decisão for nova trilha: emitir o route opening correspondente.