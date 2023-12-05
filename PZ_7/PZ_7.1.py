'''
Дана непустая строка S. Вывести строку, содержащую символы строки S, между
которыми вставлено по одному пробелу.
'''


def solution(S: str):
    return " ".join(S)

test_str = 'qwertqwert'

print(f"Исходная строка:\n {test_str}\n Результат:\n {solution(test_str)}")
