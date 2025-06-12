from conexion import SQLiteConnection

db1 = SQLiteConnection

db = db1("db1.db")
db.connect()
    
    
sql = "select * from users"
params = None
db.execute_query(sql, params)

rows=db.fetch_all()

for row in rows:
    print(row)
    
    
header = ["Id", "Cedula"," Nombre", "Apellido", "Email"]

 #print header
print(f"{header[0]:<4} {header[1]:<8} {header[2]:<15} {header[3]:<15} {header[4]:<25}")
print("-" * 72)

 #print rows
for row in rows:
    print(f"{row[0]:<4} {row[1]:<8} {row[2]:<15} {row[3]:<15} {row[4]:<25}")
db.close()
 
 
 
 
    