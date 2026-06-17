export function DegradedBanner(scenario) {
  return `
    <aside class="degraded-banner" data-component="DegradedBanner">
      <strong>Modo degradado</strong>
      <span>Nenhuma acao parecida com execucao fica disponivel. ${scenario.degradedSafeStep}</span>
    </aside>
  `;
}

