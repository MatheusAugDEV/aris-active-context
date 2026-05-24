# BEDROCK_GATE — Chão Inviolável do ARIS

## Draft do manifesto de fixtures dry-run de request
Este draft define o manifesto canônico dos fixtures simulados que serão usados futuramente para testar as regras de validação do request sem executar o Bedrock real.
Ele não materializa fixtures reais, não valida requests reais, não promove produto e não cria veredito real.

### Identidade do manifesto
Campos obrigatórios:
- `manifest_id`
- `manifest_schema_version`
- `bedrock_gate_version`
- `created_for_phase`
- `created_at`
- `created_by`
- `fixture_schema_version`
- `validation_rules_version`
- `input_contract_version`
- `fixture_count`
- `positive_fixture_count`
- `negative_fixture_count`
- `coverage_targets`
- `non_execution_guarantee`

### Estrutura de cada fixture
Cada fixture do manifesto deve ter:
- `fixture_id`
- `fixture_name`
- `fixture_category`
- `fixture_priority`
- `target_type`
- `requested_verdict_scope`
- `expected_validation_status`
- `expected_rejection_ids`
- `expected_warning_ids`
- `expected_lab_continuation_allowed`
- `expected_product_promotion_allowed`
- `expected_commercial_use_allowed`
- `covered_validation_layers`
- `covered_rejection_rules`
- `covered_target_rules`
- `covered_scope_rules`
- `requires_human_review_mock`
- `requires_rollback_mock`
- `requires_boundary_mock`
- `requires_evidence_bundle_mock`
- `requires_blocker_scan_mock`
- `future_fixture_path`
- `future_expected_path`

### Prioridades
As prioridades canônicas são:
- `critical`
- `high`
- `medium`
- `low`

Regras:
- fixtures que cobrem product promotion indevida devem ser `critical`
- fixtures que cobrem commercial delivery indevida devem ser `critical`
- fixtures que cobrem runtime/network/action runtime/real mutation sem rollback devem ser `critical`
- fixtures positivos Lab-only podem ser `medium` ou `high`
- fixtures de documentação/cobertura complementar podem ser `low`

### Conjunto mínimo de fixtures
O manifesto define 22 fixtures no total, com 5 positivos e 17 negativos.

Positivos:
- `valid_lab_continuation_partial_evidence`
- `valid_technical_readiness_no_product_pass`
- `valid_product_candidate_with_conditions`
- `valid_safety_blocker_review_partial_evidence`
- `valid_evidence_completeness_review_no_product_pass`

Negativos:
- `invalid_missing_target_id`
- `invalid_missing_target_type`
- `invalid_target_type_unknown`
- `invalid_missing_source_commit`
- `invalid_product_promotion_without_evidence_bundle`
- `invalid_product_promotion_without_blocker_scan`
- `invalid_product_promotion_without_human_review`
- `invalid_runtime_change_without_boundary_evidence`
- `invalid_real_mutation_without_rollback_evidence`
- `invalid_commercial_delivery_without_risk_register`
- `invalid_commercial_delivery_without_known_limits`
- `invalid_source_of_truth_contradictory`
- `invalid_dirty_worktree_without_notes`
- `invalid_llm_as_sole_judge_requested`
- `invalid_attempt_to_skip_completeness_gate`
- `invalid_attempt_to_skip_blocker_scan`
- `invalid_attempt_to_promote_lab_only_to_product`

### Coverage matrix
O manifesto deve cobrir:
- todas as validation layers do R17
- todos os requested scopes do R16/R17
- todos os target types do R16/R17/R15
- todas as hard-block rejection rules canônicas
- as invariantes de nao execucao

### Expected outcome rules
Regras obrigatórias:
- nenhum fixture pode declarar `expected_product_promotion_allowed=true`
- nenhum fixture pode declarar `expected_commercial_use_allowed=true`
- fixtures positivos podem ser aceitos para Bedrock evaluation, mas nunca como product pass
- fixtures Lab-only devem manter product promotion false
- fixtures negativos devem ter ao menos um rejection ID
- commercial delivery sem human review, risk register ou known limits deve ser blocked
- runtime/action runtime/network/real mutation sem boundary ou rollback deve ser blocked
- LLM-as-sole-judge deve ser blocked
- attempts to skip completeness gate or blocker scan devem ser blocked

### Future runner relation
Um runner determinístico futuro deve:
- ler o manifesto
- carregar um fixture por vez
- aplicar as regras do R17
- comparar a saida com o esperado
- permanecer dry-run only
- não executar runtime
- não chamar rede
- não criar veredito real
- emitir apenas artifact de dry-run

### Future paths
Os caminhos futuros propostos são:
- `artifacts/bedrock/fixtures/evaluation_requests/fixture_manifest.json`
- `artifacts/bedrock/fixtures/evaluation_requests/<fixture_id>.json`
- `artifacts/bedrock/fixtures/evaluation_requests/<fixture_id>_expected.json`

R19 define o manifesto apenas.
Ele não materializa os fixtures, não executa runner e não avalia Bedrock.

## Draft de schema de dry-run fixtures de validação de request
Este draft define fixtures simulados para testar as regras de validação do request sem executar o Bedrock real.
Ele não valida requests reais, não promove produto e não cria veredito real.

### Identidade do fixture
Campos obrigatórios:
- `fixture_id`
- `fixture_schema_version`
- `bedrock_gate_version`
- `fixture_name`
- `fixture_description`
- `fixture_category`
- `target_type`
- `requested_verdict_scope`
- `expected_validation_status`
- `expected_rejection_ids`
- `expected_warning_ids`
- `expected_lab_continuation_allowed`
- `expected_product_promotion_allowed`
- `expected_commercial_use_allowed`
- `created_for_phase`
- `source_phase`
- `non_execution_guarantee`

### Categorias de fixture
Categorize fixtures as:
- `valid_lab_only_request`
- `valid_technical_readiness_request`
- `valid_product_candidate_request_with_conditions`
- `invalid_missing_target`
- `invalid_missing_source_commit`
- `invalid_product_scope_without_evidence_bundle`
- `invalid_product_scope_without_blocker_scan`
- `invalid_product_scope_without_human_review`
- `invalid_runtime_change_without_boundary_evidence`
- `invalid_real_mutation_without_rollback_evidence`
- `ambiguous_target_request`
- `stale_source_of_truth_request`
- `contradictory_source_of_truth_request`
- `dirty_worktree_without_notes_request`
- `llm_as_sole_judge_requested`
- `attempt_to_skip_completeness_gate`
- `attempt_to_skip_blocker_scan`
- `attempt_to_promote_lab_only_result_to_product`
- `commercial_scope_without_risk_register`
- `commercial_scope_without_known_limits`

### Fixture payload structure
Cada fixture deve conter:
- `input_request`
- `mock_source_state`
- `mock_evidence_references`
- `mock_source_of_truth_state`
- `mock_boundary_state`
- `mock_risk_state`
- `mock_human_review_state`
- `mock_non_goal_assertions`
- `expected_validation_result`
- `expected_remediations`
- `expected_next_allowed_scope`
- `expected_blocked_scope`

### Input request
Use the R16 request fields:
- `evaluation_request_id`
- `request_schema_version`
- `bedrock_gate_version`
- `requested_at`
- `requested_by`
- `request_reason`
- `target_type`
- `target_id`
- `target_phase`
- `target_scope`
- `requested_verdict_scope`
- `requested_output_artifacts`
- `source_repositories`
- `source_commits`
- `source_branch`
- `worktree_state`

