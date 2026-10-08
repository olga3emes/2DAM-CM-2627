# Comprensión de lista
l = [1, 2, 3]
l2 = [n ** 2 for n in l]
l3 = [n for n in l if n%2==0]
#No haría falta la función filter
print(l2)  # Imprime [1, 4, 9]
print(l3)  # Imprime [2]
# Comprensión de diccionario
d = {n: n ** 2 for n in l}
print(d)  # Imprime {1: 1, 2: 4, 3: 9}
# Comprensión de conjunto
s = {n ** 2 for n in l}
print(s)  # Imprime {1, 4, 9}
# Comprensión de conjunto con condición
s2 = {n for n in l if n % 2 == 0}
print(s2)  # Imprime {2}
# Comprensión de generador
g = (n ** 2 for n in l)
print(list(g))  # Imprime [1, 4, 9]
# Comprensión de generador con condición
g2 = (n for n in l if n % 2 == 0)
print(list(g2))  # Imprime [2]
# Comprensión de lista con función
def cuadrado(n):
    return n ** 2
l5 = [cuadrado(n) for n in l]
print(l5)  # Imprime [1, 4, 9]
# Comprensión de generador con función
g4 = (cuadrado(n) for n in l)
print(list(g4))  # Imprime [1, 4, 9]
# Comprensión de generador con función y condición
g5 = (cuadrado(n) for n in l if n % 2 == 0)
print(list(g5))  # Imprime [4]
# Comprensión de lista anidada
l4 = [[i, j] for i in range(3) for j in range(2)]
print(l4)  # Imprime [[0, 0], [0, 1], [1, 0], [1, 1], [2, 0], [2, 1]]
# Comprensión de diccionario anidado
d2 = {i: {j: i * j for j in range(3)} for i in range(3)}
print(d2)  # Imprime {0: {0: 0, 1: 0, 2: 0}, 1: {0: 0, 1: 1, 2: 2}, 2: {0: 0, 1: 2, 2: 4}}
# Comprensión de conjunto anidado
s2 = {i * j for i in range(3) for j in range(2)}
print(s2)  # Imprime {0, 1, 2, 3, 4}
# Comprensión de generador anidado
g3 = (i * j for i in range(3) for j in range(2))
print(list(g3))  # Imprime [0, 0, 0, 1, 2, 3, 4]
# Comprensión de lista con función y condición
l6 = [cuadrado(n) for n in l if n % 2 == 0]
print(l6)  # Imprime [4]
# Comprensión de diccionario con función
d3 = {n: cuadrado(n) for n in l}
print(d3)  # Imprime {1: 1, 2: 4, 3: 9}
# Comprensión de conjunto con función
s3 = {cuadrado(n) for n in l}
print(s3)  # Imprime {1, 4, 9}
# Comprensión de lista con múltiples condiciones
l7 = [n ** 2 for n in l if n % 2 == 0 if n > 1]
print(l7)  # Imprime [4]
# Comprensión de diccionario con múltiples condiciones
d4 = {n: n ** 2 for n in l if n % 2 == 0 if n > 1}
print(d4)  # Imprime {2: 4}
# Comprensión de conjunto con múltiples condiciones
s4 = {n ** 2 for n in l if n % 2 == 0 if n > 1}
print(s4)  # Imprime {4}
# Comprensión de generador con múltiples condiciones
g6 = (n ** 2 for n in l if n % 2 == 0 if n > 1)
print(list(g6))  # Imprime [4]
# Comprensión de lista con función y múltiples condiciones
l8 = [cuadrado(n) for n in l if n % 2 == 0 if n > 1]
print(l8)  # Imprime [4]
# Comprensión de diccionario con función y múltiples condiciones
d5 = {n: cuadrado(n) for n in l if n % 2 == 0 if n > 1}
print(d5)  # Imprime {2: 4}