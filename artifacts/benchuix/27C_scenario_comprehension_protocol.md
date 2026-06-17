# BENCHUIX-27C Scenario Comprehension Protocol

## objective

Evaluate whether the static Visual Sandbox communicates value, control, risk, evidence and rollback boundaries before any future browser-based review.

Este protocolo não executa sessão real.

## synthetic persona

- Persona: dono solo que decide rapido, nao quer jargao tecnico e precisa saber claramente o que ARIS vai fazer, o que nao vai fazer e qual risco fica exposto.
- Environment: artifact-only review using the static source pack and the 27A/27B contracts.
- Constraint: no browser, no localhost, no runtime, no real user, no real state.

## future execution instructions

1. Use the 27B source pack or a future local-only preview phase as the visual reference.
2. Review one scenario at a time, following Today -> Approve -> History/Receipts -> Rollback/Undo -> Degraded.
3. Record answers using the 27C expected observation schema.
4. Mark a failure immediately if the no-real-state boundary becomes ambiguous.
5. Stop the review if any screen suggests CRISOL, product-ready execution or live integration.

## standard scenario questions

1. O que ARIS vai fazer?
2. O que ARIS nao vai fazer?
3. Qual e o risco?
4. Voce precisa aprovar?
5. Que evidencia aparece?
6. Da para desfazer ou compensar?
7. Algum estado real foi tocado?

## scenario: barbearia_after_hours_vip_exception

### expected responses

- ARIS vai bloquear o encaixe automatico, mostrar impacto de fila, pedir gate do dono e gerar comprovante sintetico.
- ARIS nao vai confirmar atendimento real, mandar mensagem real, alterar agenda real ou cobrar valor real.
- O risco e atrasar atendimentos sinteticos seguintes.
- Sim, a excecao VIP depende de aprovacao explicita do dono.
- A evidencia inclui SandboxBadge, stateTouched false, comprovante demonstrativo, codigo de verificacao e itens da politica/slot/decisao.
- Da para reverter apenas a historia documental do sandbox.
- Nenhum estado real foi tocado.

### failure criteria

- Missing will-not-do language.
- Approval looks like direct booking execution.
- Receipt or rollback omits documentary-only scope.
- StateTouched false is absent or contradicted.

### severity

- S1_BLOCKER if real booking or real-state mutation can be inferred.
- S2_MAJOR if approval or evidence boundary is unclear.
- S3_MINOR if copy hierarchy slows understanding.
- S4_POLISH if wording can be tightened without changing meaning.

### observations

- Compare Today against Approve to verify the same contract remains visible.
- Confirm Degraded keeps the flow fail-closed.

## scenario: mercado_suspected_refund_declined

### expected responses

- ARIS vai recusar o reembolso instantaneo, mostrar sinais de risco, abrir revisao manual documental e gerar comprovante sintetico.
- ARIS nao vai devolver dinheiro real, chamar PSP real, alterar estoque real ou alterar caixa/ERP real.
- O risco e perda financeira sintetica e precedente fora da politica.
- Nao para o bloqueio inicial; gate aparece apenas na trilha de override/manual review.
- A evidencia inclui recibo demonstrativo, policy block, faixa de risco, stateTouched false e badge de sandbox.
- A compensacao possivel e criar revisao manual documental sem dinheiro real.
- Nenhum estado real foi tocado.

### failure criteria

- Manual review sounds like live refund override.
- Refusal evidence is weak or absent.
- Degraded mode leaves an execution-like refund path visible.

### severity

- S1_BLOCKER if money movement or integration can be inferred.
- S2_MAJOR if risk or decision boundary is ambiguous.
- S3_MINOR if manual-review language is harder than needed.
- S4_POLISH if density or labels can be refined.

### observations

- Pay special attention to the difference between "keep blocked" and "manual review story".
- Receipt language must stay clearly documentary.

## scenario: escritorio_attachment_intercepted

### expected responses

- ARIS vai interceptar o anexo sintetico, colocar em quarentena visual, mostrar motivo seguro e gerar comprovante sintetico.
- ARIS nao vai abrir anexo real, disparar servico externo, executar automacao real ou ensinar tecnica ofensiva.
- O risco e aceitar decisao sem contexto e sem trilha confiavel.
- Sim, qualquer liberacao depende de revisao humana documental.
- A evidencia inclui badge de sandbox, stateTouched false, comprovante demonstrativo, motivo de quarentena e referencia de politica.
- A reversao e apenas uma historia controlada apos revisao humana documental.
- Nenhum estado real foi tocado.

### failure criteria

- UI implies a live security workflow or real document release.
- The scenario exposes unsafe detail instead of a safe reason.
- Rollback suggests release without review limits.

### severity

- S1_BLOCKER if a real attachment or integration appears implied.
- S2_MAJOR if the human-review requirement is unclear.
- S3_MINOR if copy obscures owner understanding.
- S4_POLISH if evidence labels can be more scan-friendly.

### observations

- Verify that quarantine remains fail-closed under Degraded.
- Verify that receipt detail reinforces demo-only scope.

## scope limits

- No browser execution.
- No localhost.
- No package manager.
- No runtime or backend.
- No real users.
- No field data.
- No Project_ARIS mutation outside the active-context subrepo.
- No CRISOL admission.
- No product-ready claim.
