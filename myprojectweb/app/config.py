import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='j3232777',
    database='mydb'
)
cursor = connection.cursor()