### Expected validation result
Each fixture must declare:
- `validation_status`
- `accepted_for_bedrock_evaluation`
- `accepted_for_lab_only`
- `accepted_for_product_scope`
- `accepted_for_commercial_scope`
- `rejection_reasons`
- `warning_reasons`
- `missing_inputs`
- `required_remediations`
- `required_next_artifacts`
- `human_review_required`
- `next_recommended_phase`

Positive fixtures must preserve the rule that a valid request does not imply Product Ready.

### Positive fixture classes
- lab continuation request valid with partial evidence
- technical readiness request valid without product pass
- product candidate request valid with conditions
- safety blocker review valid with partial evidence
- evidence completeness review valid without product pass

### Negative fixture classes
- target absent
- target_type invalid
- source commit absent
- product promotion without Evidence Bundle
- product promotion without blocker scan
- commercial delivery without human review
- runtime change without boundary evidence
- real mutation without rollback evidence
- source-of-truth contradictory
- LLM-as-sole-judge attempt
- completeness gate skip attempt
- Lab-only to product promotion attempt

### Fixture invariants
- no runtime execution
- no network call
- no real file mutation
- no real verdict creation
- no real Evidence Bundle creation
- no frontend/backend/action runtime/voice mutation
- no dependency installation
- no secret use
- no Obsidian bulk-read
- small and auditable
- usable by a future deterministic runner

### Relationship to R16 and R17
- R16 defines the request contract.
- R17 defines the request validation rules.
- R18 defines dry-run fixtures for testing those rules.
- R18 does not execute validation real or substitute the real Bedrock stack.

### Future fixture paths
Proposed future paths:
- `artifacts/bedrock/fixtures/evaluation_requests/<fixture_id>.json`
- `artifacts/bedrock/fixtures/evaluation_requests/<fixture_id>_expected.json`
- `artifacts/bedrock/fixtures/evaluation_requests/fixture_manifest.json`

R18 does not create the future tree yet; it only defines the schema.

## Draft de regras de validação da solicitação de avaliação
Este draft define as regras determinísticas que validam uma solicitação Bedrock antes de qualquer completeness gate, blocker scan ou verdict futuro.
Ele não executa o Bedrock real, não promove produto e não substitui R16.

### Camadas de validação
As camadas obrigatórias são:
- `identity_validation`
- `target_validation`
- `scope_validation`
- `source_state_validation`
- `evidence_reference_validation`
- `source_of_truth_validation`
- `boundary_validation`
- `risk_validation`
- `human_review_validation`
- `non_goal_validation`
- `rejection_reason_validation`

Cada camada deve registrar objetivo, campos exigidos, critérios de aprovação, critérios de rejeição, status possível e remediação mínima.

### Estados de validação
Estados canônicos:
- `input_valid`
- `input_incomplete`
- `input_invalid`
- `input_ambiguous`
- `input_stale`
- `input_contradictory`
- `input_product_scope_blocked`
- `input_requires_human_review`
- `input_lab_only_allowed`

### Regras por escopo
- `lab_continuation_only`: aceita evidência parcial, mas marca `product_promotion_allowed=false`.
- `technical_readiness_only`: nunca emite product pass.
- `product_candidate_review`: exige evidence bundle referenciado; lacunas documentadas podem existir.
- `product_promotion_review`: exige evidence bundle, completeness gate e blocker scan.
- `commercial_delivery_review`: exige evidence bundle completo, blocker scan completo, human review explícita, risk register e known limits.
- `runtime_change_review`: exige boundary evidence e rollback/recovery evidence.
- `safety_blocker_review`: pode iniciar com evidência parcial, mas nunca libera produto sozinho.
- `evidence_completeness_review`: valida completude, não produto.

### Regras por target type
- `runtime_change`, `frontend_change`, `backend_change`, `action_runtime_change`, `voice_change`, `network_change` exigem boundary evidence.
- Mudanças mutantes reais exigem rollback/recovery evidence.
- Candidatos produto exigem Evidence Bundle, blocker scan, source-of-truth atualizado e human review.
- Candidatos comerciais exigem risk register, known limits, UX evidence, cost/performance evidence e human review.
- `phase`, `capability` e `macroblock` podem ser Lab-only se o escopo for limitado.

### Rejeições hard-block
Rejeições canônicas:
- `missing_target_id`
- `missing_target_type`
- `invalid_target_type`
- `missing_requested_scope`
- `invalid_requested_scope`
- `missing_source_commit`
- `missing_source_repository`
- `missing_active_context_read_evidence`
- `stale_or_contradictory_source_of_truth`
- `dirty_worktree_without_notes`
- `product_scope_without_evidence_bundle`
- `product_scope_without_blocker_scan`
- `product_scope_without_human_review`
- `runtime_change_without_boundary_evidence`
- `real_mutation_without_rollback_evidence`
- `commercial_scope_without_known_limits`
- `commercial_scope_without_risk_register`
- `llm_as_sole_judge_requested`
- `attempt_to_skip_completeness_gate`
- `attempt_to_skip_blocker_scan`
- `attempt_to_use_memory_against_active_context`
- `attempt_to_promote_lab_only_result_to_product`

### Source-of-truth validation
Request validation must prove:
- active-context was read;
- `CURRENT_STATE.md`, `NEXT_ACTION.md`, `DECISION_LOCKS.md`, `CONTEXT_INDEX.md`, `ARIS_PHASE_LEDGER.md` were considered;
- `BEDROCK_GATE.md` was considered;
- stale/conflicting context was recorded;
- Obsidian was either not used or explicitly not used;
- stale memory was not used against active source-of-truth.

### Worktree and repo state validation
Request validation must record:
- branch
- commit
- remote status
- dirty worktree
- staged changes
- unrelated changes preserved
- source repo separated from active-context repo
- push status

Worktree dirtiness does not automatically block Lab, but blocks product-grade unless scoped notes exist and diffs are bounded.

### Future output schema
Future validation output should contain:
- `phase`
- `evaluation_request_id`
- `request_schema_version`
- `target_id`
- `target_type`
- `requested_verdict_scope`
- `validation_status`
- `validation_layers`
- `accepted_for_bedrock_evaluation`
- `accepted_for_lab_only`
- `accepted_for_product_scope`
- `rejection_reasons`
- `warning_reasons`
- `missing_inputs`
- `required_remediations`
- `required_next_artifacts`
- `human_review_required`
- `next_recommended_phase`

### Relation to R10-R16
- R16 defines the contract of the request.
- R17 defines the deterministic validation rules for that request.
- R17 decides whether evaluation may start.
- R17 does not run completeness, blocker scan, or verdict artifact logic.
- R17 does not imply product pass.

## Draft de contrato de entrada da avaliação
Este draft define o formato mínimo de uma solicitação Bedrock válida antes que qualquer avaliação futura possa começar.
Ele não executa a avaliação, não promove produto e não substitui as camadas R12 a R15.

### Identidade da solicitação
Campos obrigatórios:
- `evaluation_request_id`
- `request_schema_version`
- `bedrock_gate_version`
- `requested_at`
- `requested_by`
- `request_reason`
- `target_type`
- `target_id`
- `target_phase`
- `target_scope`
- `requested_verdict_scope`
- `requested_output_artifacts`
- `source_repositories`
- `source_commits`
- `source_branch`
- `worktree_state`

### Tipos de alvo aceitos
O contrato consolida os `target_type` canônicos de R12/R13/R15:
- `phase`
- `capability`
- `macroblock`
- `runtime_change`
- `frontend_change`
- `backend_change`
- `action_runtime_change`
- `voice_change`
- `network_change`
- `product_release_candidate`
- `commercial_delivery_candidate`

