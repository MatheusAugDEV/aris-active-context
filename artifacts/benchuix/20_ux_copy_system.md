## tese da linguagem

A linguagem do ARIS nao existe para enfeitar a operacao. Ela existe para dizer a verdade com calma, mostrar limite sem tecnicismo e orientar a proxima acao segura quando algo sai do esperado.

## principios de escrita

- diga o que esta acontecendo agora;
- diga o que a pessoa pode fazer agora;
- diga o que nao vai acontecer sem permissao ou revisao;
- prefira verbo claro a categoria tecnica;
- troque detalhe interno por efeito operacional;
- mantenha a mensagem curta antes do detalhe expandido.

## tom permitido

Direto, humano, concreto, calmo e responsavel. A mensagem pode ser firme sem soar burocratica. O foco e orientar decisao, nao impressionar.

## tom proibido

Promessa vazia, misterio, jargao desnecessario, eufemismo para risco, culpa ao usuario e frases vagas como "algo deu errado" ou "processando".

<!-- ALLOW_JARGON_START -->
Exemplos tecnicos ruins permitidos para contraste interno:
- "validator falhou e bloqueou o pipeline"
- "runtime indisponivel por exception sem trace"
- "schema fora do padrao e json rejeitado"
<!-- ALLOW_JARGON_END -->

## como explicar risco

Risco deve dizer impacto e cuidado pedido. Em vez de nome tecnico, diga se a acao pede revisao, se pode gerar custo extra, se depende de aprovacao ou se pode exigir compensacao depois.

## como explicar limite

Limite deve mostrar o boundary sem soar como parede muda. O usuario precisa saber se o limite e de acesso, de custo, de momento, de confianca do dado ou de irreversibilidade da acao.

## como explicar permissao

Permissao deve ser descrita como escopo atual: "voce pode seguir", "voce pode revisar", "voce nao pode concluir esta etapa com o acesso atual". Nao esconda a diferenca entre ver, revisar, aprovar e desfazer.

## como explicar falha

Falha deve dizer o que parou, o que ficou preservado e qual caminho continua seguro. Se houve impacto parcial, isso precisa aparecer logo na primeira leitura.

## como explicar desfazer e compensar

Quando der para voltar atras, diga isso de forma clara. Quando nao der, diga que a acao nao sera desfeita automaticamente e aponte a compensacao segura disponivel.

## como explicar comprovante

Comprovante deve ser apresentado como prova do que aconteceu, com horario, escopo e proxima consulta. O usuario nao precisa aprender termo interno para confiar no recibo.

## como explicar custo estimado

Custo estimado deve ser tratado como previsao com margem, nunca como valor final. A mensagem deve dizer se continua dentro do teto, se pede revisao ou se a estimativa ainda esta incompleta.

## como explicar dado atrasado

Dado atrasado deve ser chamado de "dado atrasado" ou "snapshot anterior". A mensagem precisa mostrar idade do dado e se a decisao ainda e segura com essa referencia.

## exemplos bons e ruins

Bom: "Esta aprovacao ainda depende de revisao humana antes de seguir."

Bom: "Mostramos o ultimo snapshot seguro de 4 minutos atras."

Bom: "Voce pode revisar este comprovante agora, mas nao pode alterar esta etapa."

<!-- ALLOW_JARGON_START -->
Ruim para cliente:
- "O gate do active-context bloqueou este artifact"
- "RBAC insuficiente para concluir o rollback"
- "CI verde, mas o validator ainda acusa exception"
<!-- ALLOW_JARGON_END -->

## regras de nao ocultar risco

- risco alto nao pode aparecer como nota secundaria;
- bloqueio nao pode virar frase vaga;
- dado parcial nao pode ser vendido como visao completa;
- acao irreversivel precisa dizer que nao volta sozinha;
- custo estimado acima do teto precisa aparecer antes do detalhe fino.

## criterios PASS/WARN/BLOCK/INVALID

PASS: a pessoa entende risco, permissao, falha, comprovante, custo e dado atrasado sem depender de termo tecnico.

WARN: alguma mensagem ainda precisa refinamento de nuance para BENCHUIX-21, mas a verdade operacional ja esta preservada.

BLOCK: a linguagem mascara risco, apaga limite, exige termo tecnico para entendimento ou usa mensagem vaga em situacao critica.

INVALID: qualquer claim de produto pronto, Bedrock pronto, seguranca final, live route aberta, integracao real, mutacao de Project_ARIS ou copy que esconda um risco real.

<!-- ALLOW_JARGON_START -->
## anti-escopo

Termos proibidos como linguagem primaria nesta fase: runtime, gate, schema, artifact, ledger, tenant, idempotency, active-context, hash, validator, ci, stack trace, exception, json, pipeline, trace, token, policy engine e rbac.
<!-- ALLOW_JARGON_END -->
