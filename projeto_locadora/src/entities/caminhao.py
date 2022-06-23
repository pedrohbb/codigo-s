from .veiculo import Veiculo


class Caminhao(Veiculo):

    def __init__(self, id: str, placa: str, km: float, carga: float, status: str):
        Veiculo.__init__(self, id, placa, km, status)
        self.carga = carga
