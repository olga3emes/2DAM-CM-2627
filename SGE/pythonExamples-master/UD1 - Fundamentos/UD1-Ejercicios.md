# Ejercicios - Fundamentos de Python - 100 ejercicios resueltos

 Ejercicios para practicar los fundamentos de Python, incluyendo variables, tipos de datos, estructuras de control y más.
## Ejercicios

###  1. **Hola Mundo**
 Crea un programa que imprima "¡Hola, Mundo!" en la consola.
```python
print("¡Hola, Mundo!")
```
###  2. **Variables y Tipos de Datos**
 Crea variables de diferentes tipos de datos (entero, flotante, cadena, booleano) y muestra su tipo.
```python 
entero = 42
flotante = 3.14
cadena = "Python"
booleano = True
print(type(entero))    ### <class 'int'>
print(type(flotante))  ### <class 'float'>
print(type(cadena))    ### <class 'str'>
print(type(booleano))  ### <class 'bool'>
```

###  3. **Operaciones Aritméticas**
 Crea un programa que realice las siguientes operaciones aritméticas y muestre los resultados:
- Suma de dos números
```python 
def suma(a, b):
    return a + b
print(suma(5, 3))  # Resultado: 8
```
 - Resta de dos números
```python 
def resta(a, b):
    return a - b
print(resta(5, 3))  # Resultado: 2
```
 - Multiplicación de dos números
```python 
def multiplicacion(a, b):
    return a * b
print(multiplicacion(5, 3))  # Resultado: 15
```
 - División de dos números
```python 
def division(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b
print(division(5, 3))  # Resultado: 1.6666666666666667
```

###  4. **Condicionales**
 Crea un programa que verifique si un número es par o impar.
```python 
def es_par(numero):
    return numero % 2 == 0
print(es_par(4))  # Resultado: True
print(es_par(5))  # Resultado: False
```

###  5. **Bucles**
 Crea un programa que imprima los números del 1 al 10 utilizando un bucle `for`.
```python
for i in range(1, 11):
    print(i)
```
###  6. **Listas**
 Crea una lista de números y realiza las siguientes operaciones:
`numeros = [1, 2, 3, 4, 5]`
 - Añadir un número al final de la lista
```python 
def añadir_numero(lista, numero):
    lista.append(numero)
    return lista
numeros = [1, 2, 3, 4, 5]
print(añadir_numero(numeros, 6))  # Resultado: [1, 2, 3, 4, 5, 6]
```
 - Eliminar un número de la lista
```python 
def eliminar_numero(lista, numero):
    if numero in lista:
        lista.remove(numero)
    return lista
numeros = [1, 2, 3, 4, 5, 6]
print(eliminar_numero(numeros, 3))  # Resultado: [1, 2, 4, 5, 6]
```
 - Ordenar la lista
```python 
def ordenar_lista(lista):
    return sorted(lista)
numeros = [5, 2, 4, 1, 6]
print(ordenar_lista(numeros))  # Resultado: [1, 2, 4, 5, 6]
 ```

###  7. **Diccionarios**
 Crea un diccionario con información de una persona (nombre, edad, ciudad) y muestra sus valores.
```python 
def crear_diccionario(nombre, edad, ciudad):
    return {'nombre': nombre, 'edad': edad, 'ciudad': ciudad}
persona = crear_diccionario("Juan", 30, "Madrid")
print(persona)  # Resultado: {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid'}```
```
###   8. **Funciones**
 Crea una función que reciba dos números y retorne su máximo común divisor (MCD).
```python 
def mcd(a, b):
    while b:
        a, b = b, a % b
    return a
print(mcd(48, 18))  # Resultado: 6```
```
###   9. **Excepciones**
 Crea un programa que solicite un número al usuario y maneje la excepción si el usuario ingresa un valor no numérico.
```python 
def solicitar_numero():
    try:
        numero = int(input("Introduce un número: "))
        return numero
    except ValueError:
        return "Error: Debes introducir un número válido."
print(solicitar_numero())  ### Si se introduce un número, lo mostrará; si no, mostrará el error.```
```
###   10. **Sumar Elementos de una Lista**
 Dada una lista de números, utiliza la función `sum()` para calcular la suma de todos sus elementos.
```python 
def sumar_lista(lista):
    return sum(lista)
numeros = [1, 2, 3, 4, 5]
print(sumar_lista(numeros))  # Resultado: 15```
```
###   11. **Ordenar una Lista de Tuplas**
 Dada una lista de tuplas, ordena las tuplas por el segundo elemento de cada una.
```python 
def ordenar_tuplas(tuplas):
    return sorted(tuplas, key=lambda x: x[1])  ### Ordena por el segundo elemento de cada tupla
tuplas = [(1, 3), (2, 1), (3, 2)]
print(ordenar_tuplas(tuplas))  # Resultado: [(2, 1), (3, 2), (1, 3)]```
```
###   12. **Contar Vocales en una Cadena**
 Crea una función que cuente la cantidad de vocales en una cadena de texto.
```python 
def contar_vocales(cadena):
    return sum(1 for char in cadena.lower() if char in 'aeiou')
cadena = "Hola Mundo"
print(contar_vocales(cadena))  # Resultado: 4 (o, a, u, o)```
```
###   13. **Invertir una Cadena**
 Crea una función que reciba una cadena y retorne la cadena invertida.
```python 
def invertir_cadena(cadena):
    return cadena[::-1]
cadena = "Python"
print(invertir_cadena(cadena))  # Resultado: "nohtyP"```
```
###   14. **Encontrar el Elemento Más Grande en una Lista**
 Crea una función que reciba una lista de números y retorne el número más grande.
```python 
def encontrar_mayor(lista):
    return max(lista)
