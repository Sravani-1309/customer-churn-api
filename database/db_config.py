import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sravani@2002",
        database="churn_db"
    )
    return conn