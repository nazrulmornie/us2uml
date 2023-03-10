import mysql.connector

cnx = mysql.connector.connect(
    user="root", 
    password="", 
    host="localhost", 
    database="us2uml")

cursor = cnx.cursor()
table_name = "userszsss"
query = f"CREATE TABLE {table_name} (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255))"

cursor.execute("SHOW TABLES")
tables = cursor.fetchall()
exist = False

for table in tables:
    if table[0] == table_name:
        exist = True
        print (f"Table {table_name} exists!")

if not (exist):
    create_user = cnx.cursor()
    create_user.execute(query)
    print (f"Table {table_name} is created successfully")
else:
    print("Table exist!")

cnx.commit()
cursor.close()
cnx.close()