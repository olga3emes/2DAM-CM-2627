class Ejemplo:
    def publico(self):
        print("Publico")
    def __privado(self):
        print("Privado")

def main():
    ej = Ejemplo()
    ej.publico()
    # ej.__privado()
    # Esto generará un error porque __privado es un metodo privado
    ej._Ejemplo__privado()
    # Esto funciona porque se accede al metodo privado usando su nombre mangled

if __name__ == "__main__":
    main()