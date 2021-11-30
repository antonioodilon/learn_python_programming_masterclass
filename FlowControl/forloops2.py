#Code taken from slicing2 file in HelloWorld project

numbers = "3,464 575:686;797,808 919"
separators = ""

for char in numbers:
    if not char.isnumeric():
        separators = separators + char

print(separators)

#Try to do this with a list and append function in the future

print("-" * 80)

values = "".join(char if char not in separators else " " for char in numbers).split()
print([int(val) for val in values]) #Printing a list with the values