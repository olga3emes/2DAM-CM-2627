#BUCLES
# Ejemplo de bucle while
i=1
while i <= 5:
    print(i)
    i += 1

# Ejemplo de bucle for
for j in range(1, 6): #podemos poner un paso como 3er parámetro
    print(j)

# Ejemplo de bucle for con lista
lista = ['manzana', 'banana', 'cereza']
for fruta in lista:
    print(fruta)

# Ejemplo de bucle for con diccionario
diccionario = {'a': 1, 'b': 2, 'c': 3}
for clave, valor in diccionario.items():
    print(f'Clave: {clave}, Valor: {valor}')

# Ejemplo de bucle for con cadena
cadena = 'Hola'
for letra in cadena:
    print(letra)



   #traditional for

for i in range(0, len(lista)):
    print(lista[i])

# extended for = foreach de Java

for fruta in lista:
    print(fruta)