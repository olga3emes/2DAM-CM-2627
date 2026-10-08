#Strings o cadenas de caracteres
triple=""" esto es una linea
 y esta es otra linea"""
print(triple)  # Imprime el texto con saltos de línea
# Concatenación de cadenas
cadena1 = "Hola"
cadena2 = "Mundo"
cadena_concatenada = cadena1 + " " + cadena2
print(cadena_concatenada)  # Imprime 'Hola Mundo'
# Repetición de cadenas
cadena_repetida = cadena1 * 3
print(cadena_repetida)  # Imprime 'HolaHolaHola'
# Longitud de una cadena
longitud_cadena = len(cadena1)


# Python ofrece la posibilidad de usar f-string. Estas son cadenas de
# caracteres con el prefijo f o F. Estas cadenas pueden incluir pares de llaves
# con expresiones cuyo valor puede ser sustituido en tiempo de ejecución.
# Dentro de los pares de llaves también podemos especificar detalles del
# tipo de dato que se espera y la anchura del campo entre otros.
nombre: str = 'Juan'
telefono: int = 678900123
altura: float = 182.3
print(f'{(nombre*2):10s} ==> {telefono:10d} => {altura:.2f}')
# En este caso, el nombre se repetirá dos veces, el teléfono se mostrará como un
# número entero de 10 dígitos y la altura se mostrará con dos decimales.
# También podemos usar el método format() para formatear cadenas de manera similar.
print('Obligatorio:'+f'{nombre[:3]} ==> {(str(telefono))[:8]} => {(altura):.1f}')
#limitando el nº de caracteres
print('{} {} {}'.format(nombre, telefono, altura))
# Python también permite el uso de cadenas multilínea utilizando comillas triples.
# Estas cadenas pueden abarcar varias líneas y conservar los saltos de línea.
# Ejemplo de cadena multilínea
cadena_multilinea = """Esta es una cadena
multilínea
que conserva los saltos de línea
y los espacios."""
print(cadena_multilinea)
# Otra alternativa para formatear cadenas es el operador %. Este operador
# compone una cadena de texto donde aparecen %, posiblemente seguidos
# por especificadores de tipo como antes, con una tupla de parámetros. El
# resultado es la sustitución de cada % junto con la especificación de tipo
# por el valor del parámetro correspondiente.
print('fruit:%10s, price:%8.2f' % ('apple', 6.056))

#Métodos de cadenas
# Python proporciona una variedad de métodos para manipular cadenas.
# Algunos de los métodos más comunes son:
# - upper(): Convierte la cadena a mayúsculas.
# - lower(): Convierte la cadena a minúsculas.
# - strip(): Elimina los espacios en blanco al principio y al final de la cadena.
# - replace(old, new): Reemplaza todas las ocurrencias de una subcadena por otra.
# - split(separator): Divide la cadena en una lista de subcadenas utilizando un separador.
# - splitlines(keepends): Divide la cadena en líneas, opcionalmente conservando los saltos de línea.
# - join(iterable): Une los elementos de un iterable en una cadena, utilizando la cadena como separador.
# - find(substring): Busca una subcadena y devuelve su índice, o -1 si no se encuentra.
# - count(substring): Cuenta cuántas veces aparece una subcadena en la cadena.
# - index(substring): Similar a find, pero lanza una excepción si la subcadena no se encuentra.
# - rfind(substring): Busca una subcadena desde el final de la cadena y devuelve su índice, o -1 si no se encuentra.
# - lfind(substring): Busca una subcadena desde el principio de la cadena y devuelve su índice, o -1 si no se encuentra.
# - lindex(substring): Similar a rfind, pero lanza una excepción si la subcadena no se encuentra.
# - rindex(substring): Similar a rfind, pero lanza una excepción si la subcadena no se encuentra.
# - lstrip(): Elimina los espacios en blanco al principio de la cadena.
# - rstrip(): Elimina los espacios en blanco al final de la cadena.
# - isspace(): Comprueba si todos los caracteres de la cadena son espacios en blanco.
# - startswith(prefix): Comprueba si la cadena comienza con un prefijo dado.
# - endswith(suffix): Comprueba si la cadena termina con un sufijo dado.
# - isalpha(): Comprueba si todos los caracteres de la cadena son alfabéticos.
# - isdigit(): Comprueba si todos los caracteres de la cadena son dígitos.
# - isalnum(): Comprueba si todos los caracteres de la cadena son alfanuméricos.
# - capitalize(): Convierte el primer carácter de la cadena a mayúsculas.
# - title(): Convierte el primer carácter de cada palabra a mayúsculas.
# - swapcase(): Cambia mayúsculas por minúsculas y viceversa.
# - zfill(width): Rellena la cadena con ceros a la izquierda hasta alcanzar una longitud especificada.
# - format(*args, **kwargs): Formatea la cadena utilizando los argumentos proporcionados.
# - format_map(mapping): Formatea la cadena utilizando un diccionario como mapeo.
# - casefold(): Convierte la cadena a una forma más baja, útil para comparaciones.
# - removeprefix(prefix): Elimina un prefijo específico de la cadena.
# - removesuffix(suffix): Elimina un sufijo específico de la cadena.
# - translate(table): Traduce caracteres en la cadena utilizando una tabla de traducción.
# - center(width, fillchar): Centra la cadena en un campo de ancho especificado, rellenando con un carácter dado.
# - ljust(width, fillchar): Alinea la cadena a la izquierda en un campo de ancho especificado, rellenando con un carácter dado.
# - rjust(width, fillchar): Alinea la cadena a la derecha en un campo de ancho especificado, rellenando con un carácter dado.
# - partition(separator): Divide la cadena en tres partes: antes del separador, el separador y después del separador.
# - rpartition(separator): Similar apartition, pero busca el separador desde el final de la cadena.
# # isspace(): Comprueba si todos los caracteres de la cadena son espacios en blanco.
# - isidentifier(): Comprueba si la cadena es un identificador válido en Python.
# - isprintable(): Comprueba si todos los caracteres de la cadena son imprimibles.
# - format_spec(): Devuelve la especificación de formato de la cadena.
# - maketrans(): Crea una tabla de traducción para usar con translate().
# - zfill(width): Rellena la cadena con ceros a la izquierda hasta alcanzar una longitud especificada.


