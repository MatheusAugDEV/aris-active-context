# BENCHUIX-26 Demo Sandbox Spec

Pacote documental candidate-only. Esta especificacao nao implementa runtime, nao abre live route e nao toca Project_ARIS.

## superficies simuladas

- Tela sintetica "Hoje" com tres cards de risco controlado.
- Inbox sintetico de aprovacoes e bloqueios.
- Comprovante sintetico de decisao com codigo verificavel.
- Painel sintetico de rollback/compensacao documental.

## estados sinteticos

- Barbearia com agenda, barbeiros e regra de horario em estado congelado.
- Mercado com pedido, limite de reembolso e dois sinais sinteticos de risco.
- Escritorio com caixa documental e anexo sintetico em quarentena.

## eventos sinteticos

- Pedido de encaixe VIP fora do horario.
- Solicitacao de reembolso integral suspeito.
- Entrada de anexo com linguagem sintetica de excecao de politica.

## comprovantes sinteticos

- Cada demo produz recibo sintetico com politica aplicada, decisao, evidencia resumida e codigo de verificacao.
- Cada demo mostra tambem a opcao de rollback ou compensacao como historia visivel, nunca como execucao real.

## limites explicitos

- Todos os dados sao sinteticos e imutaveis.
- Nenhuma cena dura mais do que o previsto na matriz de timing.
- O operador so interage com decisoes sinteticas de aprovacao, recusa ou quarentena.

## proibicoes

- Proibido dado real, segredo, integracao real, PSP real, OAuth real, runtime real, real_apply ou qualquer mutacao em Project_ARIS.
- Proibido transformar a demo em aula de arquitetura, infraestrutura ou seguranca ofensiva.

## o que nao e executado

- Nenhuma automacao real e executada.
- Nenhuma chamada de rede externa e disparada.
- Nenhum anexo real e aberto.
- Nenhuma agenda, pagamento, documento ou atendimento real e alterado.

## como impedir confusao com produto real

- Cada superficie deve exibir o selo "Sandbox candidate-only".
- Cada dominio deve exibir a frase "Dados sinteticos. Nenhum estado real foi tocado."
- Toda decisao exibida deve ser acompanhada de "Historia demonstrativa, nao execucao real."

## como sinalizar sandbox / dados sinteticos

- O selo visual deve aparecer no cabecalho e no comprovante.
- O valor deve ser mostrado pela clareza da decisao, nao por promessa de disponibilidade imediata.
- O texto de apoio deve dizer "Veja como a decisao seria apresentada" em vez de "Isso ja esta rodando".

## fail-closed

- Se qualquer marcador de dado real, segredo ou integracao real for detectado, a demo e invalidada e o pacote deve parar em bloqueio documental.
- Se uma cena sugerir execucao real, cobranca real ou mudanca em sistema real, o roteiro deve ser rejeitado.
- Se o texto do anexo sintetico virar instrucao operacional, o material deve ser removido e refeito em modo seguro.
