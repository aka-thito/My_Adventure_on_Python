# Ejercicio de clase 30

# hacer que Python haga un conteo de las lineas de texto que tiene
# el .txt del cuento de caperucita roja

with open("6 reading and writing\cuento.txt", "r") as file:

    lines = file.readlines()

    print(len(lines))