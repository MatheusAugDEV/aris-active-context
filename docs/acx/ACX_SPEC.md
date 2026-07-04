# ACX_SPEC.md — ACX v2 "Lastro"

## 0. Propósito e limite

Esta spec substitui o comportamento implícito do ACX v1. Ela não executa nada. Nenhum código nesta fase. Exit desta fase: este arquivo commitado + entrada em `DECISION_LOCKS.md` registrando a criação do track e o congelamento da spec.

Teto duro: ~150 linhas efetivas de conteúdo normativo (fora esta seção e a de riscos). Se passar disso, corta escopo — não é permitido justificar tamanho com completude.

## 1. Inventário de fatos duplicados (mapa de espelhos atual)

| Fato | Onde vive hoje | Espelhos | Autoridade real |
|---|---|---|---|
| Status do finding IF09-FIND-001 | `ACTIVE_CONTEXT_STATE.json` (`closed`) | `DECISION_LOCKS.md` (~30 entradas dizendo `open`) | JSON, por regra — mas markdown é ruído dominante em volume |
| `next_phase` | `ACTIVE_CONTEXT_STATE.json` (`null`) | `ROADMAP_CANONICAL.md` (`Próxima fase:` da seção ativa aponta pra fase real) | Contraditório — a própria regra de derivação produz valor diferente do campo |
| Locks de execução | `ACTIVE_CONTEXT_STATE.json.authorization` + `.execution_locks` (duplicado dentro do mesmo arquivo) | — | Nenhum motivo pra existirem dois blocos com os mesmos 16 campos |
| `sha_lido` | Campo de topo do envelope (hash do blob) e campo interno do JSON (hash de commit do projeto) | — | Mesmo nome, dois referentes — fonte de confusão, não de espelho, mas mesma categoria de risco |
| Fase de status do sistema | `ACTIVE_CONTEXT_STATE.json` | Renders esperados: `CURRENT_STATE.md`, `NEXT_ACTION.md`, `README.md` | Historicamente ficaram congelados enquanto JSON avançava, forçando registro em `DECISION_LOCKS.md` (ver §5, F-06) |

## 2. Máquina de estados

**Ciclo de vida de fase**, sete estados: `IDLE → SPEC_FROZEN → AUTHORIZED → EXECUTING → REPORTED → VALIDATED → CLOSED → IDLE`.

Transições legais:
- `IDLE → SPEC_FROZEN`: Claude/GPT propõe spec de fase. Nenhum outro estado alcançável daqui.
- `SPEC_FROZEN → AUTHORIZED`: só operador. Nunca automático, nunca por inferência de padrão anterior.
- `AUTHORIZED → EXECUTING`: Codex abre via `acx open`.
- `EXECUTING → REPORTED`: Codex fecha via `acx report` (comando único, obrigatório).
- `REPORTED → VALIDATED`: Claude/GPT valida evidência, nunca autorrelato.
- `VALIDATED → CLOSED`: avança `roadmap_cursor`.
- `CLOSED → IDLE`: automático, mesma transação.

Qualquer tentativa de pular estado é rejeitada pelo validador (R1) por violação de FSM, não por regra ad hoc.

**roadmap_cursor**: tipo enum `{CANDIDATE, AUTHORIZED, ACTIVE, END}`, nunca `null`. Transição `→ EXTEND` permite reabrir `END` de forma auditável quando o roadmap precisar crescer — evento nomeado, não edição manual. Resolve o problema de "candidate-only" ser nota de prosa em vez de estado tipado com transição própria.

## 3. Schema v2 — campos normativos novos

## 4. Tabela de invariantes

| Invariante | Mecanismo de garantia |
|---|---|
| Markdown nunca é fonte, só render | R2: CLI é único escritor de `STATE.json`; renders gerados, nunca editados |
| Nenhum campo com nome ambíguo entre hash de blob e hash de commit | Schema v2 renomeia (`state_blob_hash` / `project_commit_sha`) |
| `Próxima fase:` nunca aponta pra `Status: CLOSED` | Regra de validador (R1) |
| Toda seção do ROADMAP tem exatamente um cursor ativo | Validador falha se zero ou mais de um |
| Contador de gate/repair não pode ser isento por classificação | Todo evento incrementa; `NO_RITUAL_AUTHORIZATION` deixa de suspender contagem |
| Evidência citável nunca vive em `/tmp` ou clone descartável | Regra de validador: caminho de evidência precisa estar dentro do repo versionado |
| CI verde ≠ suíte verde | Dois campos separados no relatório de fase; nunca um substitui o outro |
| Fold é função pura, sem side-effect | Efeitos externos só disparam no momento do append original, nunca durante replay/refold |

