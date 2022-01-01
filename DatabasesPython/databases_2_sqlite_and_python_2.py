import sqlite3

db = sqlite3.connect("contacts.sqlite")  # Connecting to the already created
# database

update_db = "UPDATE contacts set email='updated@updatedemail.com' WHERE " \
            "name='Antonio'"
update_cursor = db.cursor()
update_cursor.execute(update_db)
print("{} rows have been updated".format(update_cursor.rowcount))
print("-" * 30)

print("Are connections the same? Answer: {}".format(update_cursor.connection == db))
# Since connections are the same, then it is better to update the database
# via the cursor than via the db
print("-" * 30)

update_cursor.connection.commit()  # The cursor can also commit the changes
# using .connection. It's better this way
# db.commit()  # If we don't commit the change to the database, the contacts
# won't be updated
update_cursor.close()

# We don't necessarily need to create a cursor to iterate through our db:
for name, phone, email in db.execute("SELECT * from contacts"):
    print(name)
    print(phone)
    print(email)
    print("-" * 30)

# for row in db.execute("SELECT * from contacts"):
#     print(row)

db.close()