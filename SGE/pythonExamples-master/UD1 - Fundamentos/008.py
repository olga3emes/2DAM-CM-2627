# Para poder iterar sobre una secuencia de números se puede utilizar
# la función range(), la cual genera un conjunto de números enteros.
#✍️ Investiga cómo funciona range()

# Ejemplo de bucle for con range
for i in range(1, 6):
    print(i)
# # Ejemplo de bucle for con range y paso
for j in range(1, 11, 2):  # Paso de 2
    print(j)
# # Ejemplo de bucle for con range y números negativos
for k in range(10, 0, -1):  # De 10 a 1
    print(k)
# # Ejemplo de bucle for con range y números negativos y paso
for l in range(10, -1, -2):  # De 10 a 0 con paso de -2
    print(l)
# # Ejemplo de bucle for con range y números negativos y paso
for n in range(-5, 6, 2):  # De -5 a 5 con paso de 2
    print(n)
