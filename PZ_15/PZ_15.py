'''
Приложение КОММАНДИРОВОЧНЫЕ РАСХОДЫ для автоматизированного
финансового контроля на предприятии. БД должна содержать таблицу Статьи расходов,
имеющую следующую структуру записи: № приказа, Фамилия, Место командировки,
Оплата, Аванс, Вид расходов, Сумма расходов,
'''

import sqlite3 as sq

with sq.connect("sql.db") as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS expenses")
    cur.execute(
'''
CREATE TABLE IF NOT EXISTS expenses (
order_id INTEGER PRIMARY KEY AUTOINCREMENT,
lastname TEXT,
place TEXT,
payment REAL,
prepayment REAL,
payment_type TEXT,
payment_amount REAL
)
'''
)

    cur.executemany(
        """
        INSERT INTO expenses VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        [
            (1, "Светличный", "пер. Халтуринский 28/40", 174.7, 20.31, "Безнал.", 321.32),
        ]
    )

    cur.execute(
        """
        SELECT * FROM expenses WHERE lastname = 'Светличный'
        """
    )
    res = cur.fetchall()
    print(f"Все оплаты, Светличного:\n{res}")
