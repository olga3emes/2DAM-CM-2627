import csv


def lineas_de_fichero(file:str,encoding='utf-8') -> list[str]:
    with open(file,encoding=encoding) as f:
        lineas_de_fichero = [linea.rstrip('\n')
                             for linea in f]
    return lineas_de_fichero

lineas = lineas_de_fichero("datos.txt", 'utf-8')
contar_lineas = 0
for ln in lineas:
    contar_lineas = contar_lineas+1
print(f"Hay {contar_lineas} lineas")

contar_lineas_vacias = 0
for ln in lineas:
    if len(ln) == 0:
        contar_lineas_vacias = contar_lineas_vacias+1
print(f"Hay {contar_lineas_vacias} lineas vacías")

def lineas_de_csv(file:str, delimiter:str=",",encoding='utf-8')-> list[list[str]]:
 with open(file,encoding= encoding) as f:
    lector = csv.reader(f, delimiter = delimiter)
    lineas_de_fichero = [linea for linea in lector]
 return lineas_de_fichero

lineas=lineas_de_csv("datos.txt",delimiter=',')
numeros = 0
suma = 0
for ln in lineas:
    for num in ln:
        numeros = numeros+1
        suma = suma+int(num)
print(f"Hay {numeros} números, cuya suma da {suma}.")