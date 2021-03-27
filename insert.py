import sqlite3

# DB 생성 (오토 커밋)
conn = sqlite3.connect("test.db", isolation_level=None)

# 커서 획득
c = conn.cursor()

# 테이블 생성 (데이터 타입은 TEST, NUMERIC, INTEGER, REAL, BLOB 등)
c.execute("CREATE TABLE IF NOT EXISTS table1 \
    (id integer PRIMARY KEY, name text, birthday text)")

# 데이터 삽입 방법 1 c.execute(“INSERT INTO table1 VALUES(여기에 값)”
# c.execute("INSERT INTO table1 \
#     VALUES(1, 'LEE', '1987-00-00')")

# 데이터 삽입 방법 2
# c.execute("INSERT INTO table1(id, name, birthday) \
#     VALUES(?,?,?)", \
#     (2, 'KIM', '1990-00-00'))

# 데 삽 방 3
# test_tuple = (
#     (3, 'PARK', '1991-00-00'),
#     (4, 'CHOI', '1999-00-00'),
#     (5, 'JUNG', '1989-00-00')
# )
# c.executemany("INSERT INTO table1(id, name, birthday) VALUES(?,?,?)", test_tuple)