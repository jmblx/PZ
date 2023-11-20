'''
Составить функцию, которая напечататает сорок любых символов
'''


def write_40_chars():
    stroka = ''
    for _ in range(1, 41):
        stroka += 'a'
    print(stroka)


# print(len())
print('40 символов "а":')
write_40_chars()
