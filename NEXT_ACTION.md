# NEXT_ACTION

> Fonte primária: `ACTIVE_CONTEXT_STATE.json`. Este arquivo é mirror derivado.
> JSON é autoridade máxima. Markdown contraditório é drift.
> Última atualização: LAPIDARIUM_FASE_5_CLEANUP_EXECUTION_AUTHORIZED_MINIMAL_SAFE_SET (2026-06-30)

---

## CURRENT CANONICAL NEXT ACTION

- **Source of truth:** `ACTIVE_CONTEXT_STATE.json`
- **phase_id:** `LAPIDARIUM`
- **sha_lido:** `0a64f632bd25e50c29112a4468298b72ee31af73`

### Status Atual

**Revisão dos Itens Restantes de Baixo Escopo concluída com decisão=pass** em 2026-06-29.

F5-004 e F5-005 inspecionados: são diretórios (não arquivos). Conteúdo TSV de resultados de execução F15.
F5-006 inspecionado: TTS ativo confirmado em `src/aris/voice/tts.py` — backup não é única cópia.
Todos os 3 itens classificados como REMOVE_CANDIDATE (HIGH confidence).

---

### Próximas Ações (por prioridade)

**1. OPERADOR — Autorizar remoção de F5-004, F5-005, F5-006 (opcional, em prompt separado):**

Revisão concluída. Os 3 itens são seguros para remoção. Para autorizar:
- F5-004 (`temp_audit/f15z1`): diretório com TSVs de snapshot F15 Zone 1 — nenhuma dependência funcional
- F5-005 (`temp_audit/f15z1_post_z3`): diretório com TSVs de snapshot F15 pós-Zone-3 — nenhuma dependência funcional
- F5-006 (`legacy/wake/tts.py.backup`): backup legacy; TTS ativo está em `src/aris/voice/tts.py` (698 linhas)

Para autorizar: emitir prompt nomeando item_ids explicitamente.

**2. OPERADOR — Decisões de itens BLOQUEADOS (separadas, por finding):**
- **F4-FIND-002** (`F5-015`): Nested Git repo em `external/mcp_candidates/` —
  escolher estratégia: submodule / vendor / remove / quarantine
- **F4-FIND-003** (`F5-013`, `F5-014`): PostScript binários em `legacy/experiments/` —
  confirmar origem e intenção antes de qualquer remoção (ação irreversível)

**3. OPERADOR — Rotação de Segredos (independente de fase):**
Ver `artifacts/lapidarium/lapidarium_f4_find001_rotation_checklist.md`.
`.env` está corretamente gitignored — avaliação de risco é responsabilidade do operador.

---

### Aguardando Instrução

Todos os locks de runtime, produto e Bedrock permanecem `false`. Nenhuma ação
não autorizada explicitamente pelo operador será iniciada.

---

## Historical Appendix

`HISTORICAL_ONLY`
`SUPERSEDED_BY_LAPIDARIUM_FASE4_AND_F4_FIND001_CONTAINMENT`
`NOT_CURRENT_STATE`

Referências a IF09/next_phase=null e P15–P19 são históricas e superseded.
