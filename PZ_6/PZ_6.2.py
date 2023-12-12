'''
Дано число K и список А размера N. Найти элемент списка, который наиболее
близок к числу К (то есть такой элемент Акб для которого величина |Ак - К|
является минимальной).
'''


def solution(K, A: list, N: int):
    diff = float("infinity")
    best = 0
    for i in A:
        cur = abs(i - K)
        if cur < diff:
            diff = cur
            best = i

    return best


A = [4, 5.6, 6.5, 4.25, 10, 15.4]
K = 7
print(f"Список: {A} k = {K}")
print(f"Результат: {solution(K, A, len(A))}")
