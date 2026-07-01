# AC-BREAK-05 — ARIS Active-Context Circuit Breaker Gate

**Decision:** PASS  
**Date:** 2026-06-03  
**Previous phase:** AC-CONTRACT-04 (ARIS Active-Context Phase Contract Hardening Gate)  
**origin/main SHA at gate open:** `67849c6`

---

## Context

AC-REPAIR-01, AC-OBS-02, AC-TRANS-03, and AC-CONTRACT-04 are four consecutive governance gates
executed without a capacity gate in between. The governance chain was at risk of indefinite
proliferation through further meta-governance corrections without producing real executable
capability (fixtures, bots, minos verdicts, etc.).

This gate installs a three-layer circuit breaker in the validator to structurally prevent this
from recurring, and sets `governance_gate_streak = 4` so the block is immediately active.

---

## What Changed (Canonical Facts)

| Artifact | Change |
|---|---|
| `scripts/validate_active_context_state.py` | Added `_check_governance_streak`, `_check_gate_signature`, `_check_cycle_nudge`, `_apply_streak_management` |
| `ACTIVE_CONTEXT_SCHEMA.json` | New required fields: `governance_gate_streak` (int), `seen_gate_signatures` (array), `phase_class` (string) |
| `ACTIVE_CONTEXT_STATE.json` | `governance_gate_streak=4`, `seen_gate_signatures=[]`, `phase_class="circuit_breaker"`, `current_phase_id="AC-BREAK-05"` |
| `ROADMAP_CANONICAL.md` | AC-BREAK-05 row added to Próxima fase; Active Route updated |
| `MANDATORY_READ_FIRST_RULES.md` | REGRA DE CIRCUIT BREAKER section added |

---

## Three-Layer Circuit Breaker

### Layer 1 — Governance Streak Check (`_check_governance_streak`)

- Reads `governance_gate_streak` from state.
- If `phase_class` is in `GOVERNANCE_CLASSES` and `streak >= 3`: **`sys.exit(1)` — BLOCK**.
- If `streak == 2`: prints `WARN` (next gate must be capacity).
- `phase_class = "circuit_breaker"` is not in `GOVERNANCE_CLASSES`, so this gate itself is not blocked.

### Layer 2 — Gate Signature Deduplication (`_check_gate_signature`)

- Computes `sha256(phase_class + authorization)[:16]`.
- If signature is in `seen_gate_signatures`: **`sys.exit(1)` — BLOCK** (gate produces no new state).
- Returns the signature for downstream use by `_apply_streak_management`.

### Layer 3 — Cycle Nudge (`_check_cycle_nudge`)

- If `gate_cycles_used >= gate_max_cycles - 1`: prints `WARN` to prompt terminal verdict.
- Does not block on its own; combines with Layer 1 to enforce urgency.

---

## Streak Management Logic (`_apply_streak_management`)

On `decision == "pass"`:

- If `phase_class` is in `CAPACITY_CLASSES`: set `governance_gate_streak = 0`.
- If `phase_class` is in `GOVERNANCE_CLASSES`: increment `governance_gate_streak` by 1.
- Append current gate signature to `seen_gate_signatures`.

**The model cannot zero the streak manually.** The only path to reset is a capacity gate pass.

---

## Streak at Close

| Gate | Class | Streak after |
|---|---|---|
| AC-REPAIR-01 | governance_repair | 1 |
| AC-OBS-02 | observability | 2 |
| AC-TRANS-03 | transition_engine | 3 |
| AC-CONTRACT-04 | contract | 4 |
| **AC-BREAK-05** | circuit_breaker (not governance) | **4** (unchanged) |

`circuit_breaker` is not in `GOVERNANCE_CLASSES`, so AC-BREAK-05 does not increment the streak.
The streak stays at 4. Any gate with a `phase_class` in `GOVERNANCE_CLASSES` will be blocked
immediately by the validator.

---

## Simulation Test Result

Temporarily setting `phase_class = "governance_repair"` with `governance_gate_streak = 4`
in a state copy causes `_check_governance_streak` to call `sys.exit(1)` with:

```
BLOCK: governance_gate_streak >= 3.
3 governance gates consecutivos sem capacidade real.
Proximo gate obrigatorio: classe de capacidade.
Operador deve autorizar explicitamente.
```

Original state restored after test.

---

## What Did NOT Change

- No execution authorized.
- No fixture materialization.
- No bot activation.
- No runtime mutation.
- No authorization flag flipped to `true`.
- No network scope change.

---

## Next Gate

**Only valid next gate: `INF-MAT-01` (class: `fixture_materialization`).**

The operator must authorize this explicitly. Any attempt to open a governance-class gate
will be blocked by the validator with `exit(1)` before any state mutation.
