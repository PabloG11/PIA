##DATOS: Pablo Emilio Guajardo De la Cruz
##MATRÍCULA: 1727651
#
#Parte1
#Importamos las librerías requeridas
import socket

#Parte2
#Se define la función scan con la cual
#se utilizan sockets para probar los diferentes
#puertos
def scan(addr, port):
    #Creando un nuevo socket
    socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Estableciendo el timeout para el nuevo objeto tipo socket
    socket.setdefaulttimeout(1)

    #Conexion exitosa devuelve 0. Devuelve error en caso contrario
    result = socket_obj.connect_ex((addr,port)) #Direccion y puerto en tupla.

    #Se cierra el objeto
    socket_obj.close()

    return result

#Parte3
#Lista de puertos a escanear
ports=[21, 22, 25, 80]

#Parte4
#Bucle por todas las ip del rango 10.0.0.*
for i in range (1,255):
    addr="10.0.0.{}".format(i)
    for port in ports:
        result=scan(addr, port)
        if result==0:
            print(addr, port, "OK")
        else:
            print(addr, port, "Failed")
            
