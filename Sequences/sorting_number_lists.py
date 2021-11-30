empty_list = []
even = [2, 4, 6, 8, 10, 12]
odd = [1, 3, 5, 7, 9, 11]

numbers = even + odd
print(numbers)

sorted_numbers = sorted(numbers)
print(sorted_numbers)

print(numbers)  # Here the list numbers is not modified

numbers.sort()  # Here we've modified the list numbers
print(numbers)

digits = sorted("93045")
print(len(digits))
print(digits)   # A list of strings

more_digits = list("67128") # Creating a list
print(more_digits)

# more_numbers = list(numbers)
# more_numbers = numbers[:] # slicing to produce a new list
more_numbers = numbers.copy()   # using the copy() method to create a new list
print(more_numbers)
print(more_numbers is numbers)  # both lists have the same output, but are
# different lists
print(more_numbers == numbers)  # both lists have the same items, but are
# not the same list