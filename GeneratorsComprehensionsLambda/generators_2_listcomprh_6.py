print(__file__)

numbers = [2, 4, 6, 8, 10]

print(numbers)

number = int(input("Type in a number and I'll tell you its square: "))

squares = [number ** 2 for number in numbers]
# The mistake seen in generators_2_listcomprh_5 doesn't happen here. The variable
# number in the list comprehension is protected and is not in the outer scope,
# preventing bugs

index_position = numbers.index(number)
print(squares[index_position])