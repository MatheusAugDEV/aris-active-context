# BENCHUIX-27A Visual Copy Contract

## role

This copy contract defines the first visual language layer for ARIS Visual Sandbox. It is candidate-only and synthetic-only. It does not validate product copy in production.

## persistent badge

Every screen must show:

`Sandbox candidate-only. Dados sinteticos. Nenhum estado real foi tocado.`

The badge must be visible without opening a modal, tooltip or receipt detail.

## base copy pattern for sensitive actions

Every sensitive action must use this order:

1. What happened.
2. What ARIS will do.
3. What ARIS will not do.
4. What risk exists.
5. Whether approval is needed.
6. Which evidence will be generated.
7. Whether it can be undone or compensated.
8. Whether real state was touched.

## plain-language labels

- `WillDoList`: "ARIS vai"
- `WillNotDoList`: "ARIS nao vai"
- `RiskBadge`: "Risco"
- `ApprovalRequirement`: "Precisa aprovacao"
- `EvidencePreview`: "Comprovante"
- `RollbackStatus`: "Pode desfazer?"
- `StateTouchedIndicator`: "Estado real tocado?"
- `SandboxBadge`: "Sandbox"

## required state copy

- `DETECTADO`: "ARIS encontrou um evento sintetico."
- `PROPOSTO`: "ARIS preparou uma proposta, mas ainda nao agiu."
- `BLOQUEADO_AUTO`: "A regra bloqueou a acao automaticamente."
- `AGUARDANDO_APROVACAO`: "A decisao depende de aprovacao humana."
- `APROVADO`: "A excecao sintetica foi aprovada."
- `RECUSADO`: "A acao sintetica foi recusada."
- `COMPROVANTE_GERADO`: "Comprovante sintetico gerado."
- `ROLLBACK_DISPONIVEL`: "Ha uma saida documental visivel."
- `DESFEITO`: "A historia sintetica foi marcada como desfeita."
- `MODO_DEGRADADO`: "Modo degradado: nenhuma acao parecida com execucao esta disponivel."

## scenario copy

### Barbearia

Primary line: "Pedido VIP fora do horario precisa de excecao."

Will do:
- "Bloquear o encaixe automatico."
- "Mostrar impacto na fila."
- "Pedir aprovacao para uma unica excecao."
- "Gerar comprovante sintetico."

Will not do:
- "Nao confirmar atendimento real."
- "Nao avisar cliente real."
- "Nao alterar agenda real."
- "Nao cobrar valor real."

Risk: "Pode atrasar dois atendimentos sinteticos seguintes."

Rollback: "A excecao pode ser revertida na historia do sandbox."

### Mercado

Primary line: "Reembolso suspeito excede o limite sintetico."

Will do:
- "Recusar o reembolso instantaneo."
- "Mostrar os sinais sinteticos de risco."
- "Abrir revisao manual documental."
- "Gerar comprovante sintetico."

Will not do:
- "Nao devolver dinheiro real."
- "Nao acionar PSP real."
- "Nao alterar estoque real."
- "Nao alterar caixa ou ERP real."

Risk: "Liberar sem revisao aumentaria perda sintetica."

Rollback: "A compensacao vira revisao manual, nao movimentacao real."

### Escritorio

Primary line: "Anexo sintetico precisa de revisao humana."

Will do:
- "Colocar o anexo em quarentena visual."
- "Mostrar a regra de revisao humana."
- "Preservar evidencia sintetica."
- "Gerar comprovante sintetico."

Will not do:
- "Nao abrir anexo real."
- "Nao disparar integracao externa."
- "Nao executar automacao real."
- "Nao explicar tecnica ofensiva."

Risk: "Liberar sem revisao criaria decisao sem contexto."

Rollback: "Liberacao so aparece como historia apos revisao humana."

## degraded mode copy

Primary line: "Nao e seguro mostrar essa acao agora."

Required support:
- "O sandbox entrou em modo degradado."
- "Apenas comprovantes e proximos passos seguros ficam visiveis."
- "Nenhum estado real foi tocado."

Forbidden CTAs:
- "Executar agora"
- "Tentar em producao"
- "Sincronizar real"
- "Cobrar"
- "Conectar conta"

Allowed CTAs:
- "Ver comprovante"
- "Voltar para Hoje"
- "Manter bloqueado"
- "Enviar para revisao"

## forbidden language

The visual sandbox must not say:

- "ja esta rodando"
- "sua conta foi conectada"
- "agenda sincronizada"
- "pagamento realizado"
- "dinheiro devolvido"
- "anexo processado"
- "producao"
- "cliente real"
- "produto pronto"
- "deploy publico"

## safe replacements

- Use "seria apresentado" instead of "foi executado".
- Use "sintetico" whenever naming data, receipts, decisions or events.
- Use "historia documental" for rollback or compensation.
- Use "nenhum estado real foi tocado" on every screen.
