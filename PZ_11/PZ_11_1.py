'''
1. Средствами языка Python сформировать текстовый файл (.txt), содержащий
последовательность из целых положительных и отрицательных чисел. Сформировать
новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
обработку элементов:
Исходные данные:
Количество элементов:
Минимальный элемент:
Количество положительных элементов в первой половине:
'''
import random

with open("source_data.txt", "w", encoding="utf-8") as file:
    arr = [str(random.randint(-5000, 5000)) for _ in range(50)]
    content = ", ".join(arr)
    file.write(content)

with open("source_data.txt", "r", encoding="utf-8") as file:
    datafile = file.readline().split(", ")

data = list(map(lambda num: int(num), datafile))

with open("result.txt", "w", encoding="utf-8") as file:
    file.write(
f"""Исходные данные: {datafile}
Количество элементов: {len(data)}
Минимальный элемент: {min(data)}
Количество положительных элементов в первой половине: {len([i for i in data[:int(len(data)/2)] if i >= 0])}
"""
    )
print(f"Исходные данные:\n{arr}")
print("Успешно")
