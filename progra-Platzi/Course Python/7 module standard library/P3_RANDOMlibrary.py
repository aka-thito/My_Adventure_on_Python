# Clase 34 P3 RANDOM

import random

# Generar un numero entero aleatorio
random_number = random.randint(1, 10) 

print(random_number)

# Elegir colores aleatorios
colors = ['Rojo', 'Azul', 'Amarillo']
random_colors = random.choice(colors)

print(random_colors)

# Barajar una lista de cartas
cards = ['As', 'Rey', 'Reina', 'Jota', '10']
random.shuffle(cards)

print(cards)
