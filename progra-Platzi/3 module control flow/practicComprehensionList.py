# Ejercicios Comprehension List

# [expresión for elemento in iterable if condición]

# Ejercicio 1
# Me piden crear una nueva lista que contenga el doble de cada
# número de la siguiente lista [1, 2, 3, 4, 5]

doble_Numbers = [x * 2 for x in range(1, 5)]

print("Valores duplicados:", doble_Numbers)

# Facilito, solo me guie con la estructura que mostraron en clase

# Ejercicio 2
# Quieres obtener una nueva lista con las palabras que tengan más
# de 3 letras y estén en mayúsculas de la siguiente lista 
# ["sol", "mar", "montaña", "rio", "estrella"]

words = ["sol", "mar", "montaña", "rio", "estrella"]
moreThreeLetters = [words.upper() for words in words if len(words) > 3]

print("Palabras Filtradas:", moreThreeLetters)

# Hice trampa mire la respuesta, no me daba la cabeza pa ver como
# era con datos tipo string

# Ejercicio 3
# Tienes dos listas, una de claves ["nombre", "edad", "ocupación"]
# y otra de valores ["Juan", 30, "Ingeniero"], combinar ambas en
# un diccionario

claves = ["nombre", "edad", "ocupación"]
valores = ["Juan", 30, "Ingeniero"]

# doble_ListDict = [[row[i] for row in claves and valores] for i in range(len(claves and valores[0]))]
# Soy malisimo xD

doble_ListDict = {claves[i]: valores[i] for i in range(len(claves))}

print(doble_ListDict)

# Ejercicio 4
# dada una la matriz, calcular la matriz traspuesta

matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

transposed = [[row[i] for row in matriz] for i in range(len(matriz[0]))]

print(transposed)

# Nada que decir, literalmente era lo mismo q en la clase

#Ejercicio 5
# Extraer de la lista los nombres de personas que vivene en
# "Madrid" y tienen mas de "30"  años.

personas = [
    {"Nombre": "Juan", "Edad": 25, "Ciudad": "Madrid"},
    {"Nombre": "Ana", "Edad": 32, "Ciudad": "Madrid"},
    {"Nombre": "Pedro", "Edad": 35, "Ciudad": "Barcelona"},
    {"Nombre": "Laura", "Edad": 40, "Ciudad": "Madrid"}
]

# Madridthirty = [(personas[i] for i in range(len(personas)))]
# soy un pendejo

Madridthirty = [persona["Nombre"] for persona in personas if persona["Ciudad"] == "Madrid" and persona["Edad"] > 30]

print("Viven en Madrid con 30 años:", Madridthirty)

# Ejercicio 6
# Crear una nueva lista multiplicando por 2 los números pares y
# dejando los impares como están, dada la lista 
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

transformation = [x * 2 if x % 2 == 0 else x for x in numbers]

print("Números transformados:", transformation)

# Pa resumir, Vali monda en estos ejercicios, siento que entiendo
# el codigo al leerlo, pero a la hora de crearlo me quedo en blanco
# y no sé como estructurarlo o hacerlo.