'''
11. Создайте базовый класс "Фигура" со свойствами "ширина" и "высота". От этого
класса унаследуйте классы "Прямоугольник" и "Квадрат".
Для класса "Квадрат" переопределите методы, связанные с вычислением площади и периметра.
'''


class Figure:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def calculate_square(self):
        print(f"Площадь фигуры: {self.width * self.height}\n")

    def calculate_perimeter(self):
        print((f"Периметр фигуры: {(self.width + self.height) * 2}\n"))


class Rectangle(Figure):
    ...


class Quadrant(Figure):
    @staticmethod
    def calculate_square_quadrant(side):
        print(f"Площадь квадрата: {side ** 2}\n")

    @staticmethod
    def calculate_perimeter_quadrant(side):
        print(f"Периметр квадрата: {side * 4}\n")

    # def calculate_square_quadrant(self):
    #     print(f"Площадь квадрата: {self.width ** 2}\n")
    #
    # def calculate_perimeter_quadrant(self):
    #     print(f"Периметр квадрата: {self.width * 4}\n")


bob = Rectangle(14, 25)
bob.calculate_square()
bob.calculate_perimeter()

side = 5
rostov = Quadrant(side, side)
rostov.calculate_square_quadrant(side)
rostov.calculate_perimeter_quadrant(side)
