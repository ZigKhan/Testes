import unittest
from random import seed
from random import randint
from Scripts.Calculadora import Calculador



class TestMethods(unittest.TestCase):

    #setup

    @classmethod
    def setUpClass(cls):
        #global calc
        seed(1)
        cls.calc = Calculador()

    def setUp(self):
        TestMethods.calc.a = randint(-100, 100)
        TestMethods.calc.b = randint(-100, 100)

    def tearDown(self):
        del TestMethods.calc.a
        del TestMethods.calc.b


    #tests soma
    def test_soma(self):
        for i in range(100):
            TestMethods.calc.a = randint(-100, 100)
            TestMethods.b = randint(-100, 100)
            self.assertEqual(TestMethods.calc.soma(),TestMethods.calc.a + TestMethods.calc.b)

    def test_soma_positiva(self):
        TestMethods.calc.a = randint(1,100)
        TestMethods.calc.b = randint(1, 100)
        self.assertGreater(TestMethods.calc.soma(),0)

    def test_soma_negativa(self):
        TestMethods.calc.a = randint(-100,-1)
        TestMethods.calc.b = randint(-100,-1)
        self.assertLess(TestMethods.calc.soma(),0)


    # tests sub
    def test_sub(self):
        for i in range(100):
            TestMethods.calc.a = randint(-100, 100)
            TestMethods.calc.b = randint(-100, 100)
            self.assertEqual(TestMethods.calc.sub(), TestMethods.calc.a - TestMethods.calc.b)

    def test_sub_positiva(self):
        TestMethods.calc.a = randint(51, 100)
        TestMethods.calc.b = randint(1, 50)
        self.assertGreater(TestMethods.calc.sub(), 0)

        TestMethods.calc.a = randint(1, 50)
        TestMethods.calc.b = randint(51, 100)
        self.assertLess(TestMethods.calc.sub(), 0)

    def test_sub_negativa(self):
        TestMethods.calc.a = randint(-100, -11)
        TestMethods.calc.b = randint(-10, -1)
        self.assertLess(TestMethods.calc.sub(), 0)
        TestMethods.calc.a = randint(-10, -1)
        TestMethods.calc.b = randint(-100, -11)
        self.assertGreater(TestMethods.calc.sub(), 0)


    # tests mult
    def test_multi(self):
        for i in range(100):
            TestMethods.calc.a = randint(-100, 100)
            TestMethods.calc.b = randint(-100, 100)
            self.assertEqual(TestMethods.calc.multi(), TestMethods.calc.a * TestMethods.calc.b)


    # tests div
    def test_div(self):
        for i in range(100):
            TestMethods.calc.a = randint(-100, 100)
            TestMethods.calc.b = randint(1, 100)
            self.assertEqual(TestMethods.calc.div(), TestMethods.calc.a / TestMethods.calc.b)

            TestMethods.calc.a = randint(-100, 100)
            TestMethods.calc.b = randint(-100, -1)
            self.assertEqual(TestMethods.calc.div(), TestMethods.calc.a / TestMethods.calc.b)

    def test_div_0(self):
        TestMethods.calc.a = randint(-100, 100)
        TestMethods.calc.b = 0
        with self.assertRaises(ZeroDivisionError):
            self.assertEqual(TestMethods.calc.div(),TestMethods.calc.a/TestMethods.calc.b)





if __name__ == '__main__': # pragma: no cover
    suite2 = unittest.TestSuite()

    #adicionando os testes
    suite2.addTest(TestMethods('test_soma'))
    suite2.addTest(TestMethods('test_soma_positiva'))
    suite2.addTest(TestMethods('test_soma_negativa'))
    suite2.addTest(TestMethods('test_sub'))
    suite2.addTest(TestMethods('test_sub_positiva'))
    suite2.addTest(TestMethods('test_sub_negativa'))
    suite2.addTest(TestMethods('test_multi'))
    suite2.addTest(TestMethods('test_div'))
    suite2.addTest(TestMethods('test_div_0'))

    unittest.TextTestRunner().run(suite2)
