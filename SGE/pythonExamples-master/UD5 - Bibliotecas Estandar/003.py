#Matemáticas - cálculo y álgebra
import math
print("Raíz cuadrada de 25:", math.sqrt(25))
print("Seno de 90°:", math.sin(math.radians(90)))
print("Factorial de 5:", math.factorial(5))
print("Constante π:", math.pi)

#Números complejos
import cmath
z = complex(3, 4)
print("Módulo:", abs(z))
print("Fase:", cmath.phase(z))
print("Raíz cuadrada de -1:", cmath.sqrt(-1))  # Resultado: 1j

#Trabajar con decimales de alta precisión - Bancos, económicas, etc.
from decimal import Decimal, getcontext
getcontext().prec = 6  # Precisión de 6 cifras decimales
a = Decimal("1") / Decimal("7")
print("Decimal con alta precisión:", a)

#Trabajar con fracciones
from fractions import Fraction
f1 = Fraction(1, 3)
f2 = Fraction(2, 5)
resultado = f1 + f2
print("Suma de fracciones:", resultado)
# Resultado: 11/15

import random
print("Número aleatorio entre 1 y 10:", random.randint(1, 10))
print("Elemento aleatorio:", random.choice(["manzana", "pera", "uva"]))
print("Lista barajada:")
lista = [1, 2, 3, 4]
random.shuffle(lista)
print(lista)

import statistics
datos = [1, 2, 3, 4, 4, 5]
print("Media:", statistics.mean(datos))
print("Mediana:", statistics.median(datos))
print("Moda:", statistics.mode(datos))
print("Desviación estándar:", statistics.stdev(datos))

