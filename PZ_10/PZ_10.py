"""
Вариант 11.
В магазинах имеются следующие товары.
Магнит - молоко, соль, сахар, печенье, сыр.
Пятерочка - мясо, молоко, сыр.
Перекресток - молоко, творог, сыр, сахар, печенье.
Лента - печенье, молоко, сыр.
Определить:
1. в каких магазинах нельзя приобрести соль.
2. в каких магазинах можно приобрести одновременно молоко, печенье и сыр.
3. в каких магазинах можно приобрести мясо и молоко.
"""
def check_func(func):
    magnit = {"молоко", "соль", "сахар", "печенье", "сыр"}
    pyat = {"мясо", "молоко", "сыр"}
    perek = {"молоко", "творог", "сыр", "сахар", "печенье"}
    lenta = {"печенье", "молоко", "сыр"}
    func(magnit, "магнит")
    func(pyat, "пятёрочка")
    func(perek, "перекрёсток")
    func(lenta, "лента")


first_res, second_res, third_res = set(), set(), set()

def check_salt(store: set, name: str):
    global first_res
    salt = {"соль"}
    if salt & store == set():
        first_res.add(name)

def check_milk_cookies_cheese(store: set, name: str):
    global second_res
    products = {"молоко", "печенье", "сыр"}
    if products - store == set():
        second_res.add(name)

def check_meat_milk(store: set, name: str):
    global third_res
    products = {"мясо", "молоко"}
    if len(store) == len(store | products):
        third_res.add(name)

check_func(check_salt)
check_func(check_milk_cookies_cheese)
check_func(check_meat_milk)

print(f"1)Нельзя приобрести соль в: {first_res}\n2)Можно приобрести одновременно молоко, печенье и сыр в:{second_res}\n3)Можно приобрести мясо и молоко: {third_res}")
