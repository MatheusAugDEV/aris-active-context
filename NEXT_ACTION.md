Prepare BLOCKED_AWAITING_HUMAN_INPUT_FOR_F32_Z13L; anchor phase F32.Z13K-Hold.
Keep the F32/F33 scope boundary explicit: F32 owns MCP read-only configuration, controlled apply, activation planning, smoke validation, zero-write/no-bulk-read validation, and closure; F33 remains reserved for SQLite Memory, FTS5 & Evaluation Baseline.
