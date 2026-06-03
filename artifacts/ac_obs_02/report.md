# AC-OBS-02 — ARIS Active-Context Observability & Drift Prevention Gate

**Decision:** pass
**Previous phase:** AC-REPAIR-01
**Next phase:** null (no next phase opened, suggested, or named)
**Gate budget:** gate_cycles_used=0 / gate_max_cycles=3, opened 2026-06-03

## Intent

Structural hardening and residue cleanup only. Zero execution, zero fixture, zero bot, zero runtime mutation.

## What changed

### Task 1 — Mirror sync enforcement
- Created `scripts/assert_mirror_sync.py`, asserting that CURRENT_STATE.md, NEXT_ACTION.md, and DECISION_LOCKS.md carry the canonical values from ACTIVE_CONTEXT_STATE.json.

### Task 2 — Gate TTL
- Added `gate_opened_at`, `gate_max_cycles`, `gate_cycles_used` to ACTIVE_CONTEXT_SCHEMA.json and ACTIVE_CONTEXT_STATE.json.
- The validator blocks with `BLOCK: gate cycle budget exhausted. Operator must close or extend.` when `gate_cycles_used >= gate_max_cycles`.
- Added `REGRA DE CICLO DE GATE` to MANDATORY_READ_FIRST_RULES.md.

### Task 3 — Auto-advance for governance phases
- Added the `auto_advance` object to schema and state (`enabled`, `allowed_phase_classes`, `blocked_phase_classes`, `condition`).
- Added `REGRA DE AUTO-ADVANCE` to MANDATORY_READ_FIRST_RULES.md.

### Task 4 — CI self-verification
- Added `POST-COMMIT VERIFICATION` to PROMPT_CONTRACT.md. The model never self-reports PASS; the CI reports PASS.

### Task 5 — Boot read receipt
- Added `last_boot_files_read: []` to ACTIVE_CONTEXT_STATE.json.
- The validator warns (does not block) when the receipt is missing canonical boot files.

### Task 6 — Residue cleanup
- `git mv` of LAB_STATUS.md, LAB_VERDICTS.md, PROJECT_CONTEXT_ARIS.md, ARIS_ROADMAP_R0_F120.md into `archive/`.
- Pruned those files from mandatory read lists (MANDATORY_READ_FIRST_RULES.md, PROMPT_CONTRACT.md) and noted them in READ_PROFILE.md as historical-only.
- Removed CONTEXT_INDEX.md from the BOOT_PROFILE.md mandatory boot order.
- Converted ARIS_PHASE_LEDGER.md to append-only one-line-per-phase format.

### Task 7 — State update
- `current_phase_id=AC-OBS-02`, `previous_phase_id=AC-REPAIR-01`, `gate_opened_at=2026-06-03`, `gate_max_cycles=3`, `gate_cycles_used=0`, `next_phase=null`, `next_phase_authorized_by_operator=false`, `last_boot_files_read=[]`.

## Safety attestation

No runtime, frontend, audio, action-runtime, provider, network, secret, or dependency mutation. No fixtures materialized. No real execution. No bot activation. No Bedrock PASS and no product promotion. The only network scope remains GitHub active-context governance.

## CI

The exact validate-active-context run URL and conclusion for this commit are recorded in the operator-facing final report. `decision.json.ci_run_url` points to the branch-main runs for the workflow.
