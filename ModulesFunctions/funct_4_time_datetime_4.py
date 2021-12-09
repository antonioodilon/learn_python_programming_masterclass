import time
import datetime

print("The epoch of this system starts at ", time.strftime("%c", time.gmtime(0)))
print("The current timezone is {0} with an offset of {1}".format(time.tzname[0],
                                                                 time.timezone))

if time.daylight == 0:
    print("\tWe are currently not on daylight saving time.")
    print("\tThe official DST timezone is: " + time.tzname[1])
else:
    print("We are under daylight saving time.")

print("The local time is " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print("The UTC time is " + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))

print("-" * 80)

print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())
# The possible differences in the output in terms of the milliseconds (.275057 ...)
# is due to the time computer takes to process each command