import sqlite3

conn = sqlite3.connect("test.db",isolation_level=None)

c = conn.cursor()
# 방법 1
param1 = (1,)
c.execute('SELECT * FROM table1 WHERE id=?', param1)
print('param1', c.fetchone())
print('param1', c.fetchall())
# 방법 2
param2 = 1
c.execute("SELECT * FROM table1 WHERE id='%s'" % param2)  # %s %d %f
print('param2', c.fetchone())
print('param2', c.fetchall())
# 방법 3
c.execute("SELECT * FROM table1 WHERE id=:Id", {"Id": 1})
print('param3', c.fetchone())
print('param3', c.fetchall())
# 방법 4
param4 = (1, 4)
c.execute('SELECT * FROM table1 WHERE id IN(?,?)', param4)
print('param4', c.fetchall())
# 방법 5
c.execute("SELECT * FROM table1 WHERE id In('%d','%d')" % (1, 4))
print('param5', c.fetchall())
# 방법 6
c.execute("SELECT * FROM table1 WHERE id=:id1 OR id=:id2", {"id1": 1, "id2": 4})
print('param6', c.fetchall())