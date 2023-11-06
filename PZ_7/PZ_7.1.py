'''
Дана непустая строка S. Вывести строку, содержащую символы строки S, между
которыми вставлено по одному пробелу.
'''


def solution(S: str):
    return "".join([f"{s} " for s in S])


print(solution('qwertqwert'))
