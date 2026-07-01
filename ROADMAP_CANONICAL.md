# ARIS ROADMAP CANONICAL

## 0. Lapidarium
phase_id: LAPIDARIUM_FINAL_ROUTE_RECONCILIATION_AND_HANDOFF_PACKET
Status: CLOSED
Objetivo: Encerrar a reconciliação final de rota e consolidar o handoff terminal sem abrir execução nova.
Resultado final esperado: Estado terminal reconciliado, successor row removida da rota viva e trilha pós-Lapidarium candidate-only registrada.
Pesquisa / arquitetura / decisões:
Entrega mínima pra fechar (evidência): `ACTIVE_CONTEXT_STATE.json` reconciliado, `ARIS_BOOT.md` alinhado e operador source + candidate track preservados em artefato/state.
Próxima fase: POST_LAPIDARIUM_ARCHITECTURE_TRACK_OPENING

## 1. Infernus FULL
phase_id: INFERNUS_FULL
Status: CLOSED
Objetivo: Revelar falhas reais do sistema sob condições adversariais controladas.
Resultado final esperado: Minos final verdict + closure pass, com handoff Purgatorium pronto em `artifacts/infernus/if11_minos_final_verdict_closure/`.
Pesquisa / arquitetura / decisões:
Entrega mínima pra fechar (evidência): evidence bundle, vulnerability register, handoff graph e Minos verdict materializados e validados em artefatos.
Próxima fase: Purgatorium FULL

## 2. Purgatorium FULL
phase_id: PURGATORIUM_FULL
Status: CLOSED
Objetivo: Corrigir, mitigar ou quarentenar os findings vindos do Infernus.
Resultado final esperado: PURG-EXIT concluído com `IF09-FIND-001` tratado via S3, sem fechar finding aqui.
Pesquisa / arquitetura / decisões:
Entrega mínima pra fechar (evidência): pacote completo em `artifacts/purgatorium/*` com findings tratados, mitigados ou quarentenados.
Próxima fase: Infernus Revalidation

## 3. Infernus Revalidation
phase_id: INFERNUS_REVALIDATION
Status: CLOSED
Objetivo: Revalidar os findings tratados pelo Purgatorium.
Resultado final esperado: `IF09-FIND-001` fechado, `finding_closed=true` e `remediation_proven=true` já refletidos no estado canônico.
Pesquisa / arquitetura / decisões:
Entrega mínima pra fechar (evidência): veredito de revalidação registrado para o finding em escopo.
Próxima fase: DIAGNOSTICO_AUTOMACAO_GATE

## 4. Diagnóstico de Automação
phase_id: DIAGNOSTICO_AUTOMACAO_GATE
Status: CANDIDATE
Objetivo: Avaliar se o ARIS está pronto para automatizar antes de construir.
Resultado final esperado: checklist das 7 camadas com decisão explícita gap/sem-gap e, se houver gap bloqueante, abertura da camada de construção.
Pesquisa / arquitetura / decisões:
Entrega mínima pra fechar (evidência): checklist fechado das camadas input/perception, reasoning, orquestração, tools/action, memória, observabilidade e governança runtime.
Próxima fase: se gap bloqueante → Camada de Construção de Automação; senão → BenchUIX

## 5. BenchUIX
phase_id: BENCHUIX_TRACK
Status: CANDIDATE
Objetivo: Validar posicionamento competitivo, produto e experiência antes de avançar para as fases de consolidação e segurança ampliada.
Resultado final esperado: BENCHUIX-27 completo, trilha pronta para revisão do operador e sem abertura de locks reais.
Pesquisa / arquitetura / decisões:
Entrega mínima pra fechar (evidência): as 28 subfases BENCHUIX-00 a BENCHUIX-27 materializadas em artefatos e o pacote de revisão do operador pronto.
Próxima fase: Cinzel-mínimo

