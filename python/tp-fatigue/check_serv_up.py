import requests
from os import system
from time import sleep

while True:
    try:
        rq = requests.get("http://localhost:5000")
        if rq.status_code == 200:
            print("all is running good !")
        else:
            print("Error")
        print(rq.status_code)
    except Exeption as e:
        print("reload serv")
        system("/site/app.py")
    sleep(10)