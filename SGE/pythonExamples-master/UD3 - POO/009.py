
# Capturando varias excepciones con un bloque try
try:
    x = int("4eK")
    print(no_existe)
except NameError as e:
    print(f"Error de nombre: {e}")
except ValueError as e:
    print(f"Error de valor: {e}")
# Capturando varias excepciones con un bloque try
try:
    print(no_existe)
    x = int("4eK")
except (NameError, ValueError) as e:
    print(f"Error: {e}")
