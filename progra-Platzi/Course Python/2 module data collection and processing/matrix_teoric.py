separador = "HHHHHHHHHHHHHHHHHHHHHHHHHHH"

# las matricse son esenciales en computación y las matemáticas
# Python puede usar listas dentro de listas para representar matrices
# bidimensionales.

# Tablero de Ajedrez
# un tablero de ajedrez es una matriz de 8x8, se representa solo
# casillas blancas y negras, donde podemos usar las fichas, para
# estas usamos letras para cada ficha.

# P = Peon
# R = Torre
# N = Caballo
# B = Alfil
# Q = Reina
# K = Rey

# minuculas = Negras
# MAYUSCULAS = Blancas

# 0 = Casilla Vacia

chess_board = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p',],
    [0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0,],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P',],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
]

print(chess_board)
print(separador)

# Movimiento de Caballo

#En ajedrez, los caballos se mueven en forma de L,
# si el caballo es ficha blanca estara en (7, 1), las posiciones
# a las que podra moverse serán

# (5,0)
# (5,2)
# (6,3)

# Es importante verificar que estas posiciones estén dentro de
# los límites del tablero y no contengan piezas blancas.
# si movemos el caballo de (7,1) a (5,2) el tablero se vería asi:

chess_board[7][1] = 0 # Posición Original del caballo | Antigua
chess_board[5][2] = 'N' # Nueva posición del caballo

print(chess_board)

