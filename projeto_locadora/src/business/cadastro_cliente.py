from src.exceptions.cliente_not_found_error import ClienteNotFoundError
from src.exceptions.not_found_error import NotFoundError
from .cadastro_abstract import CadastroAbstract
from src.exceptions.not_found_error import NotFoundError
from src.exceptions.cliente_not_found_error import ClienteNotFoundError


class CadastroCliente(CadastroAbstract):

    _cadastro = []

    def consultar(self, id: str):
        try:
            return super().consultar(id)
        except NotFoundError:
            raise ClienteNotFoundError("Cliente não encontrado.")
    
