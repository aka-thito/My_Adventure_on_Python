# Clase 32 Parte 1

# .json significa Javascript Object Notation
# un formato ligero de intercambio de datos que es facil de entender
# para maquinas y humanos. Permite tener datos de manera más eficiente
# y flexible.

import json

# Lectura del archivo
with open('products.json', mode = 'r') as file:
    
    products = json.load(file)

# Mostar el contenido
for product in products:

    #print(product)
    print(f"Product: {product['name']}, Price: {product['price']}")

