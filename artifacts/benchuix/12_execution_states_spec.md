## definição da fase

BENCHUIX-12 materializa os Estados de Execucao como uma fase candidata, legivel e synthetic-only da trilha BenchUIX. O foco aqui e tornar o estado do fluxo sempre visivel, compreensivel e auditavel.

## tese dos estados visíveis

Quando o cliente entende em que estado o fluxo esta, fica mais dificil esconder risco, falso sucesso ou falha.

## objetivo

Definir uma maquina de estados candidata com microcopy clara, idade visivel dos dados e sinais criticos compreensiveis, sem mutacao de estado real e sem execucao real.

"o cliente sabe exatamente em que estado a automação está?"

## relação com BENCHUIX-11

BENCHUIX-11 organizou a decisao em uma Approval Inbox clara. BENCHUIX-12 define como cada fluxo aparece antes, durante e depois dessa decisao, sem transformar simulacao em sucesso e sem esconder bloqueios ou falhas.

## máquina de estados em linguagem humana

O fluxo pode nascer em rascunho, ficar pronto para revisar, virar simulado, aguardar aprovacao, ser aprovado como candidato, ser negado, voltar para edicao, ser pausado, ficar bloqueado, falhar, entrar em degradado ou encerrar como concluido sintetico.

## transições permitidas

As transicoes permitidas precisam ser explicitas, com motivo claro e estado de chegada visivel. Pausa, bloqueio, falha e degradacao podem acontecer sem esconder o que estava ocorrendo antes.

## transições proibidas

E proibido transformar simulado em concluido, degradado em sucesso, falhou em concluido ou qualquer estado em algo invisivel. Tambem e proibido aprovar quando o fluxo estiver bloqueado.

## idade visível dos dados

Todo estado ativo precisa mostrar quando foi atualizado. Se a idade da informacao nao estiver visivel, o fluxo deve perder confianca e bloquear progresso sensivel.

## estados críticos

Bloqueado, falhou e degradado sao estados criticos. Eles precisam aparecer com texto, icone, motivo e proximo passo seguro; cor pode ajudar, mas nao pode carregar o sentido sozinha.

## prevenção de falso sucesso

Aprovado candidato nao significa concluido, simulado nao significa executado e degradado nao significa tudo certo. O sistema precisa impedir qualquer copy que mascare essas diferencas.

## prevenção de estado invisível

Nenhuma transicao pode sumir com o estado atual, com a idade dos dados ou com o motivo do bloqueio. Se o sistema nao souber explicar o estado, ele deve bloquear.

## acessibilidade

Cada estado precisa ter rotulo claro, anuncio assistivo, sinais visuais e textuais combinados e leitura compreensivel sem depender apenas de cor.

## critérios de BLOCK

Bloquear quando houver:

- estado sem nome visivel
- idade dos dados ausente
- falso sucesso
- falha escondida
- estado degradado tratado como conclusao
- estado critico dependente apenas de cor
- qualquer acao, mutacao ou servico real no escopo

## anti-escopo

Esta fase nao cria UI executavel, nao cria automacao real, nao chama servico real, nao toca dado real, nao muta estado real e nao autoriza produto, piloto, producao, Bedrock PASS, runtime, secrets ou real_apply.

## handoff para BENCHUIX-13

BENCHUIX-13 deve usar esta maquina de estados para definir a Tela Automações com status sempre visivel, sem falso sucesso e sem esconder falhas ou estados degradados.
