import csv
#with open("datos_2.txt",encoding=encoding) as f:
#    lector = csv.reader(f, delimiter=delimiter)
#    lineas = [linea for linea in lector]
#Diseñamos la función líneas csv para reutilizar este código.
def lineas_de_csv(file:str, delimiter:str=",",encoding='utf-8')-> list[list[str]]:
 with open(file,encoding= encoding) as f:
    lector = csv.reader(f, delimiter = delimiter)
    lineas_de_fichero = [linea for linea in lector]
 return lineas_de_fichero