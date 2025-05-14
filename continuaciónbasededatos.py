import sqlite3
con=sqlite3.connect("db1.db")
cur=con.cursor()
cur.execute("select * from users")
rows=cur.fetchall()
for row in rows:
    print(row)
con.close()
