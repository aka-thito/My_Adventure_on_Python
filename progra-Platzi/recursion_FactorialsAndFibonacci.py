# Recursividad: Factoriales y Serie Fibonacci

# FACTORIALES:
# para encontrar el factorial de N hay que encontrar el
# factorial de un caso menor (N - 1), los procesos factoriales
# tienen dos situales siones CASO BASE y CASO RECURSIVO

# CASO BASE: N = 0

# CASO RECURSIVO N > 0

# proceso factorial en codigo:
def fact(n): 
    
    if n == 0:

        return 1
    
    else:

        return n * fact(n-1)

fact_5 = print(fact(5))

# SERIE FIBONACCI
# La secuencia fibonacci inicia simpre entre la suma de 0 y 1,
# para luego proceder a sumar el resultado con el numero de
# mayor valor anterior.
# ejmplo:
# 0 + 1 = 1 + 2 = 3 + 2 = 5, etc...

# CASO BASE: F(0) = 0, F(1) = 1

# CASO RECURSIVO: F(N - 1) + F(N - 2)

# serie fibonacci en codigo:

def fibonacci(n):

    if n == 0:
        
        return 0
    
    elif n == 1:

        return 1
    
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
number = 4
print(fibonacci(number))

# una disculpa si soy malo con mis comentarios y explicaciones
# ¯\_(ツ)_/¯