'''''
    Дано целое число, лежащее в диапозоне 1-999. 
    Вывести его строку- описание вида "четное двузначное число", "нечетное трехзначное число" и т.д.
'''''
from functions import get_num


num = get_num("число от 1 до 999")
while num < 1 or num > 999:
    num = get_num("число от 1 до 999")


def get_res(n: int) -> str:

    dig = len(str(n))

    if dig == 1:
        chetn = "нечетная" if n % 2 else "четная"
    else:
        chetn = "нечетное" if n % 2 else "четное"

    if dig == 1:
        return f"{chetn} цифра"
    elif dig == 2:
        dig = "двух"
    else:
        dig = "трёх"

    return f"{chetn} {dig}значное число "


print(get_res(num))
