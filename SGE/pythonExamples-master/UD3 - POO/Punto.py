class Punto:
    """Representa un punto en el espacio"""

    def __init__(self, x, y, z):
        """Metodo de inicialización de un punto en el espacio"""
        self.x = x
        self.y = y
        self.z = z

    def mostrar(self):
        """Metodo temporal utilizado para mostrar nuestro punto"""
        print("Point ({}, {}, {})".format(self.x, self.y, self.z))

    def mostrar_fstring(self):
        """Metodo temporal utilizado para mostrar nuestro punto"""
        print(f"Point ({self.x}, {self.y}, {self.z})")

    def modulo(self):
        """Devuelve el módulo del punto"""
        return (self.x**2 + self.y**2 + self.z**2) ** (1 / 2)

    def distancia(self, other):
        #Devuelve la distancia respecto a otro punto. Las variables self y other son ambas puntos
        return ((self.x-other.x)**2 + (self.y-other.y)**2 + (self.z-other.z)**2) ** (1 / 2)

    def distancia_y_modulo(self, other=None):
        """Devuelve la distancia respecto a otro punto o por defecto al origen"""
        if other is None:
            other = Punto(0, 0, 0)
        return ((self.x-other.x)**2 + (self.y-other.y)**2 + (self.z-other.z)**2) ** (1 / 2)


p = Punto(1, 2, 3)
p.mostrar()
print("|p| =", p.modulo())
print("distancia entre p y (1, 2, 5) es ", p.distancia(Punto(1, 2, 5)))
print("|p| =", p.distance_et_module())
print("distancia entre p y (1, 2, 5) es ", p.distancia_y_modulo(Punto(1, 2, 5)))
