# importing the module
import mysql.connector
from mysql.connector import Error
class Db_connection:
    
    def __init__(self,host="localhost",user="root",passwd="") -> None:
        db= mysql.connector.connect(host=host,user=user,passwd=passwd)
        mycursor=db.cursor()
        mycursor.execute("use temperaturepy")
        mycursor.execute("show tables")
        self.connection = db
        
        # for data in mycursor:
        #     print(data)
        db.commit()
        mycursor.close()
        
    def execute_query(self, query):
        try: 
            cursor = self.connection.cursor()
            try:
                cursor.execute(query)
                self.connection.commit()
                print("Query successful")
            except Error as err:
                print(f"Error: '{err}'")
            finally:
                cursor.close()
        except Error as e:
            print(e)
       
    
    def executemany_query(self, query, val):
        print(val)
        try: 
            cursor = self.connection.cursor(buffered=True)
        except Error as e:
            print(e)
        try:
            cursor.executemany(query,val)
            self.connection.commit()
            # print("Query successful")
        except Error as err:
            print(f"Error: '{err}'")
        finally:
            cursor.close()
            
    def insert_record(self, temperature):
        query = f'INSERT INTO `record`(`temperature`) VALUES ({temperature})'
        self.execute_query(query)
        # print("inserted")
        
    def insert_many_records(self, temperatures = []):
        query = f'INSERT INTO `record`(`temperature`) VALUES (%s)'
        # print(temperatures)
        self.executemany_query(query,temperatures)
        
        
# db= Db_connection()
# db.insert_many_records(
#     temperatures=[(12,),(34,)]
# )
        
        
            

        
