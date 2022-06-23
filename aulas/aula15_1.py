"""
12.04.2022
prof.: Henrique Junqueira
tema: POO - Introdução
"""

class Funcionario:

    #método construtor    
    def __init__(self, nome: str, sobrenome: str, salario: float) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = f"{self.nome.lower().replace(' ', '')}.{self.sobrenome.lower().replace(' ', '')}@email.com"
        self._salario_inicial = salario
        self.__salario_atual = self._salario_inicial

    def dar_aumento(self, aumento_percentual: float):
        #try:
        #    self.__salario_atual = round(self.__salario_atual*(1 + aumento_percentual),2)
        #except AttributeError:
        #    self.__salario_atual = round(self.__salario_inicial*(1 + aumento_percentual),2)
        self.__salario_atual = round(self.__salario_atual*(1+aumento_percentual),2)
    
    def salario(self):
        print(self.__salario_atual)
        
    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
    
    def __repr__(self):
        return self.__str__()

x = Funcionario('Shazzan','Great Hero', float('inf'))
print(x)



