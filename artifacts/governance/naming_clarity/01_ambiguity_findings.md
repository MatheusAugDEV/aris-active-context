# Naming Ambiguity Findings

Total phase_id entries audited from `DECISION_LOCKS.md`: **51**.

Live-route facts preserved during this audit:
- `phase_id=current_phase_id=IF09_CLOSURE_MILESTONE_MIRROR_SANITY_PACKET` remains authoritative.
- `INF_REVALIDATION_ADJUDICATION_OR_CLOSURE_PACKET` remains the immediately previous canonical phase.
- `next_phase=null` and `active_next_phase=null` remain unchanged.

## Priority finding

### IF09_CLOSURE_MILESTONE_MIRROR_SANITY_PACKET
- Classification: `ambiguous_reuse`
- Why it confuses: the phase happens **after** `INF_REVALIDATION_ADJUDICATION_OR_CLOSURE_PACKET`, but its identifier reuses `IF09`, which already refers historically to the original `IF-09 Evidence Bundle + Vulnerability Register` track.
- Suggested `display_name`: `Post-Revalidation Mirror Sanity Packet`
- Supporting history: `IF-09` appears in `DECISION_LOCKS.md` line 628, while the later post-revalidation phase appears at line 15 and in the active state.

## Additional findings

### BENCHUX_ROUTE_OPENING_PACKET
- Classification: `confusing_but_unique`
- Why it confuses: Uses BENCHUX spelling while the tracked candidate program in schema/state is BENCHUIX-xx, creating near-duplicate family names for the same macro track.
- Suggested `display_name`: `BenchUIX Route Opening Packet Candidate`
- First DECISION_LOCKS occurrence: line 27 under `IF09 Closure Milestone Mirror Sanity Packet`
- Cross-file presence: ROADMAP lines 189; ACTIVE_CONTEXT_STATE lines 702

### IF-08
- Classification: `confusing_but_unique`
- Why it confuses: The parent label uses IF-08 with a hyphen, while the child wave packets use IF08_W* without the hyphen and with mixed zero-padding.
- Suggested `display_name`: `IF-08 Parent Wave Program`
- First DECISION_LOCKS occurrence: line 694 under `IF-08 W6 Final Audit Controlled Execution Lock`
- Cross-file presence: ROADMAP lines 256; ACTIVE_CONTEXT_STATE lines 620, 746

### IF-09
- Classification: `confusing_but_unique`
- Why it confuses: The original IF-09 human phase label remains in history while a later live phase_id reuses IF09 for a post-revalidation mirror-sanity packet.
- Suggested `display_name`: `Original IF-09 Evidence Bundle And Vulnerability Register`
- First DECISION_LOCKS occurrence: line 628 under `IF-09 Evidence Bundle + Vulnerability Register Lock`

### IF08_W05
- Classification: `confusing_but_unique`
- Why it confuses: Wave 05 is represented both as IF08_W05 and IF08_W5 in the same historical family, which weakens scanability and ordering clarity.
- Suggested `display_name`: `IF-08 Wave 05 Canonical Sync Lock`
- First DECISION_LOCKS occurrence: line 1147 under `IF08_W05 Controlled Execution Canonical Sync Lock`

### IF08_W5
- Classification: `confusing_but_unique`
- Why it confuses: Wave 05 is represented both as IF08_W05 and IF08_W5 in the same historical family, which weakens scanability and ordering clarity.
- Suggested `display_name`: `IF-08 Wave 05 Business Chaos`
- First DECISION_LOCKS occurrence: line 772 under `IF08_W5 Business Chaos Controlled Execution Lock`

### INF-FULL-07
- Classification: `confusing_but_unique`
- Why it confuses: Historical mirrors repeatedly narrate INF-FULL-07 as IF-11 Minos Final Verdict + Closure, so the authoritative phase_id and the human ordinal label diverge.
- Suggested `display_name`: `Infernus FULL 07 / IF-11 Minos Final Verdict Closure`
- First DECISION_LOCKS occurrence: line 315 under `ARIS Macro Roadmap Canonicalization (Camadas e Objetivos)`
- Cross-file presence: ROADMAP lines 256, 257; ACTIVE_CONTEXT_STATE lines 619, 746

