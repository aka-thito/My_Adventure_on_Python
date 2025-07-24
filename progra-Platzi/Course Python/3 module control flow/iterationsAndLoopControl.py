# Variable con valores
numbers = [1, 2, 3, 4, 5, 6]

# Ciclo for para iterar hasta el numero maximo de la lista
for i in numbers:
    
    print("Aquí i es igual a:", i + 1)

# ciclo "for" para iterar poniendo el inicio y el final con range
# ejemplo con frutas.
for i in range(3, 10):
    
    print(i)

# variable con lista de frutas
fruits = ["Manzana", "Uva", "Naranja", "Fresa"]

# Ciclo for para busqueda entre la lista
for fruit in fruits:
    
    print(fruit)

    if fruit == "Naranja":
        
        print("Naranja encontrada")

x = 0

# mientras x sea menor a 5, hara lo siguiente:
while x < 5:
    
    # condicional para detener cuando llegue a 3
    if x == 3:
        break

    # Imprimira x infinitamente
    print(x)
    # Ayudará a aumentar el valor de x en +1 en cada iteración
    # hasta cumplir la condicion de while
    x += 1

# Variable con valores
numbers = [1, 2, 3, 4, 5, 6]

# Ciclo for para iterar hasta el numero maximo de la lista
for i in numbers:

    # Continue servira para omitir el valor de la condicional
    if i == 3:
        continue
    
    print("Aquí i es igual a:", i + 1)

