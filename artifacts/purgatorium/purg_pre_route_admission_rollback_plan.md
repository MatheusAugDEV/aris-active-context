If route admission creates drift:
1. revert route admission commit;
2. restore active_next_phase/next_phase to IF-08;
3. restore active_next_phase_class to infernus_full_execution;
4. restore schema enum if necessary;
5. restore validator expected route;
6. rerun json.tool, validator, unittest, mirror sync;
7. push rollback commit;
8. CI terminal green;
9. report CANONICAL_ROUTE_ADMISSION_ROLLBACK_COMPLETE.
