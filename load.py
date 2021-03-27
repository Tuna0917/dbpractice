import sqlite3

# DB 생성 (오토 커밋)
conn = sqlite3.connect("test.db", isolation_level=None)

# 커서 획득
c = conn.cursor()


c.execute("SELECT * FROM table1")
print(c.fetchone())
print(c.fetchone())
print(c.fetchall())

# 방법 1
c.execute("SELECT * FROM table1")
for row in c.fetchall():
    print(row)
# 방법 2
for row in c.execute("SELECT * FROM table1 ORDER BY birthday ASC"):
    print(row)

conn.close()