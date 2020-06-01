#dbinit.py
import sqlite3

def init(conn):
    try:
        cursor = conn.cursor()
        sql = """
CREATE TABLE CoffeeProduct
(
    pnum      INT      PRIMARY KEY,
    pname     TEXT    NOT NULL,
    pprice     INT      NOT NULL
);
"""
        cursor.execute(sql)
        sql = """
CREATE TABLE SnackProduct
(
    pnum      INT      PRIMARY KEY,
    pname     TEXT    NOT NULL,
    pprice     INT      NOT NULL
);
"""
        cursor.execute(sql)
        sql = """
INSERT INTO CoffeeProduct(pnum, pname, pprice) VALUES(1, '밀크커피', 300);
INSERT INTO CoffeeProduct(pnum, pname, pprice) VALUES(2, '설탕커피', 300);
INSERT INTO CoffeeProduct(pnum, pname, pprice) VALUES(3, '프림커피', 400);
INSERT INTO CoffeeProduct(pnum, pname, pprice) VALUES(4, '블랙커피', 200);
INSERT INTO CoffeeProduct(pnum, pname, pprice) VALUES(5, '원두커피', 500);
"""
        cursor.executescript(sql)
        sql = """
INSERT INTO SnackProduct(pnum, pname, pprice) VALUES(1, '오감자', 400);
INSERT INTO SnackProduct(pnum, pname, pprice) VALUES(2, '오징어땅콩', 500);
INSERT INTO SnackProduct(pnum, pname, pprice) VALUES(3, '빼빼로', 600);
INSERT INTO SnackProduct(pnum, pname, pprice) VALUES(4, '칸쵸', 500);
INSERT INTO SnackProduct(pnum, pname, pprice) VALUES(5, '맛동산', 600);
"""
        cursor.executescript(sql)
    except Exception as ex:
        print('DB Init Exception = ', ex.args[0])
        conn.rollback()
    else : 
        print('DB Init Success')
        conn.commit()
    finally:
        cursor.close()