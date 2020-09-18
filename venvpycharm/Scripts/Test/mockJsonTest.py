import unittest
import json

from Scripts import CalcImcompleta

''' Mockando Classe imcompleta da calculadora'''
'''não possuo acesso nem ao resultado das funções, nem da informação nescessária pra executar'''

class calcMock(CalcImcompleta.Calculador):

    def __init__(self,a,b,somar,subr,multr,divr):
        self._a = a
        self._b = b
        self._somar = somar
        self._subr = subr
        self._multr = multr
        self._divr = divr

    @property
    def somar(self):
        return self._somar

    @property
    def subr(self):
        return self._subr

    @property
    def multr(self):
        return self._multr

    @property
    def divr(self):
        return self._divr

class TestMockJson(unittest.TestCase):

    #setup

    @classmethod
    def setUpClass(cls):
        cls.objects = []
        with open('data.txt') as json_file:
            data = json.load(json_file)
            for i in data['objCalcs']:
                cls.objects.append( calcMock(i['a'], i['b'], i['somar'], i['subr'], i['multr'], i['divr']))

    #Testes

    def test_soma(self):
        for i in range(len(TestMockJson.objects)):
            self.assertEqual(TestMockJson.objects[i].soma(), TestMockJson.objects[i].somar)

    def test_sub(self):
        for i in range(len(TestMockJson.objects)):
            self.assertEqual(TestMockJson.objects[i].sub(), TestMockJson.objects[i].subr)

    def test_mult(self):
        for i in range(len(TestMockJson.objects)):
            self.assertEqual(TestMockJson.objects[i].mult(), TestMockJson.objects[i].multr)

    def test_div(self):
        for i in range(len(TestMockJson.objects)):
            self.assertEqual(TestMockJson.objects[i].div(), TestMockJson.objects[i].divr)
