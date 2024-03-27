'''
Приложение КОММАНДИРОВОЧНЫЕ РАСХОДЫ для автоматизированного
финансового контроля на предприятии. БД должна содержать таблицу Статьи расходов,
имеющую следующую структуру записи: № приказа, Фамилия, Место командировки,
Оплата, Аванс, Вид расходов, Сумма расходов,
'''

import sqlite3 as sq

with sq.connect("sql.db") as con:
    cur = con.cursor()
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



