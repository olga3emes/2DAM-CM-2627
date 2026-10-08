from Cocodrilo_herencia_multiple import Cocodrilo

def main():
    coco = Cocodrilo(4, 0, "5 metros")
    print(f"El cocodrilo tiene {coco.patas} patas, "
          f"{coco.aletas} aletas y mide {coco.longitud}.")

if __name__ == "__main__":
    main()
