# v20r Onboarding Source Contract

## Fonte rastreavel

- Origem local: `operator_inputs/benchuix/ARIS_Onboarding.html`
- SHA-256 esperado e confirmado: `3943704aec7e919ad93ecc9888afc09037ea523666aa2637f81069119318253f`

## Contrato visual extraido

O source local mostra uma entrada extremamente contida:

- fundo quase totalmente escuro, sem painel evidente;
- wordmark `ARIS` em serif, muito grande e centralizado;
- tres pontos azuis pequenos abaixo do wordmark;
- quase nenhum texto auxiliar;
- sensacao de pausa curta antes do dashboard.

## Reparos de alinhamento aplicados no v20r

O `v20` estava funcional, mas ainda distante da composicao da fonte porque mantinha icone orbital, cards explicativos e densidade textual acima do necessario.

O `v20r` corrige isso com o menor delta possivel:

- mantem a chave `aris_benchuix_onboarding_seen_v1`;
- mantem `Começar`, `pular` e `Ver boas-vindas novamente`;
- elimina o container perceptivel, o icone orbital e os cards;
- centraliza o wordmark `ARIS`;
- introduz os tres pontos azuis;
- reduz a copia de apoio para uma unica linha curta.

## Limites intencionais

- Nenhum comportamento de backend foi introduzido.
- Nenhuma rede, integracao externa ou execucao real foi autorizada.
- O replay do onboarding continua local ao navegador e dependente de `localStorage`.
