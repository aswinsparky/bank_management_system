import pyodbc
import mysql.connector

def get_db_connection():
    conn = pyodbc.connect(
        "DSN=MyDSN;"
        "DRIVER={MySQL ODBC 9.2 Unicode Driver};"
        "SERVER=localhost;"
        "DATABASE=bank_db;"
        "UID=root;"
        "PWD=aswinraj;"
        "OPTION=3;"
    )
    return conn



def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            account_number INT UNIQUE,
            balance FLOAT
        )
    ''')
    conn.commit()
    conn.close()
