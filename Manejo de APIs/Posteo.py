#Nombre: Pablo Emilio Guajardo De la Cruz
#Matrícula: 1727651

import requests
import json

if __name__ == '__main__':
    url = "http://httpbin.org/post"
    args = {'nombre': 'Pablo','matricula': '1727651','curso':'Laboratorio de Programacion para Ciberseguridad'}

    response = requests.post(url, params=args)

    if response.status_code == 200:
        print(response.content)
