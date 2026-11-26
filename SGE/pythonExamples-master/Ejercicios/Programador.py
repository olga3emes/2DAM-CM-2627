from Ejercicios.Empleado import Empleado


class Programador(Empleado):

    def __init__(self, nombre, salario, lenguaje):
        super().__init__(nombre, salario)
        self.lenguaje = lenguaje


    def mostrar(self):
        super().mostrar()
        print(f"Lenguaje: {self.lenguaje}")

