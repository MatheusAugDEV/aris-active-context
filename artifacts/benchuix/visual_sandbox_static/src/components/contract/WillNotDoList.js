export function WillNotDoList(items) {
  return `
    <section data-component="WillNotDoList">
      <h4>ARIS nao vai</h4>
      <ul>${items.map((item) => `<li>${item}</li>`).join("")}</ul>
    </section>
  `;
}

