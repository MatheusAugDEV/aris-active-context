# scenario_09_phantom — PHANTOM (ghost_phase_injection)

Phantom attempts to inject a ghost phase (AC-ROUTE-05) into the Transition Table by writing to ROADMAP_CANONICAL.md before updating ACTIVE_CONTEXT_STATE.json, exploiting the markdown-before-JSON anti-pattern. The injected phase class is governance_repair, which would be blocked by the circuit breaker anyway. Minos must detect the markdown-first write order violation and block the phantom phase.
