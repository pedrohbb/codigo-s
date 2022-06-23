from .entidade import Entidade
from src.business.cadastro_cliente import CadastroCliente


class Cliente(Entidade):

    def __init__(self, id, nome, endereco, telefone):
        Entidade.__init__(self,id)
        self._nome = nome
        self._endereco = endereco
        self._telefone = telefone
    
    @property
    def nome(self):
        return self._nome

    @property
    def endereco(self):
        return self._endereco
    
    @property
    def telefone(self):
        return self._telefone
    
    def alugar(self):
        return  


