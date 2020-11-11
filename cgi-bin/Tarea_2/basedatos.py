import mysql.connector

class DB:

    def __init__(self,user,password):
        self.db= mysql.connector.connect(
            host="anakena.dcc.uchile.cl",
            user=user,
            password=password,
            database="cc500270_db"
        )

        self.cursor=self.db.cursor
        
    def close(self):
        self.cursor.close()
        self.db.close()