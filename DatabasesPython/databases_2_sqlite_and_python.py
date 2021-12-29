import sqlite3

# Tim's recommendation is to not use SQL semi-colons in Python

db = sqlite3.connect("contacts.sqlite")
# Create a table if it doesn't exist. If it exists, don't create it:
db.execute("CREATE TABLE IF NOT EXISTS contacts(name TEXT, phone INTEGER, "
           "email TEXT)")
db.execute("INSERT INTO contacts (name, phone, email) VALUES ('Antonio', "
           "123456, 'antonio@myemail.com')")
db.execute("INSERT INTO contacts VALUES ('Maria', 789012, 'maria@myemail.com')")

cursor = db.cursor()
cursor.execute("SELECT * from contacts")

# A cursor in SQL is an iterable, but it doesn't work the same as a list
# in Python. It doesn't keep track of what came before like lists do, so
# if you uncomment the for loop below, the one next to it will not be executed
# because the cursor will have run out of values to unpack. Since memory
# is not a problem for a cursor, we can work with billions of pieces of
# data and not run out of memory.

# for row in cursor:
#     print(row)

# Each row is a tuple, so let's unpack the tuple:
# for name, phone, email in cursor:
#     print(name)
#     print(phone)
#     print(email)
#     print("-" * 30)

# fetchall() returns a list with the tuples containing the values we inserted:
# print(cursor.fetchall())

# fetchone() returns a tuple with the values of the next row. If called again
# and no more rows exist, it returns None
print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())

# fetchmany() returns a list with the amount of rows specified. If called
# again and no more rows exist, it returns an empty list
# print(cursor.fetchmany(1))
# print(cursor.fetchmany())
# print(cursor.fetchmany())

cursor.close()
db.commit()  # Commit the change in our database. If you don't do this, the
# changes will not be in the database
db.close()