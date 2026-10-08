# UD5 - POO
1. **Listar archivos `.txt` de un directorio (`os`)**  
   Pide al usuario una ruta de carpeta y muestra todos los archivos que terminan en `.txt` usando `os.listdir()`.

2. **Crear y escribir en un archivo (`pathlib`)**  
   Crea un archivo llamado `saludo.txt` en el escritorio del usuario utilizando `pathlib`, y escribe la frase `"Hola, mundo desde Python"` en él.

3. **Leer desde entrada estándar y contar líneas (`sys.stdin`)**  
   Lee texto desde entrada estándar (usando `sys.stdin`) hasta recibir una línea vacía.  
   Al final, imprime cuántas líneas se han introducido.

4. **Buscar palabras clave en archivo (`fileinput`, `re`)**  
   Lee un archivo `.txt` usando `fileinput.input()` y busca líneas que contengan direcciones de email válidas.  
   Usa `re` para extraer los correos y mostrarlos uno por línea.

5. **Limpiar nombres con caracteres no alfabéticos (`string`)**  
   Dada una lista de nombres sucios (con símbolos, números, etc.), crea una nueva lista con solo los caracteres alfabéticos usando `string.ascii_letters`.

6. **Leer archivo CSV y mostrar datos (`csv`)**  
   Abre un archivo `datos.csv` que contiene columnas `nombre,edad` y muestra todos los nombres de personas mayores de 18 años.

7. **Convertir CSV a JSON (`csv`, `json`)**  
   Lee un archivo `productos.csv` con columnas `producto,precio`, y guarda los datos en formato JSON en `productos.json`.

8. **Filtrar líneas por patrón (`re`, `io`)**  
   Lee un archivo `.txt` línea por línea (usando `io.open`) y escribe en otro archivo solo aquellas líneas que contengan fechas con formato `dd/mm/yyyy`.

9. **Explorador con estadísticas (`pathlib`, `os`, `io`, `string`)**  
   Recorre un directorio y para cada archivo `.txt`:  
   - Muestra la cantidad de palabras, líneas y caracteres.  
   - Elimina símbolos no imprimibles antes de contar usando `string.printable`.

10. **Conversor CSV a JSON con validación (`csv`, `json`, `re`, `string`)**  
    Lee un archivo `usuarios.csv` con columnas `nombre,email,edad`. Antes de convertir a JSON:  
    - Valida que el correo sea correcto con `re`.  
    - Quita espacios adicionales con `string.whitespace`.  
    - Descarta filas con datos incompletos.  
    Guarda los usuarios válidos en `usuarios.json` y muestra cuántos fueron descartados.

11. **Cálculo de raíces y potencias (`math`)**  
    Pide al usuario un número y muestra:  
    - Su raíz cuadrada.  
    - Su valor elevado al cubo.  
    - Su logaritmo en base 10.  
    Usa funciones del módulo `math`.

12. **Precisión con decimales (`decimal`)**  
    Implementa una calculadora simple que permita sumar y multiplicar dos números decimales introducidos como texto.  
    Usa el módulo `decimal` para asegurar la precisión.

13. **Operaciones con fracciones (`fractions`)**  
    Crea un programa que permita introducir dos fracciones (por ejemplo, `3/4` y `5/6`) y muestre:  
    - La suma.  
    - La resta.  
    - La multiplicación.  
    - La fracción simplificada.  
    Usa el módulo `fractions`.

14. **Generador de apuestas (`random`)**  
    Escribe un programa que genere 6 números aleatorios entre 1 y 49 (sin repetir) simulando una apuesta de lotería.  
    Usa el módulo `random` y muestra los números ordenados.

15. **Resumen estadístico (`statistics`, `random`)**  
    Genera una lista de 100 números aleatorios entre 1 y 100. Luego muestra:  
    - La media.  
    - La mediana.  
    - La moda.  
    - La desviación estándar.  
    Usa el módulo `statistics` para los cálculos.

16. **Mostrar fecha y hora actual (`datetime`)**  
    Muestra por pantalla la fecha y hora actuales en el formato:  
    `"Hoy es lunes, 15 de julio de 2025 - 14:35"`  
    Usa `datetime.now()` y formateo con `strftime`.

