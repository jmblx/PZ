'''
Дана строка, содержащая полное имя файла. Выделить из этой строки название
первого каталога (без символов «\»). Если файл содержится в корневом каталоге, то
вывести символ «\».
'''


def solution(stroka: str) -> str:
    splited = stroka.split("\")
    return splited[1] if len(splited) != 1 else "\"


print(solution("dsa\dsa\sadqwwq\ewqda"))
