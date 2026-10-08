# Conversión de tipos en Python
x=6
y="3"
# z=x+y  TypeError: unsupported operand type(s) for +: 'int' and 'str'
# Para evitar el error de tipo, debemos convertir 'y' a un entero
z=x+int(y)
print(z)

int("3f",2) # Convierte la cadena hexadecimal "3f" a un entero
a=str(x)
print(a)  # Imprime '6' como cadena
float(a) # Convierte la cadena '6' a un número de punto flotante
float("-11.24 e8") # Convierte la cadena a un número de punto flotante -112400000.0
bool(x) # Convierte el entero 6 a booleano, devuelve True
bool(0) # Convierte el entero 0 a booleano, devuelve False
int(True)  # Devuelve 1
int(False) # Devuelve 0
bool("Hola")  # Devuelve True, ya que la cadena no está vacía
bool("")  # Devuelve False, ya que la cadena está vacía
str(3.14)  # Convierte el número de punto flotante 3.14 a cadena '3.14'
