## definição da fase

BENCHUIX-15 materializa Rollback / Desfazer / Compensar como fase candidata, synthetic-only e segura da trilha BenchUIX. O objetivo e explicar o que pode ser revertido, compensado ou apenas registrado sem prometer efeito real.

## tese de rollback/desfazer/compensar

Quando o cliente entende a diferenca entre reverter, compensar e apenas registrar, ele toma decisoes com menos falsa seguranca e mais clareza sobre impacto, limite e risco residual.

## objetivo

Definir uma linguagem de recuperacao que classifique cada caso como reversivel, compensavel, irreversivel, nao aplicavel ou exige revisao, com razao de impacto, evidencias candidatas e limites explicitos.

"o cliente entende o que pode ser desfeito, compensado ou apenas registrado?"

## relação com BENCHUIX-14

BENCHUIX-14 definiu historico, comprovantes e link referencial para rollback. BENCHUIX-15 usa esse historico para enquadrar o tipo de recuperacao permitido e a prova candidata associada.

## labels reversível/compensável/irreversível/não aplicável/exige revisão

Os labels desta fase sao:

- reversivel
- compensavel
- irreversivel
- nao aplicavel
- exige revisao

## diferença entre desfazer, compensar e registrar

Desfazer tenta retornar ao estado anterior dentro do ambiente candidato quando isso e seguro e explicitamente classificado como reversivel. Compensar cria uma resposta de equilibrio quando nao existe volta direta. Registrar apenas documenta o ocorrido quando nao cabe desfazer nem compensar.

## razão de impacto

Antes de qualquer decisao, a tela deve explicar qual impacto esta em jogo: operacao interrompida, risco residual, atraso, custo estimado, ou necessidade de revisao humana. A razao de impacto vem antes do CTA.

## evidência de rollback/compensação

A evidencia desta fase e sempre candidata e synthetic-only. Ela deve apontar comprovante relacionado, label de recuperacao, razao de impacto, limite aplicado e resultado esperado no ambiente candidato.

## limites

Rollback ou compensacao candidata precisam declarar escopo, janela de aplicacao, condicoes de bloqueio e dependencia de revisao quando houver risco de repeticao ou efeito incerto.

## timeouts

Cada proposta de recuperacao precisa explicar quando deixa de fazer sentido tentar desfazer e quando deve virar apenas compensacao, revisao ou registro.

## microcopy candidata

Exemplos de copy esperada:

- "Pode ser desfeito neste ambiente candidato."
- "Nao volta ao estado anterior, mas pode ser compensado."
- "Este efeito nao pode ser desfeito; o proximo passo e registrar e revisar."
- "Precisa de revisao antes de qualquer tentativa de recuperacao."

## acessibilidade

Labels, limites, risco residual e motivo da decisao precisam aparecer com texto claro, ordem de leitura previsivel e sinais textuais que nao dependam apenas de cor.

## critérios de BLOCK

Bloquear quando houver:

- efeito irreversivel vendido como desfeito
- compensacao chamada de reversao
- rollback duplicado sem checagem
- rollback sem limite
- razao de impacto ausente
- evidencia tratada como prova real
- qualquer acao, estado, dado ou servico real no escopo

## anti-escopo

Esta fase nao executa rollback real, nao executa compensacao real, nao executa runtime, nao cria acao real, nao usa dado real, nao autoriza produto, piloto, producao, Bedrock PASS, runtime, secrets ou real_apply.

## handoff para BENCHUIX-16

BENCHUIX-16 deve usar essa classificacao para tratar falhas e modo degradado, preservando limites de recuperacao, risco residual visivel e bloqueio de falsa promessa de desfazer.
