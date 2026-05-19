# ARIS Lab Operational Load Test Plan

Status: `operational_load_test_plan_planned`

Scope: lab-only operational simulation plan. Productization: false. Customer pilot: false.

## Purpose

This plan defines how ARIS will prove capability under simulated load and failure before any future productization. It is the bridge-load-test layer for ARIS.

## Load levels

### L1 — Motorcycle Test

Goal: prove one simple flow works safely in lab.

Required example:

- simulated customer asks for an available slot;
- context is selected;
- action plan is generated;
- dry-run validates;
- permission policy is evaluated;
- ledger records simulated result;
- final response is generated.

Pass criteria:

- no unauthorized action;
- no missing ledger event;
- no source-of-truth violation;
- no jargoned final-customer message.

### L2 — Car Test

Goal: prove a short realistic sequence works.

Required example:

- simulated customer schedules;
- simulated customer cancels;
- simulated customer reschedules;
- rollback/compensation is recorded;
- owner-facing and customer-facing messages remain simple.

Pass criteria:

- no duplicate booking;
- rollback or compensation path exists;
- all events ledgered;
- no unsafe state after sequence.

### L3 — Truck Test

Goal: prove repeated use under controlled stress.

Required example:

- at least 50 simulated interactions;
- mixed schedule/cancel/reschedule/FAQ flows;
- injected LLM failures;
- injected low-confidence intents;
- injected owner no-response;
- fallback/handoff events generated.

Pass criteria:

- fallback works when LLM fails;
- handoff occurs instead of infinite loop;
- cost/usage events generated;
- no critical blocker;
- recovery evidence exists.

### L4 — Fleet Test

Goal: prove multi-actor and conflict-heavy simulation.

Required example:

- multiple simulated customers;
- multiple simulated professionals;
- conflicting slot attempts;
- repeated cancellations;
- partial failures;
- backup/restore simulation;
- safe update rollback simulation.

Pass criteria:

- no double-booking;
- conflict prevention works;
- restore simulation preserves recoverable state;
- update rollback simulation returns to safe version;
- observability coverage complete.

### L5 — Chaos Gauntlet

Goal: prove ARIS remains safe under combined adverse conditions.

Required example:

- LLM failure + channel failure + owner no-response + conflicting booking + stale context + rollback need;
- all faults are simulated only;
- no real external side effect.

Pass criteria:

- system fails closed;
- ledger captures all relevant decisions;
- human handoff path exists;
- no customer-facing dead-end;
- no product claim generated.

### L6 — Product-Shadow Full Lab

Goal: simulate a full product-like environment without real users.

Required example:

- fake owner;
- fake customer;
- fake WhatsApp-like channel;
- fake service catalog;
- fake agenda;
- fake costs;
- fake backup;
- fake update;
- fake support/handoff.

Pass criteria:

- full transcript bundle generated;
- all actions remain simulated;
- all critical events ledgered;
- costs are simulated and labeled as such;
- no external send or production behavior.

## Required scenario families

- simple scheduling
- cancellation
- rescheduling
- FAQ
- owner approval
- customer opt-out
- low-confidence intent
- LLM invalid output
- channel unavailable
- owner no-response
- conflicting slot
- backup restore simulation
- update rollback simulation
- stuck detection
- handoff simulation
- cost ceiling simulation

## Evidence artifacts expected in future phases

- `artifacts/lab/load/l1_motorcycle_test_summary.json`
- `artifacts/lab/load/l2_car_test_summary.json`
- `artifacts/lab/load/l3_truck_test_summary.json`
- `artifacts/lab/load/l4_fleet_test_summary.json`
- `artifacts/lab/load/l5_chaos_gauntlet_summary.json`
- `artifacts/lab/load/l6_product_shadow_summary.json`

## Hard non-authorization

This plan does not authorize real users, customer pilots, external-channel sends, WhatsApp integration, network use, production deployment, payment execution, real backup execution, real update execution, or MCP activation.

## Next recommended phase

`ARIS-ROADMAP-R2-LOAD-PLAN-REVIEW — Operational Load Test Plan Review Gate`
