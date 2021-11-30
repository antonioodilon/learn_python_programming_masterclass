# numbers = {} -> This creates a dictionary. Type print(numbers, type(numbers))
# and check

# numbers = {*""} -> This creates a set using the *args we saw in the functions
# intro section, but it's hard to read

# numbers = {*{}} -> Another way to create an empty set. Very hard to read
# as well

numbers = set() # Using the set() function to create an empty set
print(numbers, type(numbers))

# numbers.add(45)
#
# print(numbers)

while len(numbers) < 6:
    next_number = int(input("Please type in a number: "))
    numbers.add(next_number)
    print(numbers)
print(f"Final set of numbers: {numbers}")

# If you enter the same value more than once, the loop will never terminate
# until it gets another unique value. Because in sets values have to be unique.
# This is one way to avoid duplicate items.