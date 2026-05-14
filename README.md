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
- Latest completed phase: `F33.W-AUTH-SUBMIT-HOLD — Schema Materialization Human Authorization Awaiting Human Input`
- F33.P-BEDROCK consolidated the controlled SQLite dry-run chain and confirmed the residue continuity boundary.
- Next principal phase: `F33.W-AUTH-R — Schema Materialization Human Authorization Evidence Review Gate`
- F33.P-BEDROCK passed on artifact/evidence only; F33.Q is the active next action under the Lab contract and product promotion remains blocked.
- F44 interpretation: `hardening/maturity of existing Lab`

Rules:

- Query-first, no bulk-read, no network, no dependency installs, no real MCP activation, no secret reads.
- `CURRENT_STATE.md`, `NEXT_ACTION.md`, and `DECISION_LOCKS.md` are the operational sources of truth.
- Historical depth belongs in `ARIS_PHASE_LEDGER.md`.
- F33.W completed the boundary finalization planning package and F33.W-AUTH-R — Schema Materialization Human Authorization Evidence Review Gate is the active next action under the Lab contract.

- F33.W-AUTH completed as an authorization gate only; human_authorization_found=False; human_authorization_valid=False; authorization_required=True

- F33.W-AUTH-H completed as an evidence intake gate only; final_authorization_statement_found_before_intake=False; placeholder_created=True; placeholder_valid=False; ready_for_next_review=True

- F33.W-AUTH-SUBMIT completed as submission-check only; final_authorization_statement_found=False; operator_submission_found=False; ready_for_review=False

- F33.W-AUTH-SUBMIT-HOLD completed as hold-only evidence capture; final_authorization_statement_found=True; operator_submission_found=True; ready_for_review=True; operator_submission_hash=`5db82b72f3761d835dcf00369c5842463d7887808799335d264717b9e10ec01c`
