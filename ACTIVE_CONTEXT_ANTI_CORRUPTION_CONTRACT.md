# ARIS Active Context Anti-Corruption Contract

This document defines the canonical anti-corruption architecture for the ARIS active-context system.
It governs how any agent (ChatGPT, Claude, Codex, or human) must read, validate, and update the active context.

ACTIVE_CONTEXT_STATE.json is always the canonical source. This file is a reference contract, not an authority file.
If this file contradicts ACTIVE_CONTEXT_STATE.json, ACTIVE_CONTEXT_STATE.json wins.

---

## 1. Canonical Source (Single Source of Truth)

| File | Role |
|---|---|
| `ACTIVE_CONTEXT_STATE.json` | **Only canonical live state.** Always read first. Always wins over Markdown. |
| `ACTIVE_CONTEXT_SCHEMA.json` | Validation contract for the live state. Read second. |
| `scripts/validate_active_context_state.py` | Anti-corruption validator. Run before any decision. |
| `ROADMAP_CANONICAL.md` | Roadmap sequence authority (not live state). |
| `ARIS_PHASE_LEDGER.md` | Historical ledger only (not live state). |
| Markdown mirrors | Derived, non-authoritative. Confirm JSON; never supersede it. |

---

## 2. File Taxonomy

| Category | Files | Authority |
|---|---|---|
| **Live state** | `ACTIVE_CONTEXT_STATE.json` | Single source of truth |
| **Validation contract** | `ACTIVE_CONTEXT_SCHEMA.json`, `scripts/validate_active_context_state.py` | Enforce live state integrity |
| **Derived mirrors** | `CURRENT_STATE.md`, `NEXT_ACTION.md`, `DECISION_LOCKS.md`, `CONTEXT_INDEX.md`, `README.md` | Confirm JSON; blocked if they contradict JSON |
| **Roadmap authority** | `ROADMAP_CANONICAL.md` | Phase sequence only; live routing from JSON |
| **Historical ledger** | `ARIS_PHASE_LEDGER.md` | Historical evidence only |
| **Governance contracts** | `BOOT_PROFILE.md`, `MANDATORY_READ_FIRST_RULES.md`, `PROMPT_CONTRACT.md` | Operational rules; must not supersede JSON |
| **Lab control plane** | `LAB_OPERATING_CONTRACT.md`, `LAB_STATUS.md`, `LAB_VERDICTS.md` | Lab governance; read after JSON |

---

## 3. Mandatory Read Order

Every agent and human must follow this order:

```
1. ACTIVE_CONTEXT_STATE.json          ← ALWAYS FIRST. No exceptions.
2. ACTIVE_CONTEXT_SCHEMA.json
3. python3 scripts/validate_active_context_state.py   ← must pass before any decision
4. Markdown mirrors as needed (read-only, confirmatory)
5. Lab files as needed
6. Governance contracts as needed
```

**Violation**: Reading any Markdown file before the JSON is an anti-corruption violation. Block the decision.

---

## 4. Agent Consultation Protocol (ChatGPT / Codex / Claude / any LLM)

### 4.1 Read Protocol

1. Fetch `ACTIVE_CONTEXT_STATE.json` from GitHub main.
2. Validate against `ACTIVE_CONTEXT_SCHEMA.json`.
3. Run `scripts/validate_active_context_state.py`. If it fails, report the drift and **do not make a routing decision**.
4. Read only the Markdown mirrors needed for the decision.
5. If any Markdown file contradicts the JSON, trust the JSON and report the drift.
6. Never use Markdown as a live routing authority.

### 4.2 Update Protocol

1. **Update `ACTIVE_CONTEXT_STATE.json` first.** Never update Markdown before the JSON.
2. Update `ACTIVE_CONTEXT_SCHEMA.json` only if the schema structure changes.
3. Update all required Markdown mirrors to reflect the JSON.
4. Update `ARIS_PHASE_LEDGER.md` with the new historical entry.
5. Run `python3 -m json.tool ACTIVE_CONTEXT_STATE.json` (must pass).
6. Run `python3 -m json.tool ACTIVE_CONTEXT_SCHEMA.json` (must pass).
7. Run `python3 scripts/validate_active_context_state.py` (must pass).
8. Commit all changes in a single atomic commit.
9. Push to the designated branch.
10. Verify merge to GitHub main.
11. Report the final commit hash.
12. **Without GitHub main verification, there is no canonical PASS.**

