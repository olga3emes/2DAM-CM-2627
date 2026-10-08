#abrir fichero con autocierre y codificación leyendo línea a línea
with open('fichero.txt', encoding='utf-8') as f:
 for linea in f:
    print(linea, end='')

#Como el código anterior es muy útil
#podemos utilizarlo y crear una función reutilizable
def lineas_de_fichero(file:str,encoding='utf-8') -> list[str]:
    with open(file,encoding=encoding) as f:
        lineas_de_fichero = [linea.rstrip('\n')
                             for linea in f]
    return lineas_de_fichero