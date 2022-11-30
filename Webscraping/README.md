Hola. En esta carpeta encontraremos algunos scripts para hacer un poco de Webscraping esto con el objetivo de saber cómo funciona y como obtener metadata de alunas páginas web a través de su código HTML, para poder hacer uso de estos scripts deberás tener en cuenta que deberás tener implementadas las librerías de beautifulsoup desde bs4, csv y requests, de lo contrario no podrás utilizar estos scripts.

#scrape_quotes.py: básicamente lo que hace este scriptes que harpa una petición a la URL del sitio, analizará el contenido HTML y generará listas, citas y autores para mostrar en pantalla y guardar en un archivo .csv.

#scrap1.py: este script lo que hace es, conectarse y traer la información de una URL dada.

#scrap2.py: en este script ahora haciendo uso de BeautifulSoup se analizará el contenido y se comenzará a formatear la información recibida.

#scrap3.py: en este script comenzamos a buscar información en base a metadatos, buscamos elementos de class “card-content”.

#scrap4.py: en este script ahora buscaremos títulos con información más precisa.

#scrap5.py: en este script procederemos solo mostrando el texto del elemento a imprimir del objeto.

#scrap6.py: en este script procedemos a limpiar los espacios en blanco haciendo un ajuste en la sección de strip().

#scrap7.py: en este script si el interés en particular es buscar empleos que esta relacionados a desarrollo de Python, editaremos la forma de búsqueda.

#scrap8.py: en este script si lo que queremos es información adicional sobre esos empleos, iteraremos sobre la información que previamente estábamos desplegando.

#scrap9.py: en este script sólo editamos el nivel de divisiones para poder encontrar la información que necesitamos.

#scrap10.py: en este script agregamos información de contacto.

#scrap11.py: en este script para que la salida incluya el link de href, se realiza otro ajuste en el código.

#scrap12.py: en este script aunque nos muestra los dos elementos de href, en realidad solo nos interesa elelemento de “Apply Here”, así que solo se realizará un ajuste flitrandolo.
