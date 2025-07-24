# Primer ejemplo de la primera clase 23 del curso en el modulo 5

class Person:
    
    def __init__(self, name, age):
    # "__init__" es un constructo, los constructo son una funcion
    # de las clases en estas se definen los atributos principales

    # teorizando y traduciendo self significa ser, apesar de que se
    # asigne como parametro dentro del constructo, este solo hace
    # de puente para definir los atributos, eso creo ¯\_(ツ)_/¯

    # en este caso nombre y edad

        self.name = name
        self.age = age

    def greet(self):

        print(f"Hola, mi nombre es {self.name} y tengo {self.age}")

persona1 = Person("Ana", 30)
persona2 = Person("Luis", 25)

persona1.greet()
persona2.greet()

# Primera parte de la clase 23 de Programación Orientada a Objetos
# Clases y Métodos Básicos