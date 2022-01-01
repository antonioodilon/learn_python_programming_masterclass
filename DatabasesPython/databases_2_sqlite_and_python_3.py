import sqlite3

db = sqlite3.connect("contacts.sqlite")
# db.execute("INSERT INTO contacts (name, phone, email) VALUES ('Antoinette', "
#            "238759, 'antoinette@heremail.com')")
# db.commit()

user_name = input("Please insert your name: ")
user_email = input("Please insert your email: ")

# TODO:
# if user_name in contacts:
    # Update the contacts
# Else, create a new entry
# list_contacts = db.execute("SELECT * FROM contacts")
# print(list_contacts)

user_update = "UPDATE contacts set email='{0}' WHERE name='{1}'"\
    .format(user_email, user_name)
user_cursor = db.cursor()
user_cursor.execute(user_update)  # The cursor needs to execute the action
# user_cursor.executescript(user_update) # executescript() executes more than
# one statement in a single call
user_cursor.connection.commit()
user_cursor.close()

print("Your email has now been updated: ")
for row in db.execute("SELECT * FROM contacts"):
    print(row)

db.close()