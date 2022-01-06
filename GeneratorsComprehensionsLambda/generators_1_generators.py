# Let's see how much memory gets stored in our computer:
import sys


# Making our own range function:
def generator_range(n: int):
    start = 0
    while start < n:
        yield start
        start += 1


def generator_range_2(n: int):
    print("generator_range_2 starts")
    start = 0
    while start < n:
        print("generator_range_2 is returning", start)
        yield start
        start += 1


big_range = range(10000)
big_range_2 = generator_range(10000)

print("big_range is {} bytes".format(sys.getsizeof(big_range)))
print("big_range_2 is {} bytes".format(sys.getsizeof(big_range_2)))

print(big_range_2)  # big_range_2 is a generator object, which we created
# with the reserved word yield in the generator_range() function

big_list = []
for value in big_range:
    big_list.append(value)

print("big_list is {} bytes".format(sys.getsizeof(big_list)))
# As can be seen in the output, big_range_2 occupies more memory than big_range,
# but a lot less memory than big_list

print("-" * 40)

# Calling a variable just with the name _ (underscore) is a Python convention
# which means that we are not in the variable; we are just interested in
# making the program wait for our input:
_ = input("line 44")
small_range = generator_range_2(5)
small_range_2 = range(5)
_ = input("line 47")

print("small_range is {} bytes".format(sys.getsizeof(small_range)))
small_list = []

_ = input("line 52")
for value in small_range:
    _ = input("line 54")
    small_list.append(value)

print("small_list is {} bytes".format(sys.getsizeof(small_list)))
print(small_range)  # small_range is a generator object, which we created
# with the reserved word yield in the generator_range() function
print(small_range_2)
print(small_list)  # small_list is a lot smaller than big_list, but still
# bigger than small_range