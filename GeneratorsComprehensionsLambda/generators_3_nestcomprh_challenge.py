# Use a nested comprehension to produce the same values as the code below:

for i in range(1, 16):  # 16 is not included
    for j in range(1, 16):  # 16 is not included
        print(i, i * j)

print("=" * 60)

for num_tuple in [(i, i * j) for i in range(1, 16) for j in range(1, 16)]:
    print(num_tuple)

print("=" * 60)

# This will produce the output we are looking for: first all the combinations
# with the first value of i will be dealt with, then all the combinations with
# the second value of i, and so on.
for list_num in [[(i, i * j) for j in range(1, 16)] for i in range(1, 16)]:
    print(list_num)

print("=" * 60)

# This will produce a different output.
for list_num in [[(i, i * j) for i in range(1, 16)] for j in range(1, 16)]:
    print(list_num)

print("=" * 60)

# In order to save up memory we can also use a generator expression:
for x, y in ((i, i * j) for i in range(1, 16) for j in range(1, 16)):
    print(x, y)
# A generator expression isn't constantly creating a list in memory.
# We can check for performance using the timeit module