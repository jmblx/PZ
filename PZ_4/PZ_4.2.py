"""
Дано целое число N (> 1). Найти наименьшее число K, при котором выполняется неравенство: 3^k>N.
"""
import functions


N = functions.get_num("целое число N (> 1)")
while N < 1:
    N = functions.get_num("целое число N (> 1)")

res, k = 0, 0

while res <= N:
    k += 1
    res = 3**k

print(f"Наименьшее число K при котором выполняется неравенство 3^k>N = {k}")
