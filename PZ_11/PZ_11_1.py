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


with open("source_data.txt", "w", encoding="utf-8") as file:
    file.write("1, 4, -2, 9, 18, -42, 34")

with open("source_data.txt", "r", encoding="utf-8") as file:
    datafile = file.readline().split(", ")

data = list(map(lambda num: int(num), datafile))

with open("result.txt", "w", encoding="utf-8") as file:
    file.write(
        f"""
        Исходные данные: {datafile}
        Количество элементов: {len(data)}
        Минимальный элемент: {min(data)}
        Количество положительных элементов в первой половине: {len([i for i in data[:int(len(data)/2)] if i >= 0])}
        """
    )
