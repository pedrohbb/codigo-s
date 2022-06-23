class Ave:

    def __init__(self, qtd_patas, cor, tamanho):
        self.qtd_patas = qtd_patas
        self.cor = cor
        self.tamanho = tamanho
    
    def bater_asa(self):
        print("Batendo asa!")


class Tucano(Ave):

    mancha_no_olho = True                 #variável de classe

    def __init__(self):
        Ave.__init__(self, 2, 'colorido', 'pequeno')

    
    def bater_asa(self):
        print("Batendo asa como tucano!")
    
    #------ou--------#

    #def __init__(self):
    #    super().__init__(2, 'colorido', 'pequeno')
    
        
corvo = Ave(2, 'preto', 'grande')
t = Tucano()
t.bater_asa()
print(type(t) == Tucano)
