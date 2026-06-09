PATCH PLAN ONLY - DO NOT APPLY IN THIS PHASE

1. schema enum change needed
Add `purgatorium_full_authority_materialization` to the live-route phase-class enum locations used by `active_next_phase_class`, `current_live_route.active_next_phase_class`, and `next_action.phase_class`.

2. validator transition rule change needed
Replace the fail-closed `INF-FULL-07 -> IF-08` assumption with an explicit route-admission gate that can admit `INF-FULL-07 -> PURG-PRE` only when the operator-reviewed evidence pack exists.

3. ROADMAP_CANONICAL Transition Table row needed
Add an explicit row that documents the future `INF-FULL-07 | pass | PURG-PRE` route with its phase class, advance mode, and minimum deliverable.

4. ACTIVE_CONTEXT_STATE live route mutation needed
Only after schema and validator land, update `next_phase`, `active_next_phase`, `active_next_phase_class`, and route-consistency mirrors in a dedicated route-admission sync.

5. mirror sync needed
Update the derived mirrors and any route summary documents so they reflect the new live route without contradicting `ACTIVE_CONTEXT_STATE.json`.

6. tests needed
Add or extend unit tests and validator assertions for the admitted route, plus regression checks that candidate-only PURG-PRE artifacts no longer masquerade as the final route-admission packet.

7. CI green required
Require local validator pass, unit-test pass, push to `main`, and terminal green CI before any route-admission PASS is declared canonical.

8. rollback plan
If any route-admission patch introduces drift or false PASS behavior, revert the route-admission commit, restore `IF-08` as the preserved live route, rerun validator/tests, and require a new operator-reviewed attempt.
