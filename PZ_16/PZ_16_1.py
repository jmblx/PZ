"""
11. Создайте класс "Товар" с атрибутами "название", "цена" и "количество". Напишите
метод, который выводит информацию о товаре в формате "Название: название,
Цена: цена, Количество: кол-во".
"""

class Product:
    def __init__(self, name: str, cost: float, quantity: int):
        self.name = name
        self.cost = cost
        self.quantity = quantity

    def get_product(self):
        print(
f"""
Название: {self.name},
Цена: {self.cost},
Количество: {self.quantity}
"""
        )

if __name__ == "__main__":
    arbuz = Product("арбуз", 128.31, 12)
    arbuz.get_product()
