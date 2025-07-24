# Codigo de los recursos de la clase 22 - Arbol de excepciones

def print_exception_tree(exception_class, indent = 0): 
    # "exception_class" esta siendo usado para definir la clase base
    # de jerarquia

    # "Ident = 0" es el número que indica cuantos espacios usará para
    # la sangria al imprimir, basicamente se usa para mostrar la
    # jerarquía visualmente
    
    print(' ' * indent + exception_class.__name__)

    # "exception_class.__name__" Imprimirá el nombre de la clase 
    # actual, procedido de el número igual al valor de "ident"

    for subclass in exception_class.__subclasses__():
    # "__subclasses__()" es un método especial que devuelve todas
        # las clases que se heredan de "exception_class"

        print_exception_tree(subclass, indent + 4)

        # Aumenta la sangría (indent) en 4 espacios

print_exception_tree(Exception)

# Pregunte a CHATGPT pa' entender este codigo
# 1. no sabia de donde saco el ".__name__" en la primera impresion
# 2. Recorde que la sangria eran los espacios que hay al inicio de las
#    lineas de codigo
