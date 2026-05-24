# BEDROCK_GATE — Chão Inviolável do ARIS

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

## Relação com NORTH_POLE
O Bedrock Gate é o chão. O North Pole é o norte.

O Bedrock Gate impede dano, mentira, bypass e ativação indevida. O North Pole exige excelência, simplicidade, eficiência, valor e vitória técnica/produto.

Uma fase só pode passar se preservar o chão e aproximar o ARIS do norte.

## Status operacional
Este contrato não autoriza implementação, runtime mutation, rede, MCP, vault write, dependency install, product promotion ou cliente real.

A próxima ação operacional continua sendo definida exclusivamente por `NEXT_ACTION.md`.
