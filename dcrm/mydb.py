import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'mysqlpsw'
)

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE dvdatabase")
print("mydb.py FINISHED")