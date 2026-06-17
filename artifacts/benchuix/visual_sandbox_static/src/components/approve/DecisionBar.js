import { GLOBAL_MODES, OWNER_ACTIONS } from "../../domain/ids.js";

const BLOCKED_IN_DEGRADED = new Set([
  OWNER_ACTIONS.OWNER_APPROVE,
  OWNER_ACTIONS.OWNER_OVERRIDE,
  OWNER_ACTIONS.OWNER_UNDO
]);

export function DecisionBar({ scenario, globalMode }) {
  return `
    <div class="decision-bar" data-component="DecisionBar">
      ${scenario.decisionOptions.map((option) => {
        const disabled = globalMode === GLOBAL_MODES.MODO_DEGRADADO && BLOCKED_IN_DEGRADED.has(option.action);
        return `
          <button class="decision-button" data-action="${option.action}" ${disabled ? "disabled" : ""}>
            ${option.label}
          </button>
        `;
      }).join("")}
    </div>
  `;
}

