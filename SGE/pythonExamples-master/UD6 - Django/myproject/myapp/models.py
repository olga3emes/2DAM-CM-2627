from django.db import models
# Create your models here.
class Author(models.Model):
    """
    Model representing an author.
    """
    name = models.CharField(max_length=100)
    birthdate = models.DateField()

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Model representing a book.
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.title

    @property
    def is_classic(self):
        """
        Check if the book is a classic (published before 1970).
        """
        return self.published_date.year < 1970

    def get_summary(self):
        """
        Return a summary of the book.
        """
        return f"{self.title} by {self.author.name}, published on {self.published_date.year}"

class BookAward(models.Model):
    nombre = models.CharField(max_length=100)
    anio = models.PositiveIntegerField()
    pais = models.CharField(max_length=50)
    organizador = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    idioma = models.CharField(max_length=30)
    dotacion_economica = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    fecha_entrega = models.DateField(null=True, blank=True)
    ciudad = models.CharField(max_length=50)
    edicion = models.PositiveIntegerField(help_text="Número de edición del premio", null=True, blank=True)
    ambito = models.CharField(max_length=50, choices=[('internacional', 'Internacional'), ('nacional', 'Nacional')])
    descripcion = models.TextField(blank=True)
    pagina_oficial = models.URLField(blank=True)
    es_activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['nombre', 'anio'], name='unique_premio_anio')
        ]


