class One:
    def __init__(self):
        self.public_attr = 10
        self._private_attr = 100


    def _private_function():
        print("Você não deveria mexer aqui!")


class One:
    def __init__(self):
        self.public_attr = 10
        self._private_attr = 100

class OneChild(One):
    def __init__(self):
        super().__init__()