17. **Cálculo de edad a partir de fecha de nacimiento (`datetime`)**  
    Pide al usuario su fecha de nacimiento en formato `dd/mm/yyyy` y calcula cuántos años tiene.  
    Ten en cuenta si ya ha cumplido años este año.

18. **Calendario mensual (`calendar`)**  
    Pide al usuario un mes y un año, y muestra el calendario de ese mes usando el módulo `calendar`.  
    El calendario debe estar alineado como los clásicos de consola.

19. **Contador regresivo (`time`)**  
    Pide al usuario un número de segundos y muestra una cuenta atrás desde ese número hasta 0.  
    Muestra el tiempo restante cada segundo. Usa `time.sleep()`.

20. **Diferencia entre fechas (`datetime`, `timedelta`)**  
    Crea un programa que reciba dos fechas y muestre:  
    - Cuántos días hay entre ellas.  
    - Si hay más de 30 días de diferencia, muestra `"Fecha lejana"`.  
    Usa `datetime` y operaciones con `timedelta`.

    - **Uso de `collections.Counter`**  
   Cuenta cuántas veces aparece cada palabra en un texto y muestra las 5 más frecuentes.

21. **Uso de `collections.namedtuple`**  
   Crea una estructura `Empleado` con nombre, departamento y salario, y calcula el promedio salarial por departamento.

22. **Programación funcional (`map`, `filter`, `reduce`, `functools`)**  
   Procesa una lista de enteros: eleva al cuadrado los impares mayores que 10 y calcula su suma total.

23. **Funciones lambda y ordenación personalizada**  
    Ordena una lista de diccionarios que contienen información de libros por el número de páginas de forma descendente.

24. **Captura de errores (`try`, `except`, `else`, `finally`)**  
    Implementa una calculadora que capture errores como división por cero, entrada no numérica y muestre mensajes adecuados.

25. **Definición y uso de excepciones personalizadas**  
    Crea una clase `Temperatura` que lance una excepción si el valor introducido está fuera de un rango razonable (-273 a 1000).

26. **Depuración con `logging`**  
    Escribe un programa que gestione registros de acceso a un sistema y use `logging` para anotar cada intento de acceso con nivel de severidad.

27. **Obtener dirección IP de un dominio (`socket`)**  
    Pide al usuario que introduzca un nombre de dominio (por ejemplo, `www.python.org`) y muestra su dirección IP.

28. **Cliente HTTP básico (`http.client`)**  
    Implementa un cliente que se conecte a un servidor HTTP (`httpbin.org` por ejemplo) y recupere el contenido de la página de inicio (`GET /`).

29. **Descargar página web y extraer enlaces (`urllib.request`, `re`)**  
    Escribe un programa que descargue el HTML de una página web usando `urllib.request` y extraiga todas las URL encontradas en los atributos `href` usando expresiones regulares.

30. **Verificación de dirección IP (`ipaddress`)**  
    Crea un programa que reciba una cadena y determine si es una dirección IP válida (IPv4 o IPv6).  
    Usa el módulo `ipaddress`.

31. **Servidor TCP simple (`socket`)**  
    Crea un servidor que escuche en el puerto 12345.  
    - Cuando un cliente se conecta, espera que le envíe una frase.  
    - El servidor responde con la frase en mayúsculas.  
    - Luego cierra la conexión.  
    Usa `socket` y controla errores básicos.

32. **Cifrado de contraseñas (`hashlib`)**  
    Pide al usuario una contraseña y muestra su hash en formato SHA-256.  
    No almacenes la contraseña original, solo el hash.

33. **Verificación de acceso seguro (`getpass`, `hashlib`)**  
    Almacena un hash de contraseña predefinido.  
    Luego pide la contraseña al usuario (sin mostrarla en pantalla, usando `getpass`) y comprueba si coincide.

34. **Generación de token aleatorio seguro (`secrets`)**  
    Escribe un programa que genere un token de 32 caracteres hexadecimal para autenticación segura de sesiones.

35. **Codificación y decodificación base64 (`base64`)**  
    Pide al usuario un texto, codifícalo en base64 y muestra el resultado.  
    Luego decodifícalo para comprobar que es el mismo texto original.

36. **Firma y verificación de mensajes (`hmac`, `hashlib`)**  
    Escribe una función que reciba un mensaje y una clave secreta y genere una firma digital usando HMAC-SHA256.  
    Luego permite verificar si una firma dada es válida para ese mensaje y clave.

