from aula16_4 import Imposto, ICMS, IPI, ISS, COFINS 

class Venda:
    
    def __init__(self, valor_bruto: float, imp: Imposto):
        self.valor_bruto = valor_bruto
        self.tributo = imp

    def calcula_valor_liquido(self):   
        self.valor_liquido = self.tributo.calcula(self.valor_bruto)

        return self.valor_liquido


v1 = Venda(1000, ICMS())
v2 = Venda(1500, IPI())
v3 = Venda(2000, ISS())
v4 = Venda(2500, COFINS())

print(v1.calcula_valor_liquido(), v2.calcula_valor_liquido(), v3.calcula_valor_liquido(), v4.calcula_valor_liquido())
    