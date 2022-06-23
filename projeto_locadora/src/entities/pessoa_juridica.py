from .cliente import Cliente


class PessoaJuridica(Cliente):

    def __init__(self, id, nome, endereco, telefone, cnpj):
        Cliente.__init__(self, id, nome, endereco, telefone)
        self._cnpj  = cnpj

    @property
    def cnpj(self):
        return self._cnpj