### PURG-01
- Classification: `confusing_but_unique`
- Why it confuses: The canonical PURG-01 route is surrounded by human subsection labels PURG-01.1 and PURG-01.2, which look phase-like but are not canonical phase_ids.
- Suggested `display_name`: `Canonical PURG-01 Route Phase`
- First DECISION_LOCKS occurrence: line 333 under `PURG-01 Stale Next-Step Reconciliation`
- Cross-file presence: ROADMAP lines 56, 198, 210, 211, 212, 213; ACTIVE_CONTEXT_STATE lines 419, 429, 440, 483, 753, 754

### PURG-04
- Classification: `confusing_but_unique`
- Why it confuses: The canonical PURG-04 route coexists with many PURG04_* packet identifiers that drop the hyphen and overload the same number for sub-packets.
- Suggested `display_name`: `Canonical PURG-04 Route Phase`
- First DECISION_LOCKS occurrence: line 1337 under `PURG-04 IF09-FIND-001 S3 Local Remediation Plan Readiness`
- Cross-file presence: ROADMAP lines 56, 260

### PURG-05
- Classification: `confusing_but_unique`
- Why it confuses: The canonical PURG-05 route coexists with pre-opening packet identifiers under PURG05_*, which makes route-opened vs candidate packet states easy to misread.
- Suggested `display_name`: `Canonical PURG-05 Route Phase`
- First DECISION_LOCKS occurrence: line 2614 under `Purgatorium Post-PURG04 Route Decision Packet`
- Cross-file presence: ROADMAP lines 56

### PURG04_B1_B3_CLEANROOM_BASELINE_REPAIR_BLOCKER_TRIAGE
- Classification: `ambiguous_reuse`
- Why it confuses: Reuses the canonical PURG-04 route number for a post-PURG-04 packet namespace, so the packet can be mistaken for the canonical route node.
- Suggested `display_name`: `Post-PURG-04 B1 B3 Cleanroom Baseline Repair Blocker Triage`
- First DECISION_LOCKS occurrence: line 1942 under `PURG04 B1/B3 Cleanroom Baseline Repair Readiness Packet`

### PURG04_B1_B3_CLEANROOM_BASELINE_REPAIR_READINESS_PACKET
- Classification: `ambiguous_reuse`
- Why it confuses: Reuses the canonical PURG-04 route number for a post-PURG-04 packet namespace, so the packet can be mistaken for the canonical route node.
- Suggested `display_name`: `Post-PURG-04 B1 B3 Cleanroom Baseline Repair Readiness Packet`
- First DECISION_LOCKS occurrence: line 1897 under `Project_ARIS Cleanroom External Context Pointer Repair`

### PURG04_B1_B3_GLOBAL_BASELINE_REPAIR_PLAN_ARTIFACT_ONLY
- Classification: `ambiguous_reuse`
- Why it confuses: Reuses the canonical PURG-04 route number for a post-PURG-04 packet namespace, so the packet can be mistaken for the canonical route node.
- Suggested `display_name`: `Post-PURG-04 B1 B3 Global Baseline Repair Plan Artifact Only`
- First DECISION_LOCKS occurrence: line 1496 under `Active-Context No Ritual Authorization Policy Repair`

### PURG04_B1_B3_PROJECT_ARIS_BASELINE_REPAIR_WITH_OPERATOR_STANDING_DIRECTION
- Classification: `ambiguous_reuse`
- Why it confuses: Reuses the canonical PURG-04 route number for a post-PURG-04 packet namespace, so the packet can be mistaken for the canonical route node.
- Suggested `display_name`: `Post-PURG-04 B1 B3 Project Aris Baseline Repair With Operator Standing Direction`
- First DECISION_LOCKS occurrence: line 1645 under `PURG-04 Project_ARIS Worktree Contamination Blocker`

### PURG04_B2_ACTIVE_CONTEXT_PATH_CONTRACT_BOUNDARY_DECISION_ARTIFACT_ONLY
- Classification: `ambiguous_reuse`
- Why it confuses: Reuses the canonical PURG-04 route number for a post-PURG-04 packet namespace, so the packet can be mistaken for the canonical route node.
- Suggested `display_name`: `Post-PURG-04 B2 Active Context Path Contract Boundary Decision Artifact Only`
- First DECISION_LOCKS occurrence: line 1549 under `PURG-04 B2 Current State Path Diagnostic Plan Artifact-Only`

