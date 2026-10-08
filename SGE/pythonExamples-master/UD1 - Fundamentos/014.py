#Tuplas
# Definición de una tupla:
t = (1, 2, True, "python")
# Tupla de un elemento:
t = (1,)
# Acceso: Igual que el de las listas.
mi_var= t[0] # mi_var es 1
mi_var= t[0:2] # mi_var es (1,2)

#Métodos de tuplas:
# Las tuplas son inmutables, por lo que no tienen métodos para modificar su contenido.
# Sin embargo, se pueden usar algunos métodos de las secuencias:
# Contar el número de ocurrencias de un elemento
t = (1, 2, 2, 3)
count_2 = t.count(2)  # count_2 vale 2
# Obtener el índice del primer elemento encontrado
index_3 = t.index(3)  # index_3 vale 3 (índice del primer 3)
# Concatenar dos tuplas
t1 = (1, 2)
t2 = (3, 4)
t_concat = t1 + t2  # t_concat vale (1, 2, 3, 4)
# Repetir una tupla
t_repeated = t1 * 3  # t_repeated vale (1, 2, 1, 2, 1, 2)
# Comprobar si un elemento está en la tupla
is_2_in_tuple = 2 in t  # is_2_in_tuple vale True
# Comprobar si un elemento no está en la tupla
is_5_not_in_tuple = 5 not in t  # is_5_not_in_tuple vale True
# Tuplas con un solo elemento
# Las tuplas con un solo elemento deben tener una coma al final para diferenciarlas de un valor entre paréntesis.
# Ejemplo de tupla con un solo elemento
t_single = (42,)  # Tupla con un solo elemento
# Acceso a elementos de una tupla
mi_var = t_single[0]  # mi_var es 42
# Tuplas anidadas
t_nested = (1, (2, 3), (4, 5))
# Acceso a elementos de una tupla anidada
mi_var = t_nested[1][0]  # mi_var es 2


#Set
# Definición de un set:
s = {1, 2, True, "python"}
# Set de un elemento:
s = {1,}  # Set con un solo elemento
# Acceso: Los sets no tienen un orden definido,
# por lo que no se puede acceder a sus elementos por índice.
#Definición de un set con duplicados:
s2 = {1, 2, 2, 3}  # Los duplicados se eliminan automáticamente
print(s2) # s2 vale {1, 2, 3}
# Métodos de sets:
# Añadir un elemento al set
s.add(3)  # Añade el elemento 3 al set
# Eliminar un elemento del set
s.remove(2)  # Elimina el elemento 2 del set (lanza un error si no existe)
# Eliminar un elemento del set sin lanzar error si no existe
s.discard(2)  # Elimina el elemento 2 del set (no lanza error si no existe)
# Comprobar si un elemento está en el set
is_2_in_set = 2 in s  # is_2_in_set vale False
# Comprobar si un elemento no está en el set
is_5_not_in_set = 5 not in s  # is_5_not_in_set vale True
# Copiar un set
s_copy = s.copy()  # Crea una copia del set
# Concatenar dos sets (unión)
s1 = {1, 2}
s2 = {3, 4}
s_union = s1 | s2  # s_union vale {1, 2, 3, 4}
# Repetir un set (no tiene sentido, pero se puede hacer)
s_repeated = s1  # Los sets no se pueden repetir, pero se puede asignar el mismo set a otra variable
# Comprobar si un set es un subconjunto de otro
s1 = {1, 2}
s2 = {1, 2, 3}
is_subset = s1.issubset(s2)  # is_subset vale True
# Comprobar si un set es un superconjunto de otro
is_superset = s2.issuperset(s1)  # is_superset vale True
# Intersección de dos sets
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s_intersection = s1 & s2  # s_intersection vale {2, 3}
# Diferencia de dos sets
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s_difference = s1 - s2  # s_difference vale {1}
# Diferencia simétrica de dos sets
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s_symmetric_difference = s1 ^ s2  # s_symmetric_difference vale {1, 4}
# Set anidados
s_nested = {1, (2, 3), (4, 5)}
# Acceso a elementos de un set anidado
# Los sets no tienen un orden definido, por lo que no se puede acceder a sus elementos por índice.
# Sin embargo, se pueden iterar los elementos del set anidado.
# Iterar sobre un set
for element in s_nested:
    print(element)  # Imprime cada elemento del set anidado

#SortedSet
# Definición de un SortedSet:
from sortedcontainers import SortedSet
ss = SortedSet([3, 1, 2])
# SortedSet de un elemento:
ss_single = SortedSet([1])  # SortedSet con un solo elemento
# Acceso: Igual que el de los sets, pero ordenado.
