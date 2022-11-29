#
##Datos: Pablo Emilio Guajardo De la Cruz
##Matrícula: 1727651
#

#Importamos módulos
import requests
#Obtener la informacion HTML de la URL
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
#Imprimir el texto de la petición GET
print(page.text)