---

## 5. Drift Classification and Response

| Drift Type | Response |
|---|---|
| Markdown contradicts JSON | Trust JSON. Report drift. Block Markdown-based decision. |
| JSON field missing from schema | Block. Schema and state must stay in sync. |
| Extra property in state (not in schema) | Block. `additionalProperties: false` is enforced. |
| Cross-field inconsistency in JSON | Block. Run validator. Fix before any decision. |
| Missing required transition file | Block. All files in `required_files_for_transition` must exist. |
| Missing artifact route (unclassified) | Block. Classify in `artifact_integrity_policy` or fix. |
| Local state not verified against GitHub main | Non-canonical. Do not use for decisions. |
| Governance contract reads Markdown before JSON | Block. All contracts must declare JSON-first. |

---

## 6. Artifact Integrity Policy

Phase-specific artifacts (in `artifacts/lab_simulation/`) are **external to this governance repository**.
They live in the ARIS project workspace. Their absence from this repo is not a blocking error — they are classified as `external_to_active_context_repo` in `artifact_integrity_policy` in the JSON state.

Governance artifacts (state, schema, validator, mirrors) **must exist locally** and are checked by the validator.

---

## 7. How to Handle Missing Files

| Situation | Action |
|---|---|
| Required transition file missing | Block. Create or restore the file before any transition. |
| Validator script missing | Block. Restore from git history. |
| Schema file missing | Block. Restore from git history. |
| Markdown mirror missing | Block. Regenerate from JSON. |
| External artifact missing | Check `artifact_integrity_policy`. If classified, not blocking. If unclassified, block. |

---

## 8. Push / GitHub Verification Failure Protocol

1. Do not declare a canonical PASS without GitHub verification.
2. If push fails: retry with exponential backoff (2s, 4s, 8s, 16s, max 4 retries).
3. If network is unavailable: mark local state as `local_checkout_is_non_canonical_until_remote_verified: true`. Do not make routing decisions from unverified local state.
4. If GitHub main diverged: fetch, inspect diff, resolve conflict in the JSON first, then update mirrors, then commit and push again.

---

## 9. Local vs GitHub Main Conflict Resolution

1. Fetch GitHub main.
2. Compare `ACTIVE_CONTEXT_STATE.json` field by field.
3. The version with the higher `latest_completed_phase` in the canonical phase sequence is the authoritative state, unless explicitly overridden by the operator.
4. Resolve in the JSON first. Then update mirrors. Then validate. Then push.

---

## 10. Versioning Contract

| Field | Meaning | Increment when |
|---|---|---|
| `active_context_version` | Governance model version | Canonical architecture changes fundamentally |
| `schema_version` | Validation contract version | Schema field set, constraints, or new required fields change |

Current: `active_context_version: "2.0"`, `schema_version: "2.1"`.
Schema v2.1: structural and evolutionary (not snapshot). Const only for permanent invariants.

---

## 11. Atomic Transition Protocol

A phase transition is atomic. All of the following must succeed or the transition is rolled back:

1. JSON state updated (`ACTIVE_CONTEXT_STATE.json`).
2. Schema updated if needed (`ACTIVE_CONTEXT_SCHEMA.json`).
3. All Markdown mirrors updated.
4. Ledger updated (`ARIS_PHASE_LEDGER.md`).
5. Validator passes (`scripts/validate_active_context_state.py`).
6. Single commit with all files.
7. Push succeeds.
8. GitHub main verified.

If any step fails, do not declare the transition complete.

---

## 12. Planning-Only Gate Protocol

When `active_next_phase_class == "planning_gate"`:
- `next_action.planning_only` must be `true`.
- `next_action.execution_authorization` must be `false`.
- All dangerous authorization flags must be `false`.
- The gate produces a plan artifact only.
- No runtime execution, no real apply, no real dry-run is authorized by this gate alone.
