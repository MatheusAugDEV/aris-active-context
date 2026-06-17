export function RollbackStatus(boundary) {
  return `
    <div class="info-row" data-component="RollbackStatus">
      <strong>Pode desfazer?</strong>
      <span>${boundary.label}</span>
      <p>${boundary.effect}</p>
    </div>
  `;
}

