import pytz
import sqlite3

db = sqlite3.connect("accounts2.sqlite")

for row in db.execute("SELECT * FROM history"):
    local_time = row[0]
    print(row, type(row), type(local_time))  # If you take a look at the output
    # without detect_types, you'll see that local_time object is of a string
    # class, not datetime

db.close()

print("-" * 80)

db2 = sqlite3.connect("accounts2.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)

for row2 in db2.execute("SELECT * FROM history"):
    local_time2 = row2[0]
    print("{0} \t {1}".format(local_time2, type(local_time2)))

db2.close()

print("-" * 80)

db3 = sqlite3.connect("accounts2.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)

for row3 in db3.execute("SELECT * FROM history"):
    utc_time = row3[0]
    local_time3 = pytz.utc.localize(utc_time).astimezone()
    print("{}\t{}".format(utc_time, local_time3))

db3.close()