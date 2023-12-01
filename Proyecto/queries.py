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

ubicacion=""
nombre=""
edad=""
tel=""
pariente=""

cursor = conn.cursor()
cursor.execute("SELECT * FROM Paciente")
result = cursor.fetchall()
cursor.close()

ubicacion=result[0][2]
nombre=result[0][1]
edad=result[0][3]

cursor=conn.cursor()
cursor.execute("SELECT * FROM Teldeemergencia")
resultado=cursor.fetchall()
cursor.close()
tel=resultado[2][3]
pariente=resultado[2][1]
