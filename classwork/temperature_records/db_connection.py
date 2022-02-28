# importing the module
import mysql.connector
from mysql.connector import Error
class Db_connection:
    
    def __init__(self,host="localhost",user="root",passwd="") -> None:
        db= mysql.connector.connect(host=host,user=user,passwd=passwd)
        mycursor=db.cursor()
        mycursor.execute("use temperaturepy")
        self.connection = db        
        
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
        try: 
            cursor = self.connection.cursor(buffered=True)
        except Error as e:
            print(e)
        try:
            cursor.executemany(query,val)
            self.connection.commit()
        except Error as err:
            print(f"Error: '{err}'")
        finally:
            cursor.close()
            
    def insert_record(self, temperature):
        query = f'INSERT INTO `record`(`temperature`) VALUES ({temperature})'
        self.execute_query(query)
        
    def insert_many_records(self, temperatures = []):
        query = f'INSERT INTO `record`(`temperature`) VALUES (%s)'
        self.executemany_query(query,temperatures)
        
        
 
        
            

        
