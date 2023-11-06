'''
Составить функцию, которая напечататет сорок любых символов
'''


def write_40_chars():
    stroka = ''
    for _ in range(1, 41):
        stroka += 'a'
    print(stroka)


# print(len())
write_40_chars()
