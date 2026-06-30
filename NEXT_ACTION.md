# NEXT_ACTION

> Fonte primária: `ACTIVE_CONTEXT_STATE.json`. Este arquivo é mirror derivado.
> JSON é autoridade máxima. Markdown contraditório é drift.
> Última atualização: LAPIDARIUM_FASE_4_REVISAO_CODIGO_GENUINO (2026-06-30)

---

## CURRENT CANONICAL NEXT ACTION (Após Fase 4)

- **Source of truth:** `ACTIVE_CONTEXT_STATE.json`
- **phase_id:** `LAPIDARIUM`
- **lapidarium_fase4_decision:** `pass`
- **sha_lido:** `43503baad5012d8a921ba2b2f534e08ae2e9474b`

### Status da Fase 4

A **Fase 4 foi concluída com sucesso como read-only review** em 2026-06-30.

- 3.875 candidatos sanitizados revisados e classificados
- 3.808 (98,3%) são código genuíno de alta confiança (A+B+C+D)
- 67 requerem revisão do operador antes de qualquer ação
- Nenhum arquivo foi deletado, movido ou alterado
- Todos os locks reais permaneceram `false`

### Próximas Ações Recomendadas (por prioridade)

**1. IMEDIATO — SEGURANÇA (independente das fases):**
Remover `.env` do git tracking e rotar segredos (F4-FIND-001).
```
git rm --cached .env
echo ".env" >> .gitignore  # se ainda não constar
# rotar todos os segredos
```
Isso NÃO exige prompt de fase — é uma remediação de segurança urgente.

**2. FASE 4B — Generator Repair (recomendado antes de cleanup):**
Emitir prompt para `LAPIDARIUM_FASE_4B_DATASET_GENERATOR_QUOTING_REPAIR`.
Corrige o bug de quoting do generator da Fase 1 que produziu 2 artifacts acidentais.
Impede reintrodução dos mesmos artefatos corrompidos em regenerações futuras.

**3. FASE 5 — Cleanup Execution Plan:**
Emitir prompt para `LAPIDARIUM_FASE_5_CLEANUP_EXECUTION_PLAN`.
Planejamento cirúrgico de remoção de lixo confirmado:
- `temp_audit/` (2 arquivos de auditoria derivados)
- `legacy/wake/tts.py.backup`, `legacy/wake/wake.py.backup`
- `legacy/experiments/tart=always` (sujeito a inspeção confirmando shell output)
- `legacy/experiments/genai` e `legacy/experiments/threading` (sujeito a confirmação PostScript acidental)

**4. SUPPLY CHAIN — External MCP:**
Decidir destino de `external/mcp_candidates/gogogadgetbytes_smart_connections_mcp/` (F4-FIND-002).
Não iniciar sem decisão do operador.

### Aguardando Instrução

A execução da próxima subfase depende de instrução explícita do operador.
Nenhuma ação de cleanup, generator repair ou remoção de arquivo será iniciada
sem prompt específico. Todos os locks reais permanecem `false`.

---

## Historical Appendix

`HISTORICAL_ONLY`
`SUPERSEDED_BY_LAPIDARIUM_FASE4`
`NOT_CURRENT_STATE`

### IF09 / next_phase=null (HISTORICAL)

`HISTORICAL_ONLY` — O estado IF09_CLOSURE_MILESTONE_MIRROR_SANITY_PACKET com next_phase=null
é histórico e superseded. A fase viva é LAPIDARIUM com Fase 4 concluída.

### ARIS-CONTEXT P15–P19 (HISTORICAL)

`HISTORICAL_ONLY`
`SUPERSEDED_BY_INF_REVALIDATION_ADJUDICATION_OR_CLOSURE_PACKET`
`NOT_CURRENT_STATE`
