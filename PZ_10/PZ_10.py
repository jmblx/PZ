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


def check_items(shop_values, items):
    return all(item in shop_values for item in items)

def cant_buy(items, **kwargs):
    res = [shop for shop, shop_values in kwargs.items() if not check_items(shop_values, items)]
    print(res)

def can_buy(items, **kwargs):
    res = [shop for shop, shop_values in kwargs.items() if check_items(shop_values, items)]
    print(res)

magnit = "молоко, соль, сахар, печенье, сыр".split(", ")
pyat = "мясо, молоко, сыр".split(", ")
perekrestok = "молоко, творог, сыр, сахар, печенье".split(", ")
lenta = "печенье, молоко, сыр".split(", ")

cant_buy(
    ["соль"], magnit=magnit, pyat=pyat,
    perekrestok=perekrestok, lenta=lenta
)

can_buy(["молоко", "печенье", "сыр"], magnit=magnit, pyat=pyat, perekrestok=perekrestok, lenta=lenta)

can_buy(["молоко", "мясо"], magnit=magnit, pyat=pyat, perekrestok=perekrestok, lenta=lenta)
