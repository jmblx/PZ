import sqlite3 as sq

with sq.connect("sql.db") as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS users")
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    sex INTEGER NOT NULL DEFAULT 1,
    old INTEGER,
    score INTEGER
    )""")

    cur.execute(
        """
        INSERT INTO users VALUES (1, 'Алексей', 1, 22, 1000)
        """
    )

    cur.executemany(
        """
        INSERT INTO users VALUES (?, ?, ?, ?, ?)
        """,
        [
            (2, "Миша", 0, 45, 1747),
            (3, "ЕГОР УБИЙЦА", 21, 40, 174774)
        ]
    )

    cur.execute("SELECT * FROM users WHERE score >= 1000 ORDER BY score DESC")
    result = cur.fetchall()
    print(result)

