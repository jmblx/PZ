"""
2. В матрице найти сумму элементов второй половины матрицы.
"""
import random

x, y = random.randint(1, 6), random.randint(1, 6)

arr = [[random.randint(-20, 20) for num in range(x)] for n in range(y)]

res_arr = []
if y == 1 and x != 1:
    for num in arr[y // 2][x // 2 + 1:]:
        res_arr.append(num)
elif x == 1 and y == 1:
    res = arr[0][0]
elif y % 2:
    for i in range(y // 2 + 1, y):
        for num in arr[i]:
            res_arr.append(num)
else:
    for i in range(y // 2, y):
        for num in arr[i]:
            res_arr.append(num)

print("Матрица:")
list(map(lambda s: print(s), arr))
print(f"\nМассив с элементами второй половиной матрицы:\n{res_arr}")
print(f"\nСумма элементов второй половины матрицы:\n{sum(res_arr)}")