Regras por classe:
- `phase`, `capability`, `macroblock`: podem pedir `lab_continuation_only`, `technical_readiness_only` e `evidence_completeness_review`; promoção de produto exige bundle completo, completeness e blocker scan quando aplicável.
- `runtime_change`, `frontend_change`, `backend_change`, `action_runtime_change`, `voice_change`, `network_change`: exigem boundary evidence, rollback/recovery evidence, source-of-truth references e human review para escopo product-grade.
- `product_release_candidate`, `commercial_delivery_candidate`: exigem bundle completo, completeness gate completo, blocker scan completo e human review explícita; não podem ser tratados como lab-only.

### Escopos de veredito aceitos
`requested_verdict_scope` deve ser um destes valores:
- `lab_continuation_only`
- `technical_readiness_only`
- `product_candidate_review`
- `product_promotion_review`
- `commercial_delivery_review`
- `runtime_change_review`
- `safety_blocker_review`
- `evidence_completeness_review`

Regras:
- `product_promotion_review` exige Evidence Bundle completo.
- `commercial_delivery_review` exige Evidence Bundle completo, blocker scan completo e human review explícita.
- `runtime_change_review` exige boundary evidence e rollback/recovery evidence.
- `safety_blocker_review` pode começar com evidência parcial, mas não pode liberar produto sem completude.
- `lab_continuation_only` nunca deve ser confundido com product pass.

### Inputs obrigatórios
Todo request deve referenciar:
- `target_identity`
- `requested_scope`
- `evidence_bundle_reference`
- `technical_artifact_references`
- `source_of_truth_references`
- `validation_references`
- `risk_references`
- `blocker_scan_reference`
- `human_review_reference`
- `known_limitations`
- `dirty_worktree_notes`
- `protected_sources_assertion`
- `non_goal_assertions`

### Regras de rejeição
O request deve ser rejeitado antes do início da avaliação se:
- o target estiver ausente ou ambíguo;
- o `target_type` for inválido;
- faltar source commit;
- faltar Evidence Bundle para escopo product-grade;
- faltar blocker scan para escopo product-grade;
- o active-context não tiver sido lido;
- houver source-of-truth contraditório sem reconciliação;
- o worktree estiver sujo sem nota;
- houver tentativa de promover produto com evidência parcial;
- houver tentativa de pular completeness gate;
- houver tentativa de pular blocker scan;
- houver tentativa de usar LLM como juiz único;
- houver tentativa de usar memória histórica contra active-context;
- houver tentativa de avaliar mutação real sem rollback;
- houver tentativa de avaliar comercialmente sem human review.

### Input status
Estados possíveis:
- `input_valid`: a solicitação pode iniciar a avaliação futura, mas não implica product pass.
- `input_incomplete`: faltam campos ou referências obrigatórias; pode permitir continuidade Lab, não produto.
- `input_invalid`: o request quebra o contrato, está malformado ou impossível de auditar.
- `input_ambiguous`: o alvo, escopo ou pedido não estão suficientemente definidos.
- `input_stale`: o request referencia estado ou evidência ultrapassados.
- `input_contradictory`: a solicitação contradiz source-of-truth ou evidência materializada.
- `input_product_scope_blocked`: há bloqueio absoluto ou falta de evidência para escopo product-grade.
- `input_requires_human_review`: a avaliação só pode prosseguir com revisão humana explícita.
- `input_lab_only_allowed`: apenas continuidade Lab é permitida.

### Segurança e boundaries
Os campos booleanos a seguir devem sempre ser acompanhados de evidência referenciável, nunca apenas declaração:
- `runtime_modified`
- `frontend_modified`
- `backend_modified`
- `action_runtime_modified`
- `voice_modified`
- `network_enabled`
- `dependencies_installed`
- `productive_path_changed`
- `product_promotion_requested`
- `commercial_use_requested`
- `human_review_required`
- `rollback_required`
- `bedrock_runtime_gate_requested`

Regras:
- declaração booleana sem evidência não basta para escopo product-grade;
- qualquer mutação real exige rollback/recovery evidence;
- qualquer uso comercial exige human review explícita;
- qualquer mudança em runtime, produto ou boundary exige evidência de fronteira.

### Relação com R12-R15
- R12 define o Evidence Bundle.
- R13 define se o Evidence Bundle está completo.
- R14 define blocker scan.
- R15 define o artefato final de veredito.
- R16 apenas valida se a solicitação pode iniciar a avaliação.
- Um request válido não implica Evidence Bundle completo.
- Um request válido não implica Product Ready.

### Futuro artifact path
Proposta para fases futuras:
- `artifacts/bedrock/evaluation_inputs/<target_id>_bedrock_evaluation_input.json`
- `artifacts/bedrock/evaluation_inputs/<target_id>_bedrock_evaluation_input_report.md`

R16 não cria essa árvore agora; apenas documenta o contrato de entrada.

## Função
O Bedrock Gate é a primeira camada obrigatória de aprovação de qualquer fase, arquitetura, prompt Codex, feature, refactor, roadmap ou decisão operacional do ARIS.

Ele responde uma pergunta simples:

> Esta decisão viola alguma fundação inviolável do ARIS?

Se a resposta for sim, o resultado deve ser `BLOCKED`, mesmo que testes locais, artifacts, revisão humana ou gates específicos da fase pareçam passar.

## Ordem obrigatória de aprovação
Toda fase futura deve ser avaliada nesta ordem:

1. `BEDROCK_GATE`
2. `NORTH_POLE_ALIGNMENT`
3. `PHASE_SPECIFIC_GATES`
4. `ACTIVE_CONTEXT_UPDATE`
5. `COMMIT_PUSH_HASH_FINAL`

Nenhum gate posterior pode compensar falha no Bedrock Gate.

## Regras invioláveis
Uma fase, prompt ou alteração deve ser bloqueada se:

- mentir sobre capacidade, evidência, execução real, teste real ou status de produção;
- promover produto, cliente real, venda ou produção sem gate futuro explícito;
- alterar runtime, frontend, backend, action runtime, rede, áudio, Obsidian, MCP ou dependências fora do escopo autorizado;
- ativar MCP, escrever config MCP, escrever no vault, fazer bulk-read de Obsidian ou liberar rede sem gate explícito;
- instalar dependências, executar scripts externos, expor segredos ou ler ambiente fora de allowlist autorizada;
- burlar `NEXT_ACTION.md`, `DECISION_LOCKS.md`, `NORTH_POLE.md` ou source-of-truth oficial;
- tratar chat, intenção, roadmap conceitual, prompt ou memória como autorização materializada;
- transformar WARN em PASS sem evidência objetiva;
- avançar fase sem atualizar active-context quando a fase exige materialização;
- remover controle crítico para reduzir atrito sem mecanismo equivalente de segurança;
- criar automação real sem plano, permissão, ledger e rollback/compensação quando aplicável.

## Resultado
- `PASS`: nenhuma fundação violada.
- `WARN`: fundação preservada, mas há dívida ou ambiguidade controlada que precisa ser registrada.
- `BLOCKED`: fundação violada ou evidência insuficiente para provar preservação.
- `INVALID`: a fase não prova o que afirma provar.

## Draft de critérios de veredito
Este draft define como um futuro veredito Bedrock deve ser classificado.
Ele não executa o gate, não autoriza promoção e não substitui evidência materializada.

