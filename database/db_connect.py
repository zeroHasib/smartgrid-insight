import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="hasib",
    database="smartgrid_insight"
)

print("Database Connected Successfully!")