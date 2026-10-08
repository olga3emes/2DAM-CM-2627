class MostrableMixin:
# Clase mixin para mostrar objetos de forma personalizada
    str_format = "PrettyPrintableObject"
    def __str__(self):
    #Representación automática de un objeto,
    # basado en el uso de una cadena de formateo que es un atributo de la clase
        return self.str_format.format(self=self)

class NombreAutomaticoMixin:
    ordinal = 65
    def __init__(self):
        self.letra = chr(NombreAutomaticoMixin.ordinal)
        NombreAutomaticoMixin.ordinal += 1


class Punto(MostrableMixin, NombreAutomaticoMixin):
    """Representa un punto en el espacio"""
    str_format = "Punto {self.letra} ({self.x}, {self.y}, {self.z})"

    def __init__(self, x, y, z):
        """Metodo de inicialización de un punto en el espacio"""
        super().__init__()
        self.x, self.y, self.z = x, y, z

    def distancia(self, other=None):
        """Devuelve la distancia respecto a otro punto o por defecto al origen"""
        if other is None:
            other = Punto(0, 0, 0)
        return ((self.x-other.x)**2 + (self.y-other.y)**2 + (self.z-other.z)**2) ** (1 / 2)

    def __add__(self, other):
        """Operador de suma"""
        return Punto(self.x + other.x,
                     self.y + other.y,
                     self.z + other.z)

    def __sub__(self, other):
        """Operador de resta"""
        return Punto(self.x - other.x,
                     self.y - other.y,
                     self.z - other.z)

    def __mul__(self, escalar):
        """Operador de multiplicación"""
        return Punto(self.x * escalar,
                     self.y * escalar,
                     self.z * escalar)

    def __iadd__(self, other):
        """Operador de suma en el sitio"""
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __isub__(self, other):
        """Operador de resta en el sitio"""
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self

    def __imul__(self, escalar):
        """Operador de multiplicación en el sitio"""
        self.x *= escalar
        self.y *= escalar
        self.z *= escalar
        return self


class Punto2D(Punto):
    """Representa un punto en el plano"""

    str_format = "Point2D {self.letra} ({self.x}, {self.y})"

    def __init__(self, x, y):
        """Metodo de inicialización de un punto en el plano"""
        super().__init__(x, y, 0)

p = Punto(1, 2, 3)
print(p)
p = Punto2D(1, 2)
print(p)
