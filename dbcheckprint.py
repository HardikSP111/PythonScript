import sqlite3

DATABASE_NAME = 'data.db'

def create_database():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            address TEXT NOT NULL
        )
    """)

    conn.close()

def fetch_records():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM records')
    records = cursor.fetchall()
    connection.close()
    return records
