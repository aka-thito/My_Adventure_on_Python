# uso de try que en español significa intentar
try:
    
    #pass # con esta palabra reservada se le dice a la maquina
         # que haga un salto de este bloque.

    div = int(input("Ingresa un número entero:"))
    result = 100/div

    print(result)

except ZeroDivisionError as e: # acá se prevee un error por usuario
                          # donde pone 0 como si fuera un
                          # número entero

    #pass

    print("Error: El divisor no puede ser cero.")
    print("Ha ocurrido un error:", e)

except ValueError as e: # acá la excepcion anticipando que el 
                   # usuario ponga strings

    print("Error: Debes introducir un número válido")
    print("Ha ocurrido un error:", e)

# Esta clase enseña más exactamente como manejar excepciones en el
# codigo segun lo que busques hacer y tambien a crear excepciones
# que por lo q entiendo en programacion en Python, esta vaina se usa
# para hacer que el codigo no se vaya a la mrd (quiero creer) y 
# tambien tener una respuesta de la maquina ante estos errores que
# estan respaldados en el codigo, idk


# Ultimo apunte, segun la profe, se supone q entre más especifico
# seas con el error en los excepciones, te identificaras como un
# excelente programador, idk

# asi que supongo que no es tan practico usar una excepción que
# abarque otras de no requerirlo el codigo