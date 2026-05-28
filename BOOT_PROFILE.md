# BOOT_PROFILE

## Canonical Boot Order

Read in this exact order. Never read a Markdown file before the JSON source.

```
1. ACTIVE_CONTEXT_STATE.json          ← canonical live state (read this first, always)
2. ACTIVE_CONTEXT_SCHEMA.json         ← validation contract
3. scripts/validate_active_context_state.py  ← run before any decision
4. CURRENT_STATE.md                   ← derived mirror (confirms JSON, does not supersede it)
5. NEXT_ACTION.md                     ← derived mirror
6. DECISION_LOCKS.md                  ← derived mirror
7. CONTEXT_INDEX.md                   ← derived mirror / artifact route index
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
5. Use `CONTEXT_INDEX.md` to locate supporting evidence without widening the boot.
6. Use `ROADMAP_CANONICAL.md` for active roadmap semantics.
7. Use `ROADMAP_AMENDMENT_PROTOCOL.md` before proposing roadmap mutation.
8. Use `ARIS_PHASE_LEDGER.md` for compact milestone history only after the active files above.

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
