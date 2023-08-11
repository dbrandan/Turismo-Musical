import json
import os

filename = "data.usuario.json"
with open(filename,"r") as file:
    data = json.load(file)
print("El usuario es:",data["nombre"])

