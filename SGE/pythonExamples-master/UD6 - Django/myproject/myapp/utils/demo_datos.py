from myapp.models import Author, Book, BookAward
from datetime import date

# python manage.py shell
# from myapp.utils.demo_datos import *

def crear_datos():
    # Crear autores
    a1 = Author.objects.create(name="Gabriel García Márquez", birthdate=date(1927, 3, 6))
    a2 = Author.objects.create(name="Isabel Allende", birthdate=date(1942, 8, 2))
    a3 = Author.objects.create(name="Mario Vargas Llosa", birthdate=date(1936, 3, 28))
    a4 = Author.objects.create(name="Jorge Luis Borges", birthdate=date(1899, 8, 24))
    a5 = Author.objects.create(name="Laura Esquivel", birthdate=date(1950, 9, 30))

    # Libros de Gabriel García Márquez
    Book.objects.create(title="Cien años de soledad", author=a1, published_date=date(1967, 5, 30), isbn="9788497592208")
    Book.objects.create(title="El amor en los tiempos del cólera", author=a1, published_date=date(1985, 9, 5), isbn="9780307389732")

    # Libros de Isabel Allende
    Book.objects.create(title="La casa de los espíritus", author=a2, published_date=date(1982, 11, 1), isbn="9788408105824")
    Book.objects.create(title="Paula", author=a2, published_date=date(1994, 1, 1), isbn="9780060927217")

    # Libros de Mario Vargas Llosa
    Book.objects.create(title="La ciudad y los perros", author=a3, published_date=date(1963, 10, 10), isbn="9788420431379")
    Book.objects.create(title="Conversación en La Catedral", author=a3, published_date=date(1969, 4, 15), isbn="9788439725077")

    # Libros de Jorge Luis Borges
    Book.objects.create(title="Ficciones", author=a4, published_date=date(1944, 1, 1), isbn="9788491050283")
    Book.objects.create(title="El Aleph", author=a4, published_date=date(1949, 1, 1), isbn="9789500426056")

    # Libros de Laura Esquivel
    Book.objects.create(title="Como agua para chocolate", author=a5, published_date=date(1989, 9, 1), isbn="9780307743855")
    Book.objects.create(title="La ley del amor", author=a5, published_date=date(1995, 3, 1), isbn="9788466329514")

def consultar_datos():
    # Metodos que devuelven QuerySets
    print("\n Todos los libros:")
    for libro in Book.objects.all():
        print(f"id: {libro.pk} - {libro.title} - {libro.author.name}")

    print("\n Todos los autores ordenados alfabéticamente:")
    for autor in Author.objects.order_by('name'):
        print(f"{autor.name} ({autor.birthdate})")

    print("\n Libros publicados antes de 1970:")
    for libro in Book.objects.filter(published_date__lt="1970-01-01"):
        print(f"{libro.title} - {libro.published_date}")

    print("\n Libros cuyo título contiene 'amor':")
    for libro in Book.objects.filter(title__icontains='amor'):
        print(libro.title)

    # Encadenamiento: Obtener libros de aquellos autores nacidos antes de 1930, que en su titulo no contengan "ficciones"
    # y ordenados por fecha de publicación descendente
    libros = Book.objects \
        .filter(author__birthdate__lt="1930-01-01") \
        .exclude(title__icontains="ficciones") \
        .order_by('-published_date')

    for libro in libros:
        print(libro.get_summary())

    # Métodos que devuelven un tipo distinto de dato a QuerySet
    # Contar cuántos libros hay en total
    total_libros = Book.objects.count()
    print(f"Total de libros: {total_libros}")

    # Obtener el primer libro (por orden por defecto, generalmente por ID)
    primer_libro = Book.objects.first()
    print(f"Primer libro creado: {primer_libro.title} ({primer_libro.published_date})")

def autores():
    # Crear un autor y guardarlo en la base de datos
    autor = Author(name='Gabriel García Márquez', birthdate='1927-03-06')
    autor.save()
    # Crear un autor y guardarlo en la base de datos
    autor = Author.objects.create(name='Isabel Allende', birthdate='1942-08-02')
    # Crear varios autores de una vez
    autores = [
        Author(name='Julio Cortázar', birthdate='1914-08-26'),
        Author(name='Mario Vargas Llosa', birthdate='1936-03-28'),
    ]
    Author.objects.bulk_create(autores)
    # Obtener o crear un autor, sin duplicados
    autor2, creado2 = Author.objects.get_or_create(name='Borges', birthdate='1899-08-24')
    # Obtener o crear un autor, sin duplicados
    autor3, creado3 = Author.objects.update_or_create(
        name='J. K. Rowling',
        defaults={'birthdate': '1965-07-31'}
    )

def crear_y_actualizar_premio():
    # Crear el premio
    premio = BookAward.objects.create(
        nombre="Premio Cervantes",
        anio=2025,
        pais="España",
        organizador="Ministerio de Cultura",
        categoria="Narrativa",
        idioma="Español",
        dotacion_economica=125000.00,
        fecha_entrega=date(2025, 4, 23),
        ciudad="Alcalá de Henares",
        edicion=50,
        ambito="nacional",
        descripcion="Máximo galardón de las letras españolas",
        pagina_oficial="https://www.culturaydeporte.gob.es",
        es_activo=True
    )

    # Guardar todos los campos (generará una UPDATE completa)
    premio.descripcion = "Premio más prestigioso de literatura en español"
    premio.save()

    # Guardar solo el campo 'ciudad' para optimizar la consulta SQL
    premio.ciudad = "Madrid"
    premio.save(update_fields=["ciudad"])

def acceso_objetos_relacionados():
    # Obtener un libro y mostrar su autor
    libro = Book.objects.first()
    if libro:
        print(f"Libro: {libro.title}")
        print(f"Autor: {libro.author.name}")
        print("")

    # Obtener un autor y mostrar sus libros
    autor = Author.objects.first()
    if autor:
        print(f"Autor: {autor.name}")
        print("Libros escritos:")
        for libro in autor.book_set.all():
            print(f" - {libro.title}")



