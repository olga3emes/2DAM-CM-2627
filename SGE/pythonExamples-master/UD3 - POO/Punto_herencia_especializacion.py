class Punto:
    """Representa un punto en el espacio"""

    def __init__(self, x, y, z):
        """Método de inicialización de un punto en el espacio"""
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

    def __mul__(self, scalaire):
        """Operador de multiplicación"""
        return Punto(self.x * scalaire,
                     self.y * scalaire,
                     self.z * scalaire)

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

    def __imul__(self, scalaire):
        """Operador de multiplicación en el sitio"""
        self.x *= scalaire
        self.y *= scalaire
        self.z *= scalaire
        return self

    def __str__(self):
        """Representación de un punto como cadena de caracteres"""
        return f"Punto ({self.x}, {self.y}, {self.z})"


class Punto2D(Punto):
    """Representa un punto en el plano"""

    def __init__(self, x, y):
        """Método de inicialización de un punto en el plano"""
        super().__init__(x, y, 0)

    def __str__(self):
        return f"Punto2D ({self.x}, {self.y})"


p = Punto2D(1, 2)
p += Punto2D(3, 0)
print(p)
