import { ACTION_STATES, SCENARIO_IDS } from "../../domain/ids.js";

export const mercadoScenario = Object.freeze({
  scenarioId: SCENARIO_IDS.MERCADO,
  domain: "mercado",
  title: "Reembolso suspeito recusado",
  shortLabel: "Mercado",
  businessAlias: "SINTETICO-MERC-PRACA-BETA",
  initialActionState: ACTION_STATES.BLOQUEADO_AUTO,
  event: {
    eventId: "SINTETICO-EVT-MKT-REF-204",
    summary: "Pedido PED-MKT-204 solicita reembolso integral acima do limite sintetico.",
    initialState: "Dois sinais sinteticos de risco acionam bloqueio deterministico."
  },
  willDo: [
    "Recusar o reembolso instantaneo no sandbox.",
    "Mostrar os sinais sinteticos de risco.",
    "Abrir revisao manual documental.",
    "Gerar comprovante sintetico de recusa."
  ],
  willNotDo: [
    "Nao devolver dinheiro real.",
    "Nao chamar provedor financeiro real.",
    "Nao alterar estoque real.",
    "Nao alterar caixa ou ERP real."
  ],
  risk: {
    label: "Perda financeira sintetica",
    severity: "alto",
    plainLanguage: "Liberar sem revisao aumentaria perda sintetica e criaria precedente fora da politica."
  },
  approvalRequired: false,
  decisionOptions: [
    { optionId: "keep_refund_blocked", label: "Manter recusa", action: "OWNER_BLOCK", requiresGate: false },
    { optionId: "manual_review_story", label: "Criar revisao manual", action: "OWNER_OVERRIDE", requiresGate: true },
    { optionId: "receipt_refund_story", label: "Gerar comprovante", action: "OWNER_RECEIPT", requiresGate: false }
  ],
  evidencePlan: {
    receiptId: "SINTETICO-RCPT-MKT-002",
    items: ["pedido sintetico", "faixa de risco", "limite diario", "politica de bloqueio", "stateTouched:false"]
  },
  receiptExample: {
    receiptId: "SINTETICO-RCPT-MKT-002",
    decision: "reembolso_instantaneo_recusado_no_sandbox",
    verificationCode: "SINTETICO-VC-MKT-02",
    isDemo: true,
    stateTouched: false
  },
  rollbackOrCompensation: {
    type: "compensacao_por_revisao_manual",
    label: "Gerar revisao manual sintetica",
    effect: "Cria fila documental sem movimentar dinheiro real."
  },
  degradedSafeStep: "Manter recusa e ver evidencia sintetica.",
  stateTouched: false,
  syntheticOnly: true
});