lista_numeros = [1, 5, 3, 9, 2]
print(encontrar_mayor(lista_numeros))  # Resultado: 9
 ```

###   15. **Calcular el Factorial de un Número**
 Crea una función que calcule el factorial de un número dado.
```python 
def factorial(n):
    if n < 0:
        return "Error: El factorial no está definido para números negativos."
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado
print(factorial(5))  # Resultado: 120
 ```

###   16. **Comprobar si una Cadena es un Palíndromo**
 Crea una función que verifique si una cadena es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
```python 
def es_palindromo(cadena):
    cadena = cadena.lower().replace(" ", "")
    return cadena == cadena[::-1]
cadena = "Anita lava la tina"
print(es_palindromo(cadena))  # Resultado: True

```
###    17. **Generar una Lista de Números Pares**
 Crea una función que genere una lista de números pares desde 2 hasta un número dado.
```python 
def generar_pares(n):
    return [i for i in range(2, n + 1, 2)]
print(generar_pares(10))  # Resultado: [2, 4, 6, 8, 10]
 ```

###     18. **Contar Palabras en una Cadena**
 Crea una función que cuente la cantidad de palabras en una cadena de texto.
```python 
def contar_palabras(cadena):
    return len(cadena.split())
cadena = "Hola mundo, ¿cómo estás?"
print(contar_palabras(cadena))  # Resultado: 5
```

###   19. **Calcular la Media de una Lista de Números**
 Crea una función que calcule la media (promedio) de una lista de números.
```python 
def calcular_media(lista):
    if not lista:
        return "Error: La lista está vacía."
    return sum(lista) / len(lista)
lista_numeros = [10, 20, 30, 40, 50]
print(calcular_media(lista_numeros))  # Resultado: 30.0
```

###   20. **Convertir una Lista de Cadenas a Mayúsculas**
Crea una función que convierta todas las cadenas de una lista a mayúsculas.
```python 
def convertir_mayusculas(lista):
    return [cadena.upper() for cadena in lista]
lista_cadenas = ["hola", "mundo", "python"]
print(convertir_mayusculas(lista_cadenas))  # Resultado: ['HOLA', 'MUNDO', 'PYTHON']
```

###   21. **Eliminar Duplicados de una Lista**
Crea una función que elimine los elementos duplicados de una lista.
```python 
def eliminar_duplicados(lista):
    return list(set(lista))
lista_con_duplicados = [1, 2, 2, 3, 4, 4, 5]
print(eliminar_duplicados(lista_con_duplicados))  # Resultado: [1, 2, 3, 4, 5]
```

###   22. **Encontrar el Elemento Común en Dos Listas**
 Crea una función que encuentre los elementos comunes entre dos listas.
```python 
def encontrar_comun(l1, l2):
    return list(set(l1) & set(l2))
lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6]
print(encontrar_comun(lista1, lista2))  # Resultado: [3, 4]
```
###  23. **Crear una Lista de Números del 1 al 100**
Crea una función que genere una lista con los números del 1 al 100.
```python 
def crear_lista_numeros():
    return list(range(1, 101))
print(crear_lista_numeros())  # Resultado: [1, 2, ..., 100]
```
###  24. **Contar la Frecuencia de Elementos en una Lista**
```python 
def contar_frecuencia(lista):
    frecuencia = {}
    for elemento in lista:
        if elemento in frecuencia:
            frecuencia[elemento] += 1
        else:
            frecuencia[elemento] = 1
    return frecuencia
lista_frecuencia = [1, 2, 2, 3, 3, 3]
print(contar_frecuencia(lista_frecuencia))  # Resultado: {1: 1, 2: 2, 3: 3}
```
###  25. **Crear una Lista de Números Aleatorios**
Crea una función que genere una lista de números aleatorios entre 1 y un rango dado.
```python
import random
def crear_lista_aleatoria(tamaño, rango):
    return [random.randint(1, rango) for _ in range(tamaño)]
print(crear_lista_aleatoria(10, 100))  # Resultado: Lista de 10 números aleatorios entre 1 y 100
```
###  26. **Encontrar el Mínimo y Máximo en una Lista**
Crea una función que encuentre el valor mínimo y máximo en una lista de números.
```python 
def encontrar_min_max(lista):
    if not lista:
        return "Error: La lista está vacía."
    return min(lista), max(lista)
lista_min_max = [10, 20, 30, 40, 50]
print(encontrar_min_max(lista_min_max))  # Resultado: (10, 50)
```
###  27. **Crear una Lista de Números Fibonacci**
 Crea una función que genere una lista de los primeros N números de la secuencia de Fibonacci.
```python 
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[:n]
print(fibonacci(10))  # Resultado: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```
###  28. **Convertir una Lista de Números a Cadenas**
 Crea una función que convierta una lista de números a una lista de cadenas.
```python 
def convertir_a_cadenas(lista):
    return [str(numero) for numero in lista]
lista_numeros = [1, 2, 3, 4, 5]
print(convertir_a_cadenas(lista_numeros))  # Resultado: ['1', '2', '3', '4', '5']
```
###  29. **Calcular el Producto de una Lista de Números**
Crea una función que calcule el producto de todos los números en una lista.
```python
def calcular_producto(lista):
    producto = 1
    for numero in lista:
        producto *= numero
    return producto
lista_productos = [1, 2, 3, 4, 5]
print(calcular_producto(lista_productos))  # Resultado: 120
```
###  30. **Crear una Lista de Números Primos**
 Crea una función que genere una lista de números primos hasta un número dado.
