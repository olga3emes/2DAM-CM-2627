

#Enunciado: Pide al usuario su nombre y edad. Muestra cuántos años tendrá dentro de 10 años.

nombre = input("Introduce aquí tu nombre: ")
edad = int(input("Introduce tu edad: "))

print(f"Hola {nombre},dentro de 10 años tendrás {edad+10} años.")

# Pedimos 2 numeros y sumamos, restamos, multipllicamos y dividimos.

num1= float(input("Introduce el primer número: "))
num2= float(input("Introduce el segundo número: "))

print("Suma: ", num1 + num2)
print("Resta: ", num1 - num2)
print("Multiplicacion: ", num1 * num2)
print("Division: ", num1 / num2)
print("Resto o módulo: ", num1 % num2)
print("Potencia:", num1 ** num2)


if(num1 % 2 ==0):
    print("es par")
else:
    print("impar")

a = float(input("Introduce el primer número: "))
b= float(input("Introduce el segundo número: "))
c= float(input("Introduce el tercer número: "))


mayor = a

if( b > mayor ):
    mayor = b
if( c > mayor ):
    mayor = c

print("El mayor es ", mayor)


semaforo="54t4t54t"

if( semaforo =="rojo"):
    print("para")
elif(semaforo=="amarillo"):
    print("cuidado peaton con prioridad")
elif(semaforo=="verde"):
    print("pasa")
else:
    print("semaforo no funciona")

match semaforo:
    case "rojo":
        print("para")
    case "amarillo":
        print("cuidado peaton con prioridad")
    case "verde":
        print("pasa")
    case _:
        print("semaforo no funciona")


#Introduce un precio y Aplicar:

#10% si supera 500 €
#5% si supera 100 €
#Sin descuento en otro caso

precio = float(input("Introduce el precio: "))

if(precio > 500):
    precio_final=precio*0.9
elif (precio > 100):
    precio_final=precio*0.95
else:
    precio_final=precio

print("Precio final: ", precio_final)

