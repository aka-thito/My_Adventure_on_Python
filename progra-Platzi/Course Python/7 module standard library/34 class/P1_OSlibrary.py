# Clase 34 P1 OS

import os

# Obtener el directorio actual
"""cwd = os.getcwd() # Current Working Directory

print("Directorio de trabajo actual", cwd)"""

# Listar los archivos .txt

txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]

print("Archivos txt:", txt_files) # No imprimira nada, no tengo un
                                  # .txt xD

# Renombrar archivo
os.rename('caperucita.txt', 'cuento.txt')

print('Archivo renombrado')

txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]

print("Archivos txt:", txt_files) 

