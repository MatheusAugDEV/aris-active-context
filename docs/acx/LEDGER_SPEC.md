# ACX Ledger Spec

## 1. Status and Scope

This document is specification-only for ACX-R2A.
It does not create runtime authority.
It does not create a ledger file.
It does not implement tools/acx.py.
It does not change enforcement.

The purpose of this spec is to freeze the future ledger model before any enforcement code exists.
It defines the minimum event contract, genesis rule, canonical serialization, naming, and migration authority boundaries that future implementation phases must follow.
Evidence artifacts committed inside the same commit MUST NOT claim to contain the final SHA of the commit that contains them; that SHA is post-commit evidence and must be reported externally or in a subsequent verification artifact.

## 2. Authority During Migration

During ACX-R2A and ACX-R2B, ACTIVE_CONTEXT_STATE.json remains the only live canonical source.
The ledger is shadow/audit-only until a later hardening phase proves fold equivalence and the operator authorizes authority change.
Markdown mirrors remain derived/non-authoritative when conflicting with JSON.

If a Markdown mirror disagrees with ACTIVE_CONTEXT_STATE.json, the JSON wins and the mirror is treated as drift.
No R2A or R2B document may elevate a derived mirror above the JSON state file.

## 3. Genesis Decision

The JSON state currently validated in ACTIVE_CONTEXT_STATE.json is the point of genesis for the future ledger.
The genesis event declares the current fold as the initial baseline.
Historical entries that conflict in DECISION_LOCKS.md, especially those related to IF09-FIND-001, are classified as historical_only.
Nothing in DECISION_LOCKS.md is rewritten, deleted, or edited in this phase.
The ledger starts by recognizing the current validated state, not by reconstructing every historical markdown lock line by line.

Genesis resolution:
- baseline source: ACTIVE_CONTEXT_STATE.json
- baseline policy: use the current validated state as the genesis baseline
- historical lock policy: preserve conflicting markdown history as historical_only
- IF09-FIND-001: keep the canonical JSON resolution as the baseline and treat contradictory lock text as historical evidence only

## 4. Event Model

Minimum conceptual event schema:

```json
{
  "event_id": "uuid",
  "event_type": "enum",
  "event_schema_version": "string",
  "phase_id": "string|null",
  "timestamp_utc": "string",
  "project_commit_sha": "string",
  "state_blob_hash": "string|null",
  "ledger_head_hash": "string|null",
  "payload": {},
  "prev_sha256": "string|null",
  "event_sha256": "string",
  "hash_algorithm": "sha256",
  "canonicalization_version": "string"
}
```

Field classes:
- Metadata: event_id, event_type, event_schema_version, phase_id, timestamp_utc, project_commit_sha, hash_algorithm, canonicalization_version
- Chain fields: prev_sha256, ledger_head_hash
- Derived fields: state_blob_hash, event_sha256
- Typed payload: payload

Hash rule:
- event_sha256 is computed from the canonical serialization of the event with event_sha256 excluded from its own hash input.
- timestamp_utc is written once at append time and hashed as the stored literal string.
- timestamp_utc is never regenerated during verification, so future wall-clock drift cannot change a recorded event hash.

## 5. Event Types

### genesis
- Purpose: establish the initial ledger baseline from the current validated JSON state.
- Minimum payload: baseline source, baseline policy, and genesis rationale.
- Alters derived state: yes.
- Shadow mode: yes.
- Main risk: anchoring the wrong baseline.

### phase_open
- Purpose: record that a phase has been opened or made active in ledger form.
- Minimum payload: phase_id, opener authority, and opening rationale.
- Alters derived state: yes.
- Shadow mode: yes.
- Main risk: unauthorized or premature phase activation.

### phase_close
- Purpose: record that a phase has been closed.
- Minimum payload: phase_id, close rationale, and closing evidence references.
- Alters derived state: yes.
- Shadow mode: yes.
- Main risk: premature close or false closure.

### transition
- Purpose: record a controlled move from one phase to another.
- Minimum payload: from_phase_id, to_phase_id, authority, and transition rationale.
- Alters derived state: yes.
- Shadow mode: yes.
- Main risk: route drift or skipped transition rules.

### rollback_compensating
- Purpose: record a compensating event that reverses the effect of an earlier event without deleting history.
- Minimum payload: target_event_id, compensation rationale, and resulting state delta.
- Alters derived state: yes.
- Shadow mode: yes.
- Main risk: incomplete compensation that leaves the fold inconsistent.

### violation_advisory
- Purpose: record a detected rule violation without claiming enforcement authority.
- Minimum payload: violated rule, severity, and supporting evidence.
- Alters derived state: no.
- Shadow mode: yes.
- Main risk: advisory text being mistaken for enforcement.

### manual_repair
- Purpose: record a human-directed repair action and its evidence.
- Minimum payload: original defect, repair action, and verification evidence.
- Alters derived state: yes when later accepted into replay, but in R2A it is shadow-only and not enforcement-bearing.
- Shadow mode: yes.
- Main risk: repair history being confused with automatic authority.

## 6. Canonical Hash Serialization

Canonical serialization rules are closed and explicit:
- JSON sort_keys=True
- UTF-8
- LF newline only
- no CRLF
- relative POSIX paths only
- no OS-specific path separator
- no volatile wall-clock field inside recomputed payload hash
- no derived render counters in hashed payload
- event_sha256 is excluded from its own hash input
- hash_algorithm is explicit
- canonicalization_version is explicit
- stable separators: comma and colon without whitespace

Serialization rule for timestamp_utc:
- timestamp_utc is stored in the event record as the append-time literal string.
- the verifier reserializes the stored value exactly as recorded.
- the verifier never substitutes a fresh clock value for a stored timestamp.

## 7. Required Naming

The ledger and future tooling must use these names exactly:
- state_blob_hash
- project_commit_sha
- ledger_head_hash

The name sha_lido must not be reintroduced.
It is prohibited because it is ambiguous about whether the value is the state blob hash or the project commit hash.

## 8. Fold Semantics

Fold is a deterministic replay of the ledger.
In R2B, fold must reproduce STATE in a golden fixture with diff zero.
While fold has not proven equivalence, it has no authority.
Fold must never depend on filesystem order, locale, timezone, or the current clock.

## 9. Verify-Chain Semantics

verify-chain recalculates event_sha256 for each event.
It confirms prev_sha256 continuity from event to event.
A broken link invalidates the chain from the point of break onward.
The property is tamper-evident, not tamper-proof.
Shadow mode only observes and reports; it does not block.

## 10. Rollback Semantics

Rollback does not delete events.
Rollback is represented by a new event of type rollback_compensating.
The ledger remains append-only.
Reversal of state is modeled as a new compensating mutation, not as history deletion.

## 11. Non-Goals

R2A does not provide:
- runtime ledger in R2A
- CLI in R2A
- hook in R2A
- CI enforcement in R2A
- schema bump in R2A
- any attempt to reconstruct all historical markdown or lock history
- cryptographic signature in R2A
- SLSA
- Sigstore
- OPA
- Temporal dependency

## 12. R2B Implementation Boundary

Only R2B may implement the following runtime surfaces:
- tools/acx.py event append
- tools/acx.py fold
- tools/acx.py verify-chain
- golden fixture test
- shadow ledger file

Even in R2B, these surfaces remain non-hard-enforcement until a later hardening phase explicitly upgrades authority.

## 13. Open Questions

NONE
