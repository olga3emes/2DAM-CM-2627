# CONTEXT MANAGER
class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")
        if exc_type is not None:
            print(f"An exception occurred: {exc_value}")
        return True  # Suppress the exception

    def do_something(self):
        print("Doing something inside the context")

# Uso del Context Manager
with MyContextManager() as manager:
    manager.do_something()
    # Puedes descomentar la siguiente línea para ver cómo se gestiona una excepción
    # raise ValueError("An error occurred")

# El Context Manager permite administrar recursos de manera eficiente, asegurando que se liberen adecuadamente.
# Este ejemplo muestra cómo crear un Context Manager personalizado en Python.
# También puedes usar context managers integrados como open() para gestionar archivos.
# Ejemplo de uso del Context Manager integrado
with open("ejemplo.txt", "w") as file:
    file.write("Este es un ejemplo de uso de un Context Manager para gestionar archivos.")
# El archivo se cierra automáticamente al salir del bloque with.