```python 
def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def crear_lista_primos(n):
    return [i for i in range(2, n + 1) if es_primo(i)]
print(crear_lista_primos(30))  # Resultado: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```
###  31. **Contar la Cantidad de Votos a Favor y en Contra**
Crea una función que cuente la cantidad de votos a favor (sí) y en contra (no) de una propuesta.
`votos = ['sí', 'no', 'sí', 'sí', 'no']`
```python 
def contar_votos(votos):
    a_favor = sum(1 for voto in votos if voto == 'sí')
    en_contra = sum(1 for voto in votos if voto == 'no')
    return a_favor, en_contra
votos = ['sí', 'no', 'sí', 'sí', 'no']
print(contar_votos(votos))  # Resultado: (3, 2)
```
###  32. **Crear una Lista de Palabras con Longitud Mayor a N**
Crea una función que reciba una lista de palabras y un número N, y retorne una lista con las palabras cuya longitud sea mayor a N.
```python 
def palabras_mayores_a(lista, n):
    return [palabra for palabra in lista if len(palabra) > n]
palabras = ['python', 'programación', 'hola', 'mundo', 'desarrollo']
print(palabras_mayores_a(palabras, 5))  # Resultado: ['programación', 'desarrollo']
```
###  33. **Encontrar el Elemento Más Pequeño en una Lista**
Crea una función que encuentre el valor más pequeño en una lista de números.
```python 
def encontrar_menor(lista):
    if not lista:
        return "Error: La lista está vacía."
    return min(lista)
lista_menor = [10, 20, 30, 40, 50]
print(encontrar_menor(lista_menor))  # Resultado: 10
```
###  34. **Crear una Lista de Números al Cuadrado**
Crea una función que reciba una lista de números y devuelva una nueva lista con los números al cuadrado.
```python 
def cuadrados(lista):
    return [numero ** 2 for numero in lista]
lista_numeros = [1, 2, 3, 4, 5]
print(cuadrados(lista_numeros))  # Resultado: [1, 4, 9, 16, 25]
```
###  35. **Contar la Cantidad de Elementos en una Lista**
Crea una función que cuente la cantidad de elementos en una lista.
```python 
def contar_elementos(lista):
    return len(lista)
lista_elementos = [1, 2, 3, 4, 5]
print(contar_elementos(lista_elementos))  # Resultado: 5
```
###  36. **Crear una Lista de Números Divisibles por 3**
Crea una función que genere una lista de números del 1 al N que son divisibles por 3.
```python 
def divisibles_por_tres(n):
    return [i for i in range(1, n + 1) if i % 3 == 0]
print(divisibles_por_tres(30))  # Resultado: [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
```
###  37. **Crear una Lista de Números Aleatorios Únicos**
 Crea una función que genere una lista de números aleatorios únicos entre 1 y un rango dado.
```python 
import random
def crear_aleatorios_unicos(tamaño, rango):
    return random.sample(range(1, rango + 1), tamaño)
print(crear_aleatorios_unicos(10, 100))  # Resultado: Lista de 10 números aleatorios únicos entre 1 y 100
```
###  38. **Contar la Cantidad de Vocales en una Cadena**
Crea una función que cuente la cantidad de vocales en una cadena de texto.
```python 
def contar_vocales_cadena(cadenastr):
    return sum(1 for char in cadenastr.lower() if char in 'aeiou')
cadena = "Hola Mundo"
print(contar_vocales_cadena(cadena))  # Resultado: 4 (o, a, u, o)
```
###  39. **Crear una Lista de Números Impares**
 Crea una función que genere una lista de números impares desde 1 hasta un número dado.
