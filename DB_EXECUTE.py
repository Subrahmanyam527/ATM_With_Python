import sqlite3

conn = sqlite3.connect('atm_database.db')
cursor = conn.cursor()

# Execute the query
cursor.execute('SELECT * FROM accounts')

# Fetch and display results
accounts = cursor.fetchall()
print("All Accounts:")
for account in accounts:
    print(account)

conn.close()