### Classes de veredito
- `INVALID`: a alegação não é sustentada por evidência, ou a fonte de verdade está contraditória.
- `BLOCKED`: existe um bloqueio absoluto ou ausência de evidência essencial.
- `LAB_ONLY_PASS`: a entrega é válida no laboratório, mas não pode ser promovida a produto.
- `TECHNICAL_PASS_PRODUCT_FAIL`: os testes técnicos passam, mas a prontidão de produto falha.
- `BEDROCK_WARN`: a entrega não tem bloqueio absoluto, mas ainda carrega dívida ou ambiguidade relevante.
- `PRODUCT_CANDIDATE`: a entrega pode entrar em piloto controlado ou pré-produção limitada.
- `PRODUCT_READY`: a entrega atende o mínimo confiável para produto, operação e auditoria.
- `EXCELLENT_PRODUCT_READY`: a entrega excede o mínimo de produto com robustez, clareza e diferenciação evidentes.

### Escala por dimensão
Cada dimensão recebe nota de `0` a `5`.
- `0`: ausente, contraditória ou impossível de provar.
- `1`: muito fraca, só observada em laboratório.
- `2`: parcial, com lacunas relevantes.
- `3`: aceitável, mas ainda não produto-ready.
- `4`: forte, consistente e auditável.
- `5`: excelente, robusta e pronta para uso comercial.

### Dimensões avaliadas
Bedrock avalia, no mínimo:
- Segurança.
- Privacidade e segredos.
- Determinismo.
- Evidência e auditabilidade.
- Testes e reprodutibilidade.
- Rollback, compensação e recuperação.
- Observabilidade.
- Isolation de falhas.
- Qualidade de resposta e comportamento.
- UX e clareza para usuário final.
- Performance e custo operacional.
- Manutenibilidade.
- Documentação e source-of-truth.
- Compatibilidade com roadmap e macroblocos.
- Prontidão comercial e de produto.
- Risco de regressão.
- Risco de automação indevida.
- Dependências externas.
- Fronteiras de runtime, frontend, backend, action runtime, voz e rede.

### Critérios bloqueantes absolutos
Os seguintes achados impedem `PRODUCT_READY`, mesmo com testes locais aprovados:
- segredo exposto.
- rede ativada sem gate explícito.
- runtime produtivo alterado sem autorização.
- ação real sem dry-run, permissão, ledger e rollback.
- ausência de evidência materializada.
- testes críticos ausentes.
- source-of-truth contraditório.
- rollback inexistente para mutação real.
- comportamento não reproduzível.
- resposta truncada ou falsa em caso crítico.
- dependência externa não pinada ou não revisada.
- Obsidian ou contexto lidos em bulk sem necessidade e sem gate.
- LLM-as-judge em decisão crítica sem mitigação determinística.
- falha de isolamento entre Lab e Produto.

### Evidência mínima por classe
- `LAB_ONLY_PASS`: testes locais, artefato-resumo e ausência de bloqueadores absolutos.
- `TECHNICAL_PASS_PRODUCT_FAIL`: testes passam, mas faltam UX, rollback, observabilidade, documentação ou evidência comercial.
- `BEDROCK_WARN`: evidência suficiente para manter a entrega no lab, mas insuficiente para promoção.
- `PRODUCT_CANDIDATE`: safety, testes, docs, rollback, observabilidade e isolamento básicos presentes; ainda requer piloto controlado.
- `PRODUCT_READY`: evidência completa, isolamento de falhas, rollback, documentação, ledger, UX mínima, custo conhecido e operação reproduzível.
- `EXCELLENT_PRODUCT_READY`: tudo do nível `PRODUCT_READY`, mais regressão baixa, UX excelente, diferenciação clara e operação exemplar.

### Relação com fases e entregas
- Uma fase pode ter `pass` no artefato local e ainda receber `LAB_ONLY_PASS` ou `TECHNICAL_PASS_PRODUCT_FAIL` no Bedrock.
- Uma capacidade ou macrobloco pode ser tecnicamente viável e ainda assim não estar pronto para produto.
- Uma entrega comercial só pode subir de classe quando a evidência materializada cobre as dimensões críticas do target.
- Mudanças em runtime, frontend, backend, action runtime, voz ou rede exigem prova específica de isolamento e rollback.

### Estrutura futura de artefato Bedrock
Um futuro artefato de veredito Bedrock deve conter, no mínimo:
- `phase`
- `target_type`
- `target_id`
- `technical_status`
- `bedrock_verdict`
- `product_boundary_decision`
- `evidence_bundle`
- `blocking_findings`
- `warning_findings`
- `score_by_dimension`
- `required_remediations`
- `product_promotion_allowed`
- `lab_continuation_allowed`
- `commercial_use_allowed`
- `runtime_change_allowed`
- `rollback_required`
- `human_review_required`
- `next_recommended_phase`

### Posicionamento de produto
Bedrock é o mecanismo que transforma o ARIS de um projeto técnico em um produto confiável, vendável e auditável.
Esse posicionamento é operacional, não promocional: ele depende de evidência, isolamento, rollback e veredito explícito.

## Draft de schema do Evidence Bundle
Este draft define o pacote mínimo de evidências que o Bedrock deve receber antes de emitir qualquer veredito sério.
Ele não executa o gate, não promove produto e não materializa bundles reais.

### Identidade do bundle
Campos obrigatórios:
- `bundle_id`
- `bundle_version`
- `target_type`
- `target_id`
- `target_phase`
- `target_scope`
- `created_at`
- `created_by`
- `source_repositories`
- `source_commits`
- `bedrock_schema_version`
- `intended_bedrock_verdict_scope`

Tipos mínimos de `target_type`:
- `phase`
- `capability`
- `macroblock`
- `runtime_change`
- `frontend_change`
- `backend_change`
- `action_runtime_change`
- `voice_change`
- `network_change`
- `product_release_candidate`
- `commercial_delivery_candidate`

### Seções obrigatórias
Todo bundle deve conter:
- `technical_artifacts`
- `test_evidence`
- `security_evidence`
- `privacy_and_secret_evidence`
- `runtime_boundary_evidence`
- `rollback_and_recovery_evidence`
- `observability_evidence`
- `ux_evidence`
- `documentation_evidence`
- `source_of_truth_evidence`
- `dependency_evidence`
- `performance_and_cost_evidence`
- `risk_register`
- `known_limits`
- `human_review_evidence`
- `bedrock_blocker_scan`

### Technical artifacts
`technical_artifacts` deve apontar para:
- summaries JSON
- reports MD
- decision files
- ledger entries
- docs touched
- source files touched
- tests touched
- scripts/runners touched
- generated artifacts
- commit hashes
- push status
- dirty worktree notes
- unrelated changes preserved

### Test evidence
`test_evidence` must expose at least five independent validation classes for relevant bundles.
Minimum validation classes:
- unit tests
- runner execution
- JSON/schema validation
- diff/static validation
- source-of-truth reread validation

Additional applicable validation classes:
- negative/safety tests
- regression tests
- build/typecheck/lint
- manual smoke checklist

Validation rule:
- A product-relevant bundle must include at least `5` distinct validation classes.
- More validations can be attached, but fewer than `5` makes the bundle insufficient for product-grade judgment.

### Security and privacy evidence
`security_evidence` and `privacy_and_secret_evidence` must prove:
- segredos não expostos
- rede não ativada indevidamente
- dependências não instaladas indevidamente
- ausência de shell/subprocess perigoso quando aplicável
- ausência de bulk-read indevido
- egress controlado
- logs sem dados sensíveis
- permissões explícitas para mutações reais
- provider/model gateway boundaries respeitadas

### Runtime boundary evidence
The bundle must carry boolean claims plus evidence references for:
- `runtime_modified`
- `frontend_modified`
- `backend_modified`
- `action_runtime_modified`
- `voice_modified`
- `network_enabled`
- `dependencies_installed`
- `productive_path_changed`
- `commercial_use_allowed`
- `product_promotion_executed`