## 6. Cinzel-mínimo
phase_id: CINZEL_MINIMO
Status: PLANNED
Objetivo: Executar uma prova de vida com um workflow ponta a ponta e 3-5 execuções reais.
Resultado final esperado: um fluxo mínimo validado sem fault injection e com evidência suficiente para mostrar vida operacional.
Pesquisa / arquitetura / decisões:
Entrega mínima pra fechar (evidência): workflow ponta a ponta, evidências de execução e registro de resultado.
Próxima fase: Crisol

## 7. Crisol
phase_id: CRISOL
Status: PLANNED
Objetivo: Consolidar o sistema e remover contradições internas.
Resultado final esperado: sistema tecnicamente coeso, com contradições relevantes removidas.
Pesquisa / arquitetura / decisões:
Entrega mínima pra fechar (evidência): artefato de consolidação mostrando o que foi harmonizado e o que permaneceu deliberadamente separado.
Próxima fase: EXT-SEC 00→04

## 8. EXT-SEC 00→04
phase_id: EXT_SEC_00_04
Status: PLANNED
Objetivo: Preparar a base defensiva pré-Bedrock sem sistema vivo.
Resultado final esperado: pacote defensivo artifact-first com ledger, threat model, hardening, fixtures sintéticas e closeout.
Pesquisa / arquitetura / decisões:
Entrega mínima pra fechar (evidência): artifacts de segurança defensiva completos e validados.
Próxima fase: Cinzel completo

## 9. Cinzel completo
phase_id: CINZEL_COMPLETO
Status: PLANNED
Objetivo: Validar automação útil em ambiente simulado de SMB brasileiro.
Resultado final esperado: pelo menos 5 cenários/workflows com métricas de tempo, custo, aprovação, rollback, retry e artefatos.
Pesquisa / arquitetura / decisões:
Entrega mínima pra fechar (evidência): métricas completas registradas para todos os cenários mínimos.
Próxima fase: EXT-SEC 05→06

## 10. EXT-SEC 05→06
phase_id: EXT_SEC_05_06
Status: PLANNED
Objetivo: Executar a etapa externa autorizada de segurança ofensiva e retest.
Resultado final esperado: relatório de DAST/pentest e retest com escopo, janela, contas de teste, dados sintéticos, rollback e autorização legal documentados.
Pesquisa / arquitetura / decisões:
Entrega mínima pra fechar (evidência): autorização, escopo e evidência completa do teste externo.
Próxima fase: Bedrock Gate

## 11. Bedrock Gate
phase_id: BEDROCK_GATE
Status: PLANNED
Objetivo: Tomar a decisão máxima sobre produto real.
Resultado final esperado: decisão explícita de Bedrock registrada pelo operador.
Pesquisa / arquitetura / decisões:
Entrega mínima pra fechar (evidência): veredito Bedrock (PASS/WARN/BLOCK/NEEDS_REVIEW/REGRESSION/OBSOLETE) com evidência primária.
Próxima fase: Produto Parte 2 / Design Partner

## 12. Produto Parte 2 / Design Partner
phase_id: PRODUTO_PARTE_2_DESIGN_PARTNER
Status: PLANNED
Objetivo: Conduzir o primeiro uso real controlado.
Resultado final esperado: design partner ativo, feedback estruturado e ciclo inicial documentado.
Pesquisa / arquitetura / decisões:
Entrega mínima pra fechar (evidência): vertical, ICP, prospects, contrato, pricing, onboarding, suporte e feedback registrados.
Próxima fase: EXT-SEC 07→08

## 13. EXT-SEC 07→08 contínuo
phase_id: EXT_SEC_07_08_CONTINUOUS
Status: PLANNED
Objetivo: Manter o ciclo de segurança contínua após o início do produto.
Resultado final esperado: ciclo contínuo de segurança operacional documentado e sustentado no tempo.
Pesquisa / arquitetura / decisões:
Entrega mínima pra fechar (evidência): ciclo de vulnerability management, retest, emulação adversarial, incident response, backup/restore e revisão de isolamento de tenant.
Próxima fase: contínuo

