"""
Вариант 11.
1. В матрице найти сумму и произведение элементов строки N (N задать с клавиатуры).
"""
import random
from functools import reduce

x, y = random.randint(1, 6), random.randint(1, 6)
print(f"Размер матрицы {x}X{y}")

arr = [[random.randint(-10, 10) for num in range(x)] for n in range(y)]
print("Матрица:")
list(map(lambda s: print(s), arr))

N = int(input("у какой строки посчитать посчитать сумму и произведение элементов строки?:\n"))
try:
    print(f"Сумма {N} строки матрицы:\n{sum(arr[N-1])}")
    print(f"Произведение {N} строки матрицы:\n{reduce(lambda n1, n2: n1*n2, arr[N-1])}")
except:
    print("Ошибка, введите число в пределах количества строк в матрице")
