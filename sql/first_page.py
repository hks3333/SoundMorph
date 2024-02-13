import sqlite3

connection = sqlite3.connect('soundmorph.db')
cursor = connection.cursor()

query = "SELECT * FROM login_details;"
cursor.execute(query)
d = []
for row in cursor.fetchall():
    d.append(row)

print(d)
cursor.close()
connection.close()
