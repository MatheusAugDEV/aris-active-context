export function WillDoList(items) {
  return `
    <section data-component="WillDoList">
      <h4>ARIS vai</h4>
      <ul>${items.map((item) => `<li>${item}</li>`).join("")}</ul>
    </section>
  `;
}