37. **Evaluador de expresiones (`eval`)**  
    Crea una calculadora que reciba una expresión aritmética como cadena (`"5 + 3 * 2"`) y devuelva el resultado utilizando `eval()`.  
    Controla errores como `SyntaxError` y `ZeroDivisionError`.

38. **Compilación y ejecución dinámica (`compile`, `exec`)**  
    Pide al usuario que introduzca varias líneas de código Python (hasta una línea vacía) y ejecútalas usando `compile()` y `exec()`.  
    Asegúrate de capturar posibles errores de ejecución.

39. **Compilar archivo `.py` a `.pyc` (`py_compile`)**  
    Escribe un programa que reciba el nombre de un archivo `.py` y lo compile a bytecode `.pyc` usando el módulo `py_compile`.  
    Informa al usuario si la compilación fue exitosa o no.

40. **Importación dinámica de módulos (`importlib`)**  
    Pide al usuario el nombre de un módulo estándar (como `math`, `datetime`, etc.) y usa `importlib.import_module()` para cargarlo dinámicamente y listar sus funciones y clases disponibles.

41. **Editor de scripts interactivo**  
    Diseña un programa que permita al usuario escribir un script Python línea a línea (guardándolo en un archivo temporal), compilarlo y ejecutarlo.  
    Muestra el resultado y los errores, si los hubiera.  
    Combina `open()`, `compile()`, `exec()`, y `tempfile`.

42. **Test de funciones matemáticas (`unittest`)**  
    Crea una función `es_par(n)` que devuelve `True` si un número es par.  
    Escribe un archivo de pruebas que verifique distintos casos válidos y uno erróneo (por ejemplo, pasar una cadena).

43. **Test de clase simple (`unittest.TestCase`)**  
    Implementa una clase `Cuenta` con métodos `ingresar` y `retirar`.  
    Escribe tests unitarios que verifiquen cambios en el saldo, retiros válidos e inválidos (saldo insuficiente).

44. **Test de excepciones personalizadas**  
    Crea una excepción personalizada `TemperaturaInvalidaError` y una función `validar_temperatura(t)` que la lance si el valor es inferior a -273.  
    Escribe un test que verifique que se lanza correctamente con temperaturas no válidas.

45. **Test con mock (`unittest.mock`)**  
    Simula una función que obtiene datos desde la red (por ejemplo, `obtener_precio_dolar()`).  
    Usa `unittest.mock` para simular una respuesta en los tests sin necesidad de conexión real.

46. **Diseño de suite de pruebas y ejecución automatizada**  
    Crea un conjunto de funciones relacionadas con productos (`calcular_precio`, `aplicar_descuento`, `formatear_etiqueta`).  
    Organiza las pruebas de cada una en una suite y ejecuta todo el conjunto mostrando un resumen final con `unittest.TextTestRunner()`.

47. **Gestión segura de archivos (`with`, archivo de texto)**  
    Escribe una función que reciba un nombre de archivo y devuelva su contenido en mayúsculas.  
    Utiliza un context manager con `with` para abrir y cerrar el archivo de forma segura.

48. **Context manager personalizado (`__enter__`, `__exit__`)**  
    Crea una clase `Temporizador` que funcione como context manager y mida el tiempo que tarda en ejecutarse un bloque de código.  
    Muestra el tiempo transcurrido al salir del bloque.

49. **Decorador de logging simple**  
    Escribe un decorador que imprima `"Ejecutando función..."` antes de ejecutar cualquier función decorada.

50. **Decorador para medir tiempo de ejecución**  
    Crea un decorador `medir_tiempo` que muestre el tiempo que tarda en ejecutarse una función usando `time.time()`.

51. **Decorador con argumentos**  
    Diseña un decorador `repetir(n)` que repita la ejecución de la función decorada `n` veces.

52. **Decorador para control de acceso**  
    Escribe un decorador `requiere_autenticacion` que verifique si una variable global `usuario_autenticado` es `True` antes de permitir la ejecución de la función.

53. **Combinación de decoradores**  
    Combina dos decoradores: uno que convierte el resultado de una función en mayúsculas, y otro que añade signos de exclamación al principio y al final.  
    Aplícalos en distintos órdenes para observar la diferencia.

54. **Generador de números pares (`yield`)**  
    Crea un generador que produzca todos los números pares entre dos valores dados.

