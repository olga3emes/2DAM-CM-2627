# Kotlin para DAM

### Nivel de examen

# Bloque 1. Funciones

## Ejercicio 1

Implementa una función `esPar()` que reciba un entero y devuelva `true` si el número es par.

---

## Ejercicio 2

Implementa una función `mayor()` que reciba dos enteros y devuelva el mayor.

---

## Ejercicio 3

Implementa una función `potencia(base, exponente)` sin utilizar librerías matemáticas.

---

## Ejercicio 4

Implementa una función que calcule el factorial de un número.

---

## Ejercicio 5

Implementa una función que determine si un número es primo.

---

# Bloque 2. Condicionales

## Ejercicio 6

Solicita una nota entre 0 y 10 y muestra:

- Suspenso
- Aprobado
- Notable
- Sobresaliente

---

## Ejercicio 7

Determina si un año es bisiesto.

---

## Ejercicio 8

Dado un número, indicar si es positivo, negativo o cero.

---

## Ejercicio 9

Dados tres números, mostrar el mayor.

---

## Ejercicio 10

Implementa una calculadora utilizando `when`.

Operaciones:

- +
- -
- *
- /

---

# Bloque 3. Bucles

## Ejercicio 11

Mostrar por pantalla los números del 1 al 100.

---

## Ejercicio 12

Mostrar los números pares entre 1 y 100.

---

## Ejercicio 13

Mostrar los múltiplos de 5 entre 1 y 200.

---

## Ejercicio 14

Calcular la suma de los números del 1 al 100.

---

## Ejercicio 15

Mostrar la tabla de multiplicar de un número introducido por el usuario.

---

# Bloque 4. Arrays

## Ejercicio 16

Crear un array de 10 enteros e imprimir todos sus elementos.

---

## Ejercicio 17

Encontrar el elemento mayor de un array.

---

## Ejercicio 18

Encontrar el elemento menor de un array.

---

## Ejercicio 19

Calcular la media de los elementos de un array.

---

## Ejercicio 20

Contar cuántos números pares contiene un array.

---

# Bloque 5. Arrays avanzados

## Ejercicio 21

Invertir un array sin utilizar `reversed()`.

---

## Ejercicio 22

Buscar un valor dentro de un array e indicar su posición.

---

## Ejercicio 23

Copiar un array en otro array.

---

## Ejercicio 24

Sumar dos arrays posición a posición.

Ejemplo:

```text
[1,2,3]
[4,5,6]

Resultado:
[5,7,9]
```

---

## Ejercicio 25

Determinar si dos arrays contienen exactamente los mismos elementos.

---

# Bloque 6. Colecciones

## Ejercicio 26

Crear una lista mutable de nombres.

Añadir cinco elementos.

---

## Ejercicio 27

Eliminar un elemento de una lista mutable.

---

## Ejercicio 28

Mostrar todos los elementos usando `forEach`.

---

## Ejercicio 29

Ordenar una lista alfabéticamente.

---

## Ejercicio 30

Contar cuántos elementos contiene una lista.

---

# Bloque 7. map, filter y reduce

## Ejercicio 31

Dada una lista de números, generar una nueva lista con los cuadrados utilizando `map`.

---

## Ejercicio 32

Obtener únicamente los números pares utilizando `filter`.

---

## Ejercicio 33

Obtener únicamente los mayores de 50 utilizando `filter`.

---

## Ejercicio 34

Multiplicar todos los números por 10 utilizando `map`.

---

## Ejercicio 35

Calcular la suma de todos los números usando `reduce`.

---

# Bloque 8. Lambdas

## Ejercicio 36

Crear una lambda que calcule el doble de un número.

---

## Ejercicio 37

Crear una lambda que calcule el cuadrado usando `it`.

---

## Ejercicio 38

Crear una lambda que reciba dos parámetros y devuelva su suma.

---

## Ejercicio 39

Crear una lambda que determine si un número es positivo.

---

## Ejercicio 40

Crear una lambda que reciba una cadena y devuelva su longitud.

---

# Bloque 9. Funciones de orden superior

## Ejercicio 41

Crear una función que reciba otra función para realizar una operación matemática.

---

## Ejercicio 42

Utilizar la función anterior para realizar una suma.

---

## Ejercicio 43

Utilizar la función anterior para realizar una multiplicación.

---

# Bloque 10. Vararg

## Ejercicio 44

Crear una función que sume un número variable de enteros.

---

## Ejercicio 45

Crear una función que devuelva el mayor utilizando `vararg`.

---

# Bloque 11. Funciones de extensión

## Ejercicio 46

Crear una función de extensión para `String` llamada `invertir()`.

---

## Ejercicio 47

Crear una función de extensión para `Int` llamada `esPar()`.

---

## Ejercicio 48

Crear una función de extensión para `List<Int>` que devuelva la suma de todos sus elementos.

---

# Bloque 12. Null Safety

## Ejercicio 49

Crear una función que reciba un `String?` y devuelva su longitud. Si es nulo devolverá 0.

---

## Ejercicio 50

Dada la siguiente lista:

```kotlin
val nombres = listOf(
    "Ana",
    null,
    "Pedro",
    null,
    "Lucía"
)
```

Mostrar únicamente los nombres no nulos.

---

# Ejercicio Final

Desarrolla una aplicación de gestión de alumnos que:

1. Cree una data class Alumno.
2. Permita almacenar alumnos en una MutableList.
3. Añada alumnos mediante funciones.
4. Calcule la nota media.
5. Obtenga los aprobados usando filter.
6. Obtenga los nombres usando map.
7. Ordene los alumnos por nota.
8. Utilice al menos una función de extensión.
9. Utilice una función con vararg.
10. Utilice Null Safety.
11. Muestre toda la información por pantalla utilizando forEach.