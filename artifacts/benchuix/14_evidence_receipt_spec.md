## definição do comprovante

O comprovante e o resumo legivel de um evento importante da automacao, criado para explicar o que aconteceu de forma clara, rastreavel e sem exigir leitura tecnica.

## campos do comprovante em linguagem humana

Cada comprovante deve conter:

- titulo do evento
- resumo do que aconteceu
- automacao relacionada
- estado associado
- quando aconteceu
- quem ou qual fluxo originou o evento
- codigo de verificacao
- impacto, risco ou custo resumidos quando aplicavel
- o que ARIS vai fazer
- o que ARIS nao vai fazer
- referencia para rollback ou compensacao futura, quando existir
- limitacoes explicitas do comprovante

## código de verificação

O codigo de verificacao deve ser curto, legivel e copiavel, pensado para consulta humana. Ele serve para localizar e conferir o comprovante no ambiente candidato, sem ser vendido como prova real ou assinatura oficial.

## o que foi simulado/decidido

O comprovante precisa deixar claro se o evento representa simulacao, aprovacao, recusa, pausa, edicao candidata, degradacao ou falha. Simulacao nao pode parecer execucao real.

## quem/qual fluxo originou o evento

Cada comprovante deve dizer se o evento veio de uma automacao candidata, de uma revisao humana, de uma fila de aprovacao ou de uma referencia futura de rollback ou compensacao.

## quando aconteceu

O comprovante deve mostrar data e horario legiveis, com referencia de idade do evento quando isso ajudar a interpretar o historico.

## estado associado

O estado associado precisa ser descrito com linguagem clara, usando termos como simulado, aguardando aprovacao, pausado, bloqueado, falhou, degradado ou concluido sintetico.

## impacto/risco/custo resumidos quando aplicável

Quando houver impacto, risco ou custo estimado, o comprovante deve resumir isso em linguagem curta e compreensivel, sem calculos tecnicos como superficie principal.

## will/will-not associado

Todo comprovante de evento sensivel deve explicitar:

- o que ARIS vai fazer
- o que ARIS nao vai fazer

## vínculo com rollback/compensação futura

Se o evento puder exigir desfazer ou compensar em uma fase futura, o comprovante deve apontar esse vinculo como referencia de continuidade, sem executar rollback real.

## limitações explícitas

O comprovante deve dizer explicitamente que pertence a um ambiente candidato e synthetic-only, que nao representa operacao produtiva e que nao substitui evidencia de execucao real.

## exemplo sintético de comprovante

Titulo: Pausa candidata registrada

Resumo: A automacao "Lembrete de cobranca leve" foi pausada para revisao do horario de envio.

Automacao relacionada: Lembrete de cobranca leve

Estado associado: pausado

Quando aconteceu: 15 jun 2026, 23:40

Origem: revisao humana na tela de automacoes

Codigo de verificacao: BX14-PAUSA-2047

Impacto resumido: novos envios ficam suspensos no ambiente candidato ate nova revisao

ARIS vai fazer: manter a automacao pausada no ambiente candidato

ARIS nao vai fazer: executar envios reais ou alterar clientes reais

Referencia futura: consultar fluxo de rollback ou compensacao se a pausa tiver sido indevida

Limitacao: este comprovante descreve apenas uma mudanca candidata e synthetic-only

## política de não edição/deleção

Depois de emitido, um comprovante antigo nao pode ser editado nem deletado. Correcao futura precisa acontecer por novo evento historico, preservando o registro anterior.
