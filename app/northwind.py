import os
import sqlite3

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "northwind_small.sqlite3")

conn = sqlite3.connect(DB_FILEPATH)
conn.row_factory = sqlite3.Row
print("CONNECTION:", conn)

curs = conn.cursor()
print("CURSOR", curs)

query = """
SELECT 
    ProductName,
    UnitPrice
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10;
"""

curs.execute(query)
print(curs.fetchall())

query2 = """
SELECT AVG (HireDate), AVG (BirthDate)
FROM Employee
"""
curs.execute(query2)
print(curs.fetchall())

# Part 3
# What are the ten most expensive items (per unit price) in the database and their suppliers?

query3 = """
SELECT p.SupplierId, p.ProductName, s.CompanyName, p.UnitPrice
FROM Product as p
JOIN Supplier as s
	ON p.SupplierId = s.id
ORDER BY UnitPrice DESC
LIMIT 10
"""
curs.execute(query3)
print(curs.fetchall())

# What is the largest category (by number of unique products in it)?
    #
query4 = """
SELECT COUNT(c.CategoryName), c.CategoryName
FROM Product as p
JOIN Category as c
	ON p.categoryId = c.id
GROUP BY CategoryName
ORDER BY COUNT(CategoryName) DESC
LIMIT 1
"""
curs.execute(query4)
print(curs.fetchall())

conn.commit()
