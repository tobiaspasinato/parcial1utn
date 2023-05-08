import json

def imprimir(message):
    print(message)

def lista_personajes():
    with open("data.json", "r") as archivo:
        data = json.load(archivo)
        return data["results"]