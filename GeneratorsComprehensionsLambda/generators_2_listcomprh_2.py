print(__file__)
# Printing the file name to make sure we are running different files on
# either side of the screen. Right click the file and select split right
# or split down to work with two files on the same screen.
# Do this to compare this file with generators_2_listcomprh

numbers = [2, 4, 6, 8, 10]

squares = [number ** 2 for number in numbers]  # A list comprehension
# A list comprehension has two parts:
# 1) number ** 2 is the expression we want to return
# 2) for number in numbers is the iteration over a sequence. It's identical
# to a for loop, but without the colon

squares_2 = [number ** 2 for number in range(12, 22, 2)]
# The second part can be any iterable. We are getting numbers in the range
# of 12 to 22 (not included), taking steps of 2

squares_3 = {number ** 2 for number in numbers}  # A set comprehension

squares_4 = [number ** 2 for number in range(12, 0, -2)]

print(squares)
print(squares_2)
print(squares_3)
print(squares_4)
