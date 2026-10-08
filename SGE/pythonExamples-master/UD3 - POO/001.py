from Persona import Persona

def main():
    # Crear una instancia de la clase Persona
    persona1 = Persona("Juan", 30)
    # Llamar al método saludar
    persona1.saludar()
    # Llamar al método cumplir_anios
    persona1.cumplir_anios()
    # Crear otra instancia de la clase Persona
    persona2 = Persona("Ana", 25)
    # Llamar al método saludar
    persona2.saludar()
    # Llamar al método cumplir_anios
    persona2.cumplir_anios()
    # Llamar al método saludar de nuevo para verificar el cambio de edad
    persona2.saludar()

if __name__ == "__main__":
    main()
