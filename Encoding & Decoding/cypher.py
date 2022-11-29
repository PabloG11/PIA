#Importamos fernet desde cryptography
#
from cryptography.fernet import Fernet

#Definicion de la función genwrite que genera una llave para cifrado
def genwrite():
    key = Fernet.generate_key()
    with open("pass.key", "wb") as key_file:
        key_file.write(key)
        
#Llamamos a la funcion para generar el archivo "pass.key"
genwrite()

#Definición de la función call_key con la cual leemos el contenido del archivo "pass.key"
def call_key():
    return open("pass.key","rb").read()

#Ahora cifraremos un mensaje almacenado y codificado previamente
key = call_key()
banner = "Hola, mi nombre es Pablo Guajardo y estudio LSTI en la FCFM".encode()
a = Fernet(key)
coded_banner = a.encrypt(banner)
print (coded_banner)

#Ahora desciframos el mensaje previamente cifrado
key = call_key()
b = Fernet(key)
decoded_banner = b.decrypt(coded_banner)
print(decoded_banner)
#
#Fin del script
#
#Datos: Pablo Emilio Guajardo De la Cruz
#Marícula: 1727651
#
