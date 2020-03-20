import os
import sqlite3

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "northwind_small.sqlite3")

conn = sqlite3.connect(DB_FILEPATH)
conn.row_factory = sqlite3.Row
print("CONNECTION:", conn)

curs = conn.cursor()
print("CURSOR", curs)

# What are the ten most expensive items (per unit price) in the database?
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

# Côte de Blaye	263.5
# Thüringer Rostbratwurst	123.79
# Mishi Kobe Niku	97
# "Sir Rodney's Marmalade"	81
# Carnarvon Tigers	62.5
# Raclette Courdavault	55
# Manjimup Dried Apples	53
# Tarte au sucre	49.3
# Ipoh Coffee	46
# Rössle Sauerkraut	45.6



#What is the average age of an employee at the time of their hiring?
query2 = """
SELECT AVG (HireDate), AVG (BirthDate)
FROM Employee
"""
curs.execute(query2)
print(curs.fetchall())

# 2025.0	1987.77777777778
# 37.3



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

# 18	Côte de Blaye	Aux joyeux ecclésiastiques	263.5
# 12	Thüringer Rostbratwurst	Plutzer Lebensmittelgroßmärkte AG	123.79
# 4	Mishi Kobe Niku	Tokyo Traders	97
# 8	"Sir Rodney's Marmalade"	Specialty Biscuits, Ltd.	81
# 7	Carnarvon Tigers	Pavlova, Ltd.	62.5
# 28	Raclette Courdavault	Gai pâturage	55
# 24	Manjimup Dried Apples	"G'day, Mate"	53
# 29	Tarte au sucre	"Forêts d'érables"	49.3
# 20	Ipoh Coffee	Leka Trading	46
# 12	Rössle Sauerkraut	Plutzer Lebensmittelgroßmärkte AG	45.6



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

# 13	Confections

conn.commit()
