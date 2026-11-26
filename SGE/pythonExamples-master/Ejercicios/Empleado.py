class Empleado:

    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Salario: {self.salario}")

