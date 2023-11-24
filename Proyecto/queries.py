from dotenv import load_dotenv
# import mysql.connector as sql
import pymysql as sql
import ssl
import os

load_dotenv()

conn=sql.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USERNAME"),
    password=os.getenv("DB_PASSWORD"),
    db=os.getenv("DB_NAME"),
    ssl_cert='client-cert.pem',
    ssl_key='client-key.pem',
    ssl_ca=''
)


cursor = conn.cursor()
cursor.execute("SELECT * FROM Paciente")
result = cursor.fetchall()
print(result)
cursor.close()