import sqlite3
con=sqlite3.connect("OurDataBase.db")
cur=con.cursor()
cur.execute("UPDATE Product SET quanity=quanity+(quanity*0.2)")
con.commit()

print("p_id \t p_name \t price \t quanity\n")
cursor=cur.execute("SELECT *FROM Product")

for row in cursor:
    print(f"{row[0]} \t {row[1]} \t {row[2]} \t{row[3]}\n")
con.close()