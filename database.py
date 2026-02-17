import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('atm_database.db')

# Create a cursor object
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS accounts (
    account_number INTEGER PRIMARY KEY,
    name TEXT NOT NULL CHECK(length(name) >= 15 AND length(name) <= 20),
    amount REAL NOT NULL,
    atm_pin INTEGER NOT NULL CHECK(atm_pin >= 1000 AND atm_pin <= 9999)
)
''')

# Commit changes and close the connection
conn.commit()
conn.close()