## 14. Post-Lapidarium Architecture Track Opening
phase_id: POST_LAPIDARIUM_ARCHITECTURE_TRACK_OPENING
Status: CANDIDATE
Objetivo: Admitir a proposta True Phases 2–6 como trilha pós-Lapidarium candidate-only sem reabrir Lapidarium.
Resultado final esperado: operador source recebido, conflito classificado, label collisions registradas e trilha candidate-only admitida sem execução real.
Pesquisa / arquitetura / decisões:
Entrega mínima pra fechar (evidência): operator source receipt, conflict analysis, collision register, route options matrix, roadmap diff e no-execution attestation.
Próxima fase: LAPIDARIUM_FASE_2_ARQUITETURA_ALVO_TRUE

## 15. Lapidarium Fase 2 — Arquitetura Alvo True
phase_id: LAPIDARIUM_FASE_2_ARQUITETURA_ALVO_TRUE
Status: CANDIDATE
Objetivo: Definir a arquitetura alvo candidata para a trilha True sem abrir execução.
Resultado final esperado: target architecture charter candidate materializado com limites e premissas explícitos.
Pesquisa / arquitetura / decisões:
Entrega mínima pra fechar (evidência): escopo, fronteiras, restrições, interfaces e dependências de arquitetura.
Próxima fase: LAPIDARIUM_FASE_3_EXECUCAO_POR_FATIAS_TRUE

## 16. Lapidarium Fase 3 — Execução por Fatias True
phase_id: LAPIDARIUM_FASE_3_EXECUCAO_POR_FATIAS_TRUE
Status: CANDIDATE
Objetivo: Planejar a execução por fatias da trilha True sem tocar runtime real.
Resultado final esperado: plano de fatias e critérios de progressão candidate-only.
Pesquisa / arquitetura / decisões:
Entrega mínima pra fechar (evidência): matriz de fatias, critérios de aceite e travas de execução preservadas.
Próxima fase: LAPIDARIUM_FASE_4_CANONIZACAO_TRUE

## 17. Lapidarium Fase 4 — Canonização True
phase_id: LAPIDARIUM_FASE_4_CANONIZACAO_TRUE
Status: CANDIDATE
Objetivo: Canonizar o encadeamento True sem colidir com a revisão genuína já executada.
Resultado final esperado: pacote de canonização candidate-only com diferenciação explícita da revisão histórica.
Pesquisa / arquitetura / decisões:
Entrega mínima pra fechar (evidência): matriz de conflito de rótulos, regra de precedência e diff canônico.
Próxima fase: LAPIDARIUM_FASE_5_SELO_TRUE

## 18. Lapidarium Fase 5 — Selo True
phase_id: LAPIDARIUM_FASE_5_SELO_TRUE
Status: CANDIDATE
Objetivo: Selar a trilha True sem reabrir o conjunto de limpeza já encerrado.
Resultado final esperado: pacote de selagem candidate-only com lock e provenance claros.
Pesquisa / arquitetura / decisões:
Entrega mínima pra fechar (evidência): evidência de selagem, proveniência e locks preservados.
Próxima fase: LAPIDARIUM_FASE_6_GUARDA_TRUE

## 19. Lapidarium Fase 6 — Guarda True
phase_id: LAPIDARIUM_FASE_6_GUARDA_TRUE
Status: CANDIDATE
Objetivo: Registrar a guarda final da trilha True e a sua ponte segura para a automação.
Resultado final esperado: guarda candidate-only concluída e pronto para retomar o caminho macro existente.
Pesquisa / arquitetura / decisões:
Entrega mínima pra fechar (evidência): attestation da guarda, critérios de avanço e preservação do estado canônico.
Próxima fase: DIAGNOSTICO_AUTOMACAO_GATE
