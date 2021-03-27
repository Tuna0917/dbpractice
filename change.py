import sqlite3

# DB 생성 (오토 커밋)
conn = sqlite3.connect("test.db", isolation_level=None)

# 커서 획득
c = conn.cursor()


# 방법 1
c.execute("UPDATE table1 SET name=? WHERE id=?", ('NEW1', 1))
# 방법 2
c.execute("UPDATE table1 SET name=:name WHERE id=:id", {"name": 'NEW2', 'id': 3})
# 방법 3
c.execute("UPDATE table1 SET name='%s' WHERE id='%s'" % ('NEW3', 5))
# 확인
for row in c.execute('SELECT * FROM table1'):
    print(row)