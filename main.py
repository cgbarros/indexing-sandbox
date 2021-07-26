import sys, re
from flask import Flask, render_template, redirect, make_response, send_from_directory, request

app = Flask(__name__, static_folder='static')

URLPrefix = "https://indexing-sandbox.elyksorab.repl.co/"

@app.route('/<path:path>')
def send_static(path):
  #print(request.remote_addr, file=sys.stdout)
  print(request.user_agent, file=sys.stdout)
  return send_from_directory(app.static_folder, path)

@app.route('/')
def index():
    #print(request.remote_addr, file=sys.stdout)
    print(request.user_agent, file=sys.stdout)
    return render_template("index.html")

@app.route('/canonical-meta.html')
def meta_canonical():
    #print(request.remote_addr, file=sys.stdout)
    print(request.user_agent, file=sys.stdout)
    return render_template("canonical-meta.html", URLPrefix=URLPrefix)

@app.route('/meta-chain<int:chain>.html')
def meta_chain(chain):
  #print(request.remote_addr, file=sys.stdout)
    print(request.user_agent, file=sys.stdout)
    return render_template("redirects/meta-chain.html", chain=chain, URLPrefix=URLPrefix)

@app.route('/redirect-chain<int:red>.html')
def redirect_chain(red):
    if red < 7:
      #print(request.remote_addr, file=sys.stdout)
      print(request.user_agent, file=sys.stdout)
      redString = str(red+1)
      return redirect(URLPrefix+"redirect-chain"+redString+".html", code=301)
    else:
      #print(request.remote_addr, file=sys.stdout)
      print(request.user_agent, file=sys.stdout)
      return render_template("redirects/redirect-end.html", chain=red)

@app.route('/redirect-hsts<int:red>.html')
def redirect_hsts(red):
    if red < 4:
      #print(request.remote_addr, file=sys.stdout)
      print(request.user_agent, file=sys.stdout)
      redString = str(red+1)
      return redirect("redirect-hsts"+redString+".html", code=301)
    else:
      #print(request.remote_addr, file=sys.stdout)
      print(request.user_agent, file=sys.stdout)
      return render_template("redirects/redirect-end.html", chain=red)

@app.route('/redirect-loop<int:red>.html')
def redirects(red):
    #print(request.remote_addr, file=sys.stdout)
    print(request.user_agent, file=sys.stdout)
    newRed = str(red%2+1)
    return redirect(URLPrefix+"redirect-loop"+newRed+".html", code=301)

@app.route('/redirect-loop-meta<int:red>.html')
def redirects_meta(red):
    #print(request.remote_addr, file=sys.stdout)
    print(request.user_agent, file=sys.stdout)
    return render_template("/redirects/redirect-loop-meta.html", red=red, URLPrefix=URLPrefix)

@app.route('/the_five_hundred.html')
def fiveHundred():
    #print(request.remote_addr, file=sys.stdout)
    print(request.user_agent, file=sys.stdout)
    return render_template("the_five_hundred.html"), 500

@app.route('/canonical-http.html')
def notIndex():
    #print(request.remote_addr, file=sys.stdout)
    print(request.user_agent, file=sys.stdout)
    resp = make_response(render_template("canonical-http.html"), 200)
    resp.headers['Link'] = "<"+URLPrefix+">; rel='canonical'"
    return resp

@app.route('/noindex-http.html')
def noIndexHttp():
    #print(request.remote_addr, file=sys.stdout)
    print(request.user_agent, file=sys.stdout)
    resp = make_response(render_template("noindex-http.html"), 200)
    resp.headers['X-Robots-Tag'] = "noindex"
    return resp

@app.route('/soft_404.html')
def soft404():
    #print(request.remote_addr, file=sys.stdout)
    print(request.user_agent, file=sys.stdout)
    return render_template("404.html", title="Soft 404")

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html', title="True 404"), 404

@app.route('/bot_404.html')
def bot404():
    #print(request.remote_addr, file=sys.stdout)
    print(request.user_agent, file=sys.stdout)
    if re.search("Googlebot", str(request.user_agent)):
      return render_template('404.html', title="Bot 404"), 404
    else:
      return render_template("bot_404.html")

app.run(host='0.0.0.0', port=8080)