from abc import ABC, abstractmethod
from src.entities.entidade import Entidade
from src.exceptions.cliente_not_found_error import ClienteNotFoundError
from src.exceptions.not_found_error import NotFoundError


class   CadastroAbstract(ABC):

    @property
    @abstractmethod
    def _cadastro(self): 
        """
        define uma variável que representa a lista de cadastro; implemente em cada subclasse
        """ 
        ...
    
    @property
    def cadastro(self):
        """
        getter para cadastro
        """
        return self._cadastro
    
    @cadastro.setter
    def cadastro(self, value: list):
        """
        setter para cadastro
        """
        if isinstance(value, list):
            if value != []:
                Check = True
                for elem in value:
                    if not isinstance(elem,Entidade):
                        Check = False
                        break
                if not Check:
                    raise ValueError("Cadastro inapropriado")
            
            self._cadastro = value
        else:
            raise ValueError("Cadastro inapropriado")

    @cadastro.deleter
    def cadastro(self):
        """
        deleter para cadastro
        """
        del self._cadastro
        
    def inserir(self, entidade):
        """
        insere um dicionário onde keys são variáveis da classe e values são seus respectivos valores; implemente em cada subclasse
        """
        self.cadastro.append(entidade)

    def consultar(self, id: str):
        aux = [entity for entity in self.cadastro if entity.id == id]
        
        if aux == []:
            raise NotFoundError("Entidade não encontrada")

        return aux[0]

    def remover_por_id(self, id: str):
        entidade = self.consultar(id)
        self.cadastro.remove(entidade)

    def remover_por_entidade(self, entidade):
       self.cadastro.remove(entidade)
    
    @classmethod
    def resetar_cadastro(cls):
        cls.cadastro = []


