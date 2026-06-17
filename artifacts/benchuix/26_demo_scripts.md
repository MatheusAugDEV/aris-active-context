# BENCHUIX-26 Demo Scripts

Candidate-only demo packet. Sandbox only. Synthetic data only. No live route, no runtime, no Project_ARIS mutation.

## Demo 1 - Barbearia

Objetivo de negocio em 1 frase:
- Mostrar que o ARIS impede atendimento fora de horario, pede aprovacao minima para uma excecao VIP e deixa recibo visivel em menos de 2 minutos.

Estado inicial sintetico:
- Agenda sintetica com tres barbeiros, fila regular estabilizada e um cliente VIP marcado como `VIP-LIGHT`.
- Politica sintetica: atendimento apos 20:00 exige excecao aprovada por operador.

Evento que dispara a automacao:
- Pedido sintetico de encaixe para `VIP-LIGHT` as 20:30.

O que ARIS entende:
- O pedido viola horario regular.
- O cliente possui tag VIP sintetica.
- A excecao ainda depende de aprovacao humana explicita.

O que ARIS vai fazer:
- Bloquear a execucao automatica do encaixe.
- Montar uma proposta de excecao com risco, horario, barbeiro sugerido e impacto na fila.
- Exibir comprovante sintetico apos a decisao.

O que ARIS nao vai fazer:
- Nao confirmar atendimento real.
- Nao enviar mensagem real ao cliente.
- Nao alterar agenda real ou cobrar qualquer valor.

Risco apresentado ao usuario:
- Aprovacao fora da politica pode atrasar dois atendimentos sinteticos seguintes.

Decisao necessaria ou bloqueio automatico:
- Operador aprova uma unica excecao VIP ou mantem o bloqueio automatico.

Comprovante visivel:
- Recibo sintetico `RCPT-BARB-001` com politica usada, risco e decisao.

Rollback/compensacao visivel:
- Botao sintetico `Reverter excecao` gera compensacao documental e restaura o bloqueio padrao.

Frase final de valor:
- "Voce viu o limite, aprovou so o necessario e saiu com recibo claro sem tocar agenda real."

Tempo estimado por cena:
| cena | segundos | resultado esperado |
| --- | ---: | --- |
| contexto da agenda sintetica | 18 | usuario entende o estado inicial |
| pedido fora de horario chega | 24 | risco e bloqueio aparecem |
| excecao VIP e aprovada | 38 | decisao humana fica explicita |
| recibo e rollback aparecem | 28 | evidencia e reversao ficam visiveis |

Criterio de falha da demo:
- Falha se a narrativa depender de explicacao tecnica longa, se a excecao parecer automatica sem humano ou se nao houver recibo e rollback visiveis.

## Demo 2 - Mercado

Objetivo de negocio em 1 frase:
- Mostrar que o ARIS recusa um reembolso suspeito, explica o limite e entrega evidencia verificavel sem tocar transacao real.

Estado inicial sintetico:
- Pedido sintetico `PED-MKT-204` com pagamento ja conciliado em ambiente ficticio.
- Politica sintetica: reembolso acima do limite diario com item de risco alto exige recusa automatica e revisao manual posterior.

Evento que dispara a automacao:
- Solicitar reembolso integral de um item classificado como `alto_risco_sintetico`.

O que ARIS entende:
- O valor pedido excede o limite sintetico permitido para reembolso instantaneo.
- O pedido combina dois sinais sinteticos de risco.
- A decisao correta e preservar caixa e pedir revisao humana offline.

O que ARIS vai fazer:
- Recusar o reembolso automatico.
- Mostrar quais sinais sinteticos acionaram a regra.
- Emitir recibo sintetico com a trilha da decisao.

O que ARIS nao vai fazer:
- Nao devolver dinheiro real.
- Nao acionar PSP real.
- Nao alterar estoque, caixa ou ERP real.

Risco apresentado ao usuario:
- Liberar o reembolso sem revisao aumentaria perda financeira sintetica e abriria precedente fora da politica.

Decisao necessaria ou bloqueio automatico:
- Bloqueio automatico do reembolso instantaneo; operador apenas agenda revisao sintetica.

Comprovante visivel:
- Recibo sintetico `RCPT-MKT-002` com motivo da recusa, politica usada e codigo de verificacao.

Rollback/compensacao visivel:
- Acao sintetica `Gerar revisao manual` cria compensacao documental sem desfazer estado real inexistente.

Frase final de valor:
- "O risco foi contido na hora e a justificativa ficou pronta para auditoria sem mover um centavo real."

Tempo estimado por cena:
| cena | segundos | resultado esperado |
| --- | ---: | --- |
| contexto do pedido sintetico | 20 | usuario entende origem do pedido |
| pedido de reembolso entra | 25 | sinais de risco ficam claros |
| recusa automatica explicada | 35 | limite e evidencia aparecem |
| recibo e revisao manual | 30 | comprovante e compensacao ficam claros |

Criterio de falha da demo:
- Falha se parecer que houve pagamento real, se a recusa nao mostrar motivo claro ou se a compensacao ficar invisivel.

## Demo 3 - Escritorio

Objetivo de negocio em 1 frase:
- Mostrar que o ARIS intercepta um anexo com linguagem de bypass de politica, pede revisao humana e preserva evidencia sem ensinar ataque.

Estado inicial sintetico:
- Caixa documental sintetica com contrato, nota e um anexo marcado como `ANX-SAFE-07`.
- Politica sintetica: qualquer anexo com linguagem de excecao de politica vai para quarentena documental.

Evento que dispara a automacao:
- Entrada do anexo sintetico com a flag `ATTACHMENT_TEXT_SYNTHETIC_POLICY_EXCEPTION_REQUEST_REQUIRES_HUMAN_REVIEW`.

O que ARIS entende:
- O texto sintetico pede excecao de politica.
- O conteudo exige quarentena e revisao humana.
- Nao existe base para executar acao automatica.

O que ARIS vai fazer:
- Interceptar o anexo no sandbox.
- Marcar a tentativa como risco documental.
- Exibir recibo sintetico com a trilha da interceptacao e a proxima acao segura.

O que ARIS nao vai fazer:
- Nao processar anexo real.
- Nao disparar integracao real.
- Nao explicar tecnicamente como um ataque funcionaria.

Risco apresentado ao usuario:
- Aceitar linguagem de bypass sem revisao criaria decisao sem contexto e sem trilha confiavel.

Decisao necessaria ou bloqueio automatico:
- Quarentena automatica; operador apenas confirma encaminhamento para revisao humana.

Comprovante visivel:
- Recibo sintetico `RCPT-OFC-003` com quarentena, risco e proxima etapa.

Rollback/compensacao visivel:
- Acao sintetica `Liberar anexo apos revisao` reverte a quarentena somente como historia documental controlada.

Frase final de valor:
- "O limite apareceu antes do erro, a evidencia ficou pronta e a liberacao continuou humana."

Tempo estimado por cena:
| cena | segundos | resultado esperado |
| --- | ---: | --- |
| contexto da caixa documental | 18 | usuario entende o material recebido |
| anexo sintetico e sinalizado | 22 | risco e quarentena aparecem |
| revisao humana e explicada | 38 | limite e proxima acao ficam claros |
| recibo e liberacao controlada | 28 | evidencia e rollback aparecem |

Criterio de falha da demo:
- Falha se o texto sintetico parecer instrucao operacional, se a interceptacao ficar obscura ou se o usuario sair sem entender o limite.
