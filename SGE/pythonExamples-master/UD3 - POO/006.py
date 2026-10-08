from Fecha import Fecha

def main():
    # Crear una instancia de Fecha
    fecha = Fecha(15, 8, 2023)

    # Imprimir la fecha
    print(f"Fecha inicial: {fecha.dia}/{fecha.mes}/{fecha.anio}")

    # Modificar la fecha
    fecha.dia = 20
    fecha.mes = 12
    fecha.anio = 2024

    # Imprimir la fecha modificada
    print(f"Fecha modificada: {fecha.dia}/{fecha.mes}/{fecha.anio}")

    # Eliminar el día
    del fecha.dia

    # Intentar imprimir el día eliminado (esto generará un error)
    try:
        print(f"Día eliminado: {fecha.dia}")
    except AttributeError as e:
        print(f"Error: {e}")

    # Crear una copia de la fecha
    fecha_copia = fecha.__clone__()
    print(f"Fecha copia: {fecha_copia.dia}/{fecha_copia.mes}/{fecha_copia.anio}")
    # Comparar dos fechas
    fecha2 = Fecha(20, 12, 2024)
    if fecha == fecha2:
        print("Las fechas son iguales.")
    else:
        print("Las fechas son diferentes.")
    # Imprimir el hash de la fecha
    print(f"Hash de la fecha: {hash(fecha)}")


if __name__ == '__main__':
    main()
