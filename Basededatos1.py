import sqlite3
con=sqlite3.connect("db1.db")
try:
    con.execute('''
        create table users(
        id integer primary ke,
        cedula text not null unique,
        nombre text (not null,
        apellido text not null,
        email tex not null unique);
    ''')
except sqlite3.OperationalError:
    print("la tabla ya existe")
             
users=[
    ("32868516","Arnheidis","Arteaga","arteagaarne@gmail.com"),]
con.executemany("insert into users (cedula,nombre,apellido,email) values(?,?,?,?)",users)
con.commit()
con.close()
  
  
  
  
  