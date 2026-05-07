# ARIS_FULL_HISTORY

## Purpose

This file contains the extended ARIS history.
It is not the default read path.
The active files in the repo beat this archive for current decisions.

## Source classification

- Verified by artifacts/docs: items backed by repo artifacts, summaries, decisions, reports, or official docs.
- Narrative reconstruction: chronology assembled from the user history and context.
- Requires verification: items that remain interpretive, incomplete, or not yet artifact-backed.

## Timeline

### 08/04/2026 — Pre-ARIS / technical environment

- Debian/Lenovo/kernel/Waydroid conflict set the earliest technical context.
- This is pre-ARIS background, not an ARIS module.

### 09/04/2026 — Birth of ARIS

- ARIS began as a personal assistant inspired by Jarvis.
- Initial shape: `main.py`, `brain.py`, `actions.py`.
- Groq was used as an early free fallback path.
- Memory persisted in `data/memory.json`.
- Dynamic greeting, time/date, and context history were added.
- An API key exposure incident became an early security lesson.

### 09-10/04/2026 — Memory and GUI/orb

- Memory grew from a simple store into structured categories.
- `memoria={}` was corrected to `memoria=None`.
- `ensure_ascii=False` was added for correct JSON output.
- A system prompt identifying Matheus as creator was introduced.
- The first orb UI direction was established.

### 10/04/2026 — First GUI and STT

- GUI became functional with interaction controls.
- STT moved from Google SpeechRecognition to Faster-Whisper offline.
- PyAudio microphone capture and sample-rate tuning were worked through.

### 11/04/2026 — Initial roadmap and TTS

- A first roadmap of 8 phases was defined.
- The orb was prototyped and then ported to Pygame.
- Piper TTS and Edge-TTS fallback entered the design.

### 12/04/2026 — Refinement, Anthropic, embeddings

- Intent/regex handling was refined.
- Anthropic usage and token economy were discussed.
- A critical embedding/memory bug was found.

### 12-14/04/2026 — systemd, greeting, wake-word issues

- systemd startup, environment variables, greeting, and duplicate wake-word behavior were debugged.
- The runtime was stabilized incrementally.

### 14/04/2026 — Safe wake-word stub and better responses

- Wake-word was reduced to a safe stub.
- Response quality, temperature routing, and memory limits were improved.

### 15/04/2026 — Two worlds and stabilization

- A legacy root stack and a newer `src/aris` stack coexisted.
- The GUI exit issue became a major blocker.

### 15/04/2026 — Block A

- Focus shifted toward tests, imports, lazy loading, and logic-core stability.

### 17/04/2026 — Technical research

- Wake word, VAD, streaming, hardening, plugins, observability, and memory research was consolidated.

### 22/04/2026 — Parallel project

- A separate news site project was explored.

### 26/04/2026 — Conversational continuity

- Context loss in conversations became a core problem.

### 27-28/04/2026 — TypeScript orb

- A new orb with particles and perceptible states was built in TypeScript.

### 01/05/2026 — Action runtime audit

- Action runtime, ledger, rollback, and permission-gate concepts were audited.

### 05/05/2026 — Context Intelligence / Obsidian

- Obsidian and MCP read-only context strategy became central.
- External MCP write access was rejected as the foundation.

### 06/05/2026 — Research, roadmap, and review

- Research on orchestration ecosystems and roadmap feasibility shaped the current architecture posture.

### F14-F21 — Mature architecture formation

- F14: semantic/understanding pipeline.
- F15: history/evaluation/golden gates.
- F16: factual repair and stable runtime behavior.
- F17: documentation/reference integrity.
- F18: voice/audio safety.
- F19: action runtime contracts.
- F20: universal answer reliability.
- F21: context operating system / Obsidian strategy.

### Pre-V6 / Cockpit Evidence Foundation

- The old `V6-F21..V6-F31` trail is now treated as Pre-V6 / cockpit evidence foundation.
- This track is closed as a foundation, not as official V6 closure.

### Official V6 via PDF F1-F29

- F23: voice safety policy.
- F24: practical proof gate for UI/rich output/voice.
- F25: observability, evaluation, reliability lab.
- F26: practical proof gate for reliability.
- F27: local packaging, diagnostics, recovery profiles.
- F28: technical debt, risk, tenant defer, source-of-truth sync.
- F29 remains blocked pending Obsidian Context Law / Context Control repair.

## Narrative notes

- The archive is a reconstruction aid.
- The active files in the repo are the decision layer.
- No claim of V6 closure should be made from this archive alone.

## Requires verification

- Protocolo Omni.
- Any exact hardware-specific claims beyond the recorded sessions.
- Any commercial/financial claim.
- Any token-saving claim.
- Any claim that Obsidian is corrected.
- Any claim that official V6 is closed.
