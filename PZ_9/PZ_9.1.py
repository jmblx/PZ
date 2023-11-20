"""
Вариант 11. Дан словарь с произвольным количеством элементов. Выяснить
имеется ли в нем элемент с ключом «фрукт = груша» и если он присутствует, то
удалить его из словаря. Вывести на экран первоначальный словарь и измененный.
"""


def solution(slovar: dict) -> dict:
    if slovar.get("фрукт") == "груша":
        slovar.pop("фрукт")
    return slovar


slovar_pos = {"фрукт": "груша", "ягода": "арбуз"}
slovar_neg = {"фрукт": "яблоко", "ягода": "банан"}
print(f"До функции:\nfirst: {slovar_pos}\nsecond: {slovar_neg}\nПосле:\n"
      f"first: {solution(slovar_pos)}\nsecond: {solution(slovar_neg)}")
