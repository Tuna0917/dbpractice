import sqlite3

# DB 생성 (오토 커밋)
conn = sqlite3.connect("test.db", isolation_level=None)

with conn:
    with open('dump.sql', 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
        print('Completed.')