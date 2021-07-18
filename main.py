import sys
from flask import Flask, render_template, redirect, make_response, send_from_directory, request

app = Flask(__name__, static_folder='static')

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

@app.route('/redirect-hell/redirect1.html')
def redirect_hell1():
    #print(request.remote_addr, file=sys.stdout)
    print(request.user_agent, file=sys.stdout)
    return redirect("/redirect-hell/redirect2.html", code=301)

@app.route('/redirect-hell/redirect2.html')
def redirect_hell2():
    #print(request.remote_addr, file=sys.stdout)
    print(request.user_agent, file=sys.stdout)
    return redirect("/redirect-hell/redirect1.html", code=301)

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
    resp.headers['Link'] = "<https://indexing-sandbox.caiobarros1.repl.co/>; rel='canonical'"
    return resp

@app.route('/noindex-http.html')
def noIndexHttp():
    #print(request.remote_addr, file=sys.stdout)
    print(request.user_agent, file=sys.stdout)
    resp = make_response(render_template("noindex-http.html"), 200)
    resp.headers['X-Robots-Tag'] = "noindex"
    return resp

app.run(host='0.0.0.0', port=8080)
