import socket
import mysql.connector


mydb = mysql.connector.connect(
    host= "localhost",
    passwd= "okwudili2009tooradmin#",
    user= "newuser",
    database = "mydatabase",
)

print(mydb)


mycursor = mydb.server_host
print(mycursor)