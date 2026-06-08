# BOOT_PROFILE

## Canonical Boot Order

Read in this exact order. Never read a Markdown file before the JSON source.

```
1. ACTIVE_CONTEXT_STATE.json          ← canonical live state (read this first, always)
2. AGENT_IDENTITY.md                  ← identidade e constituição do orquestrador (leitura obrigatória em todo boot)
3. ACTIVE_CONTEXT_SCHEMA.json         ← validation contract
4. scripts/validate_active_context_state.py  ← run before any decision
5. CURRENT_STATE.md                   ← derived mirror (confirms JSON, does not supersede it)
6. NEXT_ACTION.md                     ← derived mirror
7. DECISION_LOCKS.md                  ← derived mirror
8. ROADMAP_CANONICAL.md               ← roadmap sequence authority
9. ROADMAP_AMENDMENT_PROTOCOL.md      ← before proposing roadmap mutation
10. ARIS_PHASE_LEDGER.md              ← historical ledger only, after the above
```

## Boot Rule

- **ACTIVE_CONTEXT_STATE.json is always step 1.** Any boot that reads Markdown first is violating the anti-corruption contract.
- Run `scripts/validate_active_context_state.py`. If it fails, report drift and do not proceed.
- Markdown files confirm the JSON. If a Markdown file contradicts the JSON, the JSON wins and the drift must be reported.

## Retake Order (on re-entry)

1. Read `ACTIVE_CONTEXT_STATE.json` first — get current live state.
2. Run `scripts/validate_active_context_state.py` — verify no drift.
3. Check `NEXT_ACTION.md` second — confirm singular next step.
4. Use `DECISION_LOCKS.md` for authorization boundaries only.
5. Use `ROADMAP_CANONICAL.md` for active roadmap semantics.
6. Use `ROADMAP_AMENDMENT_PROTOCOL.md` before proposing roadmap mutation.
7. Use `ARIS_PHASE_LEDGER.md` for compact milestone history only after the active files above.

`CONTEXT_INDEX.md` is no longer a mandatory boot step. The validator already tracks the required transition files; consult `CONTEXT_INDEX.md` only as an optional artifact-route index when explicitly needed.

## Authority Stack

- `ACTIVE_CONTEXT_STATE.json` beats all Markdown, memory, chat history, and summaries.
- Active-context beats stale memory, old history, and assumptions.
- Canonical roadmap beats preserved historical overlays for active direction.
- Product Loop L1.15 remains closed evidence.
- H0 design brief remains materialized design-only evidence pending roadmap-alignment review.

## Hard Limits

- No bulk-read of docs, archive, Obsidian, or history dumps.
- Obsidian is query-first only and only when explicitly needed.
- Do not claim token savings without measurement.
- Do not modify protected sources from boot usage unless the current gate explicitly authorizes it.
- Do not treat Markdown state as authoritative if it conflicts with the JSON.