```python 
def crear_impares(n):
    return [i for i in range(1, n + 1) if i % 2 != 0]
print(crear_impares(10))  # Resultado: [1, 3, 5, 7, 9]
```
###  40. **Convertir una Lista de Cadenas a Minúsculas**
```python 
def convertir_a_minusculas(lista):
    return [cadena.lower() for cadena in lista]
lista_cadenas = ["HOLA", "MUNDO", "PYTHON"]
print(convertir_a_minusculas(lista_cadenas))  # Resultado: ['hola', 'mundo', 'python']
```
###  41. **Crear una Lista de Números del 1 al N**
```python 
def crear_lista_hasta_n(n):
    return list(range(1, n + 1))
print(crear_lista_hasta_n(10))  # Resultado: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```
###  42. **Contar la Cantidad de Consonantes en una Cadena**
```python 
def contar_consonantes(cadena):
    return sum(1 for char in cadena.lower() if char.isalpha() and char not in 'aeiou')
cadena = "Hola Mundo"
print(contar_consonantes(cadena))  # Resultado: 6 (H, l, M, n, d)
```
###  43. **Crear una Lista de Números Pares del 1 al N**
```python 
def crear_pares_hasta_n(n):
    return [i for i in range(2, n + 1, 2)]
print(crear_pares_hasta_n(10))  # Resultado: [2, 4, 6, 8, 10]
```
###  44. **Crear una Lista de Números del 1 al N al Cuadrado**
```python 
def cuadrados_hasta_n(n):
    return [i ** 2 for i in range(1, n + 1)]
print(cuadrados_hasta_n(10))  # Resultado: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```
###  45. **Contar la Cantidad de Palabras en una Cadena**
```python 
def contar_palabras_cadena(cadena):
    return len(cadena.split())
cadena = "Hola mundo, ¿cómo estás?"
print(contar_palabras_cadena(cadena))  # Resultado: 5
```
###  46. **Crear una Lista de Números del 1 al N al Cubo**
```python 
def cubos_hasta_n(n):
    return [i ** 3 for i in range(1, n + 1)]
print(cubos_hasta_n(10))  # Resultado: [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
```
###  47. **Crear una Lista de Números del 1 al N Divisibles por 5**
```python 
def divisibles_por_cinco(n):
    return [i for i in range(1, n + 1) if i % 5 == 0]
print(divisibles_por_cinco(50))  # Resultado: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
```
###  48. **Crear una Lista de Números del 1 al N Divisibles por 3 y 5**
```python 
def divisibles_por_tres_y_cinco(n):
    return [i for i in range(1, n + 1) if i % 3 == 0 and i % 5 == 0]
print(divisibles_por_tres_y_cinco(100))  # Resultado: [15, 30, 45, 60, 75, 90]
```
###  49. **Crear una Lista de Números del 1 al N que no son Primos**
```python 
def no_primos_hasta_n(n):
    return [i for i in range(1, n + 1) if not es_primo(i)]
print(no_primos_hasta_n(30))  # Resultado: [1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]
```
###  50. **Crear una Lista de Números del 1 al N que son Primos**
```python 
def primos_hasta_n(n):
    return [i for i in range(2, n + 1) if es_primo(i)]
print(primos_hasta_n(30))  # Resultado: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```
###  51. **Crear una Lista de Números del 1 al N que son Múltiplos de 4**
```python 
def multiples_de_cuatro(n):
    return [i for i in range(1, n + 1) if i % 4 == 0]
print(multiples_de_cuatro(40))  # Resultado: [4, 8, 12, 16, 20, 24, 28, 32, 36, 40]
```
###  52. **Crear una Lista de Números del 1 al N que son Múltiplos de 6**
```python 
def multiples_de_seis(n):
    return [i for i in range(1, n + 1) if i % 6 == 0]
print(multiples_de_seis(60))  # Resultado: [6, 12, 18, 24, 30, 36, 42, 48, 54, 60]
```
###  53. **Crear una Lista de Números del 1 al N que son Múltiplos de 7**
```python 
def multiples_de_siete(n):
    return [i for i in range(1, n + 1) if i % 7 == 0]
print(multiples_de_siete(70))  # Resultado: [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
```
###  54. **Crear una Lista de Números del 1 al N que son Múltiplos de 8**
```python 
def multiples_de_ocho(n):
    return [i for i in range(1, n + 1) if i % 8 == 0]
print(multiples_de_ocho(80))  # Resultado: [8, 16, 24, 32, 40, 48, 56, 64, 72, 80]
```
###  55. **Crear una Lista de Números del 1 al N que son Múltiplos de 9**
```python 
def multiples_de_nueve(n):
    return [i for i in range(1, n + 1) if i % 9 == 0]
print(multiples_de_nueve(90))  # Resultado: [9, 18, 27, 36, 45, 54, 63, 72, 81, 90]
```
###  56. **Crear una Lista de Números del 1 al N que son Múltiplos de 10**
```python 
def multiples_de_diez(n):
    return [i for i in range(1, n + 1) if i % 10 == 0]
print(multiples_de_diez(100))  # Resultado: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
```
###  57. **Crear una Lista de Números del 1 al N que son Múltiplos de 11**
```python 
def multiples_de_once(n):
    return [i for i in range(1, n + 1) if i % 11 == 0]
print(multiples_de_once(110))  # Resultado: [11, 22, 33, 44, 55, 66, 77, 88, 99, 110]
```
###  58. **Crear un Diccionario de Números del 1 al N con sus Cuadrados**
```python 
def diccionario_cuadrados(n):
    return {i: i ** 2 for i in range(1, n + 1)}
print(diccionario_cuadrados(10))  # Resultado: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
```
###  59. **Crear un Diccionario de Números del 1 al N con sus Cubos**
```python 
def diccionario_cubos(n):
    return {i: i ** 3 for i in range(1, n + 1)}
print(diccionario_cubos(10))  # Resultado: {1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729, 10: 1000}
```
###  60. **Crear un Diccionario de Números del 1 al N con sus Raíces Cuadradas**
```python 
def diccionario_raices(n):
    return {i: round(i ** 0.5, 2) for i in range(1, n + 1)}
print(diccionario_raices(10))  # Resultado: {1: 1.0, 2: 1.41, 3: 1.73, 4: 2.0, 5: 2.24, 6: 2.45, 7: 2.65, 8: 2.83, 9: 3.0, 10: 3.16}
```
###  61. **Crear una tupla de números del 1 al N**
```python 
def crear_tupla_hasta_n(n):
    return tuple(range(1, n + 1))
print(crear_tupla_hasta_n(10))  # Resultado: (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
```
###  62. **Crear un Conjunto de Números del 1 al N**
```python 
def crear_conjunto_hasta_n(n):
    return set(range(1, n + 1))
print(crear_conjunto_hasta_n(10))  # Resultado: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
```
###  63. **Usar `enumerate()` para Iterar sobre una Lista**
```python 
def enumerar_lista(lista):
    for indice, valor in enumerate(lista):
        print(f"Índice: {indice}, Valor: {valor}")
lista = ['a', 'b', 'c', 'd']
enumerar_lista(lista)
```
###  64. **Usar `zip()` para Combinar Dos Listas**
```python 
def combinar_listas(lista1, lista2):
    return list(zip(lista1, lista2))
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
print(combinar_listas(lista1, lista2))  # Resultado: [(1, 'a'), (2, 'b'), (3, 'c')]
```
###  65. **Usar `map()` para Aplicar una Función a Cada Elemento de una Lista**
```python 
def aplicar_funcion(lista, funcion):
    return list(map(funcion, lista))

def cuadrado(x):
    return x ** 2
lista_numeros = [1, 2, 3, 4, 5]
print(aplicar_funcion(lista_numeros, cuadrado))  # Resultado: [1, 4, 9, 16, 25]
```
###  66. **Usar `filter()` para Filtrar Elementos de una Lista**
```python 
def filtrar_pares(lista):
    return list(filter(lambda x: x % 2 == 0, lista))
lista_numeros = [1, 2, 3, 4, 5, 6]
print(filtrar_pares(lista_numeros))  # Resultado: [2, 4, 6]
```
###  67. **Usar `reduce()` para Reducir una Lista a un Solo Valor**
```python 
from functools import reduce
def reducir_suma(lista):
    return reduce(lambda x, y: x + y, lista)
lista_numeros = [1, 2, 3, 4, 5] 
print(reducir_suma(lista_numeros))  # Resultado: 15
```
###  68. **Usar `sorted()` para Ordenar una Lista**
```python 
def ordenar_lista(lista):
    return sorted(lista)
lista_numeros = [5, 2, 9, 1, 5, 6]
print(ordenar_lista(lista_numeros))  # Resultado: [1, 2, 5, 5, 6, 9]
```
###  69. **Usar `any()` para Comprobar si Algún Elemento Cumple una Condición**
```python 
def tiene_elemento_par(lista):
    return any(x % 2 == 0 for x in lista)
lista_numeros = [1, 3, 5, 7, 8]
print(tiene_elemento_par(lista_numeros))  # Resultado: True
```
###  70. **Usar `all()` para Comprobar si Todos los Elementos Cumplen una Condición**
```python 
def todos_son_pares(lista):
    return all(x % 2 == 0 for x in lista)
lista_numeros = [2, 4, 6, 8]
print(todos_son_pares(lista_numeros))  # Resultado: True
```
###  71. **Usar `max()` para Encontrar el Elemento Máximo en una Lista**
```python 
def encontrar_maximo(lista):
    return max(lista)
lista_numeros = [1, 2, 3, 4, 5]
print(encontrar_maximo(lista_numeros))  # Resultado: 5
```
###  72. **Usar switch para Imprimir un Mensaje según el Día de la Semana**
```python 
def dia_de_la_semana(dia):
    switcher = {
        1: "Lunes",
        2: "Martes",
        3: "Miércoles",
        4: "Jueves",
        5: "Viernes",
        6: "Sábado",
        7: "Domingo"
    }
    return switcher.get(dia, "Día no válido")
print(dia_de_la_semana(1))  # Resultado: "Lunes"
print(dia_de_la_semana(8))  # Resultado: "Día no válido"
```
###  73. **Usar `set()` para Eliminar Duplicados de una Lista**
```python 
def eliminar_duplicados_conjunto(lista):
    return list(set(lista))
lista_con_duplicados = [1, 2, 2, 3, 4, 4, 5]
print(eliminar_duplicados_conjunto(lista_con_duplicados))  # Resultado: [1, 2, 3, 4, 5]
```
###  74. **Usar `reversed()` para Invertir una Lista**
```python 
def invertir_lista(lista):
    return list(reversed(lista))
lista_numeros = [1, 2, 3, 4, 5]
print(invertir_lista(lista_numeros))  # Resultado: [5, 4, 3, 2, 1]
```
###  75. **Usar `join()` para Unir Elementos de una Lista en una Cadena**
```python 
def unir_lista(lista, separador):
    return separador.join(lista)
lista_cadenas = ['Hola', 'mundo', 'Python']
print(unir_lista(lista_cadenas, ' '))  # Resultado: "Hola mundo Python"
```
###  76. **Usar `split()` para Dividir una Cadena en una Lista**
```python 
def dividir_cadena(cadena, separador):
    return cadena.split(separador)
cadena = "Hola mundo Python"
print(dividir_cadena(cadena, ' '))  # Resultado: ['Hola', 'mundo', 'Python']
```
###  77. **Usar `strip()` para Eliminar Espacios en Blanco de una Cadena**
```python 
def eliminar_espacios(cadena):
    return cadena.strip()
cadena = "   Hola mundo Python   "
print(eliminar_espacios(cadena))  # Resultado: "Hola mundo Python"
```
###  78. **Usar `replace()` para Reemplazar Subcadenas en una Cadena**
```python 
def reemplazar_subcadena(cadena, viejo, nuevo):
    return cadena.replace(viejo, nuevo)
cadena = "Hola mundo Python"
print(reemplazar_subcadena(cadena, "Python", "Java"))  # Resultado: "Hola mundo Java"
```
###  79. **Usar `find()` para Encontrar la Posición de una Subcadena en una Cadena**
```python 
def encontrar_subcadena(cadena, subcadena):
    return cadena.find(subcadena)
cadena = "Hola mundo Python"
print(encontrar_subcadena(cadena, "mundo"))  # Resultado: 5
```
###  80. **Usar `count()` para Contar la Cantidad de Ocurrencias de una Subcadena en una Cadena**
```python 
def contar_ocurrencias(cadena, subcadena):
    return cadena.count(subcadena)
cadena = "Hola mundo Python, Python es genial"
print(contar_ocurrencias(cadena, "Python"))  # Resultado: 2
```
###  81. **Usar `startswith()` para Comprobar si una Cadena Comienza con una Subcadena**
```python 
def comienza_con(cadena, subcadena):
    return cadena.startswith(subcadena)
cadena = "Hola mundo Python"
print(comienza_con(cadena, "Hola"))  # Resultado: True
```
###  82. **Usar `endswith()` para Comprobar si una Cadena Termina con una Subcadena**
```python 
def termina_con(cadena, subcadena):
    return cadena.endswith(subcadena)
cadena = "Hola mundo Python"
print(termina_con(cadena, "Python"))  # Resultado: True
```
###  83. **Usar `capitalize()` para Capitalizar la Primera Letra de una Cadena**
```python 
def capitalizar_cadena(cadena):
    return cadena.capitalize()
cadena = "hola mundo python"
print(capitalizar_cadena(cadena))  # Resultado: "Hola mundo python"
```
###  84. **Usar `title()` para Capitalizar la Primera Letra de Cada Palabra en una Cadena**
```python 
def capitalizar_titulo(cadena):
    return cadena.title()
cadena = "hola mundo python"
print(capitalizar_titulo(cadena))  # Resultado: "Hola Mundo Python"
```
###  85. **Usar `upper()` para Convertir una Cadena a Mayúsculas**
```python 
def convertir_mayusculas(cadena):
    return cadena.upper()
cadena = "hola mundo python"
print(convertir_mayusculas(cadena))  # Resultado: "HOLA MUNDO PYTHON"
```
###  86. **Usar `lower()` para Convertir una Cadena a Minúsculas**
```python 
def convertir_minusculas(cadena):
    return cadena.lower()
cadena = "HOLA MUNDO PYTHON"
print(convertir_minusculas(cadena))  # Resultado: "hola mundo python"
```
###  87. **Usar `isalpha()` para Comprobar si una Cadena Contiene Solo Letras**    
```python 
def contiene_solo_letras(cadena):
    return cadena.isalpha()
cadena = "HolaMundo"
print(contiene_solo_letras(cadena))  # Resultado: True
```
###  88. **Usar `isdigit()` para Comprobar si una Cadena Contiene Solo Dígitos**
```python 
def contiene_solo_digitos(cadena):
    return cadena.isdigit()
cadena = "123456"
print(contiene_solo_digitos(cadena))  # Resultado: True
```
###  89. **Usar `isalnum()` para Comprobar si una Cadena Contiene Solo Letras y Dígitos**
```python 
def contiene_solo_letras_y_digitos(cadena):
    return cadena.isalnum()
cadena = "Hola123"
print(contiene_solo_letras_y_digitos(cadena))  # Resultado: True
```
###  90. **Usar `isupper()` para Comprobar si una Cadena Está en Mayúsculas**
```python 
def esta_en_mayusculas(cadena):
    return cadena.isupper()
cadena = "HOLA MUNDO"
print(esta_en_mayusculas(cadena))  # Resultado: True
```
###  91. **Usar `islower()` para Comprobar si una Cadena Está en Minúsculas**
```python 
def esta_en_minusculas(cadena):
    return cadena.islower()
cadena = "hola mundo"
print(esta_en_minusculas(cadena))  # Resultado: True
```
###  92. **Usar `isspace()` para Comprobar si una Cadena Contiene Solo Espacios en Blanco**
```python 
def contiene_solo_espacios(cadena):
    return cadena.isspace()
cadena = "   "
print(contiene_solo_espacios(cadena))  # Resultado: True
```
###  93. **Usar `swapcase()` para Intercambiar Mayúsculas y Minúsculas en una Cadena**
```python 
def intercambiar_mayusculas_minusculas(cadena):
    return cadena.swapcase()
cadena = "Hola Mundo"
print(intercambiar_mayusculas_minusculas(cadena))  # Resultado: "hOLA mUNDO"
```
###  94. **Usar `lstrip()` para Eliminar Espacios en Blanco al Inicio de una Cadena**
```python 
def eliminar_espacios_inicio(cadena):
    return cadena.lstrip()
cadena = "   Hola mundo Python"
print(eliminar_espacios_inicio(cadena))  # Resultado: "Hola mundo Python   "
```
###  95. **Usar `rstrip()` para Eliminar Espacios en Blanco al Final de una Cadena**
```python 
def eliminar_espacios_final(cadena):
    return cadena.rstrip()
cadena = "Hola mundo Python   "
print(eliminar_espacios_final(cadena))  # Resultado: "Hola mundo Python"
```
###  96. **Usar `partition()` para Dividir una Cadena en Tres Partes**
```python 
def dividir_cadena_particion(cadena, separador):
    return cadena.partition(separador)
cadena = "Hola mundo Python"
print(dividir_cadena_particion(cadena, "mundo"))  # Resultado: ('Hola ', 'mundo', ' Python')
```
###  97. **Usar `splitlines()` para Dividir una Cadena en Líneas**
```python 
def dividir_cadena_lineas(cadena):
    return cadena.splitlines()
cadena = "Hola mundo\nPython es genial"
print(dividir_cadena_lineas(cadena))  # Resultado: ['Hola mundo', 'Python es genial']
```
###  98. **Usar `format()` para Formatear una Cadena**
```python 
def formatear_cadena(nombre, edad):
    return "Mi nombre es {} y tengo {} años.".format(nombre, edad)
nombre = "Juan" 
edad = 30
print(formatear_cadena(nombre, edad))  # Resultado: "Mi nombre es Juan y tengo 30 años."
```
###  99. **Usar `f-strings` para Formatear una Cadena (Python 3.6+)**
```python 
def formatear_cadena_fstrings(nombre, edad):
    return f"Mi nombre es {nombre} y tengo {edad} años."
nombre = "Ana"
edad = 25
print(formatear_cadena_fstrings(nombre, edad))  # Resultado: "Mi nombre es Ana y tengo 25 años."
```
###  100. **Usar `str()` para Convertir un Objeto a Cadena**
```python 
def convertir_a_cadena(objeto):
    return str(objeto)
objeto = 12345
print(convertir_a_cadena(objeto))  # Resultado: "12345"
```

