from flask import Flask, request
import json

app = Flask(__name__)

with open('/home/jere/cours-ynov/cours-script/cours-scripting/python/tp-final-enfin/exercice5/web/blocked_ip.json') as f:
    data = json.load(f)

@app.route('/')
def index():
    client_ip = request.remote_addr

    if client_ip in data:
        return data[client_ip]
    else:
        return f"Connecté avec l'adresse {client_ip}"

if __name__ == '__main__':
    app.run()
