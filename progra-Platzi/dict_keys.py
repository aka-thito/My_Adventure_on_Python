# Diccionarios y Manipulacion de Datos

numbers = {1: "uno", 2: "dos", 3: "tres"}

print(numbers[2])

# diccionario de carla, esto es más como describir un objeto 
# o asi lo entiendo
information = {"Name": "Carla",
               "Last_Name": "Moreno",
               "Height": 1.50,
               "Age": 40}

print(information)

# con esto elimina la caracteristica de edad del objeto descrito
# anteriormente en el diccionario
del information["Age"]

print(information)

pasword = information.keys()

print(pasword)
print(type(pasword)) # Metodo keys

values = information.values()

print(values)

pairs = information.items()

print(pairs)

# diccionario de contactos
contacts = {
    "Carla": {"Name": "Carla",
               "Last_Name": "Moreno",
               "Height": 1.50,
               "Age": 40},

              "Diego": {"Name": "Diego",
               "Last_Name": "Alvira",
               "Height": 1.80,
               "Age": 20},
               
              "Mario": {"Name": "Mario",
               "Last_Name": "Perez",
               "Height": 1.70,
               "Age": 30}
}

print(contacts["Mario"])