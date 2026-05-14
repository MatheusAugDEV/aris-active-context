# aris-active-context

Compact, read-first ARIS context entrypoint.

Read order:

1. `CURRENT_STATE.md`
2. `NEXT_ACTION.md`
3. `DECISION_LOCKS.md`
4. `ARIS_PHASE_LEDGER.md`
5. `CONTEXT_INDEX.md`
6. `OPERATOR_PREFERENCES.md`
7. `PROMPT_CONTRACT.md`

Current snapshot:

- Official V6 is closed.
- F33.P-BEDROCK passed on artifact/evidence only; F33.Q is the active next action under the Lab contract and product promotion remains blocked.
- Latest completed phase: `F33.Y-AUTH-H — Schema Materialization Pre-Apply Human Authorization Evidence Intake`
- F33.P-BEDROCK consolidated the controlled SQLite dry-run chain and confirmed the residue continuity boundary.
- Next principal phase: `F33.Y-AUTH-SUBMIT — Schema Materialization Pre-Apply Human Authorization Evidence Submission`
- F33.P-BEDROCK passed on artifact/evidence only; F33.Q is the active next action under the Lab contract and product promotion remains blocked.
- F44 interpretation: `hardening/maturity of existing Lab`

Rules:

- Query-first, no bulk-read, no network, no dependency installs, no real MCP activation, no secret reads.
- `CURRENT_STATE.md`, `NEXT_ACTION.md`, and `DECISION_LOCKS.md` are the operational sources of truth.
- Historical depth belongs in `ARIS_PHASE_LEDGER.md`.
- F33.W completed the boundary finalization planning package and F33.W-AUTH-RC — Schema Materialization Human Authorization Review Closure Gate is the active next action under the Lab contract.

- F33.W-AUTH completed as an authorization gate only; human_authorization_found=False; human_authorization_valid=False; authorization_required=True

- F33.W-AUTH-H completed as an evidence intake gate only; final_authorization_statement_found_before_intake=False; placeholder_created=True; placeholder_valid=False; ready_for_next_review=True

- F33.W-AUTH-SUBMIT completed as submission-check only; final_authorization_statement_found=False; operator_submission_found=False; ready_for_review=False

- F33.W-AUTH-SUBMIT-HOLD completed as hold-only evidence capture; final_authorization_statement_found=True; operator_submission_found=True; ready_for_review=True; operator_submission_hash=`5db82b72f3761d835dcf00369c5842463d7887808799335d264717b9e10ec01c`

- F33.W-AUTH-R completed as review-only evidence validation; human_authorization_valid=True; human_authorization_granted=True; ready_for_next_phase=True; authorization_file_hash=`5db82b72f3761d835dcf00369c5842463d7887808799335d264717b9e10ec01c`

- F33.W-AUTH-RC completed as closure-only evidence consolidation; authorization_review_closed=True; human_authorization_validated=True; ready_for_next_phase=True; authorization_file_hash=`5db82b72f3761d835dcf00369c5842463d7887808799335d264717b9e10ec01c`

- F33.X completed as readiness planning-only; authorization_review_closure_verified=True; schema_materialization_plan_verified=True; ready_for_next_phase=True; schema_materialization_allowed_now=False; decision_hash=`2b9ddbd5f20f8297f2b588d8f75ac556378edc05c9a5890721a96546dd4e772c`

- F33.X-R completed as readiness review-only; f33x_status_verified=True; readiness_plan_reviewed=True; review_passed=True; ready_for_next_phase=True; schema_materialization_allowed_now=False; decision_hash=`5b7f2df0662ff68d6963ca124c81b4af19286a8e376fc0bf727e3aa4641adf6b`

- F33.X-AUTH completed as readiness authorization gate only; human_authorization_found=False; human_authorization_valid=False; authorization_required=True; ready_for_next_phase=False; next_phase_recommendation=`F33.X-AUTH-H — Schema Materialization Readiness Human Authorization Evidence Intake`

- F33.X-AUTH-H — Schema Materialization Readiness Human Authorization Evidence Intake completed as evidence intake only; final authorization remains manual and absent by design.

- F33.X-AUTH-SUBMIT completed as submission-check only; final_authorization_statement_found=True; operator_submission_found=True; ready_for_review=True; authorization_file_hash=`a7eaa11510e6686cfc3af13b30c73fe9718ac3ed73c487df33d0be8bad0949ab`; authorization_file_size_bytes=2950

- F33.X-AUTH-R completed as review-only validation; human_authorization_found=True; human_authorization_valid=True; human_authorization_granted=True; authorization_scope_limited_to_next_gate=True; authorization_file_hash=`a7eaa11510e6686cfc3af13b30c73fe9718ac3ed73c487df33d0be8bad0949ab`; authorization_file_size_bytes=2950

- F33.X-AUTH-RC completed as closure-only evidence consolidation; authorization_review_closed=True; human_authorization_validated=True; ready_for_next_phase=True; authorization_file_hash=`a7eaa11510e6686cfc3af13b30c73fe9718ac3ed73c487df33d0be8bad0949ab`

- F33.Y completed as pre-apply planning only; source_chain_verified=True; manual_authorization_w_unchanged=True; manual_authorization_x_unchanged=True; ready_for_next_phase=True; decision_hash=`b9e430884ed3c5f50e301fc289269868e24f79413c995769dde6c74311ffab6e`

- F33.Y-R completed as pre-apply review only; planning_verified=True; review_passed=True; ready_for_next_phase=True; decision_hash=`5d79ced85b43d3f3ee8d1c7e331c59961e4cd7d381de480af6751342a87a6f79`

- F33.Y-R completed as pre-apply review only; planning_verified=True; review_passed=False; ready_for_next_phase=False; decision_hash=`917ffc96446e01b0a2456bc002336d8218cec21410d6e0e7eb7d38734b38f1a8`

- F33.Y-R completed as pre-apply review only; planning_verified=True; review_passed=False; ready_for_next_phase=False; decision_hash=`fa99586bb23a90f40b2139e2777c8be9ffe09ee46c447d823fa0a3c2c199dc7a`

- F33.Y-AUTH completed as authorization-only gate; human_authorization_found=False; human_authorization_valid=False; human_authorization_granted=False; authorization_required=True; authorization_file_hash=``; authorization_file_size_bytes=0

- F33.Y-AUTH-H — Schema Materialization Pre-Apply Human Authorization Evidence Intake completed as evidence intake only; final authorization remains manual and absent by design.
