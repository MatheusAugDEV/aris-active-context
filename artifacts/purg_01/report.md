# PURG-01 — ARIS Purgatorium Finding Record Gate

**Decision:** PASS  
**Date:** 2026-06-03  
**Previous phase:** INF-MINOS-01 (ARIS Infernus Minos Deterministic Verdict Gate)  
**Initial origin/main SHA read:** `24ac00a7d1ddefedb6c86493aa852fbfcc24a250`

---

## Context

INF-MINOS-01 already produced one deterministic `block` verdict for the nemesis validator bypass
scenario using fixed threshold rules and `llm_as_judge=false`. This gate does not execute runtime,
does not run a bot, does not run Minos again, and does not apply any repair. It only classifies the
existing evidence into one auditable Purgatorium finding record.

---

## Deterministic Finding Classification

| Field | Value |
|---|---|
| Finding ID | `purg_nemesis_validator_bypass_001` |
| Bot | `nemesis` |
| Scenario | `scenario_11_nemesis` |
| Attack class | `validator_bypass_injection` |
| Finding type | `validator_bypass_attempt` |
| Minos verdict | `block` |
| Severity | `S0` |
| Status | `open` |
| Disposition | `requires_repair_plan` |
| Runtime patch allowed | `false` |
| Apply allowed | `false` |

All deterministic preconditions held: `source_bot_id=nemesis`, `source_scenario_id=scenario_11_nemesis`,
validator-bypass evidence was present, `llm_as_judge=false`, `deterministic=true`, and all Minos
threshold results were true.

---

## Evidence Chain

| Artifact | SHA-256 |
|---|---|
| source verdict | `ce11c696ea438cedb36862c686e698107f4ccb73ba6d6a78136b36bf0fb96512` |
| source bot log | `ae11c023e72733e31945014845ff3c171bf3a3a299616fbd5cc73eec5f9cc443` |
| fixture input | `c1a4dca4d978f306996d335682e7988c0c89fe1d0665ad1fd6e7b0b75d19b40b` |
| finding canonical hash | `f9a62f68f506f7afd9fac02f9c2186470b22be95e456f200b0b4953e6f5e134b` |

The finding canonical hash is computed from the JSON content excluding the `finding_sha256` field itself.

---

## Carried Warnings

- INF-MINOS-01 `decision.json` kept `final_origin_main_sha="pending_post_push_verification"`
  although the reported final SHA was `24ac00a7d1ddefedb6c86493aa852fbfcc24a250`.
- INF-BOT-01 `decision.json` kept `final_origin_main_sha="pending_post_push_verification"`
  although the reported final SHA was `0db6fda2de4663894c69328cd3c53161a848d0ca`.
- INF-MAT-01 `final_origin_main_sha` still points to `debc51e...`; warning preserved only.

No correction gate was opened for these historical inconsistencies.

---

## Non-Authorization Attestation

- No validator repair was applied.
- No runtime execution occurred.
- No autonomous execution occurred.
- No external network was used.
- No secrets were accessed.
- No Bedrock execution occurred.
- No product promotion occurred.
- `next_phase=null`
- `BENCH-01` was not opened automatically.
