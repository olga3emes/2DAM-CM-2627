import math

# Calcular el área de un círculo con radio 5
radio = 5
area = math.pi * math.pow(radio, 2)
print(f"Área del círculo: {area:.2f}")  # Área del círculo: 78.54
#.2f -> con dos decimales

# Calcular la hipotenusa de un triángulo rectángulo con lados 3 y 4
hipotenusa = math.sqrt(math.pow(3, 2) + math.pow(4, 2))
print(f"Hipotenusa: {hipotenusa}")  # Hipotenusa: 5.0

# Redondear un número
print(math.floor(3.9))  # 3
print(math.ceil(3.1))   # 4

# Calcular el logaritmo natural de un número
print(math.log(10))  # Logaritmo natural de 10: 2.302585092994046

# Calcular el logaritmo en base 10 de un número
print(math.log10(100))  # Logaritmo en base 10 de 100: 2.0

# Calcular el seno, coseno y tangente de un ángulo en radianes
angulo = math.radians(30)  # Convertir 30 grados a radianes
print(f"Seno de 30 grados: {math.sin(angulo)}")  # Seno de 30 grados: 0.49999999999999994
print(f"Coseno de 30 grados: {math.cos(angulo)}")  # Coseno de 30 grados: 0.8660254037844387
print(f"Tangente de 30 grados: {math.tan(angulo)}")  # Tangente de 30 grados: 0.5773502691896257

# Calcular el valor absoluto de un número
print(abs(-5))  # Valor absoluto de -5: 5

# Calcular el factorial de un número
print(math.factorial(5))  # Factorial de 5: 120

# Calcular la raíz cuadrada de un número
print(math.sqrt(16))  # Raíz cuadrada de 16: 4.0

# Calcular el máximo y mínimo de una lista de números
numeros = [1, 2, 3, 4, 5]
print(f"Máximo: {max(numeros)}")  # Máximo: 5
print(f"Mínimo: {min(numeros)}")  # Mínimo: 1
# Calcular el valor de e elevado a la potencia de un número
print(math.exp(1))  # e elevado a la potencia de 1: 2.718281828459045
# Calcular el valor de pi
print(math.pi)  # Valor de pi: 3.141592653589793
# Calcular el valor de e
print(math.e)  # Valor de e: 2.718281828459045
# Calcular el coseno hiperbólico de un número
print(math.cosh(1))  # Coseno hiperbólico de 1: 1.5430806348152437
# Calcular el seno hiperbólico de un número
print(math.sinh(1))  # Seno hiperbólico de 1: 1.1752011936438014
# Calcular la tangente hiperbólica de un número
print(math.tanh(1))  # Tangente hiperbólica de 1: 0.7615941559557649
# Calcular el arco seno de un número
print(math.asin(0.5))  # Arco seno de 0.5: 0.5235987755982989 (30 grados en radianes)
# Calcular el arco coseno de un número
print(math.acos(0.5))  # Arco coseno de 0.5: 1.0471975511965979 (60 grados en radianes)
# Calcular el arco tangente de un número
print(math.atan(1))  # Arco tangente de 1: 0.7853981633974483 (45 grados en radianes)
# Calcular el arco tangente de dos números
print(math.atan2(1, 1))  # Arco tangente de 1/1: 0.7853981633974483 (45 grados en radianes)
# Calcular el valor de un número elevado a la potencia de otro
print(math.pow(2, 3))  # 2 elevado a la potencia de 3: 8.0
# Calcular el logaritmo de un número en una base específica
print(math.log(100, 10))  # Logaritmo de 100 en base 10: 2.0
# Calcular el valor de un número elevado a la potencia de e
print(math.exp(2))  # e elevado a la potencia de 2: 7.3890560989306495
# Calcular el logaritmo natural de un número con una base específica
print(math.log(100, 10))  # Logaritmo natural de 100 en base 10: 2.0
# Calcular el logaritmo en base 2 de un número
print(math.log2(8))  # Logaritmo en base 2 de 8: 3.0
# Calcular el valor de un número elevado a la potencia de 0.5 (raíz cuadrada)
print(math.pow(16, 0.5))  # 16 elevado a la potencia de 0.5: 4.0
# Calcular el valor de un número elevado a la potencia de -1 (inverso)
print(math.pow(2, -1))  # 2 elevado a la potencia de -1: 0.5
# Calcular el logaritmo en base 2 de un número
print(math.log2(16))  # Logaritmo en base 2 de 16: 4.0
# Calcular el logaritmo en base 10 de un número
print(math.log10(1000))  # Logaritmo en base 10 de 1000: 3.0
# Calcular el valor de un número elevado a la potencia de 1/3 (raíz cúbica)
print(math.pow(27, 1/3))  # 27 elevado a la potencia de 1/3: 3.0
# Calcular el valor de un número elevado a la potencia de 2 (cuadrado)
print(math.pow(5, 2))  # 5 elevado a la potencia de 2: 25.0
# Calcular el valor de un número elevado a la potencia de 3 (cubo)
print(math.pow(3, 3))  # 3 elevado a la potencia de 3: 27.0
