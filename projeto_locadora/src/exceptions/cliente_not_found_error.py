from src.exceptions.locadora_base_error import LocadoraBaseError


class ClienteNotFoundError(LocadoraBaseError):
    
    def __init__(self, *args):
        super().__init__(*args)
