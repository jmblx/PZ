'''
Описать функцию SortInc3(А, В, С), меняющую содержимое переменных А, В, С
таким образом, чтобы их значения оказались упорядоченными по возрастанию (А,
В, С - вещественные параметры, являющиеся одновременно входными и
выходными). С помощью этой функции упорядочить по возрастанию два данных
набора из трех чисел: (Ai, Bi, Ci) и (A2, В2, C2).
'''


def SortInc3(A: float, B: float, C: float) -> float:
    arr = [A, B, C]
    sorted_arr = []  # Создание отсортированного массива
    num = float('infinity')
    for i in reversed(range(3)):  # Наполнение отсортированного массива
        for y in range(i+1):
            if arr[y] < num:
                index = y
                num = arr[y]
        sorted_arr.append(num)
        arr.pop(index)
        num = float('infinity')
    return sorted_arr[0], sorted_arr[1], sorted_arr[2]
    #  Возвращение элементов отсортированного массива


def test_func(A: float, B: float, C: float) -> None:
    print(f"до:\n{A}, {B}, {C}")
    A, B, C = SortInc3(A, B, C)
    print(f"после:\n{A}, {B}, {C}\n")


# Тесты

Ai, Bi, Ci = 4.1, 3.2, 5.6
A2, B2, C2 = 9.4, 9.4, 2.3
test_func(Ai, Bi, Ci)
test_func(A2, B2, C2)
