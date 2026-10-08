#Funciones de orden superior (las hemos visto)
from functools import reduce, lru_cache
# Reduce: suma de todos los elementos
numeros = [1, 2, 3, 4]
suma = reduce(lambda x, y: x + y, numeros)
print("Suma total:", suma)
# Memoización con lru_cache
@lru_cache(maxsize=None)
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)
print("Factorial(5):", factorial(5))

#funciones equivalentes a operadores
import operator
a, b = 10, 3
print("Suma:", operator.add(a, b))
print("Multiplicación:", operator.mul(a, b))
print("Mayor que:", operator.gt(a, b))

import itertools
# Producto cartesiano
prod = list(itertools.product([1, 2], ['a', 'b']))
print("Producto cartesiano:", prod)
#[(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]
# Combinaciones
comb = list(itertools.combinations([1, 2, 3], 2))
print("Combinaciones:", comb) #[(1, 2), (1, 3), (2, 3)]
# Ciclo infinito
ciclo = itertools.cycle("AB")
for _ in range(4):
    print(next(ciclo), end=" ")  # A B A B
print()

#Dataclasses
from dataclasses import dataclass
@dataclass
class Persona:
    nombre: str
    edad: int
p = Persona("Lucía", 30)
print("Persona:", p.nombre, p.edad)

