'''
Дан список размера N. Осуществить сдвиг элементов списка влево на одну позицию
((при эnom An перейдет в An-1, An-1 - в An-2, …, А2 - в А1, а исходное
первого элемента будет потеряно). Последний элемент полученного списка
положить равным 0.
'''
import random

def solution(A: list, N: int) -> list:
    A.pop(0)
    A.append(0)
    return A

length = int(input("Введите длину списка:\n"))
arr = [random.randint(1, 100) for i in range(length)]
print(f"Список: {arr}")
print(f"Преобразованный список: {solution(arr, len(arr))}")