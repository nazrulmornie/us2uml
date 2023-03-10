import mysql.connector

def create_db():
    cnx = mysql.connector.connect(
        user="root", 
        password="", 
        host="localhost")

    cursor = cnx.cursor()
    
    db_name = "us2uml"
    
    query = f"CREATE DATABASE {db_name}"
    cursor.execute(query)
    
    return print("Database created!")
