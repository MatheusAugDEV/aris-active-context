## definição da fase

BENCHUIX-18 materializa Permissões Progressivas como fase candidata, synthetic-only e orientada a menor privilégio da trilha BenchUIX. O foco e fazer cada pessoa ver apenas o necessario, com linguagem clara sobre o que pode e nao pode fazer.

## tese de permissões progressivas

Permissao boa nao e a que libera tudo; e a que reduz risco sem esconder contexto. O cliente precisa entender limite, responsabilidade e motivo do bloqueio sem virar administrador do sistema.

## objetivo

Definir views por papel, matriz de acesso, linguagem pode/nao pode e suspensao de acesso candidate-only para os modos A/B/C/D, preservando menor privilegio e bloqueando god mode, privilegio amplo por conveniencia e enforcement apenas client-side.

"cada pessoa vê só o que precisa e entende o que pode fazer?"

## relação com BENCHUIX-02, BENCHUIX-11, BENCHUIX-13 e BENCHUIX-17

BENCHUIX-02 separou superficies e boundaries. BENCHUIX-11 exigiu permissao explicita em aprovacoes. BENCHUIX-13 tornou a lista de automacoes auditavel e legivel. BENCHUIX-17 trouxe mobile companion com stale approval bloqueado e alternativa textual ao gesto. BENCHUIX-18 distribui esses contratos por papel sem esconder quem aprova, pausa, exporta ou apenas consulta.

## papel dono

O dono ve o panorama completo do negocio candidato, pode aprovar, pausar, editar e gerenciar acessos candidate-only. Continua sem god mode real e sem atravessar o boundary de produto, runtime ou auth real.

## papel ajudante

O ajudante acompanha o operacional e pode editar itens de baixo risco quando permitido, mas nao aprova decisoes sensiveis nem gerencia acesso. A view precisa deixar claro onde a autonomia termina.

## papel operador

O operador atua no dia a dia das automacoes candidatas, com leitura forte de status, pausa e ajustes operacionais limitados. Nao ganha acesso automatico a aprovacoes nem a exportacao ampla por conveniencia.

## papel financeiro

O financeiro precisa ver comprovantes e exportacao candidata relacionada, mas nao deve herdar permissao de editar automacoes ou aprovar fluxos fora do seu escopo. A linguagem precisa separar consulta de decisao.

## papel gerente

O gerente pode acompanhar indicadores operacionais e aprovar certos fluxos candidatos quando a role matrix permitir, mas nao deve virar superusuario silencioso. O que pode aprovar e o que nao pode alterar precisa ficar explicito.

## papel viewer

O viewer so consulta. Ve status, resumo e comprovantes permitidos, mas nao aprova, nao pausa, nao exporta tudo e nao edita. A experiencia precisa valorizar consulta segura em vez de parecer bloqueio arbitrario.

## views por papel

Cada papel deve receber apenas as superficies e acoes necessarias para sua funcao. Hoje e Historico podem ser mais amplos para consulta; Aprovar, Pausar, Exportar e Gerenciar Acesso exigem recorte explicito por papel.

## linguagem pode/não pode

Toda view precisa dizer em linguagem humana:

- o que este papel pode fazer agora;
- o que este papel nao pode fazer;
- quando uma aprovacao ou revisao adicional e necessaria.

## suspensão de acesso

Suspensao de acesso nesta fase e apenas candidata. Ela deve explicar impacto, superficies afetadas, preservacao de historico e como revisar o acesso depois, sem parecer remocao silenciosa ou irreversivel.

## defaults seguros por modo A/B/C/D

Modo A favorece dono-solo com minima distribuicao de acesso. Modo B libera colaboracao curta entre dono e ajudante. Modo C introduz papeis como gerente, operador, financeiro e viewer. Modo D prepara recortes mais finos, mas sem virar RBAC real nesta fase. Em todos os modos, o default e liberar menos e explicar mais.

## critérios de BLOCK

Bloquear quando houver:

- god mode;
- privilegio amplo por conveniencia;
- "todo mundo pode tudo";
- enforcement vendido como apenas client-side suficiente;
- aprovacao, edicao, pausa, exportacao ou comprovante sem papel explicito;
- suspensao sem explicar impacto;
- qualquer auth real, RBAC real, enforcement real, runtime real, dado real ou acao real no escopo.

## anti-escopo

Esta fase nao cria auth real, nao cria RBAC real, nao cria enforcement real, nao cria UI executavel, nao instala dependencias, nao usa OAuth real, nao usa secrets, nao executa runtime, nao executa acao real e nao autoriza produto, piloto, producao, Bedrock PASS ou real_apply.

## handoff para BENCHUIX-19

BENCHUIX-19 deve usar estas views progressivas para definir dashboard operacional avancado sem quebrar menor privilegio, clareza de permissao, bloqueio de god mode e separacao entre consulta e acao sensivel.
