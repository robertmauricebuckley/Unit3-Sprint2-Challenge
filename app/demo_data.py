import sqlite3

# establish database

conn = sqlite3.connect("demo_data.sqlite3")

curs = conn.cursor()

new_table = """
            CREATE TABLE demo(
            s TEXT,
            x INT,
            y INT
            );
"""

curs.execute(new_table).fetchall()

data = """
        INSERT INTO demo(s, x, y)
        VALUES('g', 3, 9),
        ('v', 5,7),
        ('f', 8,7 );
"""
curs.execute(data).fetchall()

query = """
SELECT COUNT(*)
FROM demo
"""
result = curs.execute(query).fetchall()
print(f"There are {result} rows") 

query2 = """
SELECT COUNT(*)
FROM demo
WHERE x >= 5
	AND y >= 5;
"""
result2 = curs.execute(query2).fetchall()
print(f"There are {result2} rows where x and y are at least 5")

query3 = """
SELECT COUNT(DISTINCT y)
FROM demo
"""
result3 = curs.execute(query3).fetchall()
print(f"There are {result3} distinct values in y")


conn.commit()