55. **Generador de líneas válidas**  
    Escribe un generador que reciba un archivo de texto y produzca solo las líneas no vacías y que no comiencen con `#`.

56. **Iterador personalizado (`__iter__`, `__next__`)**  
    Implementa una clase `CuentaRegresiva` que actúe como un iterador, devolviendo números desde un valor inicial hasta cero.

57. **Generador infinito de números primos**  
    Crea un generador que produzca números primos indefinidamente.  
    Limita su uso mostrando solo los 10 primeros con un bucle `for`.

58. **Generador con estado complejo**  
    Escribe un generador que simule una secuencia de Fibonacci y que, además, imprima un mensaje cada vez que se alcanza un número múltiplo de 100.

59. **Procesamiento en paralelo (`multiprocessing`)**  
    Crea un programa que calcule el factorial de una lista de números en paralelo.

60. **Multihilo con `threading` y control con `Lock`**  
    Simula varias operaciones bancarias simultáneas sobre una misma cuenta protegida con bloqueo.

61. **Sockets TCP (`socket`)**  
    Implementa un pequeño servidor que reciba mensajes desde un cliente y devuelva el mensaje en mayúsculas.

62. **Descarga de datos con `urllib`**  
    Escribe un programa que descargue el contenido HTML de una URL y guarde las etiquetas `<title>` y los enlaces en un archivo.

63. **Cifrado y descifrado básico con `hashlib` y `secrets`**  
    Implementa un sistema de login que guarde contraseñas cifradas y valide usando hashing.

64. **Compresión de archivos (`zipfile`, `gzip`)**  
    Escribe una función que comprima todos los archivos `.txt` de un directorio y luego los descomprima.

65. **Serialización con `json`**  
    Crea una lista de diccionarios que representen productos y guárdalos en un archivo `.json`. Después, vuelve a cargarlos y muéstralos formateados.

66. **Gestor de tareas personales con estadísticas**
Crea una aplicación de consola para gestionar tareas diarias. Cada tarea incluye: descripción, fecha de vencimiento, prioridad y estado (pendiente o completada).  
Debe permitir:
- Añadir, eliminar, completar y listar tareas.
- Ordenar tareas por prioridad o por proximidad de la fecha.
- Guardar y cargar las tareas en formato JSON.
- Mostrar estadísticas: tareas vencidas, completadas, por día, etc.
- Usar `datetime`, `json`, `operator`, `statistics`.
- Aplicar decoradores para registrar cada operación realizada.
- Escribir tests con `unittest` para verificar operaciones básicas.

67. **Cliente de monitorización de clima en ciudades**
Crea una aplicación que reciba una lista de ciudades y obtenga información del clima usando una API pública (puede usarse `urllib` y simular la respuesta en JSON).  
Debe:
- Almacenar la información localmente en un archivo.
- Mostrar la media de temperatura por país.
- Generar un resumen diario.
- Registrar errores si alguna ciudad falla con `logging`.
- Simular concurrencia usando `threading` o `asyncio` para múltiples llamadas.
- Incluir tests de validación de datos y parseo JSON.

68. **Gestor de cuentas y contraseñas cifradas**
Desarrolla una aplicación que almacene cuentas de usuario y contraseñas cifradas localmente (en JSON).  
Debe:
- Generar hashes SHA-256 de las contraseñas (`hashlib`).
- Pedir contraseña sin mostrarla (`getpass`).
- Verificar la autenticidad al iniciar sesión.
- Proteger el archivo con un token generado con `secrets`.
- Utilizar `context managers` para abrir/cerrar los archivos.
- Incluir logs con fechas (`datetime`, `logging`).
- Añadir tests unitarios para el sistema de autenticación.

69. **Compresor de archivos inteligentes**
Crea una herramienta que:
- Recorre un directorio en busca de archivos `.txt` o `.csv`.
- Comprime los archivos en `.zip` o `.gz` según el tipo.
- Muestra por pantalla el ahorro de espacio conseguido.
- Mantiene un historial en JSON con fecha, nombre del archivo original, tamaño original y tamaño comprimido.
- Usa `os`, `pathlib`, `zipfile`, `gzip`, `json`, `datetime`.
- Permite reestablecer archivos comprimidos a su forma original.
- Incluye un decorador para medir el tiempo total del proceso de compresión.