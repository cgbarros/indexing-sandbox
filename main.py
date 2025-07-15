import sys, re
import os
from flask import (
	Flask, 
	render_template, 
	redirect, 
	make_response, 
	send_from_directory, 
	request
)

app = Flask(__name__, static_folder='static')

def getUrlPrefix(request):
    return request.url_root

@app.route('/<path:path>')
def send_static(path):
  print(request.remote_addr, file=sys.stdout)
  print(request.user_agent, file=sys.stdout)
  return send_from_directory(app.static_folder, path)

@app.route('/')
def index():
    print(request.remote_addr, file=sys.stdout)
    print(request.user_agent, file=sys.stdout)
    host = request.host.split(':')[0]
    scheme = request.scheme
    if host.startswith('5xx-robots'):
        five_hundred_host = host
    elif host.startswith('indexing'):
        five_hundred_host = host.replace('indexing', '5xx-robots', 1)
    else:
        abort(404)
    five_hundred_url = f"{scheme}://{five_hundred_host}"
    return render_template("index.html", five_hundred_url=five_hundred_url)

@app.route('/canonical-meta.html')
def meta_canonical():
    print(request.remote_addr, file=sys.stdout)
    print(request.user_agent, file=sys.stdout)
    return render_template("canonical-meta.html", URLPrefix=getUrlPrefix(request))

@app.route('/meta-chain<int:chain>.html')
def meta_chain(chain):
    print(request.remote_addr, file=sys.stdout)
    print(request.user_agent, file=sys.stdout)
    return render_template("redirects/meta-chain.html", chain=chain, URLPrefix=getUrlPrefix(request))

@app.route('/redirect-chain<int:red>.html')
def redirect_chain(red):
    if red < 7:
      print(request.remote_addr, file=sys.stdout)
      print(request.user_agent, file=sys.stdout)
      redString = str(red+1)
      return redirect(getUrlPrefix(request)+"redirect-chain"+redString+".html", code=301)
    else:
      print(request.remote_addr, file=sys.stdout)
      print(request.user_agent, file=sys.stdout)
      return render_template("redirects/redirect-end.html", chain=red)

@app.route('/redirect-hsts<int:red>.html')
def redirect_hsts(red):
    if red < 4:
      print(request.remote_addr, file=sys.stdout)
      print(request.user_agent, file=sys.stdout)
      redString = str(red+1)
      return redirect("redirect-hsts"+redString+".html", code=301)
    else:
      print(request.remote_addr, file=sys.stdout)
      print(request.user_agent, file=sys.stdout)
      return render_template("redirects/redirect-end.html", chain=red)

@app.route('/redirect-loop<int:red>.html')
def redirects(red):
    print(request.remote_addr, file=sys.stdout)
    print(request.user_agent, file=sys.stdout)
    newRed = str(red%2+1)
    return redirect(getUrlPrefix(request)+"redirect-loop"+newRed+".html", code=301)

@app.route('/redirect-loop-meta<int:red>.html')
def redirects_meta(red):
    print(request.remote_addr, file=sys.stdout)
    print(request.user_agent, file=sys.stdout)
    return render_template("/redirects/redirect-loop-meta.html", red=red, URLPrefix=getUrlPrefix(request))

@app.route('/the_five_hundred.html')
def fiveHundred():
    print(request.remote_addr, file=sys.stdout)
    print(request.user_agent, file=sys.stdout)
    # return render_template("the_five_hundred.html"), 500
    return send_from_directory(os.path.join(app.root_path, 'static'), 'the_five_hundred.html'), 500

@app.route('/robots.txt')
def robots_txt():
    if request.host.startswith('5xx-robots'):
        abort(500, description="The server doesn't work for robots")
    return send_from_directory(os.path.join(app.root_path, 'static'), 'robots.txt')

@app.route('/5xx-robots.html')
def fiveHundreeRobots():
    print(request.remote_addr, file=sys.stdout)
    print(request.user_agent, file=sys.stdout)
    host = request.host.split(':')[0]
    scheme = request.scheme
    if host.startswith('5xx-robots'):
        indexing_host = host.replace('5xx-robots', 'indexing', 1)
        five_hundred_host = host
    elif host.startswith('indexing'):
        indexing_host = host
        five_hundred_host = host.replace('indexing', '5xx-robots', 1)
    else:
        abort(404)
    indexing_url = f"{scheme}://{indexing_host}"
    five_hundred_url = f"{scheme}://{five_hundred_host}"
    return render_template("5xx-robots.html", five_hundred_url=five_hundred_url, indexing_url=indexing_url)

@app.route('/canonical-http.html')
def notIndex():
    print(request.remote_addr, file=sys.stdout)
    print(request.user_agent, file=sys.stdout)
    resp = make_response(render_template("canonical-http.html"), 200)
    resp.headers['Link'] = "<"+getUrlPrefix(request)+'>; rel="canonical"'
    return resp

@app.route('/noindex-http.html')
def noIndexHttp():
    print(request.remote_addr, file=sys.stdout)
    print(request.user_agent, file=sys.stdout)
    resp = make_response(render_template("noindex-http.html"), 200)
    resp.headers['X-Robots-Tag'] = "noindex"
    return resp

@app.route('/soft_404.html')
def soft404():
    print(request.remote_addr, file=sys.stdout)
    print(request.user_agent, file=sys.stdout)
    return render_template("404.html", title="Soft 404")

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html', title="True 404"), 404

@app.route('/bot_404.html')
def bot404():
    print(request.remote_addr, file=sys.stdout)
    print(request.user_agent, file=sys.stdout)
    if re.search("Googlebot", str(request.user_agent)):
      return render_template('404.html', title="Bot 404"), 404
    else:
      return render_template("bot_404.html")

@app.route('/1p-blocked.html')
def first_party_blocked():
    print(request.remote_addr, file=sys.stdout)
    print(request.user_agent, file=sys.stdout)
    return send_from_directory(app.static_folder,'1p-blocked.html') 

@app.route('/templates/product-card.html')
def product_card():
    print(request.remote_addr, file=sys.stdout)
    print(request.user_agent, file=sys.stdout)
    return send_from_directory(os.path.join(app.root_path, 'templates'), 'product-card.html')

@app.route('/sitemap.xml')
def sitemap():
	resp = make_response(render_template("/sitemaps/sitemap.xml"), 200)
	resp.headers['Link'] = '<https://techtraining-feb2022.elyksorab.repl.co/>; rel="canonical"'
	return resp

# app.run(host='0.0.0.0', port=8990)
