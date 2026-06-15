# BENCHUIX-01 Owner-Solo Mode Spec

## Definicao do Dono-Solo

O Dono-Solo e o usuario-base da camada BenchUIX.

Perfil minimo:

- pequeno negocio;
- uma pessoa cuida de atendimento, agenda, cobranca, estoque, vendas, problemas e mensagens;
- mobile-first;
- sem TI;
- pouco tempo;
- baixa tolerancia a configuracao;
- precisa entender o ARIS em minutos;
- precisa confiar antes de aprovar;
- quer resultado, controle e comprovante, nao arquitetura.

## Tese da Fase

"O Modo A governa a experiencia. B/C/D adicionam complexidade por progressive disclosure; nao reescrevem o produto."

## Navegacao Base do Modo A

- Hoje
- Automacoes
- Aprovar
- Historico / Comprovantes
- Configuracoes

## O Que o Dono-Solo Precisa Conseguir Fazer

- entender a tela Hoje;
- iniciar primeira automacao segura;
- simular antes de executar;
- aprovar uma acao sensivel;
- entender "vai fazer / nao vai fazer";
- encontrar comprovante;
- pausar automacao;
- entender falha;
- saber se pode desfazer;
- explicar o ARIS em uma frase.

## Linguagem Permitida

- confirmar;
- simular;
- pausar;
- desfazer;
- comprovante;
- historico;
- limite;
- risco;
- atencao;
- nada foi alterado;
- precisa da sua confirmacao.

## Linguagem Proibida em UI Primaria

- runtime;
- gate;
- schema;
- validator;
- artifact;
- ledger;
- tenant;
- idempotency;
- hash;
- oracle;
- CI;
- real_apply;
- active-context.

## Metricas Candidatas

- primeira automacao segura em ate 3-5 minutos;
- tela Hoje compreendida em ate 5 segundos;
- confianca para aprovar;
- compreensao de comprovante;
- compreensao de rollback;
- reducao de ansiedade;
- capacidade de explicar ARIS para outra pessoa.

## Criterios de Block

- fluxo essencial exige jargao tecnico;
- Modo A depende de configuracao avancada;
- tela inicial vira dashboard corporativo;
- Dono-Solo precisa entender arquitetura;
- acao sensivel nao mostra "vai fazer / nao vai fazer";
- primeira automacao segura exige dado real ou runtime real.

## Invariante de Produto

- Modo A e o baseline da experiencia.
- B/C/D so adicionam complexidade por disclosure progressivo.
- Nenhum modo desta fase autoriza produto real, runtime real, secrets ou real_apply.
