# Ejercicio de clase 30

# hacer que Python haga un conteo de las lineas de texto que tiene
# el .txt del cuento de caperucita roja

import os # Funcion para interactuar con el sistema operativo

ruta = os.path.join(os.path.dirname(__file__), "cuento.txt")
# esto es para hacer que el sistema busque el archivo desde el directorio
# del .py que se esta ejecutando

with open(ruta, "r", encoding="utf-8") as file:

    contador = 0

    for linea in file:

        contador += 1
        
    print("Líneas de texto en el archivo:", contador)