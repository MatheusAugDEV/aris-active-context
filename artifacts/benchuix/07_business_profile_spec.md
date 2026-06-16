# BENCHUIX-07 Business Profile Spec

## definição da fase

BENCHUIX-07 define o perfil mínimo do negócio como contrato sintético, incremental e verificável para orientar automação segura e útil sem virar cadastro longo.

## Exceção Bedrock-governed

Esta fase é uma exceção explícita de preparação para Bedrock/Product Reality Lab. Ela não produz Bedrock PASS, não declara produto pronto e não autoriza produto, piloto, runtime, integração real, secrets, billing, OAuth real, produção ou real_apply.

## tese do perfil mínimo

O perfil do negócio só deve pedir o que muda decisão, risco ou recomendação. Tudo que não muda o primeiro valor fica para depois.

## objetivo

- capturar o contexto mínimo necessário para orientar automação segura e útil;
- manter o fluxo curto para dono-solo;
- evitar cadastro extenso;
- preservar o primeiro valor sintético iniciado em BENCHUIX-06;
- preparar handoff para BENCHUIX-08.

## pergunta principal

"quais dados mínimos permitem automação segura e útil?"

## relação com BENCHUIX-06

BENCHUIX-06 já coletou tipo de negócio, objetivo principal e canais usados para o primeiro preview. BENCHUIX-07 reaproveita esse contexto e só pede o que ainda falta para montar um perfil mínimo sem repetição.

## campos iniciais obrigatórios

Limite máximo: 3 campos iniciais obrigatórios.

1. `oferta_principal`
   Explica o que o negócio entrega com mais frequência para orientar templates, linguagem e prioridade.
2. `ritmo_operacao`
   Resume como o trabalho chega e com que urgência para ajustar fila, cadência e expectativa de resposta.
3. `acoes_que_pedem_ok`
   Identifica o que exige confirmação explícita para manter defaults seguros desde o início.

## campos incrementais opcionais

- `sazonalidade_curta`
- `horarios_sensiveis`
- `excecoes_frequentes`
- `meta_secundaria`
- `tom_de_comunicacao`
- `restricoes_operacionais`

Esses campos entram por progressive disclosure e nunca bloqueiam o primeiro perfil salvo.

## justificativa de cada campo

- `oferta_principal`: permite entender contexto de valor sem exigir catálogo completo.
- `ritmo_operacao`: evita defaults genéricos demais quando o negócio opera em urgência alta ou fluxo previsível.
- `acoes_que_pedem_ok`: protege confiança do dono-solo ao deixar claro onde a automação pode sugerir e onde deve aguardar confirmação.
- `sazonalidade_curta`: ajuda a calibrar volume sintético e priorização sem exigir histórico real.
- `horarios_sensiveis`: evita recomendações fora do horário esperado pelo negócio.
- `excecoes_frequentes`: captura padrões que precisam aparecer como alerta ou bloqueio.
- `meta_secundaria`: ajuda a ordenar sugestões quando dois caminhos parecem úteis.
- `tom_de_comunicacao`: afina a linguagem das sugestões sem exigir branding final.
- `restricoes_operacionais`: registra limites simples que evitam sugestão insegura.

## defaults seguros por modo A/B/C/D

- Modo A: perfil enxuto, confirmação forte, explicação curta, uma prioridade por vez.
- Modo B: mantém simplicidade do dono-solo, mas admite um ajudante com visibilidade parcial e pendências compartilhadas.
- Modo C: adiciona contexto de equipe pequena, filas simples e permissões básicas sem virar setup corporativo.
- Modo D: ativa defaults conservadores, disclosure gradual e avisos de que camadas avançadas dependem de autorização futura.

## política de não repetição de dados

- nenhum dado já coletado em BENCHUIX-06 pode ser pedido de novo por padrão;
- quando houver contexto anterior, a fase reaproveita, confirma ou permite editar em um único ponto;
- campos duplicados bloqueiam a fase.

## política de auto-save synthetic-only

- o perfil salva apenas rascunho sintético;
- nenhum runtime real é acionado;
- nenhum dado real é exigido;
- auto-save só registra progresso local de especificação e estado candidato;
- falha de auto-save nunca pode esconder o que foi preenchido na tela.

## estados obrigatórios

- `empty`
- `loading`
- `error`
- `success`
- `degraded`

## microcopy candidata

- "Conte so o essencial do seu negocio."
- "Se faltar algo, voce completa depois."
- "Nada real sera alterado agora."
- "Vamos guardar um rascunho simples para continuar sem pressa."
- "Diga o que sempre precisa do seu ok."
- "O resto pode entrar depois."

## acessibilidade

- labels curtos e objetivos;
- uma pergunta principal por bloco;
- foco visível;
- ajuda curta perto do campo;
- erro com orientação direta;
- loading com feedback em até 300ms;
- degraded explicando limite e próximo passo seguro;
- leitura clara em mobile.

## critérios de BLOCK

- o fluxo vira cadastro longo;
- mais de 3 campos iniciais obrigatórios;
- algum campo inicial não tem justificativa explícita;
- dado real é obrigatório;
- auto-save depende de runtime real;
- dados de BENCHUIX-06 são repetidos;
- faltam defaults seguros por modo;
- copy principal usa jargão técnico para o cliente;
- billing, OAuth real, integração real, produção, secrets ou real_apply entram no escopo.

## anti-escopo

- não cria UI executável;
- não instala dependências;
- não toca Project_ARIS;
- não acessa runtime real;
- não usa billing;
- não usa OAuth real;
- não usa integração real;
- não usa dado real de cliente;
- não abre produto, produção, secrets ou real_apply.

## handoff para BENCHUIX-08

BENCHUIX-07 entrega um perfil mínimo sintético, incremental e com defaults seguros para que BENCHUIX-08 materialize playbooks por vertical sem reabrir cadastro longo.
