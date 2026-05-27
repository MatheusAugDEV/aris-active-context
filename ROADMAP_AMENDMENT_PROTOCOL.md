# Roadmap Amendment Protocol

## Purpose
This file defines how ARIS may change the canonical roadmap without breaking governance, auditability, or historical continuity.

## Amendment Authority
- Amendment authority is gated, not implicit.
- No single prompt, chat answer, memory fragment, or commit message may mutate the active roadmap by itself.
- Canonical roadmap change requires an explicit review gate with materialized evidence.

## Mandatory Amendment Gate
Any roadmap amendment must pass a dedicated amendment gate before the change becomes active.

The mandatory gate must confirm:
- scope of the proposed roadmap change
- reason for the change
- compatibility with current active state
- compatibility with existing locks
- compatibility with preserved history
- impact on next active phase routing

## Required Artifact Package
Every roadmap amendment requires:
- decision artifact
- summary/report artifact
- drift check
- ledger note
- updated active-context routing if the amendment is approved

## Required Decision Fields
At minimum, the decision artifact must state:
- current canonical roadmap authority
- proposed change
- rationale
- affected phases or macroblocks
- migration impact
- preserved historical files
- non-authorizations preserved
- final decision

## Drift Check
A drift check is mandatory before and after any amendment.

The drift check must confirm:
- active files agree on the same next direction
- no stale route remains in active slots
- no silent promotion of historical material occurred
- no active file claims a pass retroactively without evidence

## Ledger Requirement
A ledger note is mandatory for every approved or rejected amendment.

The ledger note must record:
- amendment phase name
- status
- decision
- source artifact paths
- historical preservation action
- next canonical routing

## Prohibited Actions
- silent roadmap mutation is forbidden
- retroactive pass claims are forbidden
- destructive overwrite of preserved historical roadmap files is forbidden
- deletion of superseded evidence files without a separate audit-safe gate is forbidden
- using historical overlays as active roadmap authority without explicit reactivation is forbidden

## Historical Preservation Rule
When roadmap direction changes:
- preserve older roadmap files as historical audit trail
- mark them as `historical_only`, `superseded`, or `removed_from_active_direction` as appropriate
- prefer tombstones or explicit non-authoritative status over destructive replacement

## Activation Rule
An amendment becomes active only when:
- the dedicated amendment gate passes
- the decision artifact exists
- the summary/report exists
- the drift check passes
- the ledger note is written
- active-context routing files are updated coherently

## Non-Authorization
This protocol does not authorize:
- runtime mutation
- frontend mutation
- voice or audio mutation
- action runtime mutation
- backend mutation
- network use
- dependency installation
- pilot, customer, or commercial use
