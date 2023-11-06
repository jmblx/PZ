'''''
    Дано целое число, лежащее в диапозоне 1-999. 
    Вывести его строку- описание вида "четное двузначное число",
    "нечетное трехзначное число" и т.д.
'''''
import functions

# Ввод числа в диапозоне 1-999
num = functions.get_num("число от 1 до 999")
while num < 1 or num > 999:
    num = functions.get_num("число от 1 до 999")


def get_res(n: int) -> str:

    dig = len(str(n))  # считаем количество цифр в числе

    if dig == 1:  # если дана цифра, то в результате скажем цифра
        chetn = "нечетная" if n % 2 else "четная"
        return f"{chetn} цифра"
    else:  # иначе число
        chetn = "нечетное" if n % 2 else "четное"

    if dig == 2:
        dig = "двух"
    else:
        dig = "трёх"

    return f"{chetn} {dig}значное число "


print(get_res(num))
