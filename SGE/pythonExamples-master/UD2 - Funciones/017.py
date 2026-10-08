# Este código muestra cómo asignar múltiples valores
# a múltiples variables en Python.
def f(x, y):
    return x * 2, y * 2
a, b = f(1, 2)
# En este caso, 'a' será 2 y 'b' será 4.

def funcion():
    print ("Hola, mundo!")
funcion()
#sin return

#Ejemplo con parámetros opcionales
def mi_funcion(param1, param2="default2"):
    """
    Esta función toma un parámetro obligatorio y uno opcional.
    :param param1: Primer parámetro, obligatorio.
    :param param2: Segundo parámetro, opcional, por defecto "default2".
    :return: Producto de los dos parámetros.
    """
    return param1 * param2
print(mi_funcion("hola",2))#holahola
print(mi_funcion(param2=2, param1="hola")) #holahola

# Ejemplo con número variable de argumentos
def suma(*args):
    """
    Esta función suma un número variable de argumentos.
    :param args: Argumentos a sumar.
    :return: Suma de todos los argumentos.
    """
    return sum(args)
print(suma(1, 2, 3))  # Imprime 6

# Ejemplo con argumento como diccionario
def imprimir_info(**kwargs):
    """
    Esta función imprime información basada en argumentos nombrados.
    :param kwargs: Argumentos nombrados.
    """
    for key, value in kwargs.items():
        print(f"{key}: {value}")

imprimir_info(nombre="Juan", edad=30, ciudad="Madrid")