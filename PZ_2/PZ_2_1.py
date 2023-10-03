# Дано двузначное число. Вывести вначале его левую цифру даннаого числа(десятки), а затем его правую цифру(единицы)
try:
    num = int(input('Введите двузначное число:\n'))
    if len(str(num)) != 2:
        raise ValueError
    first = num // 10
    second = num % 10
    print(f'Первая цифра в вашем числе - {first}\n')
    print(f'Вторая цифра в вашем числе - {second}')
except TypeError:
    print('Введите двузначное ЧИСЛО')
except ValueError:
    print('Введите ДВУЗНАЧНОЕ число')
