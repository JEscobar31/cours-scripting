from os import system, chdir

system("sudo apt-get update")
system("sudo apt-get install python3-pip")
system("pip install requests")
system("pip install flask")
system("mkdir site")
chdir("site")
system("mkdir templates")
system("touch templates/index.html")
system("mkdir static")
system("echo \"*/5 * * * * /tp-fatigue/site/app.py\" | crontab -")

with open('app.py', 'w') as f:
    f.write('''
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
app.run(host="0.0.0.0", port=5000)
''')