# PURG-00 Route Admission Rollback Plan

If PURG-00 route admission creates drift:
- restore active_next_phase/next_phase to PURG-PRE;
- restore active_next_phase_class to purgatorium_full_authority_materialization;
- restore validator expected route;
- restore mirror references to the pre-admission live route;
- report PURG00_ROUTE_ADMISSION_ROLLBACK_COMPLETE.
