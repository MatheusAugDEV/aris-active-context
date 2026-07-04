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
