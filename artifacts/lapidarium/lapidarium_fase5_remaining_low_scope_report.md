# LAPIDARIUM FASE 5 — Revisão dos Itens Restantes de Baixo Escopo

**Fase:** LAPIDARIUM_FASE_5_REMAINING_LOW_SCOPE_ITEM_REVIEW  
**Data:** 2026-06-29  
**Decisão:** PASS (read-only review)  
**SHA de início:** `c5bd314cc9c44dcdb908fd392ec26a77829f95e7`

---

## Escopo

Revisão read-only de 3 itens restantes: F5-004, F5-005, F5-006.

**Fora de escopo:** F5-013, F5-014, F5-015 (BLOQUEADOS), F5-016/.env (KEEP).  
**Nenhum cleanup foi executado.** Esta fase é análise + recomendação apenas.

---

## Confirmações Preliminares

### 9 itens removidos — confirmados ausentes

| Item | Path | Status |
|------|------|--------|
| F5-001 | temp_audit/ambiguity_resolver_report.md | AUSENTE ✓ |
| F5-002 | temp_audit/ambiguity_resolver_summary.json | AUSENTE ✓ |
| F5-003 | temp_audit/ambiguity_resolution_samples.jsonl | AUSENTE ✓ |
| F5-007 | legacy/wake/wake.py.backup | AUSENTE ✓ |
| F5-008 | legacy/experiments/tart=always | AUSENTE ✓ |
| F5-009 | debug_audio.wav | AUSENTE ✓ |
| F5-010 | teste.wav | AUSENTE ✓ |
| F5-011 | `[:alnum:] \n \` | AUSENTE ✓ |
| F5-012 | `how --stat --summary 5dda82a` | AUSENTE ✓ |

### Itens bloqueados — confirmados intocados

| Item | Path | Status |
|------|------|--------|
| F5-013 | legacy/experiments/genai | EXISTE, NÃO TOCADO ✓ |
| F5-014 | legacy/experiments/threading | EXISTE, NÃO TOCADO ✓ |
| F5-015 | external/mcp_candidates/gogogadgetbytes_smart_connections_mcp | EXISTE, NÃO TOCADO ✓ |
| F5-016 | .env | EXISTE, NÃO LIDO ✓ |

---

## F5-004: `temp_audit/f15z1`

**CORREÇÃO DO INVENTÁRIO:** O inventário classificou este item como arquivo (120B, text/plain). Na verdade é um **diretório** com 4 arquivos TSV (≈32KB total).

**Conteúdo:**
- `scripts_run1.tsv` / `scripts_run2.tsv`: 33 linhas cada — saída de execução de scripts F15 com exit code e status string
- `tests_run1.tsv` / `tests_run2.tsv`: 32 linhas cada — resultados de testes F15 Zone 1 (vários com exit=1, status=*_warn/*_blocked)

**Análise:**
- Snapshot de execução do F15 Zone 1 (zona antes do Z3). Scripts/testes mostrando estado de warn/blocked.
- Sem imports de código-fonte: nenhum arquivo em `src/`, `scripts/`, `tests/` referencia este diretório funcionalmente.
- Referências existentes: apenas listagens de inventário em artifacts/lapidarium e artifacts/f17.
- Git history preserva o conteúdo (commit `5125c4d3`).
- run1 e run2 são capturas duplicadas dentro do mesmo diretório.
- Verificação de gate marker: **NEGATIVO** — conteúdo é TSV de resultado de execução.

**Classificação:** `REMOVE_CANDIDATE` | Confiança: **HIGH**  
**Risco de remoção:** LOW  
**Pré-requisito:** Autorização explícita do operador por item_id

---

## F5-005: `temp_audit/f15z1_post_z3`

**CORREÇÃO DO INVENTÁRIO:** Mesma correção que F5-004 — é um **diretório** com 4 TSVs (≈32KB).

**Conteúdo:**
- Mesma estrutura que f15z1, mas captura o estado **pós-Zone-3**.
- Diff vs f15z1: scripts/testes que antes tinham exit=1/warn/blocked agora mostram exit=0/ready/passed/completed.
- Documenta a progressão de estado Z1→Z3 dentro do F15.

**Análise:**
- Sem imports funcionais em nenhum arquivo de código.
- Referências: apenas listagens de inventário.
- Git history preserva o conteúdo (commit `5125c4d3`).
- Os artifacts/f15/ são a fonte canônica autorizada do estado de execução F15.
- Verificação de gate marker: **NEGATIVO**.

**Classificação:** `REMOVE_CANDIDATE` | Confiança: **HIGH**  
**Risco de remoção:** LOW  
**Pré-requisito:** Autorização explícita do operador por item_id

---

## F5-006: `legacy/wake/tts.py.backup`

**Resolução da preocupação anterior:** "Pode ser a única cópia do código TTS."

**Nova evidência:** Existe um módulo TTS ativo e evoluído em `src/aris/voice/tts.py`:
- 698 linhas / 24.800 bytes — vs backup com ~130 linhas / 6.621 bytes
- Integrado com: settings, secrets, logging, persona, external_boundary, security
- Importado por: `src/aris/turn/boot_manager.py` (TTSRuntimeError, falar, get_tts_runtime_status, is_tts_runtime_executable)

**O backup:**
- `legacy/wake/tts.py` (sem .backup) **não existe** — o backup é o único arquivo com esse nome nesse diretório
- Porém o backup **não é importável** (.backup extension, não está no Python path)
- Nenhum arquivo importa `legacy/wake/tts.py.backup`
- Referências: apenas documentais (ARCHITECTURE_STATUS.md, PROJECT_CONTEXT_ARIS.md, voice wiring readiness)
- Git history preserva o conteúdo em commits `49343a05` e `dcf6da5f`

**Classificação:** `REMOVE_CANDIDATE` | Confiança: **HIGH** (upgrade de MEDIUM)  
**Risco de remoção:** LOW  
**Pré-requisito:** Autorização explícita do operador por item_id

---

## Matriz de Decisões Finais

| Item | Path | Decisão Anterior | Nova Decisão | Confiança | Risco |
|------|------|-----------------|--------------|-----------|-------|
| F5-004 | temp_audit/f15z1 | NEEDS_OPERATOR_DECISION | **REMOVE_CANDIDATE** | HIGH | LOW |
| F5-005 | temp_audit/f15z1_post_z3 | NEEDS_OPERATOR_DECISION | **REMOVE_CANDIDATE** | HIGH | LOW |
| F5-006 | legacy/wake/tts.py.backup | REMOVE_CANDIDATE (MEDIUM) | **REMOVE_CANDIDATE** | HIGH | LOW |

---

## Próximos Passos Recomendados

Para autorizar a remoção destes 3 itens, o operador deve emitir prompt explícito nomeando os item_ids:

```
Autorizo remoção de F5-004 (temp_audit/f15z1).
Autorizo remoção de F5-005 (temp_audit/f15z1_post_z3).
Autorizo remoção de F5-006 (legacy/wake/tts.py.backup).
```

Uma nova fase de execução de cleanup será emitida com apenas os itens autorizados.

**Itens que permanecem BLOQUEADOS e fora de escopo desta fase:**
- F5-013, F5-014: PostScript binários — aguardando decisão do operador sobre origem/intenção
- F5-015: Nested git repo — aguardando decisão de supply chain
- F5-016: .env — KEEP (gitignored, rotação é responsabilidade do operador)

---

## Attestation

- Nenhum arquivo foi deletado, movido ou modificado nesta fase.
- `.env` não foi lido nem imprimido.
- Todos os locks de runtime/produto/Bedrock/secrets permanecem `false`.
