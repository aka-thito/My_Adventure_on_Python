# Clase donde enseñan funciones

# Ejemplo 1
# para declarar una funcion se usa "def" seguido del nombre que tendra la funcion y (),
# en este caso "greet()"
def greet(name, last_name = "No tiene Apellido"):
    # se puede asignar una respuesta en los () de la funcion

    print ("Hola", name, last_name) # Esperara recibir los datos
    # name y last_name cuando se llame la funcion.

greet("Juan", "Moreno") # ejemplo donde se llama la funcion con
# normalidad asignando los datos

greet("Diego") # caso de no poner last_name

greet(last_name = "Florida", name = "Carli") # Tratando de desordenar
# los datos, igualmente imprimira en el orden en que se definio en
# la funcion