from flask import Flask, render_template, redirect, make_response, send_from_directory, request
import sys

app = Flask(__name__, static_folder='static')

@app.route('/static/<path:path>')
def send_static(path):
  return send_from_directory(app.static_folder, path)

@app.route('/robots.txt')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/canonical-is-the-index.html')
def canonical():
    return render_template("canonical-is-the-index.html")


@app.route('/softly_crashing.html')
def soft_404():
    return render_template("softly_crashing.html")


@app.route('/redirect-hell/redirect1.html')
def redirect_hell1():
    return redirect("/redirect-hell/redirect2.html", code=301)


@app.route('/redirect-hell/redirect2.html')
def redirect_hell2():
    return redirect("/redirect-hell/redirect1.html", code=301)


@app.route('/the_five_hundred.html')
def fiveHundred():
    return render_template("the_five_hundred.html"), 500


@app.route('/not-index.html')
def notIndex():
    resp = make_response(render_template("not-index.html"), 200)
    resp.headers['Link'] = "<https://Search-Central-HTTP-headers.caiobarros1.repl.co/>; rel='canonical'"
    return resp

@app.route('/noindex-http.html')
def noIndexHttp():
    resp = make_response(render_template("noindex-http.html"), 200)
    resp.headers['X-Robots-Tag'] = "noindex"
    return resp

@app.route('/request')
def showIpUa():
  request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
  request.environ['REMOTE_ADDR']
  print(request.remote_addr, file=sys.stderr)
  print(request.user_agent, file=sys.stderr)
  return render_template("index.html")

app.run(host='0.0.0.0', port=8080)