### PURG04_B2_ACTIVE_CONTEXT_PATH_CONTRACT_NORMALIZATION_PLAN_ARTIFACT_ONLY
- Classification: `ambiguous_reuse`
- Why it confuses: Reuses the canonical PURG-04 route number for a post-PURG-04 packet namespace, so the packet can be mistaken for the canonical route node.
- Suggested `display_name`: `Post-PURG-04 B2 Active Context Path Contract Normalization Plan Artifact Only`
- First DECISION_LOCKS occurrence: line 1583 under `PURG-04 B2 Active-Context Path Contract Boundary Decision Artifact-Only`

### PURG04_B2_ACTIVE_CONTEXT_PATH_CONTRACT_NORMALIZATION_REPAIR_ARTIFACT_ONLY
- Classification: `ambiguous_reuse`
- Why it confuses: Reuses the canonical PURG-04 route number for a post-PURG-04 packet namespace, so the packet can be mistaken for the canonical route node.
- Suggested `display_name`: `Post-PURG-04 B2 Active Context Path Contract Normalization Repair Artifact Only`
- First DECISION_LOCKS occurrence: line 1614 under `PURG-04 B2 Active-Context Path Contract Normalization Plan Artifact-Only`

### PURG04_B2_CURRENT_STATE_PATH_DIAGNOSTIC_PLAN_ARTIFACT_ONLY
- Classification: `ambiguous_reuse`
- Why it confuses: Reuses the canonical PURG-04 route number for a post-PURG-04 packet namespace, so the packet can be mistaken for the canonical route node.
- Suggested `display_name`: `Post-PURG-04 B2 Current State Path Diagnostic Plan Artifact Only`
- First DECISION_LOCKS occurrence: line 1520 under `PURG-04 B1 B3 Global Baseline Repair Plan Artifact-Only`

### PURG04_CLEANROOM_FRESH_RECLONE_PREREQUISITE_PACKET
- Classification: `ambiguous_reuse`
- Why it confuses: Reuses the canonical PURG-04 route number for a post-PURG-04 packet namespace, so the packet can be mistaken for the canonical route node.
- Suggested `display_name`: `Post-PURG-04 Cleanroom Fresh Reclone Prerequisite Packet`
- First DECISION_LOCKS occurrence: line 1989 under `PURG04 B1/B3 Cleanroom Baseline Repair Blocker Triage`

### PURG04_FOCUSED_FAILURE_SURFACE_CLASSIFICATION_PACKET
- Classification: `ambiguous_reuse`
- Why it confuses: Reuses the canonical PURG-04 route number for a post-PURG-04 packet namespace, so the packet can be mistaken for the canonical route node.
- Suggested `display_name`: `Post-PURG-04 Focused Failure Surface Classification Packet`
- First DECISION_LOCKS occurrence: line 2087 under `PURG04 Fresh Reclone Execution Packet`

### PURG04_FRESH_RECLONE_EXECUTION_PACKET
- Classification: `ambiguous_reuse`
- Why it confuses: Reuses the canonical PURG-04 route number for a post-PURG-04 packet namespace, so the packet can be mistaken for the canonical route node.
- Suggested `display_name`: `Post-PURG-04 Fresh Reclone Execution Packet`
- First DECISION_LOCKS occurrence: line 2039 under `PURG04 Cleanroom Fresh Reclone Prerequisite Packet`

### PURG04_GLOBAL_TEST_BASELINE_TRIAGE_ARTIFACT_ONLY
- Classification: `ambiguous_reuse`
- Why it confuses: Reuses the canonical PURG-04 route number for a post-PURG-04 packet namespace, so the packet can be mistaken for the canonical route node.
- Suggested `display_name`: `Post-PURG-04 Global Test Baseline Triage Artifact Only`
- First DECISION_LOCKS occurrence: line 1404 under `PURG-04 IF09-FIND-001 S3 Local Remediation Apply Result`

### PURG04_MIXED_SURFACE_REPAIR_SPLIT_PACKET
- Classification: `ambiguous_reuse`
- Why it confuses: Reuses the canonical PURG-04 route number for a post-PURG-04 packet namespace, so the packet can be mistaken for the canonical route node.
- Suggested `display_name`: `Post-PURG-04 Mixed Surface Repair Split Packet`
- First DECISION_LOCKS occurrence: line 2140 under `PURG04 Focused Failure Surface Classification Packet`

