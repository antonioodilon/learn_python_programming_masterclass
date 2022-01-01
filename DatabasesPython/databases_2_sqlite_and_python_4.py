import sqlite3

db = sqlite3.connect("contacts.sqlite")

user_name = input("Please insert your name: ")
user_email = input("Please insert your email: ")

# user_update = "UPDATE contacts set email='{0}' WHERE name='{1}'" \
#     .format(user_email, user_name)
user_update = "UPDATE contacts set email = ? WHERE name = ?"  # This is much
# safer than using the .format() method because it helps protect against
# sql injection attacks
print(user_update)

user_cursor = db.cursor()
user_cursor.execute(user_update, (user_email, user_name))  # executescript() executes more than
# one statement in a single call
print("{} rows updated".format(user_cursor.rowcount))

user_cursor.connection.commit()
user_cursor.close()

# The solution to the challenge Tim presented is below. Retrieve just one
# user's information (the user who gave the input).
print("Your email has now been updated: ")
# for row in db.execute("SELECT * FROM contacts"):
#     if user_name in row:
#         print(row)

# Tim's solution to the challenge:
# for row in db.execute("SELECT * FROM contacts WHERE name = ?", (user_name,)):
for row in db.execute("SELECT * FROM contacts LIKE name = ?", (user_name,)):
    print(row)
    # If someone types their name in lowercase, LIKE takes care of that
    # Important: remember that (user_name,) is a tuple
    # Parentheses don't automatically transform (user_name) in a tuple. For
    # Python to understand it is a tuple, you need the comma at the end:
    # (user_name,)

    # for name, phone, email in enumerate(row):
    #     if name == user_name:
    #         print(name)
    #         print(phone)
    #         print(email)
            # print(row)
     # db.execute("SELECT ")
    # If the name inside the tuple is equal to the name inserted,
    # retrieve that one tuple
    # print(row)

db.close()