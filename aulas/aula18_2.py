from abc import ABC, abstractmethod, abstractproperty
import math

#aula18, mas sem usar property
#em aula18 também não faria diferença não usar property, mas estaria formalmente incorreto
#pois em calcula_area usa-se o fato de numlados estar bem definido como property (repare na diferença
# entre o nome do primeiro método de cada script)

class Poligono_Reg(ABC):

    @abstractmethod
    def num_lados(self, n=None):
        """
        define uma variável de instância que representa o número de lados do polígono regular
        """
        self.numlados = n

    @abstractmethod
    def __init__(self, complados):
        self.complados = complados
        self.num_lados()

    
    @abstractmethod
    def calcula_area(self):
        apotema = self.complados/(2*math.tan(math.pi/self.numlados))

        return self.numlados*(self.complados*apotema)/2

class Triângulo(Poligono_Reg):

    def num_lados(self):
        super().num_lados(3)

    def __init__(self, complados):
        super().__init__(complados)
    
    def calcula_area(self):
        return super().calcula_area()

class Quadrado(Poligono_Reg):

    def num_lados(self):
        super().num_lados(4)

    def __init__(self, complados):
        super().__init__(complados)


    def calcula_area(self):
        return super().calcula_area()

class Hexagono(Poligono_Reg):

    def num_lados(self):
        super().num_lados(6)

    def __init__(self, complados):
        super().__init__(complados)


    def calcula_area(self):
        return super().calcula_area()
    
hex = Hexagono(5)

print(hex.numlados, hex.complados)
print(hex.calcula_area())