These fields are not assertions by themselves; each must point at evidence in the bundle.

### Rollback and recovery evidence
`rollback_and_recovery_evidence` must include:
- rollback plan
- rollback tested
- compensation plan
- previous state preserved
- ledger entry
- restore path
- failure mode recovery
- irreversible operation flag

### Source-of-truth evidence
`source_of_truth_evidence` must point to:
- active-context lido
- summaries usados
- docs usados
- Obsidian usado ou não usado
- stale conflicts detected
- precedence aplicada
- arquivos atualizados
- próxima ação registrada
- ledger atualizado

### Bundle completeness rules
`bundle_completeness` must resolve to one of:
- `complete`
- `incomplete`
- `insufficient`
- `contradictory`
- `stale`
- `invalid`
- `product_promotion_blocked`

Rule:
- `incomplete` may allow Lab continuation.
- `incomplete` never allows product promotion.
- `invalid`, `contradictory`, `stale`, and `insufficient` must block product-grade judgment until repaired.

### Blocker scan
`bedrock_blocker_scan` must be an array of objects with:
- `blocker_id`
- `description`
- `status`
- `evidence`
- `severity`
- `blocks_product_ready`
- `required_remediation`

The scan must inherit the absolute blockers from the verdict criteria draft and surface any failure as evidence-backed status, not opinion.

### Future artifact names
Future bundles should follow:
- `artifacts/bedrock/evidence_bundles/<target_id>_evidence_bundle.json`
- `artifacts/bedrock/evidence_bundles/<target_id>_evidence_bundle_report.md`

This draft does not create that tree yet. It only defines the shape.

## Draft de gate de completude do Evidence Bundle
Este draft define a regra deterministica que decide se um bundle do R12 e suficiente para julgamento Bedrock.
Ele nao executa o Bedrock real, nao promove produto e nao substitui o veredito de R11.

### Classes de completude
- `COMPLETE`: identidade valida, secoes obrigatorias presentes, matriz minima atendida, validacoes independentes suficientes e sem bloqueio absoluto ativo. Permite julgamento Bedrock, mas nao garante `PRODUCT_READY`.
- `INCOMPLETE`: ha partes faltando, mas a entrega ainda pode continuar no lab. Bloqueia promocao produto.
- `INSUFFICIENT`: existe evidenca parcial, porem ela nao sustenta julgamento product-grade. Bloqueia novo veredito ate evidencias adicionais.
- `CONTRADICTORY`: o bundle conflita com source-of-truth, commits, ledger, ou artefatos previos. Bloqueia julgamento ate reconciliacao.
- `STALE`: a evidenca relevante esta desatualizada, substituida ou nao corresponde ao estado atual. Bloqueia julgamento ate refresh.
- `INVALID`: identidade, schema, referencia ou auditabilidade quebradas. Bloqueia julgamento por definicao.
- `PRODUCT_PROMOTION_BLOCKED`: um bloqueador absoluto do R11 esta ativo; promocao produto e proibida ate remediacao explicita.

### Required evidence matrix
The matrix below defines the minimum evidence expectations per target type.

- `phase`, `capability`, `macroblock`:
  - tests: `yes`
  - rollback: `only if the bundle claims a mutation path`
  - human_review: `yes`
  - ux_evidence: `only if user-facing`
  - security/privacy: `yes` when the target crosses trust boundaries
  - dependency_evidence: `only if dependencies are touched or referenced`
  - runtime_boundary_evidence: `only if runtime boundaries are touched`
  - source_of_truth_evidence: `yes`
  - performance_and_cost_evidence: `only if the bundle makes performance or cost claims`
  - lab_only: `yes`
  - product_ready_candidate: `yes`, but only with full product evidence
- `runtime_change`, `frontend_change`, `backend_change`, `action_runtime_change`, `voice_change`, `network_change`:
  - tests: `yes`
  - rollback: `yes`
  - human_review: `yes`
  - ux_evidence: `yes` for frontend and voice, optional otherwise if user-facing
  - security/privacy: `yes`
  - dependency_evidence: `yes` when touched or transitively affected
  - runtime_boundary_evidence: `yes`
  - source_of_truth_evidence: `yes`
  - performance_and_cost_evidence: `yes`
  - lab_only: `yes`
  - product_ready_candidate: `yes`
- `product_release_candidate`, `commercial_delivery_candidate`:
  - tests: `yes`
  - rollback: `yes`
  - human_review: `yes`
  - ux_evidence: `yes`
  - security/privacy: `yes`
  - dependency_evidence: `yes`
  - runtime_boundary_evidence: `yes`
  - source_of_truth_evidence: `yes`
  - performance_and_cost_evidence: `yes`
  - lab_only: `no`
  - product_ready_candidate: `yes`

### Minimum validation rule
- A relevant bundle must contain at least `5` independent validation classes.
- Independent means the classes observe different failure surfaces; duplicate reruns of the same check do not count twice.
- Valid classes can include `json.tool`, `git diff --check`, `git status`, unit test, runner execution, build, lint, smoke, negative test, regression test, or source-of-truth reread, but each bundle must name the classes explicitly.
- For product-relevant bundles, at least one validation class must cover security/privacy or runtime boundary risk.
- For bundles involving real mutation, at least one validation class must cover rollback or compensation.

### Evidence scoring without LLM-as-judge
- Scores are derived from evidence references, not from model opinion.
- The model may summarize or classify, but it cannot be the sole authority for a critical Bedrock decision.
- A critical gate requires deterministic criteria, machine-checkable artifacts, or explicit human review.
- Missing evidence counts against the bundle.
- Contradictory evidence blocks the bundle.

### Completeness decision algorithm draft
1. Validate bundle identity and schema version.
2. Validate target type and target scope are allowed.
3. Validate the required sections from the R12 schema.
4. Validate the required evidence matrix for the target type.
5. Count independent validation classes and confirm the minimum of `5`.
6. Scan for blocker findings from the R11 absolute blocker set.
7. Detect contradictions across source-of-truth, commits, ledger, and artifacts.
8. Detect stale evidence or evidence superseded by newer material.
9. Detect evidence that cannot be audited or reproduced.
10. Determine `completeness_class`.
11. Determine whether `bedrock_verdict_allowed`.
12. Determine whether `product_promotion_allowed`, `lab_continuation_allowed`, and `commercial_use_allowed`.
13. Emit required remediations for missing, stale, contradictory, or blocked evidence.

