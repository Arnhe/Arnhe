import sqlite3

class SQLiteConnection:
    
    def __init__(self,dbname):
        print(dbname)
        self.db_name=dbname
        #self.connection=None
        #self.cursor=None
        print(f"BD {self.db_name}")
        
    def connect(self):
        try:
            self.connection=sqlite3.connect(self.db_name)
            self.cursor=self.connection.cursor()
            print(f"Conectado a la BD{self.db_name}")
        
        except sqlite3.error as e:
            print(f"Error al conectar a BD:{e}")

    def execute_query(self,query,params):
        try:
            if self.cursor is None:
                raise Exception("conexion a BD no es establecida")
            if params is not None:
                self.cursor.execute(query,params)
            else:
                self.cursor.execute(query)
            self.connection.commit()
            print("Consulta ejecutada")
        
        except sqlite3.Error as e:
            print("Error al ejecutar la consulta")
        
    def fetch_all(self):
        try:
            if self.cursor is None:raise Exception("conexion a la BD no establecida")
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print("Error al obtener datos")
            return None
        
    def close(self):
        if self.connection:
            self.connection.close()
            print("conexion cerrada")
        
