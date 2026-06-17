import { ACTION_STATES, GLOBAL_MODES, OWNER_ACTIONS } from "./ids.js";
import { nextActionState, receiptRequiredForState } from "./stateMachine.js";

export function arisCanPropose() {
  return nextActionState(ACTION_STATES.DETECTADO, OWNER_ACTIONS.OWNER_PROPOSE) === ACTION_STATES.PROPOSTO;
}

export function arisCannotAutoApproveSensitiveAction() {
  return nextActionState(ACTION_STATES.PROPOSTO, OWNER_ACTIONS.OWNER_APPROVE) === ACTION_STATES.AGUARDANDO_APROVACAO;
}

export function sensitiveActionNeedsVisualGate(scenario) {
  return scenario.approvalRequired === true ? scenario.decisionOptions.some((option) => option.requiresGate) : true;
}

export function refusalOrBlockGeneratesReceipt() {
  return receiptRequiredForState(ACTION_STATES.BLOQUEADO_AUTO) && receiptRequiredForState(ACTION_STATES.RECUSADO);
}

export function degradedBlocksOwnerControls() {
  return [
    OWNER_ACTIONS.OWNER_APPROVE,
    OWNER_ACTIONS.OWNER_OVERRIDE,
    OWNER_ACTIONS.OWNER_UNDO
  ].every((actionType) => nextActionState(ACTION_STATES.AGUARDANDO_APROVACAO, actionType, GLOBAL_MODES.MODO_DEGRADADO) === ACTION_STATES.AGUARDANDO_APROVACAO);
}

export function stateTouchedAlwaysFalse(items) {
  return items.every((item) => item.stateTouched === false);
}

export function receiptsAreDemoOnly(items) {
  return items.every((item) => item.receiptExample?.isDemo === true);
}

