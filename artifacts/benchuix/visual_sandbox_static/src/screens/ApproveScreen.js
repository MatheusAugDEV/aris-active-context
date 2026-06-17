import { SandboxBadge } from "../components/shell/SandboxBadge.js";
import { ApprovalPanel } from "../components/approve/ApprovalPanel.js";

export function ApproveScreen({ scenario, state }) {
  return `
    <section class="screen" data-screen="approve">
      ${SandboxBadge()}
      ${ApprovalPanel({ scenario, state })}
    </section>
  `;
}

