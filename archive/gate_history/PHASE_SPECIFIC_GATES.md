## No-Warn Advancement Policy

- policy_name: `NO_WARN_ADVANCEMENT_POLICY`
- PASS is the only outcome that can release the next gate.
- WARN is diagnostic only and requires repair or rework before any advancement.
- WARN cannot close a phase and cannot release a functional next gate.
- WARN may only route to repair, review, or cleanup gates that resolve the warning debt.
- BLOCKED means security, scope, authorization, evidence, or source-of-truth failure.
- INVALID means the phase does not prove what it claims to prove.
- REWORK is an intermediate category that remains non-advancing until resolved.
# PHASE_SPECIFIC_GATES — Gates Técnicos da Fase

## Função
`PHASE_SPECIFIC_GATES.md` define a terceira camada obrigatória de aprovação de uma fase do ARIS.

Depois de passar por `BEDROCK_GATE.md` e `NORTH_POLE.md`, cada fase ainda precisa provar que cumpriu exatamente seus critérios técnicos locais, sem sair do escopo aprovado.

## Ordem no approval stack
Toda fase futura deve passar por:

1. `BEDROCK_GATE.md` — chão inviolável.
2. `NORTH_POLE.md` — excelência total, duas vitórias e mínimo mecanismo necessário.
3. `PHASE_SPECIFIC_GATES.md` — prova técnica local da fase.
4. `ACTIVE_CONTEXT_UPDATE` — materialização correta do estado.
5. `COMMIT_PUSH_HASH_FINAL` — commit/push/hash final.

## Perguntas obrigatórias da fase
Cada fase deve responder, no mínimo:

- Qual é o objetivo técnico específico desta fase?
- Qual escopo está autorizado?
- Qual escopo está explicitamente proibido?
- Quais arquivos podem ser alterados?
- Quais arquivos não podem ser alterados?
- Quais capabilities devem permanecer bloqueadas?
- Quais artifacts, summaries, ledgers ou reports devem ser criados/atualizados?
- Quais testes, runners, validações estáticas ou greps defensivos provam a fase?
- Qual evidência objetiva demonstra sucesso?
- Qual evidência objetiva demonstraria falha?
- Qual rollback/compensação existe se aplicável?
- Como a fase atualiza `CURRENT_STATE.md`, `NEXT_ACTION.md`, `DECISION_LOCKS.md`, `CONTEXT_INDEX.md` e `ARIS_PHASE_LEDGER.md`?
- Qual é o commit hash final?

## Classificação obrigatória da fase
Cada fase deve ser classificada como uma ou mais categorias:

- `BUILD` — constrói uma peça real.
- `GATE` — bloqueia risco real.
- `SIMULATE` — testa ataque, falha, cenário ou comportamento.
- `REPAIR` — corrige drift, dívida, ponteiro, ruído ou inconsistência.
- `PROVE` — gera evidência objetiva.
- `COMPRESS` — reduz complexidade sem perder segurança.

Se uma fase não se encaixar em nenhuma categoria, ela deve ser revisada, fundida, adiada, rejeitada ou bloqueada.

## Critérios mínimos de aprovação
Uma fase só pode passar se:

- `BEDROCK_GATE` não tiver falha;
- `NORTH_POLE_ALIGNMENT` for `PASS` only; `WARN` is diagnostic-only and requires repair/rework before advancement;
- todos os critérios locais da fase forem satisfeitos;
- o escopo autorizado for respeitado;
- os locks forem preservados;
- a evidência for materializada;
- o active-context for atualizado quando requerido;
- o resultado final for rastreável por commit hash.

## Resultados possíveis
- `PASS`: todos os gates críticos passaram e a fase entregou evidência suficiente para liberar o próximo gate.
- `WARN`: diagnóstico בלבד; requer repair/review/cleanup antes de qualquer avanço.
- `REWORK`: a fase é válida, mas precisa ser refeita, compactada ou ajustada antes de poder passar.
- `BLOCKED`: a fase viola Bedrock, locks, autorização, escopo ou segurança.
- `INVALID`: a fase não prova o que afirma provar.

## Regra contra falso progresso
Uma fase não pode passar apenas porque criou documentos ou confirmou locks. Ela precisa demonstrar pelo menos uma das seguintes melhorias:

- mais confiança;
- mais capacidade;
- mais valor;
- menos risco;
- menos complexidade;
- melhor evidência;
- melhor previsibilidade;
- melhor preparação para produto futuro sem violar locks.

## Status operacional
Este contrato não autoriza runtime mutation, rede, MCP, vault write, dependency install, product promotion, customer-real use ou production release.

Ele apenas define como gates específicos de fase devem ser avaliados daqui em diante.
