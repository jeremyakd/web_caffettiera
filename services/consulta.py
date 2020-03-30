import sqlite3

conector = sqlite3.connect('db.sqlite3')

cursor = conector.cursor()

cursor.execute("SELECT * FROM services_service")

rows = cursor.fetchall()

conector.close()

def return_data_from_database():
    return rows