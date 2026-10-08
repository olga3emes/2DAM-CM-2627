# Funciones Lambda
# Funciones anónimas
#Ejemplo de función lambda

# Función lambda para sumar dos números
suma = lambda x, y: x + y
print(suma(3, 5))  # Imprime 8
# Función lambda para ordenar una lista de tuplas por el segundo elemento
lista_tuplas = [(1, 3), (2, 1), (3, 2)]
ordenada = sorted(lista_tuplas, key=lambda x: x[1])
print(ordenada)  # Imprime [(2, 1), (3, 2), (1, 3)]
# Función lambda para filtrar números pares de una lista
numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Imprime [2, 4, 6]
# Función lambda para aplicar una operación a cada elemento de una lista
numeros = [1, 2, 3, 4, 5]
doble = list(map(lambda x: x * 2, numeros))
print(doble)  # Imprime [2, 4, 6, 8, 10]

# Ejemplo de uso de la función filter con una función lambda
l = [1, 2, 3]
l2 = filter(lambda n: n % 2.0 == 0, l)
#Está restringido a una sola expresión
print(list(l2))  # Imprime [2]
# Ejemplo de uso de la función map con una función lambda
l3 = map(lambda n: n ** 2, l)
print(list(l3))  # Imprime [1, 4, 9]
# Ejemplo de uso de la función reduce con una función lambda
from functools import reduce
l4 = reduce(lambda a, b: a + b, l)
print(l4)  # Imprime 6
# Ejemplo de uso de la función zip con una función lambda
l5 = [1, 2, 3]
l6 = ['a', 'b', 'c']
l7 = zip(l5, l6)
print(list(l7))  # Imprime [(1, 'a'), (2, 'b'), (3, 'c')]

