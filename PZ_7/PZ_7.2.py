'''
Дана строка, содержащая полное имя файла. Выделить из этой строки название
первого каталога (без символов «\»). Если файл содержится в корневом каталоге, то
вывести символ «\».
'''


def solution(stroka: str) -> str:
    splited = stroka.split("\\")
    return splited[0] if len(splited) != 1 else "\\"


print(solution(r"dsa\dsa1\sadqwwq\ewqda"))
print(solution(r"dsadqwe"))
