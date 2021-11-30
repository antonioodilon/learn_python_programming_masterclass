parrot = "Norwegian Blue"
#Slicing in steps

print(parrot[0:13:3]) #Nwi u
print(parrot[0:7:3]) #Nwi
print(parrot[::4]) #Nenu

numbers = "3,464 575:686;797,808 919"
separators = numbers[1::4]
print(separators)

values = "".join(char if char not in separators else " " for char in numbers).split()
print([int(val) for val in values]) #Printing a list with the values