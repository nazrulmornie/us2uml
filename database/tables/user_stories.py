import mysql.connector
import string


my_db = mysql.connector.connect(
    host="localhost",
    database="us2uml",
    user="root",
    password=""
)

my_cursor = my_db.cursor()
table_name = "user stories"
query = f"CREATE TABLE {table_name} (id INT AUTO_INCREMENT PRIMARY KEY, user_id INT, story TEXT, project_id VARCHAR(255), created_at DATETIME DEFAULT NOW(), updated_at DATETIME DEFAULT NOW() ON UPDATE NOW(), priority INT, FOREIGN KEY (user_id) REFERENCES users(id), FOREIGN KEY (project_id) REFERENCES projects(id))"

my_cursor.execute(query)

my_db.commit()

my_cursor.close()
my_db.close()