import os
# Obtener el directorio/carpeta actual
print("Directorio actual:", os.getcwd())
# Listar archivos de una carpeta/directorio
print("Contenido:", os.listdir("."))
# Crear un nuevo directorio/carpeta
os.mkdir("nueva_carpeta")

import io
# Crear un flujo de texto en memoria
archivo_virtual = io.StringIO()
archivo_virtual.write("Hola, mundo")
archivo_virtual.seek(0)
print(archivo_virtual.read())  # Imprime: Hola, mundo

import sys
# Mostrar argumentos pasados al script
print("Argumentos:", sys.argv)
# Salir del programa con código de salida
# sys.exit(0)

import shutil
# Copiar archivo
shutil.copy("archivo.txt", "copia_archivo.txt")
# Mover archivo
shutil.move("copia_archivo.txt", "nueva_carpeta/copia_archivo.txt")

from pathlib import Path
ruta = Path("nueva_carpeta") / "copia_archivo.txt"
print("Ruta completa:", ruta)
# Verificar si existe
if ruta.exists():
    print("El archivo existe")
# Obtener nombre del archivo
print("Nombre del archivo:", ruta.name)

import fileinput
# Leer múltiples archivos como si fuera uno solo
for linea in fileinput.input(files=('archivo1.txt', 'archivo2.txt')):
    print(linea.strip())