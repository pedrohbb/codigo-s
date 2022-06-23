from .entidade import Entidade


class Veiculo(Entidade):

    def __init__(self, id: str, placa: str, km: float, status: str):
        Entidade.__init__(self,id)
        self._km = km
        self._placa = placa
        self._tatus = status

    @property
    def placa(self):
        return self._placa
    
    @property
    def km(self):
        return self._km
    