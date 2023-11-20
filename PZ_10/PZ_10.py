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


def cant_buy_salt(**kwargs):
    res = []
    for shop in kwargs:
        shop_values = kwargs.get(shop)
        if "соль" not in shop_values:
            res.append(shop)
    print(res)


def can_buy_milk_cookie_sugar(**kwargs):
    res = []
    for shop in kwargs:
        shop_values = kwargs.get(shop)
        if "молоко" in shop_values and "печенье" in shop_values and "сыр" in shop_values:
            res.append(shop)
    print(res)

def can_buy_milk_meat(**kwargs):
    res = []
    for shop in kwargs:
        shop_values = kwargs.get(shop)
        if "молоко" in shop_values and "мясо" in shop_values:
            res.append(shop)
    print(res)

magnit = "молоко, соль, сахар, печенье, сыр".split(", ")
pyat = "мясо, молоко, сыр".split(", ")
perekrestok = "молоко, творог, сыр, сахар, печенье".split(", ")
lenta = "печенье, молоко, сыр".split(", ")

cant_buy_salt(magnit=magnit, pyat=pyat, perekrestok=perekrestok, lenta=lenta)

can_buy_milk_cookie_sugar(magnit=magnit, pyat=pyat, perekrestok=perekrestok, lenta=lenta)

can_buy_milk_meat(magnit=magnit, pyat=pyat, perekrestok=perekrestok, lenta=lenta)
