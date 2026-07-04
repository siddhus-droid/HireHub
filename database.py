import sqlite3
import os

DATABASE = 'recruitment.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    schema_path = os.path.join(os.path.dirname(__file__), 'database', 'schema.sql')
    with open(schema_path, 'r') as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()

if __name__ == '__main__':
    # Initialize the database if ran directly
    init_db()
    print("Database initialized successfully.")
