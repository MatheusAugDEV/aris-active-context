import { ACTION_STATES, SCENARIO_IDS } from "../../domain/ids.js";

export const escritorioScenario = Object.freeze({
  scenarioId: SCENARIO_IDS.ESCRITORIO,
  domain: "escritorio",
  title: "Anexo suspeito em quarentena",
  shortLabel: "Escritorio",
  businessAlias: "SINTETICO-OFC-CENTRO-GAMA",
  initialActionState: ACTION_STATES.DETECTADO,
  event: {
    eventId: "SINTETICO-EVT-OFC-ANX-07",
    summary: "Anexo ANX-SAFE-07 traz marcador sintetico de excecao de politica.",
    initialState: "Caixa documental sintetica exige revisao humana antes de qualquer liberacao."
  },
  willDo: [
    "Interceptar o anexo sintetico.",
    "Colocar em quarentena visual.",
    "Mostrar motivo sem detalhe ofensivo.",
    "Gerar comprovante sintetico."
  ],
  willNotDo: [
    "Nao abrir anexo real.",
    "Nao disparar servico externo.",
    "Nao executar automacao real.",
    "Nao ensinar tecnica ofensiva."
  ],
  risk: {
    label: "Excecao de politica",
    severity: "alto",
    plainLanguage: "Liberar sem revisao criaria decisao sem contexto e sem trilha confiavel."
  },
  approvalRequired: true,
  decisionOptions: [
    { optionId: "human_review_story", label: "Enviar para revisao", action: "OWNER_APPROVE", requiresGate: true },
    { optionId: "keep_quarantine_story", label: "Manter quarentena", action: "OWNER_BLOCK", requiresGate: false },
    { optionId: "receipt_attachment_story", label: "Gerar comprovante", action: "OWNER_RECEIPT", requiresGate: false }
  ],
  evidencePlan: {
    receiptId: "SINTETICO-RCPT-OFC-003",
    items: ["anexo sintetico", "marcador seguro", "politica de quarentena", "revisao humana", "stateTouched:false"]
  },
  receiptExample: {
    receiptId: "SINTETICO-RCPT-OFC-003",
    decision: "anexo_em_quarentena_no_sandbox",
    verificationCode: "SINTETICO-VC-OFC-03",
    isDemo: true,
    stateTouched: false
  },
  rollbackOrCompensation: {
    type: "liberacao_apos_revisao_documental",
    label: "Liberar apos revisao humana",
    effect: "Mostra historia controlada de liberacao sem mudar documento real."
  },
  degradedSafeStep: "Manter quarentena e consultar comprovante sintetico.",
  stateTouched: false,
  syntheticOnly: true
});

