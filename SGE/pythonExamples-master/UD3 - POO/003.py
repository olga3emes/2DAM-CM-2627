from Instrumento import Instrumento
from Instrumento import Bateria
from Instrumento import Guitarra

def main():
    # Crear una instancia de la clase Instrumento
    instrumento = Instrumento(100)
    instrumento.tocar()
    instrumento.romper()

    # Crear una instancia de la clase Bateria
    bateria = Bateria(200)
    bateria.tocar()
    bateria.romper()

    # Crear una instancia de la clase Guitarra
    guitarra = Guitarra(150, 6)
    guitarra.tipo()
    guitarra.tocar()
    guitarra.romper()

if __name__ == "__main__":
    main()