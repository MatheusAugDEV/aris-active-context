import { SandboxBadge } from "../components/shell/SandboxBadge.js";
import { ReceiptCard } from "../components/receipts/ReceiptCard.js";
import { ReceiptDetail } from "../components/receipts/ReceiptDetail.js";

export function HistoryScreen({ scenario, state }) {
  return `
    <section class="screen" data-screen="history">
      ${SandboxBadge()}
      ${ReceiptCard({ scenario, state })}
      ${ReceiptDetail({ scenario })}
    </section>
  `;
}