# Ejemplo de uso de algunos métodos de cadenas
cadena = "  Hola, Mundo!  "
print(cadena.upper())          # Convierte a mayúsculas
print(cadena.lower())          # Convierte a minúsculas
print(cadena.strip())          # Elimina espacios en blanco al principio y al final
print(cadena.replace("Mundo", "Python"))  # Reemplaza "Mundo" por "Python"
print(cadena.split(","))       # Divide la cadena en una lista de subcadenas
print(cadena.splitlines())     # Divide la cadena en líneas
print(cadena.find("Mundo"))    # Busca "Mundo" y devuelve su índice
print(cadena.count("o"))       # Cuenta cuántas veces aparece "o"
print(cadena.index("Mundo"))   # Busca "Mundo" y devuelve su índice (lanza excepción si no se encuentra)
print(cadena.rfind("o"))       # Busca "o" desde el final y devuelve su índice
print(cadena.lstrip())         # Elimina espacios en blanco al principio
print(cadena.rstrip())         # Elimina espacios en blanco al final
print(cadena.startswith("  Hola"))
print(cadena.endswith("!  "))    # Comprueba si termina con "!  "
print(cadena.isalpha())        # Comprueba si todos los caracteres son alfabéticos
print(cadena.isdigit())        # Comprueba si todos los caracteres son dígitos
print(cadena.isalnum())        # Comprueba si todos los caracteres son alfanuméricos
print(cadena.capitalize())     # Convierte el primer carácter a mayúsculas
print(cadena.title())          # Convierte el primer carácter de cada palabra a mayúsculas
print(cadena.swapcase())       # Cambia mayúsculas por minúsculas y viceversa
print(cadena.zfill(20))        # Rellena con ceros a la izquierda hasta alcanzar una longitud de 20
print(cadena.format())         # Formatea la cadena (no hay marcadores de formato en este caso)
print(cadena.format_map({"name": "Python"}))  # Formatea la cadena utilizando un diccionario
print(cadena.casefold())       # Convierte a una forma más baja, útil para comparaciones
print(cadena.removeprefix("  "))  # Elimina el prefijo "  "
print(cadena.removesuffix("!  "))  # Elimina el sufijo "!  "
print(cadena.translate(str.maketrans("aeiou", "12345")))  # Traduce vocales a números
print(cadena.center(30, '-'))  # Centra la cadena en un campo de ancho 30, rellenando con '-'
print(cadena.ljust(30, '-'))   # Alinea a la izquierda en un campo de ancho 30, rellenando con '-'
print(cadena.rjust(30, '-'))   # Alinea a la derecha en un campo de ancho 30, rellenando con '-'
print(cadena.partition(","))   # Divide en tres partes: antes, el separador y después
print(cadena.rpartition(","))  # Similar a partition, pero busca desde el final
# Ejemplo de uso de join
lista = ["Hola", "Mundo", "Python"]
cadena_unida = " ".join(lista)  # Une los elementos de la lista en una cadena
print(cadena_unida)  # Imprime 'Hola Mundo Python'
# Ejemplo de uso de isspace
cadena_espacios = "   "
print(cadena_espacios.isspace())  # Comprueba si todos los caracteres son espacios en blanco
# Ejemplo de uso de startswith y endswith
cadena_inicio = "Hola, Mundo!"
print(cadena_inicio.startswith("Hola"))  # Comprueba si comienza con "Hola"
print(cadena_inicio.endswith("!"))    # Comprueba si termina con "!"
# Ejemplo de uso de isalpha, isdigit e isalnum
cadena_alpha = "Hola"
cadena_digit = "12345"
cadena_alnum = "Hola123"
print(cadena_alpha.isalpha())  # Comprueba si todos los caracteres son alfabéticos
print(cadena_digit.isdigit())  # Comprueba si todos los caracteres son dígitos
print(cadena_alnum.isalnum())  # Comprueba si todos los caracteres son alfanuméricos
# Ejemplo de uso de capitalize, title y swapcase
cadena_capitalizada = "hola, mundo!"
print(cadena_capitalizada.capitalize())  # Convierte el primer carácter a mayúsculas
print(cadena_capitalizada.title())       # Convierte el primer carácter de cada palabra a mayúsculas
print(cadena_capitalizada.swapcase())    # Cambia mayúsculas por minúsculas y viceversa
# Ejemplo de uso de zfill
cadena_numero = "42"
print(cadena_numero.zfill(5))  # Rellena con ceros a la izquierda hasta alcanzar una longitud de 5
# Ejemplo de uso de format y format_map
cadena_formateada = "Hola, {}. Tu número es {}.".format("Juan", 12345)
print(cadena_formateada)  # Imprime 'Hola, Juan. Tu número es 12345'
# Ejemplo de uso de format_map
cadena_formateada_map = "Hola, {name}. Tu número es {number}.".format_map({"name": "Juan", "number": 12345})
print(cadena_formateada_map)  # Imprime 'Hola, Juan. Tu número es 12345'
# Ejemplo de uso de casefold
cadena_casefold = "HOLA, MUNDO!"
print(cadena_casefold.casefold())  # Convierte a una forma más baja, útil para comparaciones
# Ejemplo de uso de removeprefix y removesuffix
cadena_prefijo = "  Hola, Mundo!  "
print(cadena_prefijo.removeprefix("  "))  # Elimina el prefijo "  "
print(cadena_prefijo.removesuffix("  "))  # Elimina el sufijo "  "
# Ejemplo de uso de translate
tabla_traduccion = str.maketrans("aeiou", "12345")  # Traduce vocales a números
cadena_traducida = "Hola, Mundo!".translate(tabla_traduccion)
print(cadena_traducida)  # Imprime 'H4l1, M5nd4!'
# Ejemplo de uso de center, ljust y rjust
cadena_justificada = "Hola"
print(cadena_justificada.center(20, '-'))  # Centra la cadena en un campo de ancho 20, rellenando con '-'
print(cadena_justificada.ljust(20, '-'))   # Alinea a la izquierda en un campo de ancho 20, rellenando con '-'
print(cadena_justificada.rjust(20, '-'))   # Alinea a la derecha en un campo de ancho 20, rellenando con '-'
# Ejemplo de uso de partition y rpartition
cadena_particion = "Hola, Mundo!"
print(cadena_particion.partition(","))  # Divide en tres partes: antes, el separador y después
print(cadena_particion.rpartition(","))  # Similar a partition, pero busca desde el final
# Ejemplo de uso de join
cadena_join = " - ".join(lista)  # Une los elementos de la lista en una cadena con " - " como separador
print(cadena_join)  # Imprime 'Hola - Mundo - Python'
print("Longitud de la cadena:", longitud_cadena)  # Imprime la longitud de 'Hola'

