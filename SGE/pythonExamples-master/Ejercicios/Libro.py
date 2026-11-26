# Ejercicio 15. Gestión de biblioteca con POO
#
# Clases:
#
# Libro
# Usuario
# Biblioteca
#
# Funciones:
#
# Prestar libro
# Devolver libro
# Listar disponibles
# Buscar por título



class Libro:

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.prestado = False

    def prestar(self):
        if( not self.prestado):
            self.prestado = True
            return True
        return False
    def devolver(self):
        if(self.prestado):
            self.prestado = False
            return True
        return False

    def __str__(self):
        estado= "Prestado"  if self.prestado else "Disponible"
        return estado + ": " + self.titulo + " - " + self.autor