import { ACTION_STATES, SCENARIO_IDS } from "../../domain/ids.js";

export const barbeariaScenario = Object.freeze({
  scenarioId: SCENARIO_IDS.BARBEARIA,
  domain: "barbearia",
  title: "Pedido VIP fora do horario",
  shortLabel: "Barbearia",
  businessAlias: "SINTETICO-BARB-LUZ-ALFA",
  initialActionState: ACTION_STATES.DETECTADO,
  event: {
    eventId: "SINTETICO-EVT-BARB-20H30",
    summary: "VIP-LIGHT pede encaixe as 20:30, fora da janela sintetica.",
    initialState: "Agenda sintetica fecha as 20:00 e exige excecao do dono."
  },
  willDo: [
    "Bloquear o encaixe automatico no sandbox.",
    "Mostrar impacto na fila sintetica.",
    "Pedir gate do dono para uma excecao VIP.",
    "Gerar comprovante sintetico depois da decisao."
  ],
  willNotDo: [
    "Nao confirmar atendimento real.",
    "Nao avisar cliente real.",
    "Nao alterar agenda real.",
    "Nao cobrar valor real."
  ],
  risk: {
    label: "Fila posterior pode atrasar",
    severity: "medio",
    plainLanguage: "A excecao pode atrasar dois atendimentos sinteticos seguintes."
  },
  approvalRequired: true,
  decisionOptions: [
    { optionId: "approve_vip_story", label: "Aprovar excecao sintetica", action: "OWNER_APPROVE", requiresGate: true },
    { optionId: "refuse_vip_story", label: "Manter bloqueio", action: "OWNER_REFUSE", requiresGate: true },
    { optionId: "receipt_vip_story", label: "Gerar comprovante", action: "OWNER_RECEIPT", requiresGate: false }
  ],
  evidencePlan: {
    receiptId: "SINTETICO-RCPT-BARB-001",
    items: ["politica de horario", "slot pedido", "decisao do dono", "risco resumido", "stateTouched:false"]
  },
  receiptExample: {
    receiptId: "SINTETICO-RCPT-BARB-001",
    decision: "excecao_vip_aprovada_no_sandbox",
    verificationCode: "SINTETICO-VC-BARB-01",
    isDemo: true,
    stateTouched: false
  },
  rollbackOrCompensation: {
    type: "reversao_documental",
    label: "Reverter excecao sintetica",
    effect: "Marca a historia como desfeita sem mudar agenda real."
  },
  degradedSafeStep: "Ver comprovante sintetico ou manter bloqueio.",
  stateTouched: false,
  syntheticOnly: true
});

