# LISTAS
# Declaración:
l = [22, True, "una lista", [1, 2]]
#Acceso:
# Una dimensión:
l = [11,False]
mi_var = l[0] # mi_var vale 11
mi_var= l[-1] # mi_var vale False
# Varias dimensiones:
l = ["una lista", [1, 2]]
mi_var = l[1][0] # mi_var vale 1
# Asignación de un valor:
l = [22, True]
l[0] = 99 # Con esto valdrá [99, True]
#Métodos de listas:
l = [22, True, "una lista", [1, 2]]
# Añadir un elemento al final de la lista
l.append("nuevo elemento")
# l vale [22, True, "una lista", [1, 2], "nuevo elemento"]
# Añadir varios elementos al final de la lista
l.extend([3, 4])
# l vale [22, True, "una lista", [1, 2], "nuevo elemento", 3, 4]
# Insertar un elemento en una posición específica
l.insert(1, "insertado")
# l vale [22, "insertado", True, "una lista", [1, 2], "nuevo elemento", 3, 4]
# Eliminar un elemento por valor
l.remove("una lista")
# l vale [22, "insertado", True, [1, 2], "nuevo elemento", 3, 4]
# Eliminar un elemento por índice
l.pop(2)
# Elimina el elemento en la posición 2 (True),
# l vale [22, "insertado", [1, 2], "nuevo elemento", 3, 4]
# Eliminar el último elemento
l.pop()
# Elimina el último elemento ("nuevo elemento"), l vale [22, "insertado", [1, 2], 3, 4]
# Limpiar la lista
l.clear()  # l vale []
# Contar el número de ocurrencias de un elemento
l = [1, 2, 2, 3, 4]
count_2 = l.count(2)  # count_2 vale 2
# Obtener el índice del primer elemento encontrado
index_3 = l.index(3)  # index_3 vale 3 (índice del primer 3)
# Ordenar la lista
l = [3, 1, 4, 2]
l.sort()  # l vale [1, 2, 3, 4]
# Invertir el orden de los elementos de la lista
l.reverse()  # l vale [4, 3, 2, 1]
# Copiar una lista
l = [1, 2, 3]
l_copy = l.copy()  # l_copy vale [1, 2, 3]
# Concatenar dos listas
l1 = [1, 2]
l2 = [3, 4]
l_concat = l1 + l2  # l_concat vale [1, 2, 3, 4]
# Repetir una lista
l_repeated = l1 * 3  # l_repeated vale [1, 2, 1, 2, 1, 2]
# Comprobar si un elemento está en la lista
l = [1, 2, 3]
is_2_in_list = 2 in l  # is_2_in_list vale True
# Comprobar si un elemento no está en la lista
is_5_not_in_list = 5 not in l  # is_5_not_in_list vale True
# Obtener la longitud de la lista
l_length = len(l)  # l_length vale 3
