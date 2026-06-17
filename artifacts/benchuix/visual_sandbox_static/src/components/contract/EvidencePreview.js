export function EvidencePreview(plan) {
  return `
    <section class="evidence-preview" data-component="EvidencePreview">
      <h4>Comprovante</h4>
      <p>${plan.receiptId}</p>
      <ul>${plan.items.map((item) => `<li>${item}</li>`).join("")}</ul>
    </section>
  `;
}

