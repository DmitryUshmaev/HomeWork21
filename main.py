"""Объект класса Store"""
from courier import Courier
from exceptions import InvalidRequest, BaseError
from request import Request
from shop import Shop
from store import Store

store = Store(items={
    "печенька": 25,
    "собачка": 25,
    "елка": 25
})

"""Объект класса Shop"""

shop = Shop(items={
    "печенька": 2,
    "собачка": 2,
    "елка": 2
})

storages = {
    "магазин": shop,
    "склад": store
}


def main():
    print("Добрый день!")

    while True:
        for storage_name in storages:
            print(f'Сейчас в {storage_name}:\n {storages[storage_name].get_items()}')

        user_input = input("Введите запрос в формате: 'Доставить 3 печенька из склад в магазин'\n"
                           "Введите 'stop' если хотите закончить\n")

        if user_input in ('stop', 'стоп'):
            break

        try:
            request = Request(request=user_input)
        except InvalidRequest as error:
            print(error.message)
            continue

        courier = Courier(request=request, storages=storages)

        try:
            courier.move()
        except BaseError as error:
            print(error.message)


if __name__ == '__main__':
    main()
