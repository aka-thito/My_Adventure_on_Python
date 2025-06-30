x = 5

if x > 5:

    print("X es mayor que 5")
    print("Estamos adentro del IF")
    
elif x == 5:

    print("X es igual que 5")

else:

    print("X es menor que 5")
    print("Estamos adentro del ELSE")

print("Estamos afuera")

# Condicionales con AND, OR y NOT

z = 15
y = 20

if z > 10 and y > 25:

    print("Z es mayor que 10 y Y es mayor que 15")

if z > 10 or y > 25:

    print("Z es mayor que 10 o Y es mayor que 25")

if not z > 10:
    
    print("Z no es mayor que 10") 

# Condicionales con Booleanos

is_member = True
age = 15

if is_member:
    if age >= 18:
        
        print("Tienes acceso ya que eres miembro y mayor o igual a 15 años")
    
    else:

        print("No tienes acceso por ser menor de edad")

else:
    
    print("No eres miembro y NO TIENES ACCESO")
