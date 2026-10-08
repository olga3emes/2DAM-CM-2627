#Escritura de una lista en un fichero
lineas = ['Uno', 'Dos', 'Tres']
dirFichero = './fichero_escribir.txt'
fichero = open(dirFichero, 'w')
for l in lineas:
    fichero.write(l + '\n')
fichero.close()


