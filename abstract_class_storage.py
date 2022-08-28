from abc import ABC, abstractmethod

"""Абстрактный класс Storage"""


class Storage(ABC):
    """Добавить товар"""

    @abstractmethod
    def add(self, name: str, amount: int):
        pass

    """Удалить товар"""

    @abstractmethod
    def remove(self, name: str, amount: int):
        pass

    """Вернуть количество свободных мест"""

    @abstractmethod
    def get_free_space(self):
        pass

    """Возвращает сожержание склада в словаре"""

    @abstractmethod
    def get_items(self):
        pass

    """Возвращает количество уникальных товаров"""

    @abstractmethod
    def get_unique_items_count(self):
        pass
