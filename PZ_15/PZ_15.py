'''
В-11
Приложение КОММАНДИРОВОЧНЫЕ РАСХОДЫ для автоматизированного
финансового контроля на предприятии. БД должна содержать таблицу Статьи расходов,
имеющую следующую структуру записи: № приказа, Фамилия, Место командировки,
Оплата, Аванс, Вид расходов, Сумма расходов,
'''
import sqlite3


def setup_database():
    conn = sqlite3.connect(':memory:')
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS expenses")
    cur.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        order_id INTEGER PRIMARY KEY AUTOINCREMENT,
        lastname TEXT,
        place TEXT,
        payment REAL,
        prepayment REAL,
        payment_type TEXT,
        payment_amount REAL
    )""")
    initial_data = [
        (1, "Светличный", "пер. Халтуринский 28/40", 174.7, 20.31, "Безналичный расчет", 321.32),
        (2, "Жилин", "пер. Халтуринский 108/20", 121.3, 29.31, "Безналичный расчет", 228.02),
        (3, "Кузнецов", "ул. Ленина 15/2", 189.5, 15.75, "Наличные", 149.63),
        (4, "Иванова", "пер. Советский 7/14", 98.2, 10.5, "Безналичный расчет", 85.12),
        (5, "Петров", "ул. Гагарина 42/5", 215.8, 18.9, "Наличные", 162.36),
        (6, "Сидоров", "пер. Пушкина 10/5", 150.6, 12.7, "Выписка чека", 125.25),
        (7, "Светличный", "ул. Ленина 77/3", 198.4, 14.8, "Оплата ценными бумагами", 210.75),
        (8, "Никитин", "пер. Гагарина 15/3", 112.9, 9.4, "Электронные деньги", 97.68),
        (9, "Смирнова", "ул. Ленина 30/1", 176.2, 17.3, "Безналичный расчет", 192.51),
        (10, "Федоров", "пер. Советский 5/8", 132.7, 11.9, "Наличные", 105.63),
        (11, "Козлов", "ул. Гагарина 20/15", 189.8, 16.5, "Выписка чека", 158.42),
        (12, "Павлов", "пер. Пушкина 12/7", 145.3, 13.2, "Оплата ценными бумагами", 174.98),
        (13, "Васильев", "ул. Ленина 55/4", 201.6, 18.7, "Безналичный расчет", 237.82),
        (14, "Светличный", "пер. Гагарина 10/2", 118.4, 10.8, "Наличные", 92.73),
        (15, "Тимофеев", "ул. Пушкина 33/8", 195.1, 15.6, "Электронные деньги", 207.84)
    ]
    cur.executemany("INSERT INTO expenses VALUES (?, ?, ?, ?, ?, ?, ?)", initial_data)
    conn.commit()
    return conn


def print_database(conn, event=''):
    cur = conn.cursor()
    cur.execute("SELECT * FROM expenses")
    rows = cur.fetchall()
    print(f"Состояние базы данных после {event}:")
    for row in rows:
        print(row)


conn = setup_database()
print_database(conn)


def create_expense(conn, expense_data):
    cur = conn.cursor()
    cur.execute("INSERT INTO expenses VALUES (?, ?, ?, ?, ?, ?, ?)", expense_data)
    conn.commit()

# Read
def read_expenses_by_lastname(conn, lastname):
    cur = conn.cursor()
    cur.execute("SELECT * FROM expenses WHERE lastname = ?", (lastname,))
    return cur.fetchall()


def delete_expense_by_payment_type(conn, payment_type):
    cur = conn.cursor()
    cur.execute("DELETE FROM expenses WHERE payment_type = ?", (payment_type,))
    conn.commit()


new_expenses = [
    (None, "Игнатов", "ул. Советская 1/1", 120.0, 10.0, "Наличные", 110.0),
    (None, "Белов", "пер. Гагарина 20/4", 135.5, 15.5, "Безналичный расчет", 120.0),
    (None, "Орлов", "ул. Ленина 12/7", 145.0, 20.0, "Выписка чека", 125.0)
]
for expense in new_expenses:
    create_expense(conn, expense)

print_database(conn, "добавления 3-х записей")
svetlichny_expenses = read_expenses_by_lastname(conn, "Светличный")
print("Записи  Светличного:", svetlichny_expenses)

delete_expense_by_payment_type(conn, "Выписка чека")
print_database(conn, "delete_expense_by_payment_type(conn, 'Выписка чека')")

def read_expenses_by_lastname_and_place(conn, lastname, place):
    cur = conn.cursor()
    cur.execute("SELECT * FROM expenses WHERE lastname = ? AND place LIKE ? ORDER BY payment DESC", (lastname, f'%{place}%'))
    return cur.fetchall()

def aggregate_payments_by_type(conn):
    cur = conn.cursor()
    cur.execute("""
        SELECT payment_type, SUM(payment) as total_payment, SUM(prepayment) as total_prepayment
        FROM expenses
        GROUP BY payment_type
        ORDER BY total_payment DESC
    """)
    return cur.fetchall()


svetlichny_lenina_expenses = read_expenses_by_lastname_and_place(conn, "Светличный", "Ленина")
print("Записи для Светличный по адресам на улице Ленина:", svetlichny_lenina_expenses)

payment_summary = aggregate_payments_by_type(conn)
print("Суммарные платежи и предоплаты по типам платежей:")
for summary in payment_summary:
    print(summary)


def find_expenses_with_conditions(conn):
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM expenses
        WHERE prepayment < 15 AND payment > 150
    """)
    return cur.fetchall()


