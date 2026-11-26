from Ejercicios.Empleado import Empleado


class Comercial(Empleado):

    def __init__(self, nombre,salario,comision):
        super().__init__(nombre,salario)
        self.comision = comision

    def mostrar(self):
        super().mostrar()
        print(f"Comision: {self.comision}")

