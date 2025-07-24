# Segundo ejemplo de la primera clase 23 del curso en el modulo 5

# Definición de la clase
class BankAccount:

    # Método constructor que iniciliza los atributos de la cuenta
    def __init__(self, account_holder, balance):

        self.account_holder = account_holder # Nombre del titular
        self.balance = balance               # Saldo inicial
        self.is_active = True                # Estado de cuenta

    # Método para depositar dinero en la cuenta
    def deposit(self, amount):

        # Condicional que verifica que este activa para depositar
        if self.is_active:

            self.balance += amount
            print(f"Se ha depositado {amount}. Saldo actual {self.balance}")

        else:

            print("No se puede depositar, Cuenta inactiva")

    # Método para retirar dinero de la cuenta
    def withdraw(self, amount):

        if self.active:

            if amount <= self.balance: # verifica que haya suficiente
                                       # saldo

                self.balance -= amount 

                print(f"Se ha retirado {amount}, Saldo actual {self.balance}")

    # Método para desactivar cuenta
    def deactive_account(self):
        
        self.is_active = False

        print(f"La cuenta ha sido desactivada")

    # Método para activar cuenta
    def activate_account(self):

        self.is_active = True

        print(f"La cuenta ha sido activada")

# creacion de dos cuentas 
account1 = BankAccount("Ana", 500)
account2 = BankAccount("Domingo", 1000)

# Llamada a los metodos

account1.deposit(200)
account2.deposit(100)

account1.deactive_account()
account1.deposit(50)

account1.activate_account()
account1.deposit(50)