conditioned_expenses = find_expenses_with_conditions(conn)
print("Записи с предоплатой меньше 15 и платежом более 150:")
for expense in conditioned_expenses:
    print(expense)


def update_payment_type_for_high_payments(conn):
    cur = conn.cursor()
    cur.execute("""
        UPDATE expenses
        SET payment_type = 'Специальные условия'
        WHERE payment > 150 AND prepayment < 20
    """)
    conn.commit()
    print_database(conn)


def increment_prepayment_for_surnames(conn):
    cur = conn.cursor()
    cur.execute("""
        UPDATE expenses
        SET prepayment = prepayment + 10
        WHERE lastname LIKE 'С%'
    """)
    conn.commit()
    print_database(conn, "increment_prepayment_for_surnames")


def discount_cash_payments(conn):
    cur = conn.cursor()
    cur.execute("""
        UPDATE expenses
        SET payment = payment * 0.85
        WHERE payment_type = 'Наличные' AND payment > 100
    """)
    conn.commit()
    print_database(conn, "discount_cash_payments")


def delete_low_payments_and_prepayments(conn):
    cur = conn.cursor()
    cur.execute("""
        DELETE FROM expenses
        WHERE payment < 120 AND prepayment < 15
    """)
    conn.commit()
    print_database(conn, "delete_low_payments_and_prepayments")


def delete_specific_lastname_cash(conn):
    cur = conn.cursor()
    cur.execute("""
        DELETE FROM expenses
        WHERE lastname LIKE '%ов' AND payment_type = 'Наличные'
    """)
    conn.commit()
    print_database(conn, "delete_specific_lastname_cash")


def delete_above_average_noncash_payments(conn):
    cur = conn.cursor()
    cur.execute("""
        DELETE FROM expenses
        WHERE payment_type = 'Безналичный расчет' AND payment > (SELECT AVG(payment) FROM expenses WHERE payment_type = 'Безналичный расчет')
    """)
    conn.commit()
    print_database(conn, "delete_above_average_noncash_payments")


update_payment_type_for_high_payments(conn)
increment_prepayment_for_surnames(conn)
discount_cash_payments(conn)

delete_low_payments_and_prepayments(conn)
delete_specific_lastname_cash(conn)

delete_above_average_noncash_payments(conn)
