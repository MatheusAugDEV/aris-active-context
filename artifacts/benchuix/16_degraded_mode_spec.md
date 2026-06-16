## definição de modo degradado

Modo degradado e o estado em que parte da experiencia continua disponivel, mas com limitacoes explicitadas e defaults seguros ativados.

## princípios de degradação segura

- mostrar apenas o que continua confiavel
- bloquear o que depender de contexto ausente
- explicar a limitacao antes da acao
- preservar caminho de saida ou proximo passo

## o que ainda pode ser mostrado

Podem continuar visiveis resumo do estado atual, historico confiavel, comprovantes candidatos relacionados, limite atual e opcoes seguras como revisar historico, tentar novamente ou pedir revisao.

## o que deve ser bloqueado

Devem ser bloqueadas acoes que dependam de dado incompleto, simulacao inconsistente, recuperacao ambigua ou confirmacao que pareca segura sem base suficiente.

## como sinalizar limitação

A limitacao deve aparecer com titulo curto, motivo em linguagem humana, impacto esperado e proximo passo recomendado.

## política contra spinner infinito

Espera prolongada precisa virar estado explicito de falha ou degradado com mensagem e opcao segura. O cliente nao pode ficar preso em carregamento indefinido.

## política contra white screen

Mesmo em erro severo, a tela precisa manter estrutura minima com mensagem legivel, contexto do que foi afetado e proximo passo.

## política contra stack trace para cliente

Detalhe tecnico bruto pode existir em camada interna, mas o cliente deve receber apenas resumo humano do problema e orientacao.

## política de próximo passo

Todo estado degradado precisa sugerir uma acao clara: tentar novamente, simular novamente, revisar comprovante, aguardar atualizacao ou pedir revisao.

## relação com defaults seguros

Defaults seguros reduzem a superficie do que pode ser feito no modo degradado, evitando CTA enganoso, confirmacao arriscada ou leitura falsa de sucesso.

## exemplo sintético de modo degradado

Situacao: a simulacao de impacto nao concluiu.

O que continua visivel: nome da automacao, ultimo estado confiavel, comprovante candidato anterior e limite atual.

O que fica bloqueado: aprovacao baseada nessa simulacao e qualquer decisao que dependa do valor ausente.

Proximo passo: simular novamente ou revisar historico relacionado.

## limitações explícitas

Modo degradado nesta fase e apenas candidato e synthetic-only. Nenhuma acao real, runtime real, integracao real ou mutacao real ocorre a partir deste estado.
