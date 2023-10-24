"""
Дано целое число N (> 1). Найти наибольшее число K, при котором выполняется неравенство 3^k>N.
"""
import PZ_3.functions


N = PZ_3.functions.get_num("целое число N (> 1)")
while N < 1:
    N = PZ_3.functions.get_num("целое число N (> 1)")

res, k = 0, 0

while res <= N:
    k += 1
    res = 3**k

print(k)
