import sys

# Now I am going to test the generator in generator_range_2 from generators_1_generators.py
# First I'm recreating the function without yield:
# I wasn't able to do the same thing using start, so what I said I wanted to do
# on line 4 didn't work. The comparison is interesting nonetheless


def generator_range(n: int):
    print("generator_range starts")
    a_list = []
    start = 0
    while start < n:
        print("start is now", start)
        start += 1
        a_list.append(start)
    return a_list


_ = input("line 20")
small_range = generator_range(5)
_ = input("line 22")

_ = input("line 24")
for value in small_range:
    _ = input("line 26 - inside loop")
    print(value)

print("-" * 40)

# Now run the program compare with the code below. See how different they
# behave:


def generator_range_2(n: int):
    print("generator_range_2 starts")
    start = 0
    while start < n:
        print("generator_range_2 is returning", start)
        yield start
        start += 1


# yield puts the code in a sort of "suspended" state. I believe that with yield
# the function gets called several times instead of just once, like in generator_range.
# yield works like an iterator.
_ = input("line 47")
small_range_2 = generator_range_2(5)
_ = input("line 48")

# print("small_range is {} bytes".format(sys.getsizeof(small_range_2)))
small_list = []

_ = input("line 53")
for value in small_range_2:
    _ = input("line 55 - inside loop")
    small_list.append(value)

print("small_list is {} bytes".format(sys.getsizeof(small_list)))
print(small_range_2)  # small_range is a generator object, which we created
# with the reserved word yield in the generator_range() function
print(small_list)