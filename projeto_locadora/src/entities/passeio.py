from .veiculo import Veiculo


class Passeio(Veiculo):

    def __init__(self, id: str, placa: str, km: float, bagageiro: int, portas: int, status: str):
        Veiculo.__init__(self, id, placa, km, status)
        self._bagageiro = bagageiro
        self._portas = portas
    
    @property
    def bagageiro(self):
        return self._bagageiro
    
    @property
    def portas(self):
        return self._portas

    
