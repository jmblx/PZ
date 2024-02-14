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

store_products = {
    "Магнит": {"молоко", "соль", "сахар", "печенье", "сыр"},
    "Пятерочка": {"мясо", "молоко", "сыр"},
    "Перекресток": {"молоко", "творог", "сыр", "сахар", "печенье"},
    "Лента": {"печенье", "молоко", "сыр"}
}

first_task = [store for store, products in store_products.items() if "соль" not in products]

second_task_products = {"молоко", "печенье", "сыр"}
second_task = [store for store, items in store_products.items() if items & second_task_products == second_task_products]

third_task = [store for store, products in store_products.items() if {"мясо", "молоко"}.issubset(products)]

print(f"1) {first_task}\n2){second_task}\n3){third_task}")
