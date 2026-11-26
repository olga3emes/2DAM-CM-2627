# divina el número
#
# El ordenador genera un número aleatorio entre 1 y 100.
#
# El usuario debe adivinarlo.
#
# Después de cada intento indica:
#
# Mayor
# Menor
# Correcto
import random

numero= random.randint(1,100)

while True:
    intento = int(input("Introduce un numero: "))

    if(intento < numero):
        print("Más grande")
    elif(intento > numero):
        print("Más pequeño")
    else:
        print("¡Correcto!")
        break
