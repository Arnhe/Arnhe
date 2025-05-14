import sqlite3
con=sqlite3.connect("db1.db")
try:
    con.execute('''create table users(id integer primary key,
    cedula text not null unique,     nombre text no null,
      apellido text not null,
         email text not null Unique);
    ''')
except sqlite3.OperationalError:
      print("la tabla ya exite")
users=[("32868516", "Arnheidis", "Arteaga", "arteagaarne@gmail.com")]
con.executemany("insert into users(cedula, nombre, apellido, email)values(?,?,?,?)",users)
con.commit()
con.close()
