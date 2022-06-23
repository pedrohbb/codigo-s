from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        raise NotImplementedError()

    
class MySQL(Database):

    def connect(self):
        print("Conectando ao MySQL")


class PostgreSQL(Database):

    def connect(self):
        print("Conectando ao PostgreSQL")


class SQLServer(Database):

    def connect(self):
        print("Conectando ao SQLServer")
    pass


s = SQLServer()


