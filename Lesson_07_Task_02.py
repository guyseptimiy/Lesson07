# Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
#   реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import abstractmethod


class Wear:

    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        return self.amount + other.amount

    @abstractmethod
    def amount(self):
        pass


class Coat(Wear):

    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def amount(self):
        return self.size / 6.5 + 0.5


class Suit(Wear):

    def __init__(self, name, heiht):
        super().__init__(name)
        self.heiht = heiht

    @property
    def amount(self):
        return 2 * self.heiht + 0.3


coat = Coat('Red coat', 10)
print(f'{coat.name} is {coat.amount}')

suit = Suit('Black suit', 10)
print(f'{suit.name} is {suit.amount}')

print(coat + suit)
