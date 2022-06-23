from .cliente import Cliente


class PessoaFisica(Cliente):
    
    def __init__(self, id, nome, endereco, telefone, cpf):
        Cliente.__init__(self, id, nome, endereco, telefone)
        self._cpf = cpf
    
    @property
    def cpf(self):
        return self._cpf
