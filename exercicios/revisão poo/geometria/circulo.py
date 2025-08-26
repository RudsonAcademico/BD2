from formaGeometrica import FormaGeometrica
class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio
        self.pi = 3.14

    def calcular_perimetro(self):
        return 2*self.pi*self.raio