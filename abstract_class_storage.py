from abc import ABC, abstractmethod

"""Абстрактный класс Storage"""


class Storage(ABC):

    @abstractmethod
    def add(self, name: str, amount: int):
        """Добавить товар"""
        pass

    @abstractmethod
    def remove(self, name: str, amount: int):
        """Удалить товар"""
        pass

    @abstractmethod
    def get_free_space(self):
        """Вернуть количество свободных мест"""
        pass

    @abstractmethod
    def get_items(self):
        """Возвращает сожержание склада в словаре"""
        pass

    @abstractmethod
    def get_unique_items_count(self):
        """Возвращает количество уникальных товаров"""
        pass
