# Clase 25

class Vehicle:
    
    def __init__(self, brand, model, price):

        # Encapsulamiento
        # es la estructura de las variables de instacia que contienen
        # los caracteres privados del objeto
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True

    def sell(self):

        if self.is_available:

            self.is_available = False

            print(f"El vehiculo {self.brand}. Ha sido vendido")
        
        else:

            print(f"El vehiculo {self.brand}. No está disponible")
        
    # Abstracción
    # para acceder a las variables de isntacia solo se puede mediante
    # los metodos de verficación (check) y conseguir (get)
    def check_available(self):
        
        return self.is_available
    
    def get_price(self): # Cuando se quiere usar el retorno de un parametro
        # es comun que se use Get en la variable

        return self.price
    
    def start_engine(self):

        raise NotImplementedError("Este metodo debe ser implementado por la subclase")
    
    def stop_engine(self):
        
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")
    
# Herencia
# Es la forma en que un objeto adquiere propiedades del primer modelo
# diseñado, en este caso el carro (Car) esta heredando los caracteres de la
# clase padre vehiculo (Vehicle)
class Car(Vehicle):
        
    # Polimorfismo
    # parasece que hace referencia a que podemos tener muchas formas
    # pero un comportamiento diferente, en este caso el comportamiento
    # del auto era decir que el motor del auto estaba en funcion, en
    # cambio en la bicicleta tenemos otro comportamiento al no tener
    # motor.
    def start_engine(self):

        if not self.is_available:

            return f"El motor del carro {self.brand} está en marcha"
            
        else:

            return f"El carro {self.brand} no está disponible"
            
    def stop_engine(self):

        if self.is_available:

            return f"El motor del carro {self.brand} se ha detenido"
            
        else:

            return f"El carro {self.brand} No está disponible"
            
# Clase 26

class Bike(Vehicle):
        
    def start_engine(self):

        if not self.is_available:

            return f"La bicicleta {self.brand} está en marcha"
            
        else:

            return f"La bicicleta {self.brand} no está disponible"
            
    def stop_engine(self):
            
        if self.is_available:

            return f"La bicicleta {self.brand} se ha detenido"
            
        else:

            return f"La bicicleta {self.brand} No está disponible"
    
class Truck(Vehicle):

    def start_engine(self):

        if not self.is_available:

            return f"El motor del camión {self.brand} está en marcha"
            
        else:

            return f"El camión {self.brand} no está disponible"
            
    def stop_engine(self):
            
        if self.is_available:

            return f"El motor del camión {self.brand} se ha detenido"
            
        else:

            return f"El camión {self.brand} No está disponible"
        
class Customer:

    def __init__(self, name):

        self.name = name
        self.purchased_vehicles = []

    def buy_vehicle(self, vehicle: Vehicle):

        if vehicle.check_available():

            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
        
        else:

            print(f"Lo siento, {vehicle.brand} non está disponible")
    
    def inquire_vehicle(self, vehicle: Vehicle):

        if vehicle.check_available():

            availablity = "Disponible"
        
        else:

            availablity = "No disponible"
        
        print(f"El {vehicle.brand} está {availablity} y cuesta {vehicle.get_price()}.")

class Dealership:

    def __init__ (self):

        self.inventory = []
        self.customers = []
    
    def add_vehicles(self, vehicle: Vehicle):

        self.inventory.append(vehicle)

        print(f"El {vehicle.brand} ha sido añadido al inventario")

    def register_customers(self, customer: Customer):

        self.customers.append(customer)

        print(f"El cliente {customer.name} ha sido añadido")

    def show_available_vehicle(self):
        
        print("Vehiculos disponibles en la tienda")

        for vehicle in self.inventory:

            if vehicle.check_available():

                print(f"- {vehicle.brand} por {vehicle.get_price()}")

# Clase 27

# Explican algo de:
# Abstrapción
# Capsulamiento
# Polimorfismo

car1 = Car("Toyota", "Corolla", 20000)
bike1 = Bike("Yamaha", "MT-02", 800)
truck1 = Truck("Volvo", "FH16", 100000)

customer1 = Customer("Carlos")

dealership = Dealership()
dealership.add_vehicles(car1)
dealership.add_vehicles(bike1)
dealership.add_vehicles(truck1)

# Mostrar vehiculos disponibles

dealership.show_available_vehicle()

# Cliente consultar un vehiculo

customer1.inquire_vehicle(car1)

# Cliente comprar un vehiculo

customer1.buy_vehicle(car1)

# mostrar vehiculos otra vez
dealership.show_available_vehicle()

# Nota
# La profe dice que un ejercicio practico como programador es observar
# el entorno para identificar las clases y las instancias que se pueden
# sacar de esto
