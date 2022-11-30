Hola. Este script necesitará que tengas una máquina virtual con linux para que funcione, así que asegurate de tener una máquina virtual con un sistema operativo con linux para poder trabajar este script. Primero que nada deberás configurar un servidor FTP en tu máquina virtual para poder hacer uso de este script.

#comunicacionFTP.py: primero que nada se importan las librerías necesarias como from ftplib import FTP, posteriormente deberás tener tu servidor FTP listo para poder establecer la conexión con este, se logueara un usuario dado junto con su contraseña mediante la función ftp.login, posterirormente el script se ubicará con la funcion ftp.cwd para encontrar el archivo ADVERTENCIA.txt, posteriormente se lista el archivo dentro del directorio con la función ftp.retrlines y por último se hace el envio del archivo con la función ftp.storlines, dado todo esto se cierra la conexión con el servidor FTP con la función ftp.quit().

#ADVERTENCIA.txt: archivo dado para el ejemplo del envio de archivos.

Una vez que hayas ejecutado el script en windows, deberás entrar a tu máquina virtual, para corroborar que el envio del archivo se realizó correctamente.
