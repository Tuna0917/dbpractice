BEGIN TRANSACTION;
CREATE TABLE table1     (id integer PRIMARY KEY, name text, birthday text);
INSERT INTO "table1" VALUES(2,'LEE','1987-00-00');
INSERT INTO "table1" VALUES(4,'CHOI','1999-00-00');
COMMIT;
