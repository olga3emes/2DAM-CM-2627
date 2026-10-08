class EjemploSingleton():
    __instancia = None
    def __init__(self):
        # Constructor privado para evitar la creación de instancias
        if EjemploSingleton.__instancia is not None:
            raise Exception("Esta clase es un singleton, no se puede crear otra instancia.")
    def __new__(cls):
        # Metodo para controlar la creación de instancias
        if cls.__instancia is None:
            cls.__instancia = super(EjemploSingleton, cls).__new__(cls)
        return cls.__instancia

a = EjemploSingleton()
b = EjemploSingleton()
print (a is b) # True , misma referencia a objeto