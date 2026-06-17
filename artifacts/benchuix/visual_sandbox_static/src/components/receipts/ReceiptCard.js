import { StatusPill } from "../primitives/StatusPill.js";

export function ReceiptCard({ scenario, state }) {
  return `
    <article class="receipt-card" data-component="ReceiptCard" data-is-demo="true">
      <div>
        <p class="eyebrow">Comprovante sintetico</p>
        <h3>${scenario.receiptExample.receiptId}</h3>
        <p>${scenario.receiptExample.decision}</p>
      </div>
      ${StatusPill(state.actionState)}
    </article>
  `;
}

