from formaGeometrica import FormaGeometrica
class Retangulo(FormaGeometrica):
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def calcular_perimetro(self):
        return self.altura * self.largura