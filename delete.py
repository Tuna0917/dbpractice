import sqlite3

conn = sqlite3.connect("test.db",isolation_level=None)

c = conn.cursor()

# 방법 1
c.execute("DELETE FROM table1 WHERE id=?", (1,))
# 방법 2
c.execute("DELETE FROM table1 WHERE id=:id", {'id': 3})
# 방법 3
c.execute("DELETE FROM table1 WHERE id='%s'" % 5)
# 확인
for row in c.execute('SELECT * FROM table1'):
    print(row)