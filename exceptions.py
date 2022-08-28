"""Исключения и ошибки"""

class BaseError(Exception):
    message = "Неожиданная ошибка"


class NotEnoughSpace(BaseError):
    message = "Недостаточно места на складе"


class NotEnoughProduct(BaseError):
    message = "Недостаточно товара на складе"


class TooManyProducts(BaseError):
    message = "Слишком много разных товаров"


class InvalidRequest(BaseError):
    message = "Неправильный запрос"