### Blocker handling
Each R11 absolute blocker must behave as follows:
- `secret exposed`: blocks `PRODUCT_READY`; blocks `commercial_use_allowed`; `LAB_ONLY_PASS` only if the target is fully quarantined and the secret is not on a product path; required remediation is secret removal and rotation.
- `network activated without gate`: blocks `PRODUCT_READY`; blocks `commercial_use_allowed`; `LAB_ONLY_PASS` only if the network path is lab-only and explicitly gated; required remediation is gate insertion or network disablement.
- `runtime product altered without authorization`: blocks `PRODUCT_READY`; blocks `commercial_use_allowed`; `LAB_ONLY_PASS` only if the change is reverted or confined to a non-product path; required remediation is authorization or revert.
- `real action without dry-run, permission, ledger, rollback`: blocks `PRODUCT_READY`; blocks `commercial_use_allowed`; `LAB_ONLY_PASS` only if the action is never promoted and stays isolated; required remediation is dry-run, permission, ledger, and rollback.
- `absence of evidence`: blocks `PRODUCT_READY`; blocks `commercial_use_allowed`; `LAB_ONLY_PASS` only if the bundle is explicitly lab-only and the missing evidence is non-critical; required remediation is evidence materialization.
- `critical tests absent`: blocks `PRODUCT_READY`; blocks `commercial_use_allowed`; `LAB_ONLY_PASS` only if the target is lab-only and tests are not relevant; required remediation is test coverage or explicit rationale.
- `source-of-truth contradictory`: blocks `PRODUCT_READY`; blocks `commercial_use_allowed`; `LAB_ONLY_PASS` only after reconciliation; required remediation is source-of-truth repair.
- `rollback nonexistent for real mutation`: blocks `PRODUCT_READY`; blocks `commercial_use_allowed`; `LAB_ONLY_PASS` only if no real mutation occurred; required remediation is rollback or compensation design.
- `behavior non-reproducible`: blocks `PRODUCT_READY`; blocks `commercial_use_allowed`; `LAB_ONLY_PASS` only if the behavior is explicitly exploratory; required remediation is reproducibility evidence.
- `response truncated or false for critical case`: blocks `PRODUCT_READY`; blocks `commercial_use_allowed`; `LAB_ONLY_PASS` only if the case is non-critical and clearly labeled; required remediation is corrected behavior and verification.
- `dependency external not pinned or reviewed`: blocks `PRODUCT_READY`; blocks `commercial_use_allowed`; `LAB_ONLY_PASS` only if the dependency is not on the promotion path; required remediation is pinning and review.
- `Obsidian/context bulk-read`: blocks `PRODUCT_READY`; blocks `commercial_use_allowed`; `LAB_ONLY_PASS` only if the bundle does not rely on that read and the violation is repaired; required remediation is query-first repair.
- `LLM-as-judge without deterministic mitigation`: blocks `PRODUCT_READY`; blocks `commercial_use_allowed`; `LAB_ONLY_PASS` only if the critical decision is moved to deterministic criteria or human review; required remediation is deterministic mitigation.
- `failure of isolation between Lab and Product`: blocks `PRODUCT_READY`; blocks `commercial_use_allowed`; `LAB_ONLY_PASS` only if the path is proven lab-only and isolation is restored; required remediation is boundary repair.

### Future output schema
Future completeness-gate output should contain at least:
- `phase`
- `target_id`
- `target_type`
- `bundle_id`
- `bundle_version`
- `schema_version`
- `completeness_class`
- `bedrock_verdict_allowed`
- `product_promotion_allowed`
- `lab_continuation_allowed`
- `commercial_use_allowed`
- `minimum_validation_count`
- `validation_classes_detected`
- `missing_required_sections`
- `missing_required_evidence`
- `blocking_findings`
- `warning_findings`
- `stale_findings`
- `contradiction_findings`
- `invalid_schema_findings`
- `required_remediations`
- `next_recommended_phase`

### Relation with R11 and R12
- R11 defines what Bedrock judges.
- R12 defines what evidence must exist.
- R13 defines whether that evidence is complete enough for judgment.
- R13 still does not execute the Bedrock runtime gate.

## Draft de schema do blocker scan
Este draft define como o Bedrock representa, valida e materializa blockers absolutos de forma auditavel.
Ele nao executa scanner runtime real, nao promove produto e nao altera o R10 global boundary.

### Identidade do scan
Campos obrigatorios do future blocker scan:
- `scan_id`
- `scan_version`
- `schema_version`
- `target_id`
- `target_type`
- `target_phase`
- `bundle_id`
- `created_at`
- `created_by`
- `source_commits`
- `scan_scope`
- `scan_mode`
- `bedrock_gate_version`

### Estados por blocker
Cada blocker deve usar exatamente um destes estados:
- `not_applicable`: exige justificativa e escopo claro.
- `not_detected`: exige evidencia verificavel.
- `detected`: bloqueia `PRODUCT_READY` e ativa bloqueio de promocao para target product-grade.
- `suspected`: bloqueia `PRODUCT_READY` ate verificacao.
- `unknown`: bloqueia `PRODUCT_READY` quando a evidencia deveria existir.
- `unverified`: bloqueia `PRODUCT_READY` para target product-grade.
- `remediated_pending_verification`: continua bloqueando produto ate validacao.
- `waived_with_human_approval`: exige review humano, escopo, prazo e justificativa; nunca pode bypassar segredo exposto, rede indevida, acao real sem permissao/ledger/rollback, ou falha de isolamento Lab/Produto.

### Severidades
Cada blocker usa uma severidade desta lista:
- `critical`
- `high`
- `medium`
- `low`
- `informational`

Regras de severidade:
- Todos os 14 blockers absolutos do R11 sao `critical` ou `high`.
- `critical detected` gera `PRODUCT_PROMOTION_BLOCKED`.
- `high detected` bloqueia `PRODUCT_READY` e `commercial_use_allowed`.
- Severidade nao pode ser reduzida por opiniao do modelo.
- Reducao de severidade exige evidencia materializada ou human review explicita.

