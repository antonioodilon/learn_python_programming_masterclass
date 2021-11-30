data = [1345, 1023, 307, 6702, 1820, 2709, 105, 1263, 3789, 5093, 573, 1372,
        1680, 1709]

print(len(data))

min_value = 1000
max_value = 2000

for index in range(len(data) - 1, -1, -1):
    if data[index] < min_value or data[index] > max_value:
        print(index, data)
        del(data[index])

print(data)