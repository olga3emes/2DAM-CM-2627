import time
def timming_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timming_decorator
def ejemplo_funcion(n):
    """Función que simula un procesamiento intensivo."""
    total = 0
    for i in range(n):
        total += i
    return total
if __name__ == "__main__":
    resultado = ejemplo_funcion(1000000)
    print(f"Resultado: {resultado}")
#Este código define un decorador que mide el tiempo de ejecución de una función.
