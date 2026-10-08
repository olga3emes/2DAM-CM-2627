#LOGS
import logging
# Configuración básica
logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(message)s")
logging.debug("Mensaje de depuración")
logging.info("Mensaje informativo")
logging.warning("Mensaje de advertencia")
logging.error("Mensaje de error")
logging.critical("Mensaje crítico")

#WARNINGS
import warnings
# Generar una advertencia
warnings.warn("Esta es una advertencia personalizada", UserWarning)

#Rastreo de errores
import traceback
try:
    1 / 0  # Error intencional
except ZeroDivisionError:
    print(f"Ocurrió un error:{traceback.print_exc()}")

#pdb – Depurador interactivo
import pdb
def sumar(a, b):
    pdb.set_trace()
    return a + b
print("Resultado:", sumar(2, 3))

