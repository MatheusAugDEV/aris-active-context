## definição da fase

BENCHUIX-16 materializa Falhas & Modo Degradado como fase candidata, synthetic-only e segura da trilha BenchUIX. O objetivo e tornar a falha visivel, compreensivel e acionavel, sem opacidade ou abandono.

## tese de falhas e modo degradado

Quando o cliente entende o que falhou, qual limite apareceu e qual e o proximo passo seguro, a falha deixa de parecer caos e passa a ser uma decisao assistida.

## objetivo

Definir uma biblioteca de falhas com comportamento degradado, defaults seguros e proximo passo claro para que o cliente nunca encontre tela branca, espera infinita ou erro sem orientacao.

"o cliente entende o que falhou e o que pode fazer agora?"

## relação com BENCHUIX-12 e BENCHUIX-15

BENCHUIX-12 definiu os estados visiveis, inclusive degradado e falhou. BENCHUIX-15 definiu como classificar recuperacao. BENCHUIX-16 conecta esses contratos a mensagens de falha, bloqueio e proximo passo seguro.

## categorias de falha

As categorias minimas desta fase sao:

- dado ausente
- dado stale
- dado incompleto
- simulacao nao concluida
- aprovacao pendente indisponivel
- falha parcial
- limite de contexto ou confianca
- recuperacao exige revisao

## sintomas visíveis

Cada falha deve mostrar o sintoma em linguagem humana: o que deixou de aparecer, o que ficou indisponivel e o que continua disponivel.

## causa provável em linguagem humana

A causa provavel precisa evitar jargao tecnico e explicar se o problema veio de informacao insuficiente, limite temporario, resposta incompleta ou necessidade de revisao.

## risco para o cliente

Toda falha precisa dizer o risco atual: atraso, decisao bloqueada, dados possivelmente desatualizados, leitura parcial ou necessidade de confirmar antes de agir.

## default seguro

O default seguro deve impedir acao confusa, esconder CTAs inseguros e preservar apenas o que continua confiavel no estado atual.

## próximo passo recomendado

Toda falha precisa trazer um proximo passo: tentar novamente, simular novamente, revisar historico, aguardar contexto, pedir revisao ou seguir em modo degradado.

## quando bloquear

Bloquear quando a falha impedir entendimento minimo do que aconteceu, quando houver risco residual alto sem contexto suficiente ou quando a acao seguinte nao puder ser explicada com seguranca.

## quando permitir retry

Permitir retry quando a falha parecer temporaria, delimitada e sem risco de multiplicar impacto ou mascarar estado inconsistente.

## quando orientar simular novamente

Orientar simular novamente quando preview, estimativa ou avaliacao candidata nao puderem concluir de forma confiavel, mas houver base para nova tentativa sem abrir superficie real.

## microcopy candidata

Exemplos esperados:

- "Nao foi possivel concluir esta simulacao agora."
- "Parte das informacoes esta indisponivel; mostramos apenas o que continua confiavel."
- "Este passo precisa de revisao antes de continuar."
- "Voce pode tentar novamente ou revisar o historico relacionado."

## acessibilidade

Falhas e modo degradado precisam manter titulos claros, ordem de leitura previsivel, texto de causa e proximo passo separados, e sinais textuais que nao dependam apenas de cor.

## critérios de BLOCK

Bloquear quando houver:

- white screen
- spinner infinito
- stack trace para cliente
- falha sem proximo passo
- falha escondida
- sucesso mostrado em estado degradado ou de falha
- qualquer acao, dado ou servico real no escopo

## anti-escopo

Esta fase nao executa runtime, nao executa acao real, nao usa dado real, nao autoriza produto, piloto, producao, Bedrock PASS, runtime, secrets ou real_apply.

## handoff para BENCHUIX-17

BENCHUIX-17 deve usar esta biblioteca de falhas e degradacao para modelar mobile companion e cache seguro, preservando defaults seguros e orientacao de proximo passo.
