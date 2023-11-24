import unittest

# Importe a classe que você deseja testar
from calc import Calculadora

class TestCalculadora(unittest.TestCase):

    def setUp(self):
        # Crie uma instância da classe antes de cada teste, se necessário
        self.calculadora = Calculadora()

    def test_somar(self):
        # Teste para o método de soma
        resultado = self.calculadora.somar(3, 5)
        self.assertEqual(resultado, 8)

    def test_subtrair(self):
        # Teste para o método de subtração
        resultado = self.calculadora.subtrair(8, 4)
        self.assertEqual(resultado, 4)

    def test_multiplicar(self):
        # Teste para o método de multiplicação
        resultado = self.calculadora.multiplicar(2, 3)
        self.assertEqual(resultado, 6)

# Executar os testes se o script for executado diretamente
if __name__ == '__main__':
    unittest.main()
