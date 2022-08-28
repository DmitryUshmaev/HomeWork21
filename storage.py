from typing import Dict

from abstract_class_storage import Storage
from exceptions import NotEnoughSpace, NotEnoughProduct

"""Класс BaseStorage наследуется от абстрактного класса Storage"""


class BaseStorage(Storage):
    def __init__(self, items: Dict[str, int], capacity: int):
        self.__items = items
        self.__capacity = capacity

    def add(self, name: str, amount: int):

        """Проверка количества мест"""

        if self.get_free_space() < amount:
            raise NotEnoughSpace

        if name in self.__items:
            self.__items[name] += amount
        else:
            self.__items[name] = amount

    def get_free_space(self):
        current_space = 0

        for value in self.__items.values():
            current_space += value

        return self.__capacity - current_space

    def remove(self, name, amount: int):

        """Проверить есть ли товар и достаточно ли количество товара"""

        if name not in self.__items or self.__items[name] < amount:
            raise NotEnoughProduct

        self.__items[name] -= amount

        if self.__items[name] == 0:
            self.__items.pop(name)

    def get_items(self):
        return self.__items

    def get_unique_items_count(self):
        return len(self.__items)
