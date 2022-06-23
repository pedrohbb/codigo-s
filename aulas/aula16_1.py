"""
12.04.2022
prof.: Henrique Junqueira
tema: POO - Introdução - parte 2
"""

class Funcionario:

    #método construtor    
    def __init__(self, nome: str, sobrenome: str, salario: float) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = f"{self.nome.lower().replace(' ', '')}.{self.sobrenome.lower().replace(' ', '')}@email.com"
        self.__salario_inicial = salario
        self.salario_atual = self.__salario_inicial

    def dar_aumento(self, aumento_percentual: float):
        self.salario_atual = round(self.salario_atual*(1+aumento_percentual),2)
    
    #@property
    def salario_inicial(self):
        return self.__salario_inicial
    
    def bonus(self,x):
        return self.__salario_inicial + x

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
    
    def __repr__(self):
        return self.__str__()




