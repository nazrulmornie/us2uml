import mysql.connector
import create_db

cnx = mysql.connector.connect(user="root", password="", host="localhost")

cursor = cnx.cursor()

# cursor.execute("CREATE DATABASE us2uml")

cursor.execute("SHOW DATABASES")
db_name = "us2uml"
database_exists = False

for database in cursor:
    if database == db_name:
        database_exists = True
        
if database_exists:
    print("The database exists")
else:
    create_db.create_db()
    
cursor.close()
cnx.close()