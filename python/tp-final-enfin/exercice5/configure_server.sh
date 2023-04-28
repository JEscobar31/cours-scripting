#!/bin/bash

# Création du dossier web
mkdir -p /home/jere/cours-ynov/cours-script/cours-scripting/python/tp-final-enfin/exercice5/web

# Création des fichiers blocked_ip.txt et app_flask.py
touch /home/jere/cours-ynov/cours-script/cours-scripting/python/tp-final-enfin/exercice5/web/blocked_ip.txt
touch /home/jere/cours-ynov/cours-script/cours-scripting/python/tp-final-enfin/exercice5/web/app_flask.py

cat << EOF > /home/jere/cours-ynov/cours-script/cours-scripting/python/tp-final-enfin/exercice5/web/app_flask.py
from flask import Flask, request
app = Flask(__name__)
@app.route('/')
def index():
    return f"Connecté avec l'adresse {request.remote_addr}"
    app.run()
EOF
