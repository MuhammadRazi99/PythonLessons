import sqlite3
con=sqlite3.connect("OurDataBase.db")
cur=con.cursor()

cur.execute("INSERT INTO Product(p_name,price,quanity) VALUES('AutoCad',200,20)")
cur.execute("INSERT INTO Product(p_name,price,quanity) VALUES('Quick hill',330,12)")
cur.execute("INSERT INTO Product(p_name,price,quanity) VALUES('Keyboard',250,25)")
cur.execute("INSERT INTO Product(p_name,price,quanity) VALUES('Mouse',150,34)")

print("Data inserted !")
con.commit()
con.close()