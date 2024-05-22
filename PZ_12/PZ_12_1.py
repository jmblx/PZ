'''
1.В последовательности на n целых чисел найти и вывести:
1. минимальный среди положительных
2. элементы кратные пяти
3. их среднее арифметическое
'''
import random

arr = [random.randint(-5000, 5000) for _ in range(int(input("Введите n длину последовательности:\n")))]
min_positive = min(list(filter(lambda num: num >= 0, arr)))
multiple_five = list(filter(lambda num: not num % 5, arr))
mean = sum(arr) / len(arr) # могу посчитать сумму и длину без встроенных при помощи например reduce и list comprehension, но это бессмысленно

print(f'''
Исходные данные: {arr}
Минимальный среди положительных: {min_positive}
Элементы кратные пяти: {multiple_five}
Их среднее арифметическое: {mean}
'''
)
