a = [ 1,2,3,4,5 ]
b = a #basicamente la misma mrd de lista que tiene a

print(a)
print(b)

del a[0]

print(id(a)) # pues entiendo que acá se le asignan ids para a y b
print(id(b)) # que en teoria son la misma id por b ser igual que a

c = a[:]

print(id(a))
print(id(b))
print(id(c)) # luego se crea una id para C, haciendo referencia
# que la id de esta variable sera distinta y asi obteninedo una
# separacion de informacion entre las memorias 

a.append(6)
print(a)
print(b)
print(c)

# no entendi esta clase pero bueno