### Canonical blocker catalog
Os 14 IDs canonicos e estaveis sao:
- `secret_exposed`: title=`Secret exposed`; description=`Secret, token, credential or private key exposed in artifact, log, prompt or output.`; default_severity=`critical`; blocks_product_ready=`True`; blocks_commercial_use=`True`; may_allow_lab_continuation=`False` when exposure reaches a product path; required_evidence=`secret scan, redaction proof, scope check`; required_remediation=`remove exposure, rotate secret, scrub artifacts`; verification_method=`secret scan plus manual artifact review`; waiver_allowed=`False`; waiver_constraints=`non-waivable`.
- `network_enabled_without_gate`: title=`Network enabled without gate`; description=`Network path activated without explicit gate, scope or approval.`; default_severity=`critical`; blocks_product_ready=`True`; blocks_commercial_use=`True`; may_allow_lab_continuation=`False` when network reaches product path; required_evidence=`gate proof, egress control, scope isolation`; required_remediation=`insert gate or disable network`; verification_method=`runtime/config review plus validation`; waiver_allowed=`False`; waiver_constraints=`non-waivable for product paths`.
- `productive_runtime_modified_without_authorization`: title=`Productive runtime modified without authorization`; description=`Runtime prod path changed without explicit permission and ledgered approval.`; default_severity=`critical`; blocks_product_ready=`True`; blocks_commercial_use=`True`; may_allow_lab_continuation=`False` when the change touches product path; required_evidence=`authorization record, diff, scope proof`; required_remediation=`authorize or revert`; verification_method=`diff plus decision ledger review`; waiver_allowed=`False`; waiver_constraints=`non-waivable for product runtime`.
- `real_action_without_dry_run_permission_ledger_rollback`: title=`Real action without dry-run, permission, ledger, rollback`; description=`Real mutation attempted or claimed without dry-run, permission, ledger and rollback/compensation.`; default_severity=`critical`; blocks_product_ready=`True`; blocks_commercial_use=`True`; may_allow_lab_continuation=`False` when the action is real or promoted; required_evidence=`dry-run record, permission, ledger entry, rollback plan`; required_remediation=`add dry-run, permission, ledger and rollback`; verification_method=`execution ledger review plus rollback proof`; waiver_allowed=`False`; waiver_constraints=`non-waivable for real action`.
- `materialized_evidence_missing`: title=`Materialized evidence missing`; description=`Required evidence exists only as assertion or is absent.`; default_severity=`high`; blocks_product_ready=`True`; blocks_commercial_use=`True`; may_allow_lab_continuation=`True` only when lab-only and non-critical; required_evidence=`materialized artifacts, traceable refs`; required_remediation=`materialize evidence bundle`; verification_method=`artifact presence review`; waiver_allowed=`True`; waiver_constraints=`requires human review, scope and TTL`.
- `critical_tests_missing`: title=`Critical tests missing`; description=`Critical validation classes are absent for the claimed target.`; default_severity=`high`; blocks_product_ready=`True`; blocks_commercial_use=`True`; may_allow_lab_continuation=`True` only for lab-only exploratory work; required_evidence=`test plan, test results, coverage map`; required_remediation=`add critical tests or narrow claim`; verification_method=`test inventory review`; waiver_allowed=`True`; waiver_constraints=`requires human review and explicit lab-only scope`.
- `source_of_truth_contradictory`: title=`Source of truth contradictory`; description=`Artifacts, ledger or current state conflict with source-of-truth.`; default_severity=`high`; blocks_product_ready=`True`; blocks_commercial_use=`True`; may_allow_lab_continuation=`False` until reconciliation; required_evidence=`conflict trace, precedence decision, reconciled state`; required_remediation=`reconcile source-of-truth`; verification_method=`cross-file reconciliation review`; waiver_allowed=`True`; waiver_constraints=`requires explicit reconciliation plan`.
- `rollback_missing_for_real_mutation`: title=`Rollback missing for real mutation`; description=`A real mutation path lacks a viable rollback or compensation path.`; default_severity=`high`; blocks_product_ready=`True`; blocks_commercial_use=`True`; may_allow_lab_continuation=`True` only if no real mutation occurred; required_evidence=`rollback plan, restore path, compensation plan`; required_remediation=`design or prove rollback`; verification_method=`rollback evidence review`; waiver_allowed=`True`; waiver_constraints=`must not cover real mutation`.
- `non_reproducible_behavior`: title=`Non reproducible behavior`; description=`The behavior cannot be reproduced under the stated inputs, state and scope.`; default_severity=`high`; blocks_product_ready=`True`; blocks_commercial_use=`True`; may_allow_lab_continuation=`True` only for exploratory lab cases; required_evidence=`repro steps, rerun proof, environment notes`; required_remediation=`add reproducibility evidence`; verification_method=`rerun validation plus artifact comparison`; waiver_allowed=`True`; waiver_constraints=`requires explicit lab-only scope`.
- `critical_response_truncated_or_false`: title=`Critical response truncated or false`; description=`Critical case received a truncated or false response or summary.`; default_severity=`high`; blocks_product_ready=`True`; blocks_commercial_use=`True`; may_allow_lab_continuation=`True` only if the case is not product-critical and is clearly labeled; required_evidence=`full response trace, comparison, failure example`; required_remediation=`correct response path and verify`; verification_method=`case review plus comparison`; waiver_allowed=`True`; waiver_constraints=`requires non-critical scope and human review`.
- `external_dependency_unpinned_or_unreviewed`: title=`External dependency unpinned or unreviewed`; description=`Dependency is not pinned or not reviewed for the promotion path.`; default_severity=`high`; blocks_product_ready=`True`; blocks_commercial_use=`True`; may_allow_lab_continuation=`True` only when dependency is not on the promotion path; required_evidence=`pin, review record, dependency inventory`; required_remediation=`pin and review dependency`; verification_method=`dependency audit`; waiver_allowed=`True`; waiver_constraints=`requires explicit risk acceptance`.
- `obsidian_or_context_bulk_read_violation`: title=`Obsidian or context bulk read violation`; description=`Bulk-read of Obsidian or context occurred outside query-first rules.`; default_severity=`high`; blocks_product_ready=`True`; blocks_commercial_use=`True`; may_allow_lab_continuation=`True` only if the violation is repaired and isolated from product path; required_evidence=`query log, scope, read trace`; required_remediation=`repair query-first discipline`; verification_method=`read-path audit`; waiver_allowed=`True`; waiver_constraints=`requires source-of-truth repair and no product-path reuse`.
- `llm_as_judge_for_critical_gate_without_deterministic_mitigation`: title=`LLM as judge without deterministic mitigation`; description=`Critical decision relied on model opinion without deterministic guardrails or human review.`; default_severity=`high`; blocks_product_ready=`True`; blocks_commercial_use=`True`; may_allow_lab_continuation=`True` only if the critical decision is moved to deterministic criteria or explicit human review; required_evidence=`deterministic criteria, human review trace`; required_remediation=`add deterministic mitigation`; verification_method=`decision trace review`; waiver_allowed=`True`; waiver_constraints=`cannot waive away deterministic mitigation requirement`.
- `lab_product_isolation_failure`: title=`Lab product isolation failure`; description=`Isolation between lab and product paths failed or is not provable.`; default_severity=`critical`; blocks_product_ready=`True`; blocks_commercial_use=`True`; may_allow_lab_continuation=`False` when the failure touches product boundary; required_evidence=`isolation proof, boundary trace, path separation`; required_remediation=`repair isolation boundary`; verification_method=`boundary audit`; waiver_allowed=`False`; waiver_constraints=`non-waivable for product promotion`.

### Blocker entry fields
Every blocker scan item must include:
- `status`
- `severity`
- `evidence_refs`
- `evidence_quality`
- `source_paths_checked`
- `commands_or_validations_used`
- `findings`
- `remediation_required`
- `remediation_owner`
- `verification_required`
- `blocks_product_ready`
- `blocks_commercial_use`
- `lab_continuation_allowed`
- `human_review_required`
- `waiver_status`
- `waiver_reason`
- `waiver_approved_by`
- `last_verified_at`

### Evidence quality
Evidence quality must be one of:
- `materialized`
- `partial`
- `declarative_only`
- `missing`
- `contradictory`
- `stale`
- `not_auditable`

Rules:
- `materialized` is preferred for product.
- `declarative_only` is not enough for `PRODUCT_READY`.
- `missing`, `contradictory`, `stale`, and `not_auditable` block product when tied to an absolute blocker.
- `partial` may allow Lab, but not product, unless the target is explicitly lab-only and safe.

### Waiver policy
- Waiver is an exception, not the default path.
- Waiver requires explicit human review, scope, TTL and justification.
- Waiver cannot release commercial use if the blocker involves secret exposure, real mutation without ledger/rollback, network indevida, or Lab/Product isolation failure.
- Waiver does not turn missing evidence into valid evidence.
- Waiver must appear in the Evidence Bundle and in the future Bedrock Verdict Artifact.

### Integration with completeness gate
- Any `detected`, `suspected`, `unknown` or `unverified` blocker on a target product-grade path must affect `completeness_class`.
- A critical active blocker yields `PRODUCT_PROMOTION_BLOCKED`.
- A high active blocker blocks `PRODUCT_READY` and `commercial_use_allowed`.
- A blocker scan that is incomplete, contradictory, stale or invalid can move the bundle to `INSUFFICIENT`, `CONTRADICTORY`, `STALE` or `INVALID`.
- A clean blocker scan only removes one class of block; it never guarantees `PRODUCT_READY`.

### Future output schema
Future blocker scan output should contain at least:
- `phase`
- `target_id`
- `target_type`
- `bundle_id`
- `scan_id`
- `scan_status`
- `scan_completeness`
- `blocker_count`
- `detected_blockers`
- `suspected_blockers`
- `unknown_blockers`
- `waived_blockers`
- `critical_blockers`
- `high_blockers`
- `product_promotion_blocked`
- `commercial_use_allowed`
- `lab_continuation_allowed`
- `required_remediations`
- `human_review_required`
- `next_recommended_phase`

### Relation with R11, R12 and R13
- R11 defines the absolute blockers.
- R12 requires `bedrock_blocker_scan` as a mandatory Evidence Bundle section.
- R13 determines whether blocker findings collapse completeness into `PRODUCT_PROMOTION_BLOCKED`, `INSUFFICIENT`, `INVALID`, `CONTRADICTORY` or `STALE`.
- R14 defines the internal blocker scan schema used by future Bedrock evidence.
- R14 still does not execute a scanner runtime.

