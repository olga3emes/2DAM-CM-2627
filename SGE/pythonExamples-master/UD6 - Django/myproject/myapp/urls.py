from django.urls import path
from . import views

urlpatterns = [
    path('', views.devuelve_saludo, name='saludo'),
    path('redirect/', views.redirecciona_saludo, name='redireccion'),
    path('libro/<int:id>/json', views.detalle_libro_json, name='detalle_libro_json'),
    path('libro/<int:id>/', views.detalle_libro, name='detalle_libro'),
    path('autor/<int:autor_id>/libros/', views.libros_por_autor, name='libros_por_autor'),
    path('autor/<int:autor_id>/libros/excepciones', views.libros_por_autor_excepciones, name='libros_por_autor_excepciones')
]
