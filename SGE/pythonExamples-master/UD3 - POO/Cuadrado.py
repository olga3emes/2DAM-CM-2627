from functools import total_ordering

@total_ordering
class Cuadrado:
    def __init__(self,lado):
        self.lado = lado
    def __lt__(self,otro):
        return self.lado < otro.lado
    def __eq__(self,otro):
        return self.lado == otro.lado

    def __str__(self):
        return f"Cuadrado de lado {self.lado}"

