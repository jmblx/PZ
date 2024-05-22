from typing import Pattern
import re

with open("ex_data.txt", "r", encoding="utf-8") as f:
    data = f.read()
    print(data, "data")


task1 = re.findall(r"\d+", data)
print(f"Все натуральные числа: {' | '.join(task1)}\n")

task2 = re.findall(r"[A-ZА-Я]+", data)
print(f"Все «слова», написанные капсом: {' | '.join(task2)}\n")

task3 = re.findall(r"[А-Я][0-9].", data)
print(f"Все слова, в которых есть русская буква, а за ней цифра: {' | '.join(task3)}\n")

# проврить
task4 = re.findall(r"\b[А-ЯA-ZЁ]{1}[а-яa-zё]+\b", data)
print(
    f"Все слова, начинающиеся с русской или латинской большой букв: {' | '.join(task4)}\n"
)

task5 = re.findall(r"\b[АЕЁИОУЫЭЮЯaeiou]\w+", data)
print(f"Все слова, которые начинаются на гласную: {' | '.join(task5)}\n")

task6 = re.findall(r"\b[а-яA-Z]+\d{2,}[а-яA-Z]+", data)
print(f"Все натуральные числа, не находящиеся на границе слова: {' | '.join(task6)}\n")

task7 = re.findall(r"\S*\*\S", data, flags=re.DOTALL)
print(
    f"Найдите строчки, в которых есть символ * (. — это точно не конец строки!): {' | '.join(task7)}\n"
)

task8 = re.findall(r"\(.*?\)+", data, flags=re.DOTALL)
print(
    f"Найдите строчки, в которых есть открывающая и когда-нибудь потом закрывающая скобки: {' | '.join(task8)}\n"
)

task9 = re.findall(r"<a href=\"#\d+\">.*</a>", data, flags=re.DOTALL)
print(
    f"Выделите одним махом весь кусок оглавления (в конце примера, вместе с тегами): \n{' | '.join(task9)}\n"
)

task10 = re.findall(r'<a href="#\d+">(.*?)</a>', data, flags=re.DOTALL)
print(
    f"Выделите одним махом только текстовую часть оглавления, без тегов: {' | '.join(task10)}\n"
)

task11 = re.findall(r"^\s*$", data, flags=re.MULTILINE)
print(f"Найдите пустые строчки: {' | '.join(task11)}\n")

task12 = re.findall(r'(<a href="#\d+">).*?(</a>)', data)
print("Все теги, не включая их содержимое: ")
[print(tags) for tags in map(lambda x: " ".join(x), task12)]
