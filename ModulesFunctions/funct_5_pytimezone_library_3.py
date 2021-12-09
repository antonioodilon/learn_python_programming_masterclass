import datetime
import pytz

# According to Buchalka, it is better to write your program using UTC time
# as standard and letting the user convert it to their local times when
# needed

local_time = datetime.datetime.now()
utc_time = datetime.datetime.utcnow()
print("Naive local time: {}".format(local_time))
print("Naive UTC time: {}".format(utc_time))

aware_local_time = pytz.utc.localize(utc_time).astimezone()
# The .astimezone() method converts the time to whatever is the timezone
# the user finds her/himself in
aware_utc_time = pytz.utc.localize(utc_time)

print("Aware local time: {} . Time zone: {}".format(aware_local_time,
                                                    aware_local_time.tzinfo))
print("Aware UTC time: {} . Time zone: {}".format(aware_utc_time,
                                                  aware_utc_time.tzinfo))

print("-" * 80)

# Using the calculation of seconds since epoch to analyze the gap in the
# UK time when the country went to daylight saving time in 2015

gap_time = datetime.datetime(2015, 10, 25, 1, 30, 0, 0)
print(gap_time)
print(gap_time.timestamp())  # Depending on where you are, this value, being
# the amount of seconds, will be different

s = 1445733000  # Date, hour, seconds etc in gap_time expressed in terms of
# seconds
t = s + (60 * 60)  # When the UK entered daylight saving time in Oct 25th 2015,
# the clocks went forward one hour.

gb = pytz.timezone("GB")  # Input of timezone() method is a string
dt1 = pytz.utc.localize(datetime.datetime.fromtimestamp(s)).astimezone(gb)
dt2 = pytz.utc.localize(datetime.datetime.fromtimestamp(t)).astimezone(gb)

print("(WRONG) {} seconds since epoch is {}".format(s, dt1))
print("(WRONG) {} seconds since epoch is {}".format(t, dt2))
# The problem is that the fromtimestamp() method "return[s] the local date
# and time corresponding to the POSIX timestamp", not the UK time. So this
# is referencing Brazil, not the UK
# The class method utcfromtimestamp(), on the other hand, "return[s] the UTC
# datetime corresponding to the POSIX timestamp". We have deliberately not
# heeded to the advice that we should always work with UTC time first.
# See documentation:
# https://docs.python.org/3.10/library/datetime.html#datetime.datetime.utcfromtimestamp

# Doing it correctly now:
gb2 = pytz.timezone("GB")  # Input of timezone() method is a string
dt3 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(s)).astimezone(gb2)
dt4 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(t)).astimezone(gb2)

print("(CORRECT) {} seconds since epoch is {}".format(s, dt3))
print("(CORRECT) {} seconds since epoch is {}".format(t, dt4))
