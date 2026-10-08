import threading
import time
#Programación con hilos
def tarea(nombre):
    print(f"{nombre} ha comenzado")
    time.sleep(2)
    print(f"{nombre} ha terminado")

# Crear hilos
hilo1 = threading.Thread(target=tarea, args=("Hilo 1",))
hilo2 = threading.Thread(target=tarea, args=("Hilo 2",))
# Iniciar
hilo1.start()
hilo2.start()
# Esperar a que terminen
hilo1.join()
hilo2.join()

#Procesos paralelos
import multiprocessing
import time

def proceso(nombre):
    print(f"{nombre} iniciado")
    time.sleep(2)
    print(f"{nombre} finalizado")

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=proceso, args=("Proceso 1",))
    p2 = multiprocessing.Process(target=proceso, args=("Proceso 2",))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
# Importante:
# multiprocessing requiere proteger el bloque if __name__ == "__main__": para evitar errores en Windows.

import asyncio
async def tarea(nombre):
    print(f"{nombre} ha comenzado")
    await asyncio.sleep(2)
    print(f"{nombre} ha terminado")

async def main():
    await asyncio.gather(
        tarea("Tarea 1"),
        tarea("Tarea 2")
    )
asyncio.run(main())
