from math import pow


class Triangulo:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return self.a + self.b + self.c

    def tipo_lado(self):
        if (self.a == self.b) and (self.b == self.c):
            return "equilátero"
        elif (self.a == self.b) or (self.b == self.c) or (self.a == self.c):
            return "isósceles"
        else:
            return "escaleno"

    def retangulo(self):
        if pow(self.c, 2) == pow(self.a, 2) + pow(self.b, 2):
            return True
        else:
            return False

    def semelhantes(self, triangulo):
        if (self.a / triangulo.a == self.b / triangulo.b
                and self.b / triangulo.b == self.c / triangulo.c
                and self.c / triangulo.c == self.a / triangulo.a):
            return True
        return False


