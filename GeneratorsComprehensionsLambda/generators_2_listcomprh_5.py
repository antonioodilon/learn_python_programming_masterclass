print(__file__)

numbers = [2, 4, 6, 8, 10]

print(numbers)
# We are deliberately making a mistake here. number is also used as the loop
# control variable. Notice that the same mistake doesn't happen with a list
# comprehension. See code in generators_2_listcomprh_6.py to understand
number = int(input("Type in a number and I'll tell you its square: "))

squares = []
for number in numbers:
    squares.append(number ** 2)

index_position = numbers.index(number)
print(squares[index_position])