## Draft de schema do Bedrock Verdict Artifact
Este draft define o artefato final canonical que um futuro Bedrock verdict deve produzir.
Ele conecta R10, R11, R12, R13 e R14 em uma saida auditavel, reproduzivel e separada de qualquer pass tecnico local.

### Identidade do veredito
Campos obrigatorios:
- `verdict_id`
- `verdict_schema_version`
- `bedrock_gate_version`
- `phase`
- `target_id`
- `target_type`
- `target_phase`
- `target_scope`
- `evaluated_at`
- `evaluated_by`
- `source_repositories`
- `source_commits`
- `evidence_bundle_id`
- `blocker_scan_id`
- `completeness_gate_id`
- `verdict_artifact_paths`

### Status tecnico separado do status produto
O artifact deve manter:
- `technical_status`
- `technical_decision`
- `technical_pass`
- `bedrock_verdict`
- `product_boundary_decision`
- `product_promotion_allowed`
- `commercial_use_allowed`
- `lab_continuation_allowed`
- `runtime_change_allowed`
- `frontend_change_allowed`
- `backend_change_allowed`
- `action_runtime_change_allowed`
- `voice_change_allowed`
- `network_change_allowed`

Regra:
- `technical_pass=true` nunca implica automaticamente `product_promotion_allowed=true`.

### Verdict classes herdadas do R11
As classes de veredito sao:
- `INVALID`
- `BLOCKED`
- `LAB_ONLY_PASS`
- `TECHNICAL_PASS_PRODUCT_FAIL`
- `BEDROCK_WARN`
- `PRODUCT_CANDIDATE`
- `PRODUCT_READY`
- `EXCELLENT_PRODUCT_READY`

Cada classe deve aparecer em `bedrock_verdict` e deve ser acompanhada pelo minimo de campos seguintes:
- `INVALID`: `technical_status`, `final_bedrock_decision`, `known_limits`, `residual_risks`, `blocked_next_scope`
- `BLOCKED`: `technical_status`, `blocking_findings`, `required_remediations`, `product_boundary_decision`, `blocked_next_scope`
- `LAB_ONLY_PASS`: `technical_status`, `lab_continuation_allowed`, `product_promotion_allowed`, `allowed_next_scope`
- `TECHNICAL_PASS_PRODUCT_FAIL`: `technical_status`, `technical_pass`, `product_boundary_decision`, `required_remediations`
- `BEDROCK_WARN`: `technical_status`, `warning_findings`, `required_remediations`, `re_evaluation_required`
- `PRODUCT_CANDIDATE`: `technical_status`, `product_boundary_decision`, `promotion_class`, `human_review_required`, `required_remediations`
- `PRODUCT_READY`: `technical_status`, `product_promotion_allowed`, `commercial_use_allowed`, `blocker_scan_status`, `evidence_completeness_class`
- `EXCELLENT_PRODUCT_READY`: `technical_status`, `product_promotion_allowed`, `commercial_use_allowed`, `score_by_dimension`, `dimension_confidence`, `dimension_risk_level`

### Relation with completeness gate
Campos obrigatorios:
- `evidence_completeness_class`
- `evidence_bundle_complete`
- `missing_required_sections`
- `missing_required_evidence`
- `validation_classes_detected`
- `minimum_validation_count`
- `minimum_validation_rule_passed`
- `completeness_findings`
- `completeness_required_remediations`

Rules:
- If `evidence_completeness_class` is not `COMPLETE`, the artifact cannot allow product promotion.
- `INCOMPLETE` may allow Lab continuation.
- `INSUFFICIENT`, `INVALID`, `CONTRADICTORY`, `STALE` and `PRODUCT_PROMOTION_BLOCKED` block product-grade judgment.

### Relation with blocker scan
Campos obrigatorios:
- `blocker_scan_status`
- `blocker_scan_completeness`
- `canonical_blocker_count`
- `detected_blockers`
- `suspected_blockers`
- `unknown_blockers`
- `unverified_blockers`
- `waived_blockers`
- `critical_blockers`
- `high_blockers`
- `blocking_findings`
- `blocker_required_remediations`

Rules:
- Any critical blocker active blocks `PRODUCT_READY`.
- Waiver cannot release commercial use where R14 forbids it.
- A clean scan removes one class of block but does not guarantee `PRODUCT_READY`.

### Score and dimension summary
The artifact must expose:
- `score_by_dimension`
- `dimension_findings`
- `dimension_evidence_refs`
- `dimension_confidence`
- `dimension_risk_level`

Dimensions inherited from R11:
- segurança
- privacidade/segredos
- determinismo
- evidência/auditabilidade
- testes/reprodutibilidade
- rollback/recuperação
- observabilidade
- failure isolation
- qualidade de resposta/comportamento
- UX
- performance/custo
- manutenibilidade
- documentação/source-of-truth
- roadmap/macroblocos
- prontidão comercial/produto
- risco de regressão
- risco de automação indevida
- dependências externas
- boundaries de runtime/frontend/backend/action runtime/voz/rede

Rule:
- Score must be derived from materialized evidence, validations or explicit human review.
- LLM may summarize, but cannot be the sole judge in a critical gate.

### Final decision
Campos obrigatorios:
- `final_bedrock_decision`
- `final_product_boundary_decision`
- `promotion_class`
- `allowed_next_scope`
- `blocked_next_scope`
- `required_remediations`
- `recommended_next_phase`
- `human_review_required`
- `re_evaluation_required`
- `expires_at_or_stale_after`
- `known_limits`
- `residual_risks`

Suggested decision values:
- `invalid_artifact`
- `blocked_before_verdict`
- `lab_continuation_allowed`
- `technical_pass_product_blocked`
- `product_candidate_with_conditions`
- `product_ready_allowed`
- `excellent_product_ready_allowed`

### Auditability and traceability
The artifact must record:
- `input_artifacts`
- `input_reports`
- `input_summaries`
- `input_commits`
- `commands_executed`
- `validations_executed`
- `files_changed`
- `protected_sources_not_modified`
- `dirty_worktree_notes`
- `context_usage_report`
- `source_of_truth_precedence_applied`
- `stale_context_conflicts_detected`
- `obsidian_usage`
- `human_approvals`
- `ledger_entries`

### Future artifact names
Future verdict artifacts should follow:
- `artifacts/bedrock/verdicts/<target_id>_bedrock_verdict.json`
- `artifacts/bedrock/verdicts/<target_id>_bedrock_verdict_report.md`

This draft does not create that tree yet. It only defines the shape.

### Relation with R10 through R14
- R10 defines the global role of Bedrock.
- R11 defines verdict classes and blockers.
- R12 defines the Evidence Bundle.
- R13 defines bundle completeness.
- R14 defines blocker scan structure.
- R15 defines the final verdict artifact.
- R15 still does not execute a real judgment.

## Relação com NORTH_POLE
O Bedrock Gate é o chão. O North Pole é o norte.

O Bedrock Gate impede dano, mentira, bypass e ativação indevida. O North Pole exige excelência, simplicidade, eficiência, valor e vitória técnica/produto.

Uma fase só pode passar se preservar o chão e aproximar o ARIS do norte.

## Status operacional
Este contrato não autoriza implementação, runtime mutation, rede, MCP, vault write, dependency install, product promotion ou cliente real.

A próxima ação operacional continua sendo definida exclusivamente por `NEXT_ACTION.md`.
