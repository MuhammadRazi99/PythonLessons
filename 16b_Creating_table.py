import sqlite3
con=sqlite3.connect('OurDataBase.db')
cur=con.cursor()
cur.execute('CREATE TABLE Product(p_id INTEGER PRIMARY KEY AUTOINCREMENT,p_name TEXT NOT NULL,price REAL,quanity INTEGER)')
print("Table created in Data Base")
con.close()