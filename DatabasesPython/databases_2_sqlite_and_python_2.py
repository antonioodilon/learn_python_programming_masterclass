import sqlite3

db = sqlite3.connect("contacts.sqlite")  # Connecting to the already created
# database

for row in db.execute("SELECT * from contacts"):
    print(row)

db.close()