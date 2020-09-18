import unittest
from random import seed
from random import randint
from Scripts import Calculadora
import unittest.mock as Mock


class TestMock(unittest.TestCase):

    def setUp(self):
        seed(1)
        self.calc = Calculadora.Calculador()
        self.calc.a = randint(-100, 100)
        self.calc.b = randint(-100, 100)
        self.calc.soma = Mock.MagicMock(return_value=self.calc.a + self.calc.b)
        self.calc.sub = Mock.MagicMock(return_value=self.calc.a - self.calc.b)
        self.calc.multi = Mock.MagicMock(return_value=self.calc.a * self.calc.b)
        self.calc.div = Mock.MagicMock(return_value=self.calc.a / self.calc.b)


    def test_mock_soma(self):
        self.calc.soma = Mock.MagicMock(return_value=self.calc.a + self.calc.b)
        self.assertEqual(self.calc.soma(), self.calc.a + self.calc.b)

    def test_mock_sub(self):
        self.calc.sub= Mock.MagicMock(return_value=self.calc.a - self.calc.b)
        self.assertEqual(self.calc.sub(), self.calc.a - self.calc.b)

    def test_mock_multi(self):
        self.calc.multi = Mock.MagicMock(return_value=self.calc.a * self.calc.b)
        self.assertEqual(self.calc.multi(), self.calc.a * self.calc.b)

    def test_mock_div(self):
        self.calc.div = Mock.MagicMock(return_value=self.calc.a / self.calc.b)
        self.assertEqual(self.calc.div(), self.calc.a / self.calc.b)

if __name__ == '__main__': # pragma: no cover
    suite3 = unittest.TestSuite()

    #adicionando os testes
    suite3.addTest(TestMock('test_mock_soma'))
    suite3.addTest(TestMock('test_mock_sub'))
    suite3.addTest(TestMock('test_mock_multi'))
    suite3.addTest(TestMock('test_mock_div'))


    unittest.TextTestRunner().run(suite3)

