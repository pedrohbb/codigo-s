"""
How Bootcamps - Stone - /código[s]
Data: 19/04/2022
Autor: Henrique Junqueira Branco
Enunciado: POO - parte 3 - comparação entre objetos de classes próprias
"""


class Employee:
    def __init__(self, name: str, salary: float, level: str) -> None:
        self.name = name
        self.salary = salary
        self.level = level

    def __eq__(self, obj) -> bool:
        if (self.name == obj.name) and (self.salary == obj.salary) and (self.level == obj.level):
            return True
        return False

    # greater than or equal (maior ou igual que)
    def __ge__(self, other) -> bool:
        return self.level >= other.level

    # less than or equal (menor ou igual que)
    def __le__(self, other) -> bool:
        return self.level <= other.level

    # greater than (maior que)
    def __gt__(self, other) -> bool:
        return self.level > other.level

    # less than (menor que)
    def __lt__(self, other) -> bool:
        return self.level < other.level

    def __add__(self, other: object) -> float:
        return self.salary + other.salary

    def __sub__(self, other: object) -> float:
        return self.salary + other.salary

emp1 = Employee("Joao", 2000)
emp2 = Employee("Joao", 5000)

# print(emp1 == emp2)
# print(emp1 >= emp2)
# print(emp1 <= emp2)
# print(emp1 > emp2)
# print(emp1 < emp2)

print(dir(emp1))
