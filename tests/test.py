import unittest

from src.promocion import main


def leer_resultados(path):
    with open(path, 'r') as archivo:
        lineas = archivo.readlines()
    valor_conseguido = lineas[0].strip()
    influencers = [linea.strip() for linea in lineas[1:]]
    return valor_conseguido, influencers


class MyTestCase(unittest.TestCase):

    def test_caso_example(self):
        main("../data/example.csv")
        valor_conseguido, influencers = leer_resultados("resultado.txt")
        valor_esperado, influencers_esperados = leer_resultados("../data/example_result.txt")
        self.assertEqual(valor_esperado, valor_conseguido)
        self.assertEqual(set(influencers_esperados), set(influencers))

    def test_caso_simple(self):
        # Ejemplo de cómo implementar un caso básico, los demás siguen una lógica similar
        main("../data/simple.csv")
        valor_conseguido, influencers = leer_resultados("resultado.txt")
        valor_esperado, influencers_esperados = leer_resultados("../data/simple_result.txt")
        self.assertEqual(valor_esperado, valor_conseguido)
        self.assertEqual(set(influencers_esperados), set(influencers))

    def test_caso_grande(self):
        main("../data/large.csv")
        valor_conseguido, influencers = leer_resultados("resultado.txt")
        valor_esperado, influencers_esperados = leer_resultados("../data/large_result.txt")
        self.assertEqual(valor_esperado, valor_conseguido)
        self.assertEqual(set(influencers_esperados), set(influencers))

    def test_todos_incompatibles(self):
        main("../data/incompatibles.csv")
        valor_conseguido, influencers = leer_resultados("resultado.txt")
        valor_esperado, influencers_esperados = leer_resultados(
            "../data/incompatibles_result.txt")
        self.assertEqual(valor_esperado, valor_conseguido)
        self.assertEqual(set(influencers_esperados), set(influencers))

    def test_grupos_compatibilidad(self):
        main("../data/groups.csv")
        valor_conseguido, influencers = leer_resultados("resultado.txt")
        valor_esperado, influencers_esperados = leer_resultados(
            "../data/groups_result.txt")
        self.assertEqual(valor_esperado, valor_conseguido)
        self.assertEqual(set(influencers_esperados), set(influencers))

    def test_extra(self):
        main("../data/extra_1.csv")
        valor_conseguido, influencers = leer_resultados("resultado.txt")
        valor_esperado, influencers_esperados = leer_resultados(
            "../data/extra_1_result.txt")
        self.assertEqual(valor_esperado, valor_conseguido)
        self.assertEqual(set(influencers_esperados), set(influencers))

    def test_extra_two(self):
        main("../data/extra_2.csv")
        valor_conseguido, influencers = leer_resultados("resultado.txt")
        valor_esperado, influencers_esperados = leer_resultados(
            "../data/extra_2_result.txt")
        self.assertEqual(valor_esperado, valor_conseguido)
        self.assertEqual(set(influencers_esperados), set(influencers))


if __name__ == '__main__':
    unittest.main()
