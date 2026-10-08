class Instrumento:
    def __init__ (self, precio):
        self.precio=precio
    def tocar(self):
        print ("Estamos tocando musica")
    def romper(self):
        print ("Eso lo pagas tu")
        print ("Son", self.precio, "$$$")

class Bateria(Instrumento):
    pass # No hace nada, pero es necesario para que Bateria sea una subclase de Instrumento

class Guitarra(Instrumento):
    def __init__(self, precio, tipo_cuerdas):
        #Instrumento.__init__(self,precio)
        super().__init__(precio)  # Llama al constructor de la clase padre Instrumento
        self.tipo_cuerdas = tipo_cuerdas
    def tipo(self):
        print ("Estamos tocando una guitarra de", self.tipo_cuerdas, "cuerdas")
    def tocar(self):
        print(f"{super().tocar()} y estamos tocando una guitarra")