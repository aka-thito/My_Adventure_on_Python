# el input se usa para solicitar informacion al usuario

name = input("Ingrese su nombre:")
print(name)
print(type(name))
# En este primer ejemplo lo que se hace es solicitar
# un nombre, lo normal seria recibir un valor de 
# tipo string, en todo caso con "print(type(name))"
# lo que se hace es pedirle a la maquina detectar
# que tipo o a que clase pertenece dentro de Python

age = int(input("Ingrese su edad:"))
print(age)
print(type(age))

age2 = float(input("Ingrese su edad:"))
print(age2)
print(type(age2))