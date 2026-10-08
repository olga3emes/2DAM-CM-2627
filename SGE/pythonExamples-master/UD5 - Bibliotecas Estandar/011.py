import zipfile
# Crear un ZIP
with zipfile.ZipFile("ejemplo.zip", "w") as zipf:
    zipf.writestr("saludo.txt", "¡Hola desde un archivo zip!")

# Leer contenido del ZIP
with zipfile.ZipFile("ejemplo.zip", "r") as zipf:
    print("Contenido del ZIP:", zipf.namelist())
    print("Contenido de saludo.txt:", zipf.read("saludo.txt").decode())

import tarfile
# Crear archivo tar
with tarfile.open("ejemplo.tar.gz", "w:gz") as tar:
    tar.add("saludo.txt")  # Asegúrate de que exista
# Leer archivo tar
with tarfile.open("ejemplo.tar.gz", "r:gz") as tar:
    print("Archivos en el TAR:", tar.getnames())

import gzip
# Comprimir texto
with gzip.open("archivo.txt.gz", "wt") as f:
    f.write("Este es un texto comprimido con gzip.")
# Leerlo
with gzip.open("archivo.txt.gz", "rt") as f:
    print("Contenido gzip:", f.read())

import bz2
texto = b"Compresión usando bz2."
# Comprimir y guardar
with bz2.open("archivo.txt.bz2", "wb") as f:
    f.write(texto)
# Leerlo
with bz2.open("archivo.txt.bz2", "rb") as f:
    print("Contenido bz2:", f.read().decode())

import lzma
texto = b"Texto comprimido con lzma."
# Guardar
with lzma.open("archivo.txt.xz", "wb") as f:
    f.write(texto)
# Leer
with lzma.open("archivo.txt.xz", "rb") as f:
    print("Contenido lzma:", f.read().decode())