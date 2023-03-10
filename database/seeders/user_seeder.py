import mysql.connector
import random

# Establish a connection to the MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="us2uml"
)

# Create a cursor object to interact with the database
mycursor = mydb.cursor()

# Create a table in the database
# mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255), age INT)")

# Generate and insert data into the table
for i in range(10):
    name = "Customer " + str(i)
    email = str(random.randint(1, 100)) + "@us2uml.org"
    sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
    val = (name, email)
    mycursor.execute(sql, val)

# Commit the changes to the database
mydb.commit()

# Close the cursor and database connection
mycursor.close()
mydb.close()
