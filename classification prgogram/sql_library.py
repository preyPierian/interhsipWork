
import mysql.connector

class sql_connector :
    def __init__(self,host_name,username,password,database_name):
        mydb = mysql.connector.connect(
            host =host_name,
            user =username,
            passwd =password, 
        )
        self.db = mydb
        self.cursor = self.db.cursor()
        self.database = database_name
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS "+database_name+";")
        self.cursor.execute("USE " +database_name)

    def sql_create_table(self,table_name,columns) :
        self.cursor.execute("DROP TABLE IF EXISTS "+ table_name +";")
        self.cursor.execute("CREATE TABLE "+ table_name +columns)
        

    def sql_add_subwords(self,array,table_name):
        for x in array :
            self.cursor.execute(("INSERT INTO "+  table_name +" (word,start_index,end_index) VALUES (%s,%s,%s) "),(x.word,x.start_index,x.end_index))
        self.db.commit()
    
    def sql_search_query(self, columns, table_name, query) :
        self.cursor.execute (("SELECT "+columns+" FROM "+table_name+" WHERE "+query+";") )
        return (self.cursor.fetchall())

    def sql_fields_query(self, columns, table_name) :
        self.cursor.execute (("SELECT "+columns+" FROM "+table_name+ ";") )
        return (self.cursor.fetchall())