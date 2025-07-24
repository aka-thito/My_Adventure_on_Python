# Ejercicio de clase 17

# creacion de generadores de numeros pares e impares

# Numeros pares
# Creacion de la funcion estableciendo el limite entre ()
def num_par(limit):
    
    print("Numeros Pares:")

    # Tomará la posicion 0
    a = 0

    # Mientras que a sea menor al limite, este aumentará
    while a < limit + 1:

        yield a # yield crea una funcion generadora para iterar
                # hasta el limite
        a = a + 2 # a iniciará en 0 para luego ir subiendo en
                  # valores de 2

# imrpime hasta llegar al limite de la funcion
for num in num_par(10):

    print(num)
    

# una simple impresion para separar los ejercicios
print("=========================")

# Numeros Impares
# creacion de funcion impar

def num_impar(limit):

    print("Numeros Impares:")

    a = 1

    while a < limit + 1:

        yield a

        a = a + 2

for num in num_impar(13):

    print(num)

# Fin de la tarea, como tal para esta vaina se recicla el codigo
# anterior usado para el par, pero cambian el valor de "a"