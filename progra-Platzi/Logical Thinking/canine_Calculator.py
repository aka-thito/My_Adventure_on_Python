# PASO 1: BIENVENIDA
print('Bienvenido a la calculadora perruna')
print('¿En qué unidad ingresará la edad del perro?')

# BUCLE PARA VALIDAR LA UNIDAD
while True:
    unidad = input('Ingrese A para años o M para meses: ')

    if unidad in ['A', 'M']:
        break
    else:
        print('La unidad es incorrecta, vuelva a ingresarla')

# PASO 2: SOLICITAR LA EDAD DEL PERRO
edad_perro = int(input('Ingrese la edad del perrito: '))

# SI LA UNIDAD ES EN MESES, LA CONVERTIMOS A AÑOS
if unidad == 'M':
    edad_perro = edad_perro/12

# PASO 3: DEFINIR LA CONVERSIÓN A AÑOS HUMANOS
match edad_perro:
    
    case x if x <= 0:
        print('La edad ingresada es inválida, ingrese un número mayor a 0')
    case x if x <= 1:
        edad_humana = edad_perro * 15
    case x if x <= 2:
        edad_humana = 15 + (x - 1) * 9
    case _:
        edad_humana = 15 + 9 + (edad_perro - 2) * 5


# PASO 4: MOSTRAR EL RESULTADO SI LA EDAD ERA VÁLIDA

if edad_perro > 0 :
    print(f'La edad equivalente en años humanos es: {round(edad_humana, 1)} años')
