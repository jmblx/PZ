"""
Из исходного текстового файла (Dostoevskiy.txt) выбрать блок информации за 1857 год
и поместить ее в новый текстовый файл
"""
import re


with open("Dostoevsky.txt", "r", encoding="utf-8") as f:
    src = f.read()

p = r"\b1857\s+.*\s*([\s\S]*?)\sВ \b(?!1857)\d{4}"
res = re.findall(p, src)

with open("res.txt", "w", encoding="utf-8") as f:
    f.write(res[0])
