# Ejemplo 2 de la clase de function teoric

# declaracion de funciones de operaciones que tendra la calculadora
def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# declaracion de funcion calculadora
def calculator():
    while True:

        # impresion de opciones que puede opearar la calculadora
        print("Seleccione una operación")
        print("1. Suma:")
        print("2. Resta:")
        print("3. Multiplicación:")
        print("4. División:")
        print("5. Salir")

        # variable option definida a la respuesta del usuario ante
        # la impresion de las opciones
        option = input("Ingrese su opción (1, 2, 3, 4, 5): ")

        # si la respuesta es 5, se apagara la calculadora
        if option == "5":

            print("Saliendo de la Calculadora")
            break

        # si la respuesta esta entre 1 y 4, ejecutara la opcion en
        # especifico que se menciono de ante mano
        if option in ["1", "2", "3", "4"]:
            
            num1 = float(input("Ingrese el primer numero: "))
            num2 = float(input("Ingrese el segundo numero: "))

            # suma
            if option == "1":
                
                print ("La suma es:", add(num1, num2))

            # resta
            elif option == "2":

                print("La resta es:", substract(num1, num2))

            # multiplica
            elif option == "3":

                print("La Multiplicación es:", multiply(num1, num2))

            # divide
            elif option == "4":

                print("La división es:", divide(num1, num2))

        # mientras responda con opciones no validas (anteriormente 
        # mencionadas), ejecutara lo siguiente
        else:

            print("Opción no válida, por favor intenta de nuevo")
        

calculator()
