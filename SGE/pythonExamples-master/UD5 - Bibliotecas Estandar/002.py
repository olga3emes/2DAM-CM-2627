#Expresiones regulares
import re
texto = "Mi número es 654-123-456"
patron = r"\d{3}-\d{3}-\d{3}"
resultado = re.search(patron, texto)
if resultado:
    print("Teléfono encontrado:", resultado.group())

import string
# Mostrar caracteres alfabéticos y dígitos
print(string.ascii_letters)  # abc...XYZ
print(string.digits)         # 0123456789
# Eliminar puntuación
texto = "¡Hola, mundo!"
limpio = texto.translate(str.maketrans('', '', string.punctuation))
print(limpio)  # Hola mundo

#Formatear párrafos
import textwrap
parrafo = "Python es un lenguaje de programación muy versátil y fácil de aprender."
formateado = textwrap.fill(parrafo, width=30)
print(formateado)

#Comparación de secuencias
import difflib
texto1 = "Hola mundo"
texto2 = "Hola mundo cruel"
diferencias = difflib.ndiff(texto1.split(), texto2.split())
print("\n".join(diferencias))

import csv
# Escritura
with open("datos.csv", mode="w", newline="") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["nombre", "edad"])
    escritor.writerow(["Ana", 23])
    escritor.writerow(["Luis", 30])
# Lectura
with open("datos.csv", mode="r") as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(fila)

import json
datos = {"nombre": "Carlos", "edad": 28, "activo": True}
# Convertir a JSON y guardar
with open("usuario.json", "w") as f:
    json.dump(datos, f)
# Leer JSON
with open("usuario.json", "r") as f:
    cargado = json.load(f)
    print(cargado)

import xml.etree.ElementTree as ET
# Crear estructura XML
root = ET.Element("personas")
persona = ET.SubElement(root, "persona", nombre="Lucía")
ET.SubElement(persona, "edad").text = "35"
# Escribir archivo
tree = ET.ElementTree(root)
tree.write("personas.xml")
# Leer archivo
tree = ET.parse("personas.xml")
root = tree.getroot()
for persona in root.findall("persona"):
    print("Nombre:", persona.attrib["nombre"])
    print("Edad:", persona.find("edad").text)