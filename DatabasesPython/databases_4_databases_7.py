import sqlite3

db = sqlite3.connect("accounts3.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)

for row in db.execute("SELECT * FROM localhistory"):  # The name of the VIEW
    # is localhistory
    print(row)

db.close()