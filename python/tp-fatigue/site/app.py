
from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/images")
def images():
    # path = "/home/jere/cours-ynov/cours-script/cours-scripting/python/tp-fatigue/site/static"
    return render_template("index.html", images=["1.png","2.png"])
app.run(host="0.0.0.0", port=5000)
