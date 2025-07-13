fetch("products.html")
	.then(r => r.text())
  .then(r => {
		const products = r;
		const newDiv = document.createElement("div");
		newDiv.innerHTML = products;
		document.querySelector("body").appendChild(newDiv)
	});