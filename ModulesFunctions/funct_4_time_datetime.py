import time

print(time.gmtime())

print(time.localtime())

print(time.time())

time_here = time.localtime()

print("Year: ", time_here[0], time_here.tm_year)
print("Month: ", time_here[1], time_here.tm_mon)
print("Day: ", time_here[2], time.localtime().tm_mday)
# time.localtime()'s output is a tuple, so we can iterate over it and get
# the items at index positions 1, 2, 3 etc. Also, notice tm_mday, tm_year
# etc outputted from the codes on lines 3 and 5 - this is what Tim calls
# a named tuple.