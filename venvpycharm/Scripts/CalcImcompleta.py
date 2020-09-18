class Calculador:

    def __init__(self):
        self._a = None
        self._b = None

    def soma(self):
        return self._a + self._b

    def sub(self):
        return self._a - self._b

    def div(self):
        return self._a / self._b

    def mult(self):
        return self._a * self._b