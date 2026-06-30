# Lapidarium Fase 5 — Cleanup Execution Plan

**Phase:** LAPIDARIUM_FASE_5_CLEANUP_EXECUTION_PLAN  
**Date:** 2026-06-30  
**Decision:** PASS  
**Plan only — no cleanup executed**

---

## Summary

Fase 5 produced a complete item-by-item cleanup execution plan. 16 candidates were surveyed. No files were deleted, moved, or removed from git. No secrets were read. All execution locks remain false.

---

## Candidate Inventory Summary

| Status | Count | Items |
|--------|-------|-------|
| REMOVE_CANDIDATE | 9 | Low-risk files with clear evidence of transience/accident |
| NEEDS_OPERATOR_DECISION | 2 | temp_audit checkpoint files (f15z1, f15z1_post_z3) |
| BLOCKED | 3 | PostScript binaries + nested git repo (F4-FIND-002/003) |
| KEEP | 1 | .env (F4-FIND-001 false positive — no action) |

---

## REMOVE_CANDIDATE Items

These 9 items have clear evidence they are not production source and are candidates for removal in a future cleanup execution phase, subject to operator approval:

| Item ID | Path | Tracked | Size | Rationale |
|---------|------|---------|------|-----------|
| F5-001 | `temp_audit/ambiguity_resolver_report.md` | Yes | 2KB | Transient audit output |
| F5-002 | `temp_audit/ambiguity_resolver_summary.json` | Yes | 490B | Transient audit output |
| F5-003 | `temp_audit/ambiguity_resolution_samples.jsonl` | Yes | 9KB | Transient audit data |
| F5-006 | `legacy/wake/tts.py.backup` | Yes | 6.6KB | .backup snapshot (only copy) |
| F5-007 | `legacy/wake/wake.py.backup` | Yes | 7.2KB | .backup snapshot (wake.py exists) |
| F5-008 | `legacy/experiments/tart=always` | No | 1.7KB | CLI arg fragment as filename |
| F5-009 | `debug_audio.wav` | No | 259KB | Invalid WAV, debug capture |
| F5-010 | `teste.wav` | No | 39KB | Test recording, untracked |
| F5-011 | `[:alnum:] \n \` | Yes | 15.5KB | POSIX char class in name = pager artifact |
| F5-012 | `how --stat --summary 5dda82a` | Yes | 15.5KB | git command tail as filename = pager artifact |

**Note:** F5-011 and F5-012 require careful shell quoting for `git rm` (use `--` and single quotes).

---

## NEEDS_OPERATOR_DECISION Items

| Item ID | Path | Reason |
|---------|------|--------|
| F5-004 | `temp_audit/f15z1` | Name suggests phase 15 zone 1 checkpoint — operator must verify content |
| F5-005 | `temp_audit/f15z1_post_z3` | Name suggests post-Z3 checkpoint — operator must verify content |

---

## BLOCKED Items

These items require separate explicit operator decisions and may not be acted upon in any future cleanup execution without those decisions:

### F5-013 + F5-014 — F4-FIND-003: PostScript Binaries

| Path | Size | MIME |
|------|------|------|
| `legacy/experiments/genai` | 20.9MB | application/postscript |
| `legacy/experiments/threading` | 7.0MB | application/postscript |

Both untracked. Likely accidental pager/man-page captures but could be intentional reference material. **Action is irreversible (untracked, no git history).** Operator must confirm origin and intent before any removal. Backup recommended before any action.

### F5-015 — F4-FIND-002: Nested Git Repository

**Path:** `external/mcp_candidates/gogogadgetbytes_smart_connections_mcp`  
**Files:** 42 | **Nested git:** `source/.git` | **Declared submodule:** No

Supply chain decision required. Options:

1. `declare_submodule` — `git submodule add <remote-url> .../source`
2. `vendor_with_manifest` — remove `source/.git`, write vendor manifest, track files directly
3. `remove_after_operator_approval` — `rm -rf external/mcp_candidates/...`
4. `quarantine` — add to `EXCLUDENT_POLICY.md`, explicitly exclude

---

## KEEP

**.env** — F4-FIND-001 was resolved as a false positive. `.env` was never git-tracked. Correctly gitignored (`line 1: .env`, `line 6: *.env`). Local configuration file. **Do not touch.** Secret rotation remains operator responsibility.

---

## How to Authorize Cleanup

Operator must issue an explicit prompt naming item_ids to authorize. Example:

```
Authorize cleanup of F5-001, F5-002, F5-003, F5-007, F5-008, F5-009, F5-010, F5-012.
```

A future `LAPIDARIUM_FASE_5_CLEANUP_EXECUTION` phase will perform only the authorized removals with git commit after each batch.

**Items F5-013, F5-014, F5-015 require separate decision prompts explicitly addressing their blocking reasons before they can be authorized.**

---

## Guards Respected

- PLAN-ONLY ✓ — no cleanup executed
- NO-FILE-DELETION ✓
- NO-FILE-MOVE ✓
- NO-GIT-RM ✓
- NO-SECRET-PRINT ✓ — `.env` content never read
- NO-RUNTIME ✓
- NO-REAL-APPLY ✓
- NO-HISTORY-REWRITE ✓
- NO-FORCE-PUSH ✓
- MAIN-ONLY ✓
- COMMIT-PUSH-HASH ✓
