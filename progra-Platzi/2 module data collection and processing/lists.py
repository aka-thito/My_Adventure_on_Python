to_do = ["Dirigirnos al hotel", 
         "Ir a almorzar",
         "Visitar un museo",
         "Volver al hotel"] #Primer ejemplo de lista

print(to_do)

numbers = [1, 2, 3, 4, "cinco"]
print(type(numbers)) #Python reconoce este tipo como lista

mix = ["uno", 2, 3.14, True, [1, 2, 3]]
print(mix)
print(len(mix))
print("Primer elemento:", mix[0])
print("Segundo elemento:", mix[1])
print("Ultimo elemento:", mix[-1])

string = "Hola Mundo"
print("Primer elemento:", string[0])
print("Segundo elemento:", string[1])
print("Ultimo elemento:", string[-1])


print(mix[2:-2]) #cuando el numero que le sigue al : es negativo
# quiere decir que tomara los ultimos caracteres

print(mix)
mix.append(False)
print(mix)
mix.append(["a", "b"])
print(mix)
mix.insert(1, ["a", "b"])
print(mix) 
print(mix.index(["a", "b"]))
print(mix)

numbers = [ 1,2,100,90.45,3,4,5 ]

print("Mayor:", max(numbers))
print("Menor:", min(numbers))

del numbers[-1]
print(numbers)
del numbers[:2] #Algo que olvide, cuando se usa el : quiere decir
print(numbers) # que es la posicion 0 y el numero que le sigue
# es hasta que posicion llegará

del numbers
print(numbers) #Tira error pq ya no existe la informacion de la
# lista
