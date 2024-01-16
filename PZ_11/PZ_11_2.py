'''
Из предложенного текстового файла (text18-11.txt) вывести на экран его содержимое,
количество знаков препинания. Сформировать новый файл, в который поместить строку
наименьшей длины.
'''
import string


with open("text18-11.txt", "r", encoding="utf-16") as f:
    texts = f.read()

print(texts)

counter = sum(list(1 for i in texts if i in set(string.punctuation)))

print(counter)
