import mysql.connector.python

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password ='haryana123',
)
print(mydb)
