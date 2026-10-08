# archivo: ejemplo_doctest.py
def cuadrado(n):
    """
    Devuelve el cuadrado de un número.

    >>> cuadrado(3)
    9
    >>> cuadrado(-2)
    4
    """
    return n * n

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
