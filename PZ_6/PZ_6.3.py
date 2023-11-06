'''
Дан список размера N. Осуществить сдвиг элементов списка влево на одну позицию
((при эnom An перейдет в An-1, An-1 - в An-2, …, А2 - в А1, а исходное phaxtybt
первого элемента будет потеряно). Последний элемент полученного списка
положить равным 0.
'''


def solution(A: list, N: int) -> list:
    # for i in range(1, N):
    #     A[i-1] = A[i]
    # A[-1] = 0
    # return A
    A = [A[i+1] for i in range(N-1)]
    A[-1] = 0
    return A


arr = [1, 2, 3, 4, 5, 6]
print(solution(arr, len(arr)))
