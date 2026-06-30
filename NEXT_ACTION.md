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

O **Cleanup Autorizado Minimal Safe Set foi executado com decisão=pass** em 2026-06-30.

9 itens removidos: F5-001, F5-002, F5-003, F5-007, F5-008, F5-009, F5-010, F5-011, F5-012.
7 itens não autorizados preservados: F5-004, F5-005, F5-006, F5-013, F5-014, F5-015, F5-016.
Precheck=PASS. Postcheck=PASS. CI=green. HEAD==origin/main.

---

### Próximas Ações (por prioridade)

**1. OPERADOR — Decisão sobre F5-006 (`legacy/wake/tts.py.backup`):**
Não foi autorizado pois pode ser a única cópia do código TTS. O operador deve
confirmar se existe cópia alternativa antes de autorizar remoção em prompt separado.

**2. OPERADOR — Decisão sobre F5-004 e F5-005 (`temp_audit/f15z1`, `temp_audit/f15z1_post_z3`):**
Ler conteúdo dos dois arquivos de 120B para confirmar se são gate markers antes de autorizar remoção.

**3. OPERADOR — Decisões de itens BLOQUEADOS (separadas, por finding):**
- **F4-FIND-002** (`F5-015`): Nested Git repo em `external/mcp_candidates/` —
  escolher estratégia: submodule / vendor / remove / quarantine
- **F4-FIND-003** (`F5-013`, `F5-014`): PostScript binários em `legacy/experiments/` —
  confirmar origem e intenção antes de qualquer remoção (ação irreversível)

**4. OPERADOR — Rotação de Segredos (independente de fase):**
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
