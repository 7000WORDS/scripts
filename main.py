import mysql.connector
import socket



name = socket.gethostname()
ip = socket.gethostbyname(name)


mydb= mysql.connector.connect(
    host='127.0.0.1', 
    user='newuser',
    port='3306', 
    passwd='okwudili2009tooradmin#',
    database="mydatabase"
)


print(mydb)

mycursor = mydb.cursor()

sql ="INSERT INTO customers (name, address) VALUES(%s, %s)"
val = (name, ip)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")