# Ejercicios sin resolver
1. Solicita al usuario un número y muestra si es par o impar.
2. Pide dos números al usuario y muestra la suma, la resta, el producto y el cociente.
3. Solicita una edad e indica si es mayor de edad.
4. Pide una nota del 0 al 10 e imprime su calificación (suspenso, aprobado, notable, sobresaliente).
5. Solicita al usuario un número y muestra su tabla de multiplicar del 1 al 10.
6. Imprime todos los números del 1 al 100 que sean múltiplos de 3 y de 5.
7. Cuenta cuántas vocales hay en una cadena introducida por el usuario.
8. Solicita una frase e imprime cada carácter por separado, uno por línea.
9. Pide al usuario su nombre y muestra un saludo personalizado en mayúsculas.
10. Solicita al usuario una palabra y di si empieza por vocal.
11. Pide al usuario un número e indica si está entre 10 y 50 (ambos inclusive).
12. Solicita una lista de 10 números y muestra cuántos son positivos.
13. Crea una lista con los cuadrados de los números del 1 al 10.
14. Dada una lista de frutas, solicita una fruta y di si está en la lista.
15. Pide una palabra e imprime si es un palíndromo.
16. Solicita al usuario que introduzca una frase. Imprime cuántas veces aparece cada vocal en la frase, si la palabra "python" está incluida (sin importar mayúsculas) y muestra la frase invertida.
17. Define un diccionario con productos y precios. Solicita al usuario tres productos que desea comprar, uno por uno. Si el producto existe, muestra su precio. Si no, indica que no está disponible. Muestra el total de la compra.
18. Solicita al usuario que introduzca 10 números, uno por uno, y guárdalos en una lista. Después, crea una lista con los positivos, otra con los negativos y otra con los pares mayores que 10. Imprime cada una.
19. Crea un programa que simule un semáforo. El usuario introduce un color y se muestra un mensaje según sea "verde", "amarillo", "rojo" o un color no válido. Ignora mayúsculas/minúsculas al evaluar.
20. Solicita al usuario que introduzca 10 frases distintas. Al terminar, muestra cuántas veces aparece cada letra del abecedario. Las letras que no aparezcan deben mostrarse con 0 apariciones.
21. Solicita al usuario los nombres de personas que entran a un edificio. Finaliza cuando se introduzca "fin". Guarda los nombres en una lista. Luego, indica cuántos nombres únicos hay, cuántos se repiten y muestra los que se repiten.
22. Simula un pequeño sistema de encuestas. El programa pregunta a 5 usuarios si les gusta el cine (respondiendo "sí" o "no"). Guarda las respuestas en un diccionario y muestra el recuento final.
23. Solicita al usuario una frase. Crea un diccionario donde las claves sean las palabras de la frase y los valores cuántas veces aparece cada palabra.
24. Define una lista de alumnos de primaria y otra de secundaria, introducidos por el usuario (finalizan con "x"). Muestra qué nombres están en ambos niveles, cuáles son únicos y el conjunto total sin repeticiones.
25. Simula un sistema de control de acceso. Crea un conjunto de usuarios autorizados. El usuario introduce un nombre y el programa indica si puede acceder o no.
26. Crea una lista con las temperaturas máximas registradas en los últimos 7 días. Muestra la temperatura más alta, la más baja, el promedio y cuántos días superaron los 30 grados.
27. Solicita al usuario una serie de números hasta introducir 0. Luego muestra: la suma total, la cantidad de números introducidos, cuántos eran mayores que 100 y el promedio.
28. Dado un diccionario con nombres de alumnos y sus calificaciones, muestra el nombre del alumno con mejor nota, el que tiene la peor, y la media de la clase.
29. Solicita una lista de productos comprados con su precio. Al finalizar, genera un ticket de compra con el total y un desglose de cada producto.
30. Crea un sistema de reservas de entradas para un cine. El programa debe permitir añadir nombres a una lista hasta que se llene el aforo (por ejemplo, 10 personas). Luego muestra los asistentes por orden alfabético.
31. Crea un programa que simule el registro de votos. Cada persona introduce su nombre y elige una de las opciones disponibles. Al final, se muestra el resultado de la votación.
32. Simula el registro de asistencia a una clase. Cada vez que un nombre se introduce, se añade al conjunto de presentes. El usuario puede introducir "fin" para cerrar la lista. Al final, muestra el número total de asistentes y sus nombres.
33. Solicita 10 números al usuario y crea un diccionario donde las claves sean los números y los valores sus cuadrados.
34. Simula una agenda de contactos. El usuario puede introducir pares nombre-teléfono hasta escribir "fin". Guarda los datos en un diccionario. Al final, permite buscar el número de una persona por su nombre.
35. Solicita una cadena y crea un histograma de caracteres: cuántas veces aparece cada letra. Luego imprime un gráfico de barras en texto para visualizarlo.
36. Simula un sistema de biblioteca donde se introducen títulos de libros prestados. Al finalizar, indica cuántas veces se ha prestado cada título.
37. Solicita nombres y apellidos de socios de un club. Guárdalos en un diccionario junto con el año de inscripción. Permite consultar por nombre, añadir nuevos socios y modificar la fecha de inscripción.
38. Crea un programa que administre productos de una tienda. Cada producto tiene nombre, precio y cantidad. Guarda esta información en un diccionario y permite consultar o modificar el stock.
39. Pide al usuario introducir frases hasta que escriba "salir". Muestra las palabras más utilizadas en todas las frases.
40. Simula un registro de viajes: cada entrada contiene el nombre del viajero, el destino y la fecha. Guarda los viajes en una lista de tuplas. Al final, muestra un resumen de destinos más visitados y la cantidad de viajes totales.
41. Solicita al usuario una frase y muestra solo las palabras que tienen más de 5 letras.
42. Pide al usuario una frase y transforma todas las letras a mayúsculas. Luego reemplaza todas las vocales por asteriscos.
43. Solicita al usuario una frase y muestra cuántas palabras contiene, y cuál es la palabra más larga.
44. Solicita una frase y muestra solo los caracteres que aparecen una única vez.
45. Pide una cadena e indica si contiene únicamente letras, solo números o una combinación.
46. Solicita al usuario una cadena y elimina todos los espacios en blanco.
47. Solicita al usuario un texto y reemplaza todas las apariciones de la palabra "no" por "sí", sin importar mayúsculas/minúsculas.
48. Pide al usuario una palabra y genera una nueva palabra con las letras impares (según posición) de la original.
49. Solicita una frase y muestra todas las palabras ordenadas alfabéticamente.
50. Pide una frase y crea un nuevo string que contenga solo las consonantes.
51. Crea un sistema de control de contraseñas. Pide una contraseña y comprueba que tenga al menos 8 caracteres, una mayúscula y un número.
52. Solicita una frase e imprime cuántas palabras empiezan por vocal.
53. Pide una cadena e invierte solo las palabras, pero no el orden de las palabras.
54. Pide una frase y elimina todos los signos de puntuación.
55. Solicita una cadena y cuenta cuántas veces aparecen las sílabas "la", "le", "li", "lo", "lu".
56. Pide una frase y muestra una tabla con cada carácter distinto y su código ASCII.
57. Solicita una frase y detecta si contiene alguna palabra repetida.
58. Solicita al usuario su nombre completo y muestra las iniciales.
59. Pide una frase y reemplaza todas las letras acentuadas por su versión sin tilde.
60. Solicita al usuario una lista de correos electrónicos separados por comas y muestra cuántos son válidos (contienen "@").
61. Pide nombres separados por comas y elimina aquellos que comienzan por letra "A".
62. Solicita un texto y comprueba si hay alguna palabra que aparezca más de 3 veces.
63. Crea un sistema que detecte si una cadena es un anagrama de otra.
64. Solicita una palabra e imprime si contiene letras repetidas adyacentes (por ejemplo, "ll", "ss").
65. Pide una frase y convierte la primera letra de cada palabra a mayúsculas.
66. Pide una fecha en formato dd/mm/aaaa y verifica si es válida.
67. Solicita un número entero y muestra su representación binaria, octal y hexadecimal como cadena.
68. Solicita un número de cuenta bancaria y calcula los dígitos de control simplificados (usa operaciones con strings y números).
69. Solicita una frase y agrupa sus palabras por longitud. Muestra un diccionario donde la clave es la longitud y el valor es la lista de palabras de esa longitud.
70. Crea un sistema de puntuación de frases. Por cada vocal suma 1 punto, por cada consonante suma 2 puntos. Muestra la puntuación final.
71. Simula el análisis de un comentario en una red social. Pide un texto y muestra cuántos hashtags (#) y menciones (@) contiene.
72. Pide una lista de nombres y muestra cuántos comienzan por cada letra del abecedario.
73. Crea una lista de tuplas con información de canciones: (título, artista, duración). Permite buscar por artista y ver el total de tiempo de sus canciones.
74. Simula un sistema de registro de alumnos con sus asignaturas y notas. Permite añadir alumnos, añadir notas y calcular la media de cada uno.
75. Crea un programa que registre productos con sus precios en un diccionario. Permite modificar precios, eliminar productos y consultar precios.
76. Simula un chat: cada mensaje enviado se guarda en una lista. Al final, muestra los 5 últimos mensajes en orden inverso.
77. Pide al usuario nombres de películas hasta que escriba "fin". Después, muestra cuántas veces se repite cada título.
78. Solicita una lista de compras en formato "producto:precio" separados por comas. Calcula el total y muestra los productos ordenados por precio.
79. Solicita cadenas de texto hasta que una contenga solo números. Después, analiza cuántas contenían letras, números y símbolos.
80. Simula un sistema de registro de tareas. Cada tarea tiene un nombre y una prioridad (alta, media, baja). Permite introducir tareas y luego mostrarlas ordenadas por prioridad.
81. Pide al usuario varias frases y guarda en un conjunto todas las palabras que no se repiten en ninguna frase.
82. Crea una lista de contactos con nombre, teléfono y correo electrónico. Permite buscar por nombre y mostrar el contacto completo.
83. Pide cadenas de texto y almacena sus longitudes en una lista. Luego muestra la cadena más corta y la más larga.
84. Crea una agenda de eventos: cada evento tiene nombre, fecha y hora. Permite añadir eventos y consultar por fecha.
85. Solicita nombres y apellidos y los almacena en una lista de tuplas. Después permite ordenar alfabéticamente por apellido.
86. Simula una encuesta sobre hábitos de lectura. Almacena respuestas en un diccionario con preguntas y respuestas. Luego muestra un resumen de los resultados.
87. Crea un programa que simule la subida de temperatura diaria. Cada día se introduce un valor y se guarda en una lista. Al final, muestra la evolución.
88. Simula un sistema de validación de matrículas de coche: deben tener 4 cifras seguidas de 3 letras mayúsculas. Valida varias entradas del usuario.
89. Solicita frases e imprime aquellas que sean palíndromos completos (ignorando espacios y tildes).
90. Solicita nombres de equipos y resultados de partidos en una lista de tuplas. Luego calcula cuántos partidos ganó cada equipo.
91. Simula una base de datos de libros con título, autor y año. Permite filtrar libros por autor o año y mostrarlos.
92. Crea un sistema de puntuación de palabras estilo Scrabble: cada letra tiene un valor y se suma el total de una palabra introducida por el usuario.
93. Pide nombres y notas. Después, genera una lista de tuplas (nombre, nota) y muestra los aprobados y los suspensos.
94. Solicita textos y muestra cuáles contienen todas las vocales al menos una vez.
95. Crea una lista de tuplas con nombres de personas y su edad. Luego muestra quiénes son mayores de edad y quiénes no.
96. Simula un sistema de almacén. Cada producto tiene un código, nombre, cantidad y precio. Permite introducir nuevos productos y consultar el stock.
97. Pide al usuario 20 palabras y muestra las 5 más frecuentes
98. Crea un programa que permita registrar varios mensajes. Al final, muestra todos los que contienen signos de exclamación o interrogación.
99. Solicita una cadena y muestra si tiene caracteres repetidos no consecutivos.
100. Simula un sistema de análisis de contraseñas. Solicita varias contraseñas y muestra cuántas cumplen criterios de longitud, combinación de mayúsculas/minúsculas y números.