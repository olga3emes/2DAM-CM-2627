# Lectura de un fichero de texto línea a línea
dirFichero = './fichero_leer.txt'
reader = open(dirFichero, 'r')
for line in reader:
    print (line)
reader.close()