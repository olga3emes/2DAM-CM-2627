#Excepciones
# Ejemplo de manejo de excepciones en Python
def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b

def main():
    try:
        resultado = dividir(10, 0)
        print(f"Resultado: {resultado}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    else:
        print("División exitosa")
    finally:
        print("Fin del programa")

if __name__ == '__main__':
    main()