## 5. Seção de riscos consolidada (22 achados)

*(Tags: FATO = verificado contra estado vivo ou literatura; INFERÊNCIA = mecanismo deduzido)*

| Origem | # | Achado resumido | Vira regra em |
|---|---|---|---|
| Estado vivo | F-01 | `sha_lido` ambíguo (blob vs commit) | §3, schema v2 |
| Estado vivo | F-02/F-03 | `next_phase=null` vs regra de derivação sem referente ACTIVE | §2, roadmap_cursor |
| Estado vivo | F-04 | `Próxima fase:` apontando pra fase CLOSED | R1, invariante §4 |
| Estado vivo | F-05 | Validador de 17.969 linhas — causa-raiz de F-06/F-07 | R1, reescrita completa |
| Estado vivo | F-06 | JSON congelado, estado real forçado pro markdown | R2, CLI único escritor |
| Estado vivo | F-07 | 40 versões de schema, gaps de sumário | R1/R4, §6 disciplina de migração |
| Estado vivo | F-08 | `governance_gate_streak=0` durante maior explosão de meta-trabalho — isenção por classificação | §4, invariante de contador |
| Estado vivo | F-09 | IF09-FIND-001 `closed` (JSON) vs `open` ×30 (DECISION_LOCKS) | R2, genesis do ledger (decisão pendente, §7) |
| Estado vivo | F-10 | Evidência citada em `/tmp` e clones descartáveis | §4, invariante de evidência |
| Estado vivo | F-11 | CI verde com suíte local quebrada (1519 erros) | §4, invariante CI≠suíte |
| Estado vivo | F-12 | Rotação de segredo pendente sem função forçante | Fora de ACX — ação manual do operador |
| Teórico | 1 | Fold não-determinístico | R1, CI refolda e compara hash |
| Teórico | 2 | Side-effect durante replay | §4, invariante fold puro |
| Teórico | 3 | Staleness do lado do consumidor (cache do MCP) | R3, `ledger_head_hash` explícito no render |
| Teórico | 4 | Migração de schema sem teste de refold | §6 |
| Teórico | 5 | CLI ponto único de falha | R2, verbo `acx override` com justificativa logada |
| Teórico | 6 | Validador reativo (só pega caso já visto) | Nomeado como limitação residual aceita, não fingida como resolvida |
| Teórico | 7 | Pre-commit pulado sob pressão | R1/R2, branch protection com status check obrigatório |
| Teórico | 8 | `ROADMAP_END` sem transição de extensão | §2, evento `EXTEND` |
| Teórico | 9 | Autorização de operador sem prova de identidade | R2, confirmação interativa com phase ID digitado |
| Teórico | 10 | Taxa de onboarding futuro | R0, exemplo mínimo por verbo na própria spec |
| Pesquisa | 13 | Estado-sombra é violação nomeada (Factor 5, 12-factor agents) | R2/R3 |
| Pesquisa | 14 | Falta política de poda (LangGraph storage volume) | R3, regra de arquivamento por idade/contagem |
| Pesquisa | 15 | Snapshot inchado custa atenção (dumb zone, Factor 3) | R3, teto de tokens como critério de saída |
| Pesquisa | 16 | Migração dentro do runtime é erro raiz do F-07 | §6 |

## 6. Disciplina de migração de schema

Migração de `schema_version` é ato deliberado, nunca acoplado a um gate de fase. Checklist obrigatório antes de qualquer bump:
1. Golden-fixture do ledger completo até o commit atual.
2. Refold sob o schema novo.
3. Diff entre `STATE.json` resultante e o committed — zero diff ou migração rejeitada.
4. Sumário de changelog obrigatório e contíguo (sem números pulados).

## 7. Decisão pendente, não bloqueante

Ledger genesis (F-09): como reconciliar `closed` (JSON) vs `open` ×30 (DECISION_LOCKS) no evento zero do ledger. Decisão explícita: **adiada para R2**, por instrução do operador. Registrada aqui para não ser esquecida — R2 não pode começar sem resolver isso primeiro.

## 8. Critério de sucesso do track

`manual_repair` = tipo de evento no ledger. Contável a partir do R2. Sucesso: `manual_repair = 0` nas 3 fases reais seguintes ao R4.
