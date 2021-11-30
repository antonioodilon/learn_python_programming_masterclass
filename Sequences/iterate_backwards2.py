data = [1345, 1023, 307, 6702, 1820, 2709, 105, 1263, 3789, 5093, 573, 1372,
        1680, 1709]

print(len(data))

min_value = 1000
max_value = 2000

top_index = len(data) - 1

# To comment/uncomment: ctrl + /
for index, value in enumerate(reversed(data)):
    if value > max_value or value < min_value:
        print(top_index - index, value)
        del data[top_index - index]
    # I believe the index with the enumerate function doesn't work backwards,
    # so gotta create another variable in this case called top_index

print(data)
print(data.sort())
print(sorted(data))
print(data.count(5093))