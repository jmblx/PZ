"""
Из исходного текстового файла (Dostoevskiy.txt) выбрать блок информации за 1857 год
и поместить ее в новый текстовый файл
"""
import re


with open("Dostoevsky.txt", "r", encoding="utf-8") as f:
    src = f.read()

p = r"\b1857\s+.*\s*([\s\S]*?)\b(?!1857)\d{4}\b"
print(re.findall(p, src))
print(src)
