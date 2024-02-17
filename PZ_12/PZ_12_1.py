'''
1.В последовательности на n целых чисел найти и вывести:
1. минимальный среди положительных
2. элементы кратные пяти
3. их среднее арифметическое
2.Из заданной строки отобразить только символы пунктуации. Использовать
библиотеку string.
Строка: --msg-template="File Dir$\{path}:{line}: {column}:{C}:({symbol}){msg}"
'''
import random

arr = [random.randint(-5000, 5000) for _ in range(int(input("Введите n длину последовательности:\n")))]
min_positive = min(list(filter(lambda num: num >= 0, arr)))
multiple_five = list(filter(lambda num: not num % 5, arr))
mean = sum(arr) / len(arr) # могу посчитать сумму и длину без встроенных при помощи например reduce и list comprehension, но это бессмысленно

print(arr)
print(min_positive)
print(multiple_five)
