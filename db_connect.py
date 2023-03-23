import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="quiz_app"
    )
    cur = conn.cursor()
    return cur, conn

# password = "admin1234"
# md5 = hashlib.md5(password.encode())

# print("The corresponding hash is : ")
# print(md5.hexdigest())