# En esta clase enseñan las listas comprimidas
# Estructura de la Comprehension List:

# [Expresión for Elemento in Iterable if Condición]

# Primer Ejemplo
squares = [x ** 2 for x in range(1, 11)] # Eleva al cuadrado x en
                                         # un rango de 11 veces

print("Cuadrados:", squares) # Lo imprime

# Segundo Ejemplo
# celsius = [x for x in range(5)]
celsius = [0, 10, 20, 30, 40]
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]

print("Temperatura en F:", fahrenheit)

# Tercer Ejemplo
evens = [x for x in range(1, 21) if x%2 == 0] # x será los pares
                                              # encontrados entre
                                              # 1 y 21, si x modulo
                                              # 2 es igual a 0

print("Numeros pares:" , evens)

# Cuarto Ejemplo
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
# row sirve para decir que en cada una de las filas en la posicion
# "i", que seria el iterador dentro del rango donde consultara
# la matrix y tendra como dato inicial "0"

print("Matriz:", matrix)
print("Matriz transpuesta:", transposed)
# para ser más exacto, lo que hizo este codigo fue agrupar
# iterando cada posicion del contenido de la matriz
