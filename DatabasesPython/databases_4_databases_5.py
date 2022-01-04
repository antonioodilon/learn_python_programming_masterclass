import sqlite3

db = sqlite3.connect("accounts2.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)

# sqlite can also display the local time for the user.
# Since I couldn't get the other ways to work, this is probably the best way
for row in db.execute("SELECT strftime('%Y-%m-%d %H:%M:%f', history.time,"
                      " 'localtime') AS localtime, history.account, history.amount "
                      "FROM history ORDER BY history.time"):
    print(row)

db.close()