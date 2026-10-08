import unittest
import logging
# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def suma(a, b):
    resultado = a + b
    logging.info(f"Suma: {a} + {b} = {resultado}")
    return resultado

def division(a, b):
    if b == 0:
        logging.error("Intento de división por cero")
        raise ValueError("No se puede dividir por cero")
    resultado = a / b
    logging.info(f"División: {a} / {b} = {resultado}")
    return resultado

class TestCalculadora(unittest.TestCase):

    def test_suma_enteros(self):
        resultado = suma(4, 5)
        self.assertEqual(resultado, 9)

    def test_suma_decimales(self):
        resultado = suma(2.5, 3.1)
        self.assertAlmostEqual(resultado, 5.6)

    def test_suma_negativos(self):
        resultado = suma(-2, -3)
        self.assertEqual(resultado, -5)

    def test_division_basica(self):
        resultado = division(10, 2)
        self.assertEqual(resultado, 5)

    def test_division_decimales(self):
        resultado = division(7, 3)
        self.assertAlmostEqual(resultado, 2.3333333, places=6)

    def test_division_negativa(self):
        resultado = division(-6, 2)
        self.assertEqual(resultado, -3)

    def test_division_por_cero(self):
        with self.assertRaises(ValueError):
            division(5, 0)

if __name__ == "__main__":
    unittest.main()
