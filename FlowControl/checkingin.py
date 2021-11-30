parrot = "Norwegian Blue"
letter = input("Please enter a letter: ")

if letter in parrot:
    print("{0} is in {1}".format(letter, parrot))
else:
    print("{0} is not in the expression.".format(letter))

print("-" * 80)

if letter not in parrot:
    print("{0} is not in the expression.".format(letter))
else:
    print("{0} is in {1}".format(letter, parrot))