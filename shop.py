from exceptions import TooManyProducts
from storage import BaseStorage

"""Класс Shop наследуется от класса BaseStorage"""


class Shop(BaseStorage):

    def __init__(self, items: dict, capacity: int = 20):
        super().__init__(items, capacity)

    def add(self, name, amount):
        if self.get_unique_items_count() >= 5:
            raise TooManyProducts

        super().add(name, amount)