### PURG04_PROOF_LOOP_CORPUS_MATERIALIZATION_ARTIFACT_ONLY
- Classification: `ambiguous_reuse`
- Why it confuses: Reuses the canonical PURG-04 route number for a post-PURG-04 packet namespace, so the packet can be mistaken for the canonical route node.
- Suggested `display_name`: `Post-PURG-04 Proof Loop Corpus Materialization Artifact Only`
- First DECISION_LOCKS occurrence: line 2706 under `PURG04 Proof-Loop Corpus Materialization Readiness Packet`

### PURG04_PROOF_LOOP_CORPUS_MATERIALIZATION_READINESS_PACKET
- Classification: `ambiguous_reuse`
- Why it confuses: Reuses the canonical PURG-04 route number for a post-PURG-04 packet namespace, so the packet can be mistaken for the canonical route node.
- Suggested `display_name`: `Post-PURG-04 Proof Loop Corpus Materialization Readiness Packet`
- First DECISION_LOCKS occurrence: line 2668 under `PURG04 Proof-Loop Corpus Gap Diagnostic And Plan Artifact-Only`

### PURG04_PROOF_LOOP_CORPUS_MATERIALIZATION_RETRY_ARTIFACT_ONLY
- Classification: `ambiguous_reuse`
- Why it confuses: Reuses the canonical PURG-04 route number for a post-PURG-04 packet namespace, so the packet can be mistaken for the canonical route node.
- Suggested `display_name`: `Post-PURG-04 Proof Loop Corpus Materialization Retry Artifact Only`
- First DECISION_LOCKS occurrence: line 2978 under `PURG04 Proof-Loop Corpus Source Hash Manifest Divergence Repair Artifact-Only`

### PURG04_TRACK_A_MAIN_MERGE_EXECUTION
- Classification: `ambiguous_reuse`
- Why it confuses: Reuses the canonical PURG-04 route number for a post-PURG-04 packet namespace, so the packet can be mistaken for the canonical route node.
- Suggested `display_name`: `Post-PURG-04 Track A Main Merge Execution`
- First DECISION_LOCKS occurrence: line 2305 under `PURG04 Project_ARIS Main Moved Operator Decision Packet`
- Cross-file presence: ROADMAP lines 261, 262; ACTIVE_CONTEXT_STATE lines 761

### PURG04_TRACK_A_PATCH_REVIEW_AND_MERGE_DECISION
- Classification: `ambiguous_reuse`
- Why it confuses: Reuses the canonical PURG-04 route number for a post-PURG-04 packet namespace, so the packet can be mistaken for the canonical route node.
- Suggested `display_name`: `Post-PURG-04 Track A Patch Review And Merge Decision`
- First DECISION_LOCKS occurrence: line 2255 under `PURG04 Track A Pointer Residual Repair Patch Packet`
- Cross-file presence: ROADMAP lines 260, 261

### PURG04_TRACK_A_POST_MERGE_VALIDATION_PACKET
- Classification: `ambiguous_reuse`
- Why it confuses: Reuses the canonical PURG-04 route number for a post-PURG-04 packet namespace, so the packet can be mistaken for the canonical route node.
- Suggested `display_name`: `Post-PURG-04 Track A Post Merge Validation Packet`
- First DECISION_LOCKS occurrence: line 48 under `PURG Residual Risk Carry-Forward Admission Packet Artifact-Only`
- Cross-file presence: ROADMAP lines 262, 263; ACTIVE_CONTEXT_STATE lines 761

### PURG05_EVIDENCE_LEDGER_SIGNING_CUSTODY_PACKET
- Classification: `ambiguous_reuse`
- Why it confuses: Reuses the canonical PURG-05 route number for candidate/opening/admission packet namespaces before canonical PURG-05 is actually opened.
- Suggested `display_name`: `Pre-PURG-05 Evidence Ledger Signing Custody Packet`
- First DECISION_LOCKS occurrence: line 2613 under `Purgatorium Post-PURG04 Route Decision Packet`

### PURG05_EVIDENCE_LEDGER_SIGNING_CUSTODY_PACKET_OPERATOR_OR_ROUTE_OPENING_PACKET
- Classification: `ambiguous_reuse`
- Why it confuses: Reuses the canonical PURG-05 route number for candidate/opening/admission packet namespaces before canonical PURG-05 is actually opened.
- Suggested `display_name`: `Pre-PURG-05 Evidence Ledger Signing Custody Packet Operator Or Route Opening Packet`
- First DECISION_LOCKS occurrence: line 2882 under `PURG05 Evidence Ledger Signing Custody Admission Packet Artifact-Only`
