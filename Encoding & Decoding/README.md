Hola. Para hacer uso de estos scripts deberás tener en cuenta que son scripts realizados en python (por lo que deberás tener instalado python en tu equipo) y son ejecutados en Powershell (por lo que tendrás que cambiar las políticas de ejecución de tu equipo). Se usarán librerías como base64 así que asegurate de tenerlas instaladas en tu equipo, de caso contrario no podrás hacer uso de estos scripts.

#encode_text.py: primero que nada se importa la librería ya antes mencionada, y después le pide al usuario una entrada de teclado para que escriba alguna frase para codificarla y se guarda en la variable "frase", posteriormente se obtienen los bytes de la variable "frase", se calculan los bytes, posterior a esto se genera la frase codificada en base64 y se manda a imprimir la variable "frase" ya codificada.

#encode_imgur.py: primero que nada se importan las librerías request para poder hacer un request a un sitio web, y la librería base64, básicamente lo que hace este script es que descarga una imagen de un sitio introducido por el usuario, se dan parametros para saber cual es la imagen guardada y posterior a esto se guarda. Si esto se hace correctamente se procederá a codificar la imagen. 

#decoding_uanl.py: este script se puede usar para decodificar una imagen que se nos proporcionó en formato de .txt, se puede utilizar para decodificar otra imagen que este en formato base64, posterior a introducir el .txt codificado de la imagen se decodificará y se guardará un archivo en formato PNG que se quiso decodificar.

#cypher.py: para hacer uso de este script deberás tener implementadas la librería cryptography, dicho esto el script básicamente genera una llave con la función genwrite() que crea la llave posterior a esto de define otra función llamada call_key() para leer desde el archivo generado por la función anterior, después se genera un mensaje dado por el usuario para cifrarlo, posteriormente mandamos a descifrar la frase dada. Posterior a todo este proceso, se ejecuta en el cmd de Windows o en el idle de python para verificar cómo se ve el mensaje encriptado y desencriptado.

#coder_posh.ps1: este script básicamente lo que hace es pedir una entrada de teclado del usuario para codificar la frase dada por el usuario y al ejecutarlo te da la frase encriptada en base64.

#decoder_posh.ps1: este script básicamente lo que hace es que decodifica una frase codificada dada en base64 y al ejecutar el script en PS muestra la frase decodificada.

#command_posh.ps1: este script básicamente lo que realiza es que codifica un comando y lo decodifica, posteriormente al ejecutarlo en PS te muestra el comando codificado y decodificado.

#codipo.ps1: este script lo que hace es que codifica el contenido de un archivo dado, posteriormente lo codifica y después de esto lo manda a decodificar.

#secret.txt: archivo dado para el script anterior.
