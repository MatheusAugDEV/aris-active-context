## ARIS-CONTEXT-ACTIVE-TRACK-PHASE-RECONCILIATION — Active Track Phase Reconciliation Gate
- status: `artifact_reference_only_active_track_phase_reconciliation_ready_warn`
- reconciliation_class: `f21_canonical_f33_blocked_under_lab_governance`
- next_action_detected: `ARIS-CONTEXT-ACTIVE-TRACK-RESUME — Active Track Resume Gate`
- canonical_next_phase: `F21 — Context Source Access Policy & Untrusted Input Boundary`
- recommended_next_phase: `F21 — Context Source Access Policy & Untrusted Input Boundary`
- return_to_active_track_allowed: `True`
- f21_evidence_count: `5`
- f33_evidence_count: `3`
- p29_closure_verified: `True`
- f32_closure_verified: `True`
- f33_blocked: `True`

P29 is closed, F32 is formally closed, F33 remains paused under Lab governance, and the active track continues at F21.

## ARIS-CONTEXT-ROADMAP-CANONICAL-STATE — Roadmap Canonical State & Next Action Sanitization Gate
- status: `artifact_reference_only_roadmap_canonical_state_ready_warn`
- roadmap_class: `f21_canonical_f33_blocked_under_lab_governance`
- p29_closed: `True`
- active_track_resume_verified: `True`
- f21_state: `pending`
- f21_is_stale_next_action: `False`
- f32_state: `closed`
- f32_closure_verified: `True`
- f33_state: `blocked`
- f33_blocked: `True`
- f33_allowed_next: `False`
- canonical_next_phase: `F21 — Context Source Access Policy & Untrusted Input Boundary`
- canonical_next_phase_title: `Context Source Access Policy & Untrusted Input Boundary`
- next_action_repair_required: `True`
- next_action_single_forward_pointer: `True`
- ledger_history_preserved: `True`
- manual_selection_required: `False`

P29 remains closed, F32 remains formally closed, F33 remains blocked under Lab governance, and NEXT_ACTION is sanitized to a single forward pointer.
