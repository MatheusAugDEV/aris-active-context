# BENCHUIX-25 Task Scenario Script

Cada cenario abaixo e curto, acionavel e propositalmente sem dica de navegacao.

## task: understand_today

- Perfil alvo: `barbearia_owner_solo`, `loja_owner_operator`, `mobile_4g_user`
- Facilitator readout: "Voce acabou de abrir o ARIS no inicio do turno. Descubra o que precisa da sua atencao agora e o que pode esperar."
- Observed completion cue: participante aponta a prioridade, diferencia o que depende dele e resume o estado sem ajuda tecnica.

## task: create_automation

- Perfil alvo: `barbearia_owner_solo`, `loja_owner_operator`, `mercado_small_team`
- Facilitator readout: "Existe uma rotina repetitiva que voce quer deixar preparada para acontecer com seguranca. Monte a proposta e pare quando sentir que ela esta pronta para revisao."
- Observed completion cue: participante chega a uma proposta segura e descreve limite e condicao de uso.

## task: run_simulation

- Perfil alvo: `automation_anxious_user`, `mercado_small_team`, `agencia_operator`
- Facilitator readout: "Antes de decidir, veja o que aconteceria se essa rotina fosse aceita agora."
- Observed completion cue: participante consegue explicar o impacto esperado sem tratar a simulacao como execucao real.

## task: approve_action

- Perfil alvo: `barbearia_owner_solo`, `automation_anxious_user`, `mobile_4g_user`
- Facilitator readout: "Uma acao sensivel esta esperando sua decisao. Decida se aprovaria agora e diga por que."
- Observed completion cue: participante justifica a decisao usando risco, limite e will/will-not.

## task: find_receipt

- Perfil alvo: `escritorio_admin`, `agencia_operator`, `mobile_4g_user`
- Facilitator readout: "Alguem pediu prova do que aconteceu mais cedo. Encontre essa prova e me diga o que ela mostra."
- Observed completion cue: participante encontra o comprovante e resume o fato central com horario/acao/limite.

## task: understand_failure

- Perfil alvo: `mercado_small_team`, `escritorio_admin`, `mobile_4g_user`
- Facilitator readout: "Algo deu errado. Entenda o problema e o que voce faria em seguida."
- Observed completion cue: participante identifica a falha, descreve o motivo em linguagem humana e aponta o proximo passo.

## task: pause_automation

- Perfil alvo: `loja_owner_operator`, `mercado_small_team`, `mobile_4g_user`
- Facilitator readout: "Uma rotina precisa parar por enquanto. Interrompa sem perder o controle do que ficou suspenso."
- Observed completion cue: participante pausa, entende o novo estado e nao confunde pausa com exclusao.

## task: understand_aris_will_not

- Perfil alvo: `automation_anxious_user`, `barbearia_owner_solo`, `agencia_operator`
- Facilitator readout: "Antes de confiar, descubra o que o ARIS vai fazer e o que ele nao vai fazer neste caso."
- Observed completion cue: participante cita pelo menos um will e um will-not corretos sem adicionar promessa nao declarada.

## task: check_rollback_boundary

- Perfil alvo: `escritorio_admin`, `automation_anxious_user`, `loja_owner_operator`
- Facilitator readout: "Antes de seguir, descubra se isso pode ser desfeito depois e em que limite."
- Observed completion cue: participante distingue reversivel, compensavel ou irreversivel e explica por que.

## task: explain_aris

- Perfil alvo: `barbearia_owner_solo`, `escritorio_admin`, `agencia_operator`
- Facilitator readout: "Explique para outra pessoa, em duas ou tres frases, o que o ARIS faz para voce aqui."
- Observed completion cue: participante menciona valor, limite e gate humano quando aplicavel, sem jargao tecnico.

## bad examples rejected

- "Clique em Aprovar e leia o card de risco." Rejeitado porque entrega o caminho.
- "Voce entendeu a diferenca entre preview e execucao?" Rejeitado porque usa self-report como prova principal.
- "Agora encontre a aba Historico." Rejeitado porque nomeia a interface e reduz a tarefa a navegacao.
- "Se ficar dificil, eu posso te mostrar o caminho." Rejeitado porque contamina a medicao de ajuda.
