class Terrestre():
    def __init__(self, patas): #Definimos los Atributos
        self.patas = patas
class Acuatico():
    def __init__(self, aletas): #Definimos los Atributos
        self.aletas = aletas
class Cocodrilo(Terrestre, Acuatico):
    def __init__(self, patas, aletas,longitud):
        Terrestre.__init__(self, patas) #Llamada al primer constructor
        Acuatico.__init__(self, aletas) #Llamada al segundo constructor
        self.longitud = longitud

