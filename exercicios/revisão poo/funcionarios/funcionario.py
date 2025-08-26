class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome 
        self.salario_base = salario

    def calcular_salario(self):
        return self.salario_base