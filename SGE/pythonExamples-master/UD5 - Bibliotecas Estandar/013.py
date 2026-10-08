import argparse

parser = argparse.ArgumentParser(description="Saluda al usuario")
parser.add_argument("nombre", help="Nombre del usuario")
args = parser.parse_args()
print(f"¡Hola, {args.nombre}!")
# Para ejecutar este script desde la línea de comandos, guarda el código en un archivo llamado `saludo.py`
# y luego ejecuta el siguiente comando en la terminal:
# python saludo.py TuNombre

import subprocess

# Ejecutar 'ls' o 'dir' dependiendo del sistema operativo
comando = ["ls"]  # o ["dir"] en Windows
resultado = subprocess.run(comando, capture_output=True, text=True)
print("Salida del comando:")
print(resultado.stdout)

from typing import List

def suma_lista(numeros: List[int]) -> int:
    return sum(numeros)
print("Resultado:", suma_lista([1, 2, 3]))

# compile + eval
codigo = "3 * (2 + 1)"
codigo_compilado = compile(codigo, "<string>", "eval")
resultado = eval(codigo_compilado)
print("Resultado con eval:", resultado)

# exec para ejecutar múltiples líneas
bloque = """
for i in range(3):
    print("Línea", i)
"""
exec(bloque)
