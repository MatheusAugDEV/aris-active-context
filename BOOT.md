# BOOT

GERADO — NAO EDITE A MAO

## CARIMBO

- state_sha: `b5af97d07aba`
- schema_version: `3.22`

## AVISO DE STALE

- Se este state_sha nao bate com sha256(STATE.json), rode `python3 scripts/render_boot.py`.

## ONDE ESTOU

- camada: `Unknown`
- phase_id: `IF09_CLOSURE_MILESTONE_MIRROR_SANITY_PACKET`
- status: `if09_closure_milestone_mirror_sanity_pass`
- decision: `pass`
- resumo: IF09 Closure Milestone Mirror Sanity Packet; sem transicao sucessora definida, aguardando instrucao do operador.

## MAPA

  Infernus FULL
  Purgatorium FULL
  Infernus Revalidation
  BenchUX
  Crisol
  Polimento
  EXT-SEC 00→04
  Cinzel
  EXT-SEC 05→06
  Bedrock Gate
  Produto Parte 2 / Design Partner
  EXT-SEC 07→08 contínuo

## PROXIMO PASSO

- active_next_phase: `null`
- next_phase_class: `null`
- advance_mode: `operator`
- travas relevantes:
  - next_phase_authorized_by_operator=False
  - next_phase_execution_authorization=False
  - operator_approval_packet_review_is_execution_approval=False
  - real_apply_authorized=False
  - runtime_integration_allowed=False
  - production_authorized=False
  - product_ready=False
  - secrets_access_authorized=False
  - deferred_phase_reason=Nenhuma transição definida. Aguardando instrução do operador. ROADMAP_CANONICAL.md não define sucessor para IF09_CLOSURE_MILESTONE_MIRROR_SANITY_PACKET.

## REGRAS DE AGORA

- TODO R2: mover para RULES/ por phase_class.
- JSON vence tudo; markdown que contradiz = drift, pare e reporte.
- Proximo passo so da Transition Table; nao inferir de nome de arquivo nem historico.
- Sem execucao real/runtime/produto/Bedrock/secrets sem lock=true.
- Self-report nao e PASS; PASS = artifact + hash + CI verde + validator.
- excludent/ e archive/ nao sao fonte; forensic-only.
- Fase que muda fato canonico atualiza STATE.json primeiro.

## LEI DE ATUALIZACAO

- Atualize `ACTIVE_CONTEXT_STATE.json` primeiro.
- Regenere `BOOT.md` com `python3 scripts/render_boot.py`.
- Rode `python3 scripts/validate_active_context_state.py`.
- Commit e push apenas com BOOT sincronizado; o hook recusa drift.

## DISCIPLINA DE LEITURA

- Leia so esta pagina no boot inicial.
- Nao leia `archive/` nem `excludent/` como fonte.
- Docs profundos so quando o passo atual apontar explicitamente para eles.

## DOCS PROFUNDOS

- `ROADMAP_CANONICAL.md`
- `ACTIVE_CONTEXT_STATE.json`
- `artifacts/`
- `scripts/validate_active_context_state.py`
