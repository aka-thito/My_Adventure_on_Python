# Clase 31 Parte 1

import csv

# Leer un archivo
"""with open('products.csv', mode = 'r') as file:

    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:

        print(row)"""

# Este codigo solo captura la informacion en un diccionario, pero
# tambien se puede ir iterando atraves de las columnas que nos 
# interesan

# Mostrar la información por columnas

with open('products.csv', mode = 'r') as file:

    csv_reader = csv.DictReader(file)

    for row in csv_reader:

        print(f"Producto: {row['name']}, Precio: {row['price']}")