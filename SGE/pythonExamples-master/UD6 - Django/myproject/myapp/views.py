from django.shortcuts import redirect, render, get_list_or_404, get_object_or_404
from django.http import HttpResponse, Http404
from django.http import JsonResponse
from .models import Author, Book
from django.views.decorators.http import require_http_methods, require_GET


@require_GET
def restriccion_metodos(request):
    if request.method == "POST":
        # Se ha hecho una petición POST
        pass
    elif request.method == "GET":
        # Se ha hecho una petición GET
        pass

def devuelve_saludo(request):
    html = '<html><body>Hello, world!</body></html>'
    return HttpResponse(html)

def redirecciona_saludo(request):
    return redirect("saludo")

# Busca un libro por su ID. Si no existe, lanza Http404
def detalle_libro(request, id):
    libro = get_object_or_404(Book, id=id)
    return render(request, 'detalle_libro.html', {'libro': libro})

# Comprueba que el autor existe y busca todos sus libros.
# Si alguno de los dos no existe, lanza Http404
def libros_por_autor(request, autor_id):
    5/0
    autor = get_object_or_404(Author, id=autor_id)
    libros = get_list_or_404(Book, author=autor)
    return render(request, 'lista_libros_por_autor.html', {
        'autor': autor,
        'libros': libros
    })

# Equivalente a la vista de arriba
def libros_por_autor_excepciones(request, autor_id):
    try:
        autor = Author.objects.get(id=autor_id)
    except Author.DoesNotExist:
        raise Http404("Autor no encontrado")

    libros = Book.objects.filter(author=autor)
    if not libros.exists():
        raise Http404("Este autor no tiene libros registrados")

    return render(request, 'lista_libros_por_autor.html', {
        'autor': autor,
        'libros': libros
    })

# Busca un libro por su ID. Si no existe, lanza Http404.
# Devuelve los datos en JSON
def detalle_libro_json(request, id):
    libro = get_object_or_404(Book, id=id)
    datos = {
        'id': libro.id,
        'titulo': libro.title,
        'autor': libro.author.name
    }
    return JsonResponse(datos)