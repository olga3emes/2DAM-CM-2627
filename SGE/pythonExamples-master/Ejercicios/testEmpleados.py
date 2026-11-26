from Ejercicios.Comercial import Comercial
from Ejercicios.Programador import Programador

empleados = [ Comercial("Pedro", 1500, 100),
              Programador("Juana",3000, "Dart")]

for empleado in empleados:
    empleado.mostrar()
    print("-----------------")