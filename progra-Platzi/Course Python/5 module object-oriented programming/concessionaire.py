# Ejercico de concesionario de vehiculos Clase 24

# Asiganacion de la clase como car
class car:

    # Definiendo la funcion "__init__" con sus propiedades (modelo, 
    # cantidad y precio)
    def __init__(self, model, amount, price):

        self.model = model # Modelo
        self.price = price # Precio
        self.amount = amount # Cantidad
        self.available = True # Disponible

    def update_availability(self): # Funcion para actualizar
        # automaticamente la disponibilidad de vehiculos

        self.available = self.amount > 0

    def check_availability(self): # Funcion para confirmar vehiculos
        # disponibles en el concesionario

        if self.amount == 0: # condicional para avisar q no hay

            print(f"No hay vehiculos: {self.model} disponibles.")

        elif self.amount == 1: # condicinal para mensaje en singular

            print(f"El vehiculo {self.model} esta en bodega.")

        elif self.amount > 1: # condicional para mensaje en plural

            print(f"Los vehiculos {self.model} estan en bodega.")

    def sell(self): # Funciono para ventas

        if self.amount > 0: # Si la cantidad es mayor a 0

            self.amount -= 1 # A la cantidad se le restara 1 e imprimira:

            print(f"Se ha realizado la venta del vehiculo: {self.model}")
            print(f"Quedan {self.amount} del modelo {self.model}")

        elif self.amount == 0: # En caso de que la cantidad sea igual a 0

            self.available = False # el caracter de Disponible será Falso
            
        self.update_availability() # llamado de la función para actualizar los datos


# creacion de los modelos
car1 = car("Carrito Yamaha G240", 20, 17000000)

# llamado de verificacion de vehiculos
car1.check_availability()

# venta de vehiculo
car1.sell()