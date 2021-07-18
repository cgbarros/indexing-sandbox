import sys
from flask import Flask, render_template, redirect, make_response, send_from_directory, request

app = Flask(__name__, static_folder='static')

URLPrefix = "https://indexing-sandbox.caiobarros1.repl.co/"

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

@app.route('/canonical-is-the-index.html')
def meta_canonical():
    #print(request.remote_addr, file=sys.stdout)
    print(request.user_agent, file=sys.stdout)
    return render_template("canonical-is-the-index.html", URLPrefix=URLPrefix)

@app.route('/meta-chain<int:chain>.html')
def meta_chain(chain):
  #print(request.remote_addr, file=sys.stdout)
    print(request.user_agent, file=sys.stdout)
    return render_template("redirect_loop/meta-chain.html", chain=chain, URLPrefix=URLPrefix)

@app.route('/redirect-chain<int:red>.html')
def redirect_chain(red):
    if red < 4:
      #print(request.remote_addr, file=sys.stdout)
      print(request.user_agent, file=sys.stdout)
      redString = str(red+1)
      return redirect("/redirect-chain"+redString+".html", code=301)
    else:
      #print(request.remote_addr, file=sys.stdout)
      print(request.user_agent, file=sys.stdout)
      return render_template("redirect_hell/redirect-chain.html")

@app.route('/redirect-loop<int:red>.html')
def redirect_loop(red):
    #print(request.remote_addr, file=sys.stdout)
    print(request.user_agent, file=sys.stdout)
    newRed = str(red%2+1)
    return redirect("/redirect-loop"+newRed+".html", code=301)

@app.route('/redirect-loop-meta<int:red>.html')
def redirect_loop_meta(red):
    #print(request.remote_addr, file=sys.stdout)
    print(request.user_agent, file=sys.stdout)
    return render_template("/redirect_loop/redirect-loop-meta.html", red=red, URLPrefix=URLPrefix)

@app.route('/the_five_hundred.html')
def fiveHundred():
    #print(request.remote_addr, file=sys.stdout)
    print(request.user_agent, file=sys.stdout)
    return render_template("the_five_hundred.html"), 500

@app.route('/not-index.html')
def notIndex():
    #print(request.remote_addr, file=sys.stdout)
    print(request.user_agent, file=sys.stdout)
    resp = make_response(render_template("not-index.html"), 200)
    resp.headers['Link'] = "<"+URLPrefix+">; rel='canonical'"
    return resp

@app.route('/noindex-http.html')
def noIndexHttp():
    #print(request.remote_addr, file=sys.stdout)
    print(request.user_agent, file=sys.stdout)
    resp = make_response(render_template("noindex-http.html"), 200)
    resp.headers['X-Robots-Tag'] = "noindex"
    return resp

app.run(host='0.0.0.0', port=8080)
