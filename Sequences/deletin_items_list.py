data = [30, 46, 204, 222, 230, 247, 256, 268, 270, 289, 291, 520, 574]
#   values at index positions 0, 1, 11 and 12 are too different from the others
print(data)



del data[0:2]
print(data)
print(list(enumerate(data)))

del data[9:]    # notice that the list has been modified: 520 and 574 were
# at index positions 11 and 12, but now are at 9 and 10
print(data)


'''
min_valid = 200
max_valid = 300

for index, value in enumerate(data):
    if min_valid > value or max_valid < value:
        del data[index]

print(data)
'''
# This code doesn't work. Step through the debugger