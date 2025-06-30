print("Iteraciones con numeros:")

# crear una lsita
my_list = [1, 2, 3, 4]

# obtenemos el iterador
my_iter = iter(my_list)

# usar el iterador
print(next(my_iter)) # next sirve para observar cuales son los
print(next(my_iter)) # valores y se van guardando en memoria
print(next(my_iter))
print(next(my_iter)) # si se pasa de los 4 caracteres al macenados
                     # dará error.

print("Iteraciones para texto:")

# creando la cadena
text = "Hola Mundo"

# creando el iterador
iter_text = iter(text)

# iterar en la cadena con un ciclo
for char in iter_text:

    print(char)

print("Generador para Numeros Impares:")

# iterador para numeros impares
limit = 10

# creacion de iterador
odd_itter = iter(range(1, limit + 1, 2))

# uso del iterador
for num in odd_itter:

    print(num)

print("Generador:")

# Creacion de una funcion para el generador
def my_generator():

    yield 1
    yield 2
    yield 3

for value in my_generator():

    print(value)

# Fibonacci
# 0 1 1 2 3 5 8 13 21
print("Fibonacci:")

def fibonacci(limit):
    a, b = 0, 1 # erda por fin me muestra como poner variables
                # en una sola linea
    while a < limit:

        yield a

        a, b = b, a + b

for num in fibonacci(10): # por cada numero que esta en fibonacci
                          # queremos como limite 10
    print(num)

