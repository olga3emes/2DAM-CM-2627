## Ejemplo de uso de la función map para aplicar una función a cada elemento de una lista
def cuadrado(n):
    return n ** 2
l = [1, 2, 3]
l2 = map(cuadrado, l)
print (list(l2)) # Imprime [1, 4, 9]
print (type(l2)) # <class 'map'>

# Ejemplo de uso de la función filter para filtrar elementos de una lista
def es_par(n):
    return n % 2 == 0
l = [1, 2, 3]
l3 = filter(es_par, l)
print (list(l3)) # Imprime [2]
print (type(l3)) # <class 'filter'>

# Ejemplo de uso de la función reduce para reducir una lista a un único valor
from functools import reduce
def suma(a, b):
    return a + b
l = [1, 2, 3]
l4 = reduce(suma, l)
print(l4)  # Imprime 6
print(type(l4)) # <class 'int'>

# Ejemplo de uso de la función zip para combinar dos listas en una lista de tuplas
l5 = [1, 2, 3]
l6 = ['a', 'b', 'c']
l7 = zip(l5, l6)
print(list(l7))  # Imprime [(1, 'a'), (2, 'b'), (3, 'c')]

# Ejemplo de uso de la función sorted para ordenar una lista
l8 = [3, 1, 2]
l9 = sorted(l8)
print(l9)  # Imprime [1, 2, 3]

# Ejemplo de uso de la función any para verificar si al menos un elemento es verdadero
l10 = [0, 1, 2]
l11 = any(l10)
print(l11)  # Imprime True, ya que hay elementos verdaderos en la lista

# Ejemplo de uso de la función all para verificar si todos los elementos son verdaderos
l12 = [1, 2, 3]
l13 = all(l12)
print(l13)  # Imprime True, ya que todos los elementos son verdaderos

# Ejemplo de uso de la función enumerate para obtener índices y valores de una lista
l14 = ['a', 'b', 'c']
for index, value in enumerate(l14):
    print(f"Índice: {index}, Valor: {value}")

# Ejemplo de uso de la función reversed para invertir una lista
l15 = [1, 2, 3]
l16 = list(reversed(l15))
print(l16)  # Imprime [3, 2, 1]

