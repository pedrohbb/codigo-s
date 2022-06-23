class Imposto:

    def calcula(self):
        pass    


class ICMS(Imposto):

    def calcula(self, valor_bruto):
        return valor_bruto*(1-0.05)

class IPI(Imposto):

    def calcula(self, valor_bruto):
        return valor_bruto*(1-0.15)

class ISS(Imposto):

    def calcula(self, valor_bruto):
        return valor_bruto*(1-0.05)

class COFINS(Imposto):

    def calcula(self, valor_bruto):
        return valor_bruto*(1-0.03)

