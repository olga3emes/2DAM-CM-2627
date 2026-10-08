#SLICING
l = [99, True, "una lista", [1, 2]]
mi_var = l[0:2] # mi_var vale [99, True]
mi_var = l[0:4:2] # mi_var vale [99, “una lista”]
l = [99, True, "una lista"]
mi_var = l[1:] #mi_var vale [True, “una lista”]
mi_var = l[:2] #mi_var vale [99, True]
mi_var = l[:] # mi_var vale [99, True, ”una lista”]
mi_var = l[::2] #mi_var vale [99, “una lista”]

#Modificación de listas usando rangos (slicing)
l = [99, True, "una lista", [1, 2]]
l[0:2] = [0, 1] # l vale [0, 1, “una lista”, [1, 2]]
l[0:2] = [False] # l vale [False, “una lista”, [1, 2]]

# cadenas como listas
c = "hola mundo"
c[0] # h
c[5:] # mundo
c[::3] # hauo
# Modificación de cadenas (no se puede, son inmutables)