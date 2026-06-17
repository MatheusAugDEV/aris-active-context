export function ApprovalRequirement(required) {
  return `
    <div class="info-row" data-component="ApprovalRequirement">
      <strong>Precisa aprovacao</strong>
      <span>${required ? "Sim, gate do dono" : "Nao, regra deterministica"}</span>
    </div>
  `;
}

