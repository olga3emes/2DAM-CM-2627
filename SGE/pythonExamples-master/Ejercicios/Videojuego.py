import copy


class Videojuego:

    def __init__(self, id, titulo, precio):
        self.id = id
        self.titulo = titulo
        self.precio = precio

    def __str__(self):
        return f"{self.id}-{self.titulo}-{self.precio}€"

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id);

    def __copy__(self):
        return Videojuego(self.id, self.titulo, self.precio);

    def __deepcopy__(self, memo):
        return Videojuego(self.id, self.titulo, self.precio);


