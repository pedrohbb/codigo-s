from .cadastro_abstract import CadastroAbstract
from src.exceptions.not_found_error import NotFoundError
from src.exceptions.veiculo_not_found_error import VeiculoNotFoundError


class CadastroVeiculo(CadastroAbstract):

    _cadastro = []

    def consultar(self, id: str):
        try:
            return super().consultar(id)
        except NotFoundError:
            raise VeiculoNotFoundError("Cliente não encontrado.")