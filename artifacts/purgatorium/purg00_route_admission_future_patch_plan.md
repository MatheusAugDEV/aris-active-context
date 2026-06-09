PATCH PLAN ONLY — DO NOT APPLY IN THIS PHASE

1. Add purgatorium_full_intake to schema live-route phase-class enums.
2. Add ROADMAP_CANONICAL Transition Table row for PURG-PRE | pass | PURG-00.
3. Add validator route rule for PURG-PRE -> PURG-00.
4. Add artifact requirements for PURG-00 route admission.
5. Mutate ACTIVE_CONTEXT_STATE.json only in a dedicated route-admission phase.
6. Update mirrors.
7. Add tests preventing PURG-00 pass without IF10 graph details.
8. Preserve all no-real-exec locks.
9. CI terminal green required.
10. Rollback restores PURG-PRE as live route.
