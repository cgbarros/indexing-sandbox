async function loadTemplate() {
  const res = await fetch('/templates/product-card.html');
  return await res.text();
}

function renderProduct(template, product) {
  return template
    .replace(/{{ name }}/g, product.name)
    .replace(/{{ description }}/g, product.description)
    .replace(/{{ price }}/g, product.price)
    .replace(/{{ image }}/g, product.image)
    .replace(/{{ url }}/g, 'index.html');
}

document.addEventListener("DOMContentLoaded", async () => {
  const container = document.getElementById('product-container');
  const template = await loadTemplate();

  fetch('/static/json/products.json')
    .then(res => res.json())
    .then(products => {
      products.forEach(product => {
        const html = renderProduct(template, product);
        const div = document.createElement('div');
        div.innerHTML = html;
        container.appendChild(div);
      });
    })
    .catch(console.error);
});
