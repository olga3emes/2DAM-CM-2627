# Clases en Python

# En este ejemplo, se define una clase llamada Persona que tiene dos atributos: nombre y edad.
# Definición de la clase Persona
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")
    def cumplir_anios(self):
        self.edad += 1
        print(f"Ahora tengo {self.edad} años.")




