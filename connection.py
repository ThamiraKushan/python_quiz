import mysql.connector as conn

db_connection = conn.connect(
    host="localhost", username="root", password="root", database="quiz_app"
)
