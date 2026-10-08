# Ejemplo de uso de excepciones personalizadas en Python
# Este código define una excepción personalizada y un manejador de excepciones.
# La clase `MyException` hereda de `Exception` y se utiliza para lanzar una excepción personalizada.
# La clase `ExceptionLauncher` lanza esta excepción, y la clase `ExceptionManager` la maneja.
# La clase `main` ejecuta el programa, creando una instancia de `ExceptionManager` y llamando a su metodo para manejar excepciones.

# Clase MyException
class MyException(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)
        self.mensaje = mensaje
    def __str__(self):
        return f"MyException: {self.mensaje}"

# Clase que lanza una excepción personalizada
class ExceptionLauncher:
    def lanzar_excepcion(self):
        raise MyException("Esta es una excepción personalizada")

# Clase que maneja excepciones
class ExceptionManager:
    def manejar_excepcion(self):
        try:
            lanzador = ExceptionLauncher().lanzar_excepcion()
        except MyException as e:
            print(f"Se ha capturado una excepción: {e}")


# Clase principal que ejecuta el programa para que podamos ver la prueba
class main():
    def exec(self):
        manejador = ExceptionManager()
        manejador.manejar_excepcion()

# Prueba del programa
if __name__ == "__main__":
    programa = main().exec()
