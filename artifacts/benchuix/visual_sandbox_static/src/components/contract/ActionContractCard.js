import { SandboxBadge } from "../shell/SandboxBadge.js";
import { WillDoList } from "./WillDoList.js";
import { WillNotDoList } from "./WillNotDoList.js";
import { RiskBadge } from "./RiskBadge.js";
import { ApprovalRequirement } from "./ApprovalRequirement.js";
import { EvidencePreview } from "./EvidencePreview.js";
import { RollbackStatus } from "./RollbackStatus.js";
import { StateTouchedIndicator } from "./StateTouchedIndicator.js";

export function ActionContractCard(contract) {
  return `
    <article class="action-contract-card" data-component="ActionContractCard">
      ${SandboxBadge()}
      <header>
        <p class="eyebrow">Contrato da acao sensivel</p>
        <h3>${contract.title}</h3>
        <p>${contract.event.summary}</p>
      </header>
      <div class="contract-grid">
        ${WillDoList(contract.willDo)}
        ${WillNotDoList(contract.willNotDo)}
        ${RiskBadge(contract.risk)}
        ${ApprovalRequirement(contract.approvalRequired)}
        ${EvidencePreview(contract.evidencePlan)}
        ${RollbackStatus(contract.rollbackOrCompensation)}
        ${StateTouchedIndicator()}
      </div>
    </article>
  `;
}

