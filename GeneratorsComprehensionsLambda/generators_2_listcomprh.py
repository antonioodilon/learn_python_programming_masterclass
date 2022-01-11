print(__file__)
# Printing the file name to make sure we are running different files on
# either side of the screen. Right click the file and select split right
# or split down to work with two files on the same screen.
# Do this to compare this file with generators_2_listcomprh_2

numbers = [2, 4, 6, 8, 10]

squares = []
for number in numbers:
    squares.append(number ** 2)
    # number *= number
    # squares.append(number)

print(squares)
print(numbers[2])