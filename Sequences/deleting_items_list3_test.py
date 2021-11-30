# Be sure to always test the code thoroughly yourself after writing it!
# Check all possible scenarios that might go wrong. Check the videos
# "Test, Test, Test etc" and "Testing the program" for reference

# data = [30, 46, 79, 204, 222, 230, 247, 256, 268, 270, 289, 291, 520, 574]
# data = [204, 222, 230, 247, 256, 268, 270, 289, 291, 520, 574]
# data = [204, 222, 230, 247, 256, 268, 270, 289, 291]
# data = [30, 46, 79, 520, 574]
# data = []
data = [30, 46, 79, 204, 222, 230, 247, 256, 268, 270, 289, 291, 520, 574]

print(data)
print(len(data))

stop = 0
min_valid = 200
max_valid = 500

for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break

del data[:stop]
print(data)


start = 0

for index in range(len(data) - 1, -1, -1):
    if data[index] <= max_valid:    # data[index], not just index
        start = index + 1
        break

del data[start:]
print(data)

# Old code below. Doesn't work because start has to be 0, not the length
# of the list minus 1
'''
start = len(data) - 1

for index in range(start, -1, -1):
    if index <= max_valid:
        start = index + 1
        break

del data[start:]
print(data)
'''