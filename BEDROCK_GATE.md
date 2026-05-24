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

## Relação com NORTH_POLE
O Bedrock Gate é o chão. O North Pole é o norte.

O Bedrock Gate impede dano, mentira, bypass e ativação indevida. O North Pole exige excelência, simplicidade, eficiência, valor e vitória técnica/produto.

Uma fase só pode passar se preservar o chão e aproximar o ARIS do norte.

## Status operacional
Este contrato não autoriza implementação, runtime mutation, rede, MCP, vault write, dependency install, product promotion ou cliente real.

A próxima ação operacional continua sendo definida exclusivamente por `NEXT_ACTION.md`.
