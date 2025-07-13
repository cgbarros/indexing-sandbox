## Google Indexing rendering Demo

This is a showcase of common rendering problems in Google Search. All product data is processed by /script.js and fetched from /products.json, but this json asset is blocked by robots.txt. If you try to test the pages in a tool like [Mobile Friendly Test](https://search.google.com/test/mobile-friendly) you won't see any product data, but the browser loads it fine.

Most of the time something similar to what is showcased here happens when the website loads 3rd party assets that for some reason don't allow Googlebot to crawl them. The best way to find those is to look at View Tested Page > More Info > Page Resources in the Mobile Friendly Test or the Live Inspection in Search Console.

Typically this will appear as Soft 404 or Duplicated content (canonical) issues. That's because, since Googlebot can't see the real content, it will either think it is an error page (Soft 404, because it returns a 200 HTTP code) or it is the same content of all other product pages (hence it will choose one of them as the canonical).

The website is live at https://productrendering.caiobarros.com

## This is also a Repl

Check it at https://replit.com/@ElykSorab/ProductRendering