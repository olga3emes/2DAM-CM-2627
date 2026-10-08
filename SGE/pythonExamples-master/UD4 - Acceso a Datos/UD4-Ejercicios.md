# UD4 - Acceso a datos
1. **Lectura línea a línea**  
   Crea un programa que lea un archivo de texto llamado `notas.txt` e imprima cada línea con su número correspondiente.

2. **Contador de palabras**  
   Lee un archivo `texto.txt` y muestra cuántas palabras hay en total.

3. **Escritura de frases**  
   Pide al usuario 3 frases por teclado y guárdalas en un archivo llamado `frases.txt`, una por línea.

4. **Filtro de líneas vacías**  
   Crea un programa que copie un archivo de texto a otro, omitiendo las líneas vacías.

5. **Lectura y escritura binaria (`pickle`)**  
   Crea una lista de números enteros y guárdala en un archivo binario (`datos.bin`) usando `pickle`. Luego recupérala e imprímela.

6. **Contador de letras (`a`, `e`, `o`)**  
   Lee un archivo y muestra cuántas veces aparece cada una de esas vocales.

7. **Modificación de líneas específicas**  
   Crea un programa que lea un archivo y reemplace todas las ocurrencias de la palabra `"error"` por `"ERROR"` y lo guarde como nuevo archivo.

8. **Creación y lectura de CSV (`csv.DictWriter`)**  
   Escribe una lista de diccionarios con alumnos (`nombre`, `nota`) en un archivo `alumnos.csv`. Luego léelo y muestra la nota media.

9. **Dividir archivo grande en varios pequeños**  
   Lee un archivo `grande.txt` y divídelo en varios archivos con 10 líneas cada uno.

10. **Recuento de líneas duplicadas**  
    Lee un archivo `datos.txt` y muestra cuántas veces se repite cada línea exacta. Usa un diccionario.

11. **Conectar a MySQL y crear base de datos**  
    Conéctate al servidor MySQL y crea una base de datos llamada `empresa`.

12. **Crear tabla `empleados`**  
    Dentro de la base de datos `empresa`, crea una tabla `empleados` con:  
    `id (INT AUTO_INCREMENT PRIMARY KEY)`, `nombre (VARCHAR)`, `departamento (VARCHAR)`, `salario (FLOAT)`.

13. **Insertar datos en la tabla**  
    Inserta al menos 3 registros de empleados distintos.

14. **Consultar todos los empleados**  
    Realiza una consulta que devuelva todos los registros de la tabla y los imprima formateados desde Python.

15. **Actualizar el salario de un empleado**  
    Pide al usuario un `id` y un nuevo salario, y actualiza el campo correspondiente.

16. **Eliminar un empleado por ID**  
    Pide un `id` al usuario y elimina ese registro de la base de datos.

17. **Buscar empleados por departamento**  
    Pide un nombre de departamento y muestra todos los empleados que trabajan en él.

18. **Consulta agregada: salario medio**  
    Calcula y muestra el salario medio de todos los empleados.

19. **Listar departamentos únicos**  
    Muestra todos los departamentos diferentes presentes en la tabla `empleados`.

20. **CRUD completo**  
    Implementa un menú en consola que permita: insertar, listar, actualizar, eliminar empleados. Cada opción ejecuta la operación correspondiente sobre la tabla `empleados`.

21. **Clientes y pedidos**  
    Crea dos tablas:
    - `clientes (id, nombre, email)`
    - `pedidos (id, cliente_id, producto, cantidad)`  
    Relaciona `pedidos.cliente_id` con `clientes.id`.

    Escribe un programa que permita:
    - Insertar un nuevo pedido asociado a un cliente.
    - Ver todos los pedidos de un cliente dado su ID.
    - Eliminar un cliente solo si no tiene pedidos (controlar con consulta previa).

22. **Autores y libros**  
    Define las siguientes tablas:
    - `autores (id, nombre)`
    - `libros (id, titulo, autor_id)`  
    `libros.autor_id` es clave foránea a `autores.id`.

    Implementa un CRUD para libros que permita:
    - Añadir un libro para un autor existente.
    - Listar todos los libros con nombre del autor.
    - Modificar título o autor de un libro.
    - Eliminar un libro.

23. **Alumnos y asignaturas (matrículas)**  
    Define:
    - `alumnos (id, nombre)`
    - `asignaturas (id, nombre)`
    - `matriculas (alumno_id, asignatura_id)` → tabla intermedia con clave compuesta.

    Implementa:
    - Matricular a un alumno en una asignatura.
    - Listar todas las asignaturas de un alumno.
    - Eliminar todas las matrículas de un alumno.

24. **Películas y géneros**  
    Tablas:
    - `generos (id, nombre)`
    - `peliculas (id, titulo, genero_id)`  

    Implementa un CRUD completo para películas:
    - Añadir nueva película con su género.
    - Modificar su título o género.
    - Ver todas las películas con su género.
    - Borrar una película.

25. **Profesores y cursos impartidos**  
    Tablas:
    - `profesores (id, nombre)`
    - `cursos (id, titulo)`
    - `profesor_curso (profesor_id, curso_id)` → relación N:N

    Implementa:
    - Asignar un curso a un profesor.
    - Listar todos los cursos que imparte un profesor.
    - Quitar un curso de un profesor concreto.

