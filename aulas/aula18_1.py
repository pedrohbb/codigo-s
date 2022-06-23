from abc import ABC, abstractmethod
import math

class Poligono_Reg(ABC):

    @property
    @abstractmethod
    def numlados(self):
        """
        define uma variável de classe que representa o número de lados do polígono regular; implemente em cada subclasse
        """
        ... 
    
    @abstractmethod
    def __init__(self, complados):
        self.complados = complados

    
    #@abstractmethod
    def calcula_area(self):
        apotema = self.complados/(2*math.tan(math.pi/self.numlados))

        return self.numlados*(self.complados*apotema)/2

class Triângulo(Poligono_Reg):

    numlados = 3

    def __init__(self, complados):
        super().__init__(complados)
    
    def calcula_area(self):
        return super().calcula_area()

    

class Quadrado(Poligono_Reg):

    numlados = 4

    def __init__(self, complados):
        super().__init__(complados)


    def calcula_area(self):
        return super().calcula_area()

class Hexagono(Poligono_Reg):

    numlados = 6

    def __init__(self, complados):
        super().__init__(complados)


    #def calcula_area(self):
        #return super().calcula_area()
    
hex = Hexagono(5)

print(hex.numlados, hex.complados)
print(hex.calcula_area())


#não era preciso definir init e calcula_area como métodos abstratos