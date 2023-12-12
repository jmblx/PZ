'''
Дана строка, содержащая полное имя файла. Выделить из этой строки название
первого каталога (без символов «\»). Если файл содержится в корневом каталоге, то
вывести символ «\».
'''


def solution(stroka: str) -> str:
    splited = stroka.split("\\")
    return splited[0] if len(splited) != 1 else "\\"

def test(src):
    print(f"Cтрока полного пути к файлу: {src}\n",
          "Результат:",
          solution(src)
    )

test(r"dsa\dsa1\sadqwwq\ewqda")
test(r"dsadqwe")
