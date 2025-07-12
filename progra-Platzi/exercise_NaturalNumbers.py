# Recursividad
# EJERCICIO NUMEROS NATURALES

# definimos la funcion como la funcion del ejercicio:
def natural_num(n):
    if n <= 0:  # si el valor ingresado es igual o menor a 0

        return 0 # retornara 0
    
    elif n == 1: # si el valor ingresado resulta ser igual a 1 

        return 1 # retornara 1
    
    else: # en caso contrario de cumplir las anteriores reglas
        
        return n + natural_num(n - 1) # retornara el valor
    # ingresado sumando de forma consecutiva 

n = int(input("Ingrese un número entero: "))
print(f"La suma de números naturales hasta {n} es: {natural_num(n)}")