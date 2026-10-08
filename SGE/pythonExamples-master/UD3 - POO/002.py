from Coche import Coche

def main():
    coche1 = Coche(10)
    coche1.arrancar()
    for i in range(12):
        coche1.conducir()
    coche2 = Coche(0)
    coche2.arrancar()
    for i in range(3):
        coche2.conducir()


if __name__ == "__main__":
    main()