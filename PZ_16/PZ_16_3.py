'''
Для задачи из блока 1 создать две функции, save def load def, которые позволяют
сохранять информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно.
Использовать модуль pickle для сериализации и десериализации объектов Python в
бинарном формате.
'''
import pickle

from PZ_16.PZ_16_1 import Product

products = [
    Product(name="мяч", cost=2699.99, quantity=9),
    Product(name="монитор", cost=9000, quantity=4),
    Product(name="смартфон", cost=11499, quantity=5)
]


def dump_objs(objs: list):
    for i in range(len(objs)):
        with open(f"out{i}.bin", "wb") as file:
            pickle.dump(objs[i], file)


def load_objs(objs_len: int):
    for i in range(objs_len):
        with open(f"out{i}.bin", "rb") as file:
            products = pickle.load(file)
            print(products.__dict__)


dump_objs(products)
load_objs(len(products))
