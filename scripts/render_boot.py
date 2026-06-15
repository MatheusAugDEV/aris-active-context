#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import pathlib
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
STATE_PATH = ROOT / "ACTIVE_CONTEXT_STATE.json"
ROADMAP_PATH = ROOT / "ROADMAP_CANONICAL.md"
BOOT_PATH = ROOT / "BOOT.md"
MODEL_REASONING_POLICY_PATH = ROOT / "MODEL_REASONING_POLICY.md"

# TODO R2: mover para RULES/ por phase_class.
CORE_RULES = [
    "JSON vence tudo; markdown que contradiz = drift, pare e reporte.",
    "Proximo passo so da Transition Table; nao inferir de nome de arquivo nem historico.",
    "Sem execucao real/runtime/produto/Bedrock/secrets sem lock=true.",
    "Self-report nao e PASS; PASS = artifact + hash + CI verde + validator.",
    "excludent/ e archive/ nao sao fonte; forensic-only.",
    "Fase que muda fato canonico atualiza STATE.json primeiro.",
]

LAYER_ORDER = [
    "Infernus FULL",
    "Purgatorium FULL",
    "Infernus Revalidation",
    "BenchUX",
    "Crisol",
    "Polimento",
    "EXT-SEC 00→04",
    "Cinzel",
    "EXT-SEC 05→06",
    "Bedrock Gate",
    "Produto Parte 2 / Design Partner",
    "EXT-SEC 07→08 contínuo",
]

PHASE_TO_LAYER_PREFIXES = {
    "AC-": "Infernus FULL",
    "ACB-": "Infernus FULL",
    "IF-": "Infernus FULL",
    "INF_REVALIDATION": "Infernus Revalidation",
    "INF-": "Infernus FULL",
    "PURG": "Purgatorium FULL",
    "BENCH": "BenchUX",
    "CRISOL": "Crisol",
    "POL": "Polimento",
    "EXT-SEC": "EXT-SEC 00→04",
    "CINZEL": "Cinzel",
    "BEDROCK": "Bedrock Gate",
    "PROD": "Produto Parte 2 / Design Partner",
}

def _load_state() -> dict[str, Any]:
    return json.loads(STATE_PATH.read_text(encoding="utf-8"))


def _roadmap_text() -> str:
    return ROADMAP_PATH.read_text(encoding="utf-8")


