# Clase 28

# Los atributos son caracteristicas que tienen las clases

# Los metodos son acciones o cosas que sabe hacer la clase

# Clase Persona:
class LivingBeing:
    def __init__(self, name):

        self.name = name

class Person(LivingBeing):

    # Los atributos se inicializan en el contructor de la funcion:
    def __init__(self, name, age):
        
        # Atributos:
        super().__init__(name)
        self.age = age

    # Metodo:
    def greet(self):

        print("Hello! I am a person.")

class Student(Person):

    def __init__(self, name, age, student_id):
        super().__init__(name, age)

        self.student_id = student_id

    def greet(self):

        super().greet()
        print(f"Hello, my student ID is {self.student_id}.")

student = Student("Ana", 20, "S123")

student.greet()


# la verdad la profe hace esta clase en dos archivos, pero dado
# que en el segundo archivo lo unico que agrega es la clase Living
# pues solo pondre un solo archivo