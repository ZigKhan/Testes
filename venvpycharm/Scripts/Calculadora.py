class Calculador:

    def __init__(self):
        self._a = None
        self._b = None

    "get e set a"
    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        self._a = value

    @a.deleter
    def a(self):
        del self._a

    "get e set b"
    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        self._b = value

    @b.deleter
    def b(self):
        del self._b

    def soma(self):
        return self._a + self._b

    def sub(self):
        return self._a - self._b

    def div(self):
        return self._a / self._b

    def multi(self):
        return self._a * self._b


if __name__ == '__main__':
    pass