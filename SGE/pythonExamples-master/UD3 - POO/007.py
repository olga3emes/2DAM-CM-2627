from Cuadrado import Cuadrado

def main():
    # Crear una instancia de Cuadrado
    cuadrado = Cuadrado(5)
    # Imprimir el cuadrado
    print(f"Cuadrado inicial: {cuadrado}")
    # Modificar el lado del cuadrado
    cuadrado.lado = 10
    # Imprimir el cuadrado modificado
    print(f"Cuadrado modificado: {cuadrado}")
    # Comparar dos cuadrados
    cuadrado2 = Cuadrado(7)
    if cuadrado == cuadrado2:
        print("Los cuadrados son iguales.")
    elif cuadrado >= cuadrado2:
        print("El primer cuadrado es mayor que el segundo.")
    else:
        print("El primer cuadrado es menor que el segundo.")

if __name__ == '__main__':
    main()
