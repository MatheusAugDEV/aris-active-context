# BENCHUIX-03 Design System Spec

## Definicao

BENCHUIX-03 define a fundacao visual e interativa da experiencia ARIS. A UI e mecanismo de controle, nao estetica decorativa.

## Principios Visuais

- simples por fora, rigoroso por dentro;
- baixa densidade cognitiva no Modo A;
- risco sempre textual e visual;
- estados sempre explicitos;
- aprovacao sempre clara;
- evidencia sempre legivel;
- rollback sempre honesto;
- falha sempre com proximo passo;
- mobile-first;
- acessibilidade desde o inicio.

## Papel do Design System

- reduzir ambiguidade entre o que o ARIS mostra e o que o ARIS promete;
- padronizar linguagem visual para risco, permissao, evidencia, rollback e falha;
- impedir que cada tela invente regra nova de cor, estado ou interacao;
- preservar o baseline do Dono-Solo antes de qualquer densidade corporativa.

## Sistema de Tokens em Tres Niveis

### Reference

- valores base candidatos para cor, tipografia, espacamento, radius, sombra, motion e tamanho de alvo;
- podem mudar em Crisol sem quebrar contratos semanticos.

### System

- papeis semanticos de interface;
- mapeia tema light/dark por remap;
- define estados, risco, evidencia, permissao, degradacao e acao destrutiva.

### Component

- aplica papeis do tier system por componente;
- nao carrega valor final hardcoded;
- deve declarar estados obrigatorios e regras duras de uso.

## Regra de Tema

- dark e light devem ser resolvidos apenas por remap no tier `system`;
- componentes nao devem carregar cor final hardcoded;
- paleta final continua candidata e pode seguir para revisao em Crisol;
- contraste e semantica devem sobreviver a troca de tema sem remap por componente.

## Estados Obrigatorios

Todo componente base deve prever:

- `empty`
- `loading`
- `error`
- `success`
- `degraded`

## Semantica Obrigatoria do ARIS

- awaiting approval;
- running;
- failed;
- partial;
- rollback available;
- undone;
- paused;
- evidence verified;
- risk low;
- risk sensitive;
- risk critical;
- destructive action;
- degraded mode.

## Motion

- motion deve ser contido e funcional;
- deve respeitar `prefers-reduced-motion`;
- animacao nunca pode ser necessaria para entender uma decisao;
- motion nao pode esconder status, risco ou erro;
- feedback critico precisa ter fallback estatico.

## Acessibilidade

- contraste legivel por padrao;
- foco visivel em controles acionaveis;
- texto alem de cor para risco, erro e sucesso;
- target minimo para toque;
- status messages legiveis por tecnologia assistiva;
- compatibilidade futura com WCAG 2.2 como direcao obrigatoria.

## Regras de Linguagem

- jargao tecnico nao entra na UI primaria;
- estados devem usar linguagem humana e honesta;
- acao sensivel deve declarar o que vai fazer e o que nao vai fazer;
- evidencia deve parecer recibo verificavel, nao log tecnico.

## Regras por Estado Critico

- risco nao pode depender so de cor;
- aprovacao exige copy explicita e contexto;
- rollback precisa diferenciar reversivel, compensavel e irreversivel;
- falha sempre informa o que ainda funciona e o que fazer depois;
- modo degradado deve deixar limites visiveis.

## Motion, Performance e Mobile

- mobile-first para espacamento, tipografia e hit targets;
- componentes base nao devem depender de animacao longa;
- loading precisa escalar para conexao ruim sem gerar falsa impressao de travamento;
- tokens de component devem evitar excesso de peso visual no Modo A.

## Anti-Escopo

- nao congela branding final;
- nao cria UI executavel;
- nao cria PWA;
- nao cria componente React;
- nao instala dependencias;
- nao toca produto real;
- nao abre runtime real;
- nao usa secrets;
- nao ativa real_apply.

## Criterios de BLOCK

- cor final hardcoded em componente;
- componente sem estado de erro ou degraded;
- aprovacao sem `vai fazer / nao vai fazer`;
- evidencia parecendo log tecnico;
- motion necessario para entender decisao;
- mobile sem target adequado;
- qualquer tentativa de transformar tokens em produto executavel nesta fase.
