class MyError(Exception):
    def __init__ (self, valor):
        self.valor = valor
    def __str__(self):
        return "Error: the value is " + str(self.valor)

try:
    resultado = 30
    if resultado > 20:
        raise MyError(resultado)
except MyError as e:
    print (e)