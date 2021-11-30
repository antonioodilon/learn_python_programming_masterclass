data = [30, 46, 79, 204, 222, 230, 247, 256, 268, 270, 289, 291, 520, 574]
print(data)
print(len(data))

stop = 0
min_valid = 200
max_valid = 500

# Processing the low values in the list
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index    # Each time the loop iterates through the values
        # of data, the index will be increased by 1. When value is bigger
        # than or equal to 200, then stop will be equal to index and the
        # loop will break
        break

del data[:stop] # Having broken out of the loop, Python will delete the
# values of data up to, but not including, the value at the index position
# bigger than, or equal to, stop.
print(data)


# Processing the high values in the list
start = len(data) - 1 # data had 14 items, and now it has 12, so the 12nd
# item is at index position 11, and the length is 12

for index in range(start, -1, -1):  # Everytime the loop iterates, the start
    # index will change to start - 1
    if index <= max_valid:
        start = index + 1   # We don't want to delete the start values
        # because they are not outliers.
        break

del data[start:]
print(data)

# The code that Tim Buchalka wrote:
'''
start = 0
for index in range(len(data) - 1, -1, -1):
    if data[index] <= max_valid:
        start = index + 1
        break

del data[start:]
print(data)
'''


# Work backwards in the list, from the last value to the first
# get the length of the list and subtract one
# start equals the index?

# When the index gets to a value that is less than or equal to max_valid,
# break the loop

        # data.pop(len(data) - 1, value)
        # break

'''
for index, value in enumerate(data):
    # Work backwards in the list, from the last value to the first
    # get the length of the list and subtract one
    # start equals the index?
    start = index
    start -= 1
    if value <= max_valid:
        # When the index gets to a value that is less than or equal to max_valid,
        # break the loop
        start = index
        break

del data[start:]
print(data)
'''