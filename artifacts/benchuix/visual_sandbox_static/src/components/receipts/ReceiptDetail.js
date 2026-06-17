import { StateTouchedIndicator } from "../contract/StateTouchedIndicator.js";

export function ReceiptDetail({ scenario }) {
  return `
    <section class="receipt-detail" data-component="ReceiptDetail" data-is-demo="true">
      <h3>${scenario.receiptExample.receiptId}</h3>
      <p>Codigo: ${scenario.receiptExample.verificationCode}</p>
      <p>Decisao: ${scenario.receiptExample.decision}</p>
      <p>Evidencia: ${scenario.evidencePlan.items.join(" / ")}</p>
      <p>Comprovante demonstrativo: ${scenario.receiptExample.isDemo ? "sim" : "nao"}</p>
      ${StateTouchedIndicator()}
    </section>
  `;
}

