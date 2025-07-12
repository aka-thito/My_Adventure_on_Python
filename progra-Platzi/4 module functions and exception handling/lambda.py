add = lambda a, b: a + b # Aparentemente "lambda" se usa para
# funciones anonimas, no sé a detalle a que se refiere de momento


print(add(10, 4))

multiply = lambda a, b: a * b

print(multiply(80,5)) # por lo poco que veo lambda lo que hace
# es que podamos poner la variable dentro de los "()" del print
# para luego usarla como si fuera una funcion o algo asi 
# ¯\_(ツ)_/¯


# Cuadrado de cada numero
numbers = range(11)
squared_numbers = list(map(lambda x: x**2, numbers))

print("Cuadrados:", squared_numbers)

# PARES

even_numbers = list(filter(lambda x: x%2 == 0, numbers))

print("Pares:", even_numbers)