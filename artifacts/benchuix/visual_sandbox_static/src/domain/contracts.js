export const REQUIRED_CONTRACT_FIELDS = Object.freeze([
  "willDo",
  "willNotDo",
  "risk",
  "approvalRequired",
  "decisionOptions",
  "evidencePlan",
  "receiptExample",
  "rollbackOrCompensation",
  "stateTouched",
  "syntheticOnly"
]);

export function hasSevenSensitiveFields(scenario) {
  return [
    scenario.willDo,
    scenario.willNotDo,
    scenario.risk,
    scenario.approvalRequired !== undefined,
    scenario.evidencePlan,
    scenario.rollbackOrCompensation,
    scenario.stateTouched === false
  ].every(Boolean);
}

export function contractFromScenario(scenario) {
  return {
    title: scenario.title,
    event: scenario.event,
    willDo: scenario.willDo,
    willNotDo: scenario.willNotDo,
    risk: scenario.risk,
    approvalRequired: scenario.approvalRequired,
    decisionOptions: scenario.decisionOptions,
    evidencePlan: scenario.evidencePlan,
    receiptExample: scenario.receiptExample,
    rollbackOrCompensation: scenario.rollbackOrCompensation,
    stateTouched: false,
    syntheticOnly: true
  };
}

