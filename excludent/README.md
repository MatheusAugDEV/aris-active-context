# EXCLUDENT (active-context mirror)

EXCLUDENT is the logical exclusion zone of ARIS.

Files inside this directory are:
- NOT active context
- NOT active roadmap authority
- NOT source-of-truth
- NOT evidence for current routing
- NOT prompt input
- NOT boot input
- NOT decision authority
- NOT readable by default

## Read policy

`excludent/` is NEVER read during normal boot, context pack assembly, or routing decisions.
It may ONLY be inspected by explicit operator forensic request.

## Active canonical Infernus roadmap

`project_mirror/docs/infernus_full/infernus_full_canonroadmap.md`

## Structure

- `infernus/roadmaps/` — superseded Infernus roadmap versions (mirrors of Project_ARIS excludent)
- `routes/` — obsolete route artifacts
- `obsolete_context/` — obsolete context material

Created: 2026-06-06 | Phase: INF-FULL-06
