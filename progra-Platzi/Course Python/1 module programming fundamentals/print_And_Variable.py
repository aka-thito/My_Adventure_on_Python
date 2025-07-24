# yo mariquenado con print y variables.

hi = "Hola"
name = "Mateo"

print(hi + ' ' + name)

# sep crear un parametro de separacion para los demás argumentos
# que se imprimen

print("Hola", "Mundo", sep = " ")

# end es un parametro que permite el salto de linea lo que hace
# que cada llamado a print comience en una nueva linea

print("Hola", end = " ")
print("hermanita querida")

# tambien se puede usar print para mostrar el valor de las
# variables.

frase = "Nunca pares de aprender"
author = "Platzi"

print("Frase:", frase, "Autor:", author)

# f-strings permiten insertar expresiones dentro de cadenas de
# texto. Al anteponer una f a la cadena de texto, puedes incluir
# variables directamente dentro de las llaves {}

fraseLove = "Te ame como a nadie"
authorLove = "Mateo"

print(f"Frase: {fraseLove}, Autor: {authorLove}")

# format es otra forma de insertar valores en cadenas de texto.
# usando {} como marcadores de posició, puedes pasar los valores
# que quieras insertar como argumentos

saludo = "Buenos días"
nombre = "Mr.Marston"

print("{} {}".format(saludo, nombre))

# Puedes controlar el formato de los números al imrpimir.
# usando por ejemplo :2f que indica que el numero debe mostrar
# dos decimales. para asi imprimir 

valor = 3.123432
print("Valor: {:.2f}".format(valor))

# Para hacer saltos en lineas de Python se indica con la
# secuencia de escape \n

print("Hola\nBuenas tardes")

# para imprimir una cadena que contenga comillas simples o dobles
# dentro de ellas, debes usar secuencias de escape para evitar
# confusiones con la sintaxis de Python

print('Juls \'come monda\'')

# si necesitas imprimir una ruta de archivo, tendras que incluir
# \, también para usar la secuencia de escape correctamente para
# evitar problemas con la secuencia de escape

print("La ruta de archivo es: C:\\Users\\Usuario\\Desktop\\archivo.txt")

