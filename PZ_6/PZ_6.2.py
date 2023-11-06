'''
Дано число R и список А размера N. Найти элемент списка, который наиболее
близок к числу К (то есть такой элемент Акб для которого величина |Ак - К|
является минимальной).
'''


def solution(K: int, A: list, N: int) -> int:
    diff = float("infinity")
    best = 0
    for i in A:
        cur = abs(i - K)
        if cur < diff:
            diff = cur
            best = i

    return best


A = [4, 5, 6, 10, 15]
print(solution(7, A, len(A)))
