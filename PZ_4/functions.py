def get_num(n: str) -> int:
    num = input(f"Введите {n}\n")
    while type(num) is not int:
        try:
            num = int(num)
            return num
        except ValueError:
            print("Неправильно ввели!")
            num = input(f"Введите {n}\n")
