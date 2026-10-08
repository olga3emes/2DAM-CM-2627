#Escritura en un archivo
with open('f_e.txt', mode='w', encoding='utf-8') as f:
    f.write('Este texto se almacenará en el f.')
#Comprobemos si se ha realizado la escritura correctamente:
with open('f_e.txt', encoding='utf-8') as f:
    for linea in f:
        print(linea, end='')

# Diseñamos igualmente la función reutilizable write.
def write(file:str,texto:str) -> None:
    with open(file, "w", encoding='utf-8') as f:
        f.write(texto)

# Lectura y escritura simultáneas
with open("miarchivo.txt", "r+") as f:
    datos = f.read()
    f.seek(0)
    f.write("Encabezado añadido\n")
#Añade al principio del archivo sin borrarlo