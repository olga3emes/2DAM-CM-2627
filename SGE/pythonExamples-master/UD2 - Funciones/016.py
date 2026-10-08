def mi_funcion(param1, param2):
    """
    Esta función toma dos parámetros y devuelve una lista que contiene
    los elementos de ambos parámetros.

    :param param1: Primer parámetro, puede ser un número o una cadena.
    :param param2: Segundo parámetro, puede ser un número o una cadena.
    :return: Lista que contiene los dos parámetros.
    """
    return [param1, param2]
# Ejemplo de uso de la función
resultado = mi_funcion(5, "hola")
print(resultado)  # Imprime: [5, 'hola']
# Ejemplo de uso de la función con diferentes tipos de parámetros
resultado2 = mi_funcion("Python", 3.14)
print(resultado2)  # Imprime: ['Python', 3.14]
# Ejemplo de uso de la función con parámetros de tipo cadena
resultado3 = mi_funcion("cadena1", "cadena2")
print(resultado3)  # Imprime: ['cadena1', 'cadena2']
# Ejemplo de uso de la función con parámetros de tipo número
resultado4 = mi_funcion(10, 20)