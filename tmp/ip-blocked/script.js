fetch("https://api.ipify.org")
	.then(r => r.text())
	.then(ip => {
		console.log("Your ip is: ", ip);
		fetch("hostname.php?ip="+ip)
		.then(r=>r.text())
		.then(hostname=>{
			console.log("Hostname: ", hostname);
			if(!hostname.match(/crawl.*googlebot\.com/)) {
				fetch("products.html")
					.then(r => r.text())
				  .then(r => {
						const products = r;
						const newDiv = document.createElement("div");
						newDiv.innerHTML = products;
						document.querySelector("body").appendChild(newDiv)
					});	
			} else {
				let p = document.createElement("p");
				p.innerHTML = `You're Googlebot! I know that because your ip is ${ip} and you hostname is ${hostname}. No products for you!`;
				document.querySelector("body").appendChild(p);
			}
		});
		
});
