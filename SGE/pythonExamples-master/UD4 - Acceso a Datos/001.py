import os
# Comprobar si un archivo existe antes de abrirlo
if os.path.exists("archivo.txt"):
    with open("archivo.txt", "r") as f:
        print(f.read())
else:
    print("El archivo no existe.")