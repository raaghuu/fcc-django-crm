import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="6341",
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE raaghuudb")

print('DB Created')