# Ejercicio / Reto Clase 15

# hacer un juego de piedra papel o tijeras

import random

# Variables
options = ("piedra", "papel", "tijera")
winner = []

# Ingreso del nombre del usuario
user = input("Ingrese su Nombre:")
print(f"Bienvenid@ {user}, vamos a jugar!")

# Función para definir el ganador del juego
def DefinitWinner(player, ia):
    
    if player == ia:
        
        return "empate"
    
    elif (player == "piedra" and ia == "tijera") or \
         (player == "papel" and ia == "piedra") or \
         (player == "tijera" and ia == "papel"):
        
        return "player"
    
    else:

        return "ia"
    
#Cilco para evitar errores y tener un ganador
while True:

    player = input(f"{user}, elige piedra, papel o tijera ('salir' para dejar de jugar): ")

    if player == "salir":

        print(f"{user} gracias por jugar, hasta pronto!")
        break

    if player not in options:
        
        print("Opción inválida, elige una de las opciones")
        continue

    else:

        print(f"{user} eligió: {player}")

    # Elección de la máquina
    ia = random.choice(options)
    print(f"La elección de la maquina fue: {ia}")

    # Determinar el ganador
    print(f"El ganador es: {DefinitWinner(player, ia)}")
    winner.append(DefinitWinner(player, ia))

# Ganador acorde a la lista de resultados
print(winner)
print(f"{user} ganó {winner.count('player')} partidas")
print(f"La máquina ganó {winner.count('ia')} partidas")
print(f"Total de Empates {winner.count('empate')}")

# Retornar valor de victorias
if winner.count('player') > winner.count('ia'):

    print(f"El ganador es: {user}")
    
elif winner.count('player') < winner.count('ia'):

    print(f"El ganador definitivo es: la máquina")

else:
    print("El juego terminó en Empate")