def _parse_transition_rows(roadmap_text: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    in_table = False
    for line in roadmap_text.splitlines():
        if line.startswith("| current_phase_id |"):
            in_table = True
            continue
        if not in_table:
            continue
        if not line.startswith("|"):
            break
        if set(line.replace("|", "").replace("-", "").strip()) == set():
            continue
        parts = [part.strip() for part in line.strip().strip("|").split("|")]
        if len(parts) != 6:
            continue
        rows.append(
            {
                "current_phase_id": parts[0],
                "decision": parts[1],
                "next_phase_id": parts[2],
                "next_phase_class": parts[3],
                "advance_mode": parts[4],
                "minimum_deliverable": parts[5],
            }
        )
    return rows


def _parse_macro_chain(roadmap_text: str) -> list[str]:
    capture = False
    chain: list[str] = []
    for line in roadmap_text.splitlines():
        if line.strip() == "```text":
            if not capture:
                capture = True
                continue
        if capture and line.strip() == "```":
            break
        if capture:
            stripped = line.strip()
            if stripped and stripped != "↓":
                chain.append(stripped)
    return chain or LAYER_ORDER


def _current_layer(phase_id: str) -> str:
    for prefix, layer in PHASE_TO_LAYER_PREFIXES.items():
        if phase_id.startswith(prefix):
            return layer
    return "Unknown"


def _transition_for_state(state: dict[str, Any], rows: list[dict[str, str]]) -> dict[str, str]:
    phase_id = state.get("phase_id", "")
    decision = state.get("decision", "")
    for row in rows:
        if row["current_phase_id"] == phase_id and row["decision"] == decision:
            return row
    return {
        "current_phase_id": phase_id,
        "decision": decision,
        "next_phase_id": state.get("active_next_phase", ""),
        "next_phase_class": state.get("active_next_phase_class", ""),
        "advance_mode": "operator" if not state.get("next_phase_authorized_by_operator", False) else "prompt_only",
        "minimum_deliverable": "state_reconciliation_and_review_only",
    }


def _display_optional(value: Any) -> str:
    return "null" if value is None else str(value)


def _summary_line(state: dict[str, Any]) -> str:
    latest_completed = state.get("latest_completed_phase", "")
    active_next = state.get("active_next_phase", "")
    if active_next is None:
        return f"{latest_completed}; sem transicao sucessora definida, aguardando instrucao do operador."
    return f"{latest_completed}; aguardando {active_next} sem autorizacao de execucao."


def _relevant_locks(state: dict[str, Any]) -> list[str]:
    current_live_route = state.get("current_live_route", {})
    auth = state.get("authorization", {})
    locks = [
        f"next_phase_authorized_by_operator={state.get('next_phase_authorized_by_operator', False)}",
        f"next_phase_execution_authorization={current_live_route.get('next_phase_execution_authorization', False)}",
        (
            "operator_approval_packet_review_is_execution_approval="
            f"{current_live_route.get('operator_approval_packet_review_is_execution_approval', False)}"
        ),
        f"real_apply_authorized={auth.get('real_apply_authorized', False)}",
        f"runtime_integration_allowed={auth.get('runtime_integration_allowed', False)}",
        f"production_authorized={auth.get('production_authorized', False)}",
        f"product_ready={auth.get('product_ready', False)}",
        f"secrets_access_authorized={auth.get('secrets_access_authorized', False)}",
    ]
    deferred_reason = state.get("locks", {}).get("deferred_phase_reason")
    if deferred_reason:
        locks.append(f"deferred_phase_reason={deferred_reason}")
    return locks


def _model_reasoning_section(state: dict[str, Any]) -> list[str]:
    if not MODEL_REASONING_POLICY_PATH.exists():
        return []
    text = MODEL_REASONING_POLICY_PATH.read_text(encoding="utf-8")
    phase_class = state.get("phase_class", "")
    for line in text.splitlines():
        if phase_class in line:
            return [
                "## MODELO/RACIOCINIO",
                "",
                f"- phase_class: `{phase_class}`",
                f"- mapping: {line.strip()}",
                "",
            ]
    return []


def render_boot_text() -> str:
    state_bytes = STATE_PATH.read_bytes()
    state = _load_state()
    roadmap_text = _roadmap_text()
    transition_rows = _parse_transition_rows(roadmap_text)
    macro_chain = _parse_macro_chain(roadmap_text)
    phase_id = state.get("phase_id", "")
    current_layer = _current_layer(phase_id)
    transition = _transition_for_state(state, transition_rows)
    state_sha = hashlib.sha256(state_bytes).hexdigest()[:12]
    model_reasoning = _model_reasoning_section(state)

    map_lines = []
    for layer in macro_chain:
        marker = "▸" if layer == current_layer else " "
        suffix = f" (phase_id={phase_id})" if layer == current_layer else ""
        map_lines.append(f"{marker} {layer}{suffix}")

    lines = [
        "# BOOT",
        "",
        "GERADO — NAO EDITE A MAO",
        "",
        "## CARIMBO",
        "",
        f"- state_sha: `{state_sha}`",
        f"- schema_version: `{state.get('schema_version', '')}`",
        "",
        "## AVISO DE STALE",
        "",
        "- Se este state_sha nao bate com sha256(STATE.json), rode `python3 scripts/render_boot.py`.",
        "",
        "## ONDE ESTOU",
        "",
        f"- camada: `{current_layer}`",
        f"- phase_id: `{phase_id}`",
        f"- status: `{state.get('current_status', '')}`",
        f"- decision: `{state.get('decision', '')}`",
        f"- resumo: {_summary_line(state)}",
        "",
        "## MAPA",
        "",
        *map_lines,
        "",
        "## PROXIMO PASSO",
        "",
        f"- active_next_phase: `{_display_optional(state.get('active_next_phase', ''))}`",
        f"- next_phase_class: `{_display_optional(state.get('active_next_phase_class', ''))}`",
        f"- advance_mode: `{transition.get('advance_mode', '')}`",
        "- travas relevantes:",
    ]
    lines.extend([f"  - {item}" for item in _relevant_locks(state)])
    lines.extend([""])
    lines.extend(model_reasoning)
    lines.extend(
        [
            "## REGRAS DE AGORA",
            "",
            "- TODO R2: mover para RULES/ por phase_class.",
            *[f"- {rule}" for rule in CORE_RULES],
            "",
            "## LEI DE ATUALIZACAO",
            "",
            "- Atualize `ACTIVE_CONTEXT_STATE.json` primeiro.",
            "- Regenere `BOOT.md` com `python3 scripts/render_boot.py`.",
            "- Rode `python3 scripts/validate_active_context_state.py`.",
            "- Commit e push apenas com BOOT sincronizado; o hook recusa drift.",
            "",
            "## DISCIPLINA DE LEITURA",
            "",
            "- Leia so esta pagina no boot inicial.",
            "- Nao leia `archive/` nem `excludent/` como fonte.",
            "- Docs profundos so quando o passo atual apontar explicitamente para eles.",
            "",
            "## DOCS PROFUNDOS",
            "",
            "- `ROADMAP_CANONICAL.md`",
            "- `ACTIVE_CONTEXT_STATE.json`",
            "- `artifacts/`",
            "- `scripts/validate_active_context_state.py`",
            "",
        ]
    )
    return "\n".join(lines)


def write_boot(path: pathlib.Path = BOOT_PATH) -> None:
    path.write_text(render_boot_text(), encoding="utf-8")


def main() -> int:
    write_boot()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
