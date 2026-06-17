export function RiskBadge(risk) {
  return `
    <div class="risk-badge" data-component="RiskBadge">
      <strong>Risco ${risk.severity}</strong>
      <span>${risk.label}</span>
      <p>${risk.plainLanguage}</p>
    </div>
  `;
}

