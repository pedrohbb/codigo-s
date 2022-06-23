from src.exceptions.locadora_base_error import LocadoraBaseError


class NotFoundError(LocadoraBaseError):

    def __init__(self, *args):
        super().__init__(*args)