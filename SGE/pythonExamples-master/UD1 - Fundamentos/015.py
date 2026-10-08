#Diccionarios

d = {"Love Actually ": "Richard Curtis", "Kill Bill":"Tarantino","Amélie": "Jean-Pierre Jeunet"}
d["Love Actually "] # devuelve "Richard Curtis"
d["Kill Bill"] = "Quentin Tarantino"
f = { } # crear un diccionario vacio
f["Torrente"]= "Santiago Segura" # insertar un elemento
f["Torrente"]= "Santi Segura" # actualización del valor

# Métodos de diccionarios
#Añadir un elemento al diccionario
d["Inception"] = "Christopher Nolan"  # añade una nueva clave-valor
# Obtener el valor de una clave
valor = d.get("Amélie")  # devuelve "Jean-Pierre Jeunet"
# Obtener todas las claves del diccionario
claves = d.keys()  # devuelve un objeto dict_keys con las claves
# Obtener todos los valores del diccionario
valores = d.values()  # devuelve un objeto dict_values con los valores
# Obtener todos los pares clave-valor del diccionario
pares = d.items()  # devuelve un objeto dict_items con los pares clave-valor
# Eliminar un elemento del diccionario
d.pop("Kill Bill")  # elimina la clave "Kill Bill" y su valor
# Limpiar el diccionario
d.clear()  # elimina todos los elementos del diccionario
# Comprobar si una clave está en el diccionario
existe = "Amélie" in d  # devuelve True si "Amélie" es una clave en el diccionario
# Comprobar si una clave no está en el diccionario
no_existe = "Inexistente" not in d  # devuelve True si "Inexistente" no es una clave en el diccionario
# Copiar un diccionario
copia_d = d.copy()  # crea una copia superficial del diccionario
# Concatenar dos diccionarios
d1 = {"A": 1, "B": 2}
d2 = {"C": 3, "D": 4}
d_concat = {**d1, **d2}  # crea un nuevo diccionario con las claves y valores de d1 y d2
# Repetir un diccionario (no tiene sentido, pero se puede hacer)
d_repeated = {k: v for k, v in d.items()}  # crea una copia del diccionario
# Comprobar si un valor está en el diccionario
valor_existe = "Richard Curtis" in d.values()  # devuelve True si "Richard Curtis" es un valor en el diccionario
# Comprobar si un valor no está en el diccionario
valor_no_existe = "Inexistente" not in d.values()  # devuelve True si "Inexistente" no es un valor en el diccionario
# Diccionarios anidados
d_nested = {
    "peliculas": {
        "Love Actually": "Richard Curtis",
        "Kill Bill": "Tarantino"
    },
    "directores": {
        "Amélie": "Jean-Pierre Jeunet"
    }
}
# Acceso a un valor en un diccionario anidado
valor_anidado = d_nested["peliculas"]["Love Actually"]  # devuelve "Richard Curtis"
