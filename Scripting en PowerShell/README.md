Hola. La intención de esta práctica fue utilizar comandos básicos en powershell, para esto tendremos que tener las políticas de ejecución editadas para poder ejecutar scripts, se utilizaron dos scripts para escanear puertos.

#scan_portv1: este script básicamente realiza un escaneo de puertos, primeramente busca la gateway para saber tu segmento de subred, posteriormente se determinara el rango de tu subred y se definirá un array con puertos definidos a escanear, posteriormente te pedirá una ip a escanear para después generar un bucle foreach para evaluar cada puerto, posteriormente en pantalla te mostrará qué puertos estan abiertos.

#scan_alivev2: Hace lo mismo que el script anterior, solo que con la diferencia que se agregaron 5 líneas más.
