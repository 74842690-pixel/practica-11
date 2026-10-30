import unittest
from src.tienda_refactored import calcular_total


class TestTienda(unittest.TestCase):
    def test_cliente_vip(self):
        self.assertEqual(calcular_total([(100, 2)], "vip", 20), 160)

    def test_cliente_estudiante(self):
        self.assertEqual(calcular_total([(100, 2)], "est", 20), 170)

    def test_cliente_mayorista(self):
        self.assertEqual(calcular_total([(100, 2)], "may", 20), 140)

    def test_cliente_normal(self):
        self.assertEqual(calcular_total([(100, 1)], "normal", 20), 100)

    def test_descuento_distancia_larga(self):
        self.assertEqual(calcular_total([(100, 1)], "normal", 120), 95)

    def test_descuento_distancia_media(self):
        self.assertEqual(calcular_total([(100, 1)], "normal", 70), 98)

    def test_sin_descuento_distancia(self):
        self.assertEqual(calcular_total([(100, 1)], "normal", 50), 100)

    def test_total_no_negativo(self):
        self.assertEqual(calcular_total([(1, 1)], "vip", 120), 0)

    def test_varios_productos(self):
        self.assertEqual(calcular_total([(10, 2), (5, 3)], "normal", 20), 35)


if __name__ == "__main__":
    unittest.main()
