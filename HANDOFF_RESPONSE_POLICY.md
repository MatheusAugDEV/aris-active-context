# HANDOFF_RESPONSE_POLICY

## Purpose

This file defines the default response-size policy for Codex/agent phase handoffs in ARIS. It exists to prevent long chat outputs from duplicating information already stored in artifacts, reports, ledgers, docs, and active-context.

## Default handoff rule

- default_handoff_style: `compact`
- artifact_detail_is_source_of_truth: `true`
- chat_handoff_should_not_duplicate_artifacts: `true`
- context_usage_report_in_chat_by_default: `false`
- full_validation_log_in_chat_by_default: `false`
- full_file_list_in_chat_by_default: `false`
- full_flags_list_in_chat_by_default: `false`
- full_context_sources_list_in_chat_by_default: `false`

Codex final responses must be compact by default. Detailed evidence belongs in artifacts and reports, not in chat.

## Compact final response template

Use this default final shape unless a phase explicitly requests a full audit dump:

```text
Status: <pass|warn|blocked|invalid>
Decision: <pass|warn|blocked|invalid>
Phase: <phase id + short name>
Changed: <N files; only name categories or key files>
Validation: <passed/failed + key commands count>
Blocked flags: preserved
Artifacts: <summary/report paths>
Next: <next phase>
Commits: root <hash>; active-context <hash>
Notes: <max 3 bullets for warnings/risks>
```

## What not to paste by default

Do not paste by default:

- full changed-file list when more than 6 files changed;
- full validation command list if all passed;
- full flags list if all blocked flags are preserved;
- full context usage report;
- full read-first source list;
- full grep output;
- full artifact contents;
- full prompt summary;
- repeated explanation of known locks.

Instead write: `details recorded in artifacts/report`.

## When a longer response is allowed

A longer handoff is allowed only when:

- status is `blocked` or `invalid`;
- a validation failed;
- a protected source was touched;
- a forbidden flag changed;
- commit/push failed;
- user explicitly asks for full audit details;
- handoff is intended to be pasted into another tool as source evidence.

## Required compact fields

Even compact handoffs must include:

- status;
- decision;
- phase;
- key changes;
- validation status;
- artifact paths;
- next phase;
- root commit;
- nested active-context commit;
- any blocker/warning that affects next action.

## Non-authorizations

This policy does not authorize:

- implementation;
- runtime mutation;
- MCP activation;
- network access except authorized Git operations;
- dependency installation;
- product promotion;
- customer real use;
- production release;
- hiding failures or warnings.

Compact does not mean vague. Failures, warnings, drift, blocked pushes, protected-source touches, and forbidden flag changes must remain explicit.
