"""
Дано целое число N (> 0). Найти произведние 1.1 * 1.2 * 1.3 * (N сомножителей)
"""
import functions


N = functions.get_num("целое число N (> 0)")
while N < 0:
    N = functions.get_num("целое число N (> 0)")

res = 0

if N == 1:
    res = 1.1
else:
    res = 1
    for i in range(1, N+1):
        res *= 1 + (0.1 * i)

print(f"произведение 1.1 * 1.2 * 1.3 * ({N} сомножителей) = {res}")
