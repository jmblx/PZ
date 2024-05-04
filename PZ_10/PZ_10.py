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

magnit = {"magnit", "молоко", "соль", "сахар", "печенье", "сыр"}
pyat = {"pyat", "мясо", "молоко", "сыр"}
perek = {"perek", "молоко", "творог", "сыр", "сахар", "печенье"}
lenta = {"lenta", "печенье", "молоко", "сыр"}
store_products = {
    magnit, pyat, perek, lenta
}

first_task = {store for store, products in store_products if "соль" not in products}

second_task_products = {"молоко", "печенье", "сыр"}
second_task = {items[0] for items in store_products if items & second_task_products == second_task_products}

third_task = {products[0] for products in store_products if {"мясо", "молоко"}.issubset(products)}

print(f"1) {first_task}\n2){second_task}\n3){third_task}")
