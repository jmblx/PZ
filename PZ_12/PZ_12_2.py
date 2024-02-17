'''
2.Из заданной строки отобразить только символы пунктуации. Использовать
библиотеку string.
Строка: --msg-template="File Dir$\{path}:{line}: {column}:{C}:({symbol}){msg}"
'''
from string import punctuation

stroka = '--msg-template="File Dir$\{path}:{line}: {column}:{C}:({symbol}){msg}"'

res = "".join((list(filter(lambda c: c in punctuation, stroka))))
print(f"Символы пунктуации {res}")

# Генератором:
# def punctuation_generator(string):
#     for char in string:
#         if char in punctuation:
#             yield char
#
# res = "".join(punctuation_generator(stroka))
# print(res)