import unittest
from random import seed
from random import randint
from Scripts.Calculadora import Calculador


class TestVars(unittest.TestCase):

    #setup

    @classmethod
    def setUpClass(cls):
        global calc
        seed(1)
        calc = Calculador()

    def setUp(self):
        calc.a = randint(-100, 100)
        calc.b = randint(-100, 100)

    def tearDown(self):
        del calc.a
        del calc.b

    #Tests

    def test_equals(self):
        try:
            self.assertEqual(calc.a, calc.b)
        except AssertionError:
            pass

    def test_not_none(self):
        self.assertIsNotNone(calc.a)
        self.assertIsNotNone(calc.b)

    def test_first_greater(self):
        try:
            self.assertGreater(calc.a, calc.b)
        except AssertionError:
            pass

    def test_second_greater(self):
        try:
            self.assertGreater(calc.b,calc.a)
        except AssertionError:
            pass

    def test_is_instance(self):
        self.assertIsInstance(calc,Calculador)

    def test_is_not_instance(self):
        with self.assertRaises(AssertionError):
            self.assertNotIsInstance(calc, Calculador)

    def test_equals_0(self):
        try:
            self.assertEqual(calc.a, 0)
        except AssertionError:
            pass
        try:
            self.assertEqual(calc.b, 0)
        except AssertionError:
            pass






if __name__ == '__main__': # pragma: no cover
    suite = unittest.TestSuite()

    #adicionando os testes
    suite.addTest(TestVars('test_equals'))
    suite.addTest(TestVars('test_not_none'))
    suite.addTest(TestVars('test_first_greater'))
    suite.addTest(TestVars('test_second_greater'))
    suite.addTest(TestVars('test_is_instance'))
    suite.addTest(TestVars('test_is_not_instance'))
    suite.addTest(TestVars('test_equals_0'))

    unittest.TextTestRunner().run(suite)
