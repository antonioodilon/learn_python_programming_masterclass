name = input("What is your name? ")
age = int(input("And how old are you, {}? ".format(name)))

if 18 >= age or age > 30:
    print("I am sorry, {0}, but being {1} means you unfortunately you can't enter the party.".format(name, age))
else:
    print("Welcome aboard, {}! Enjoy the party!".format(name))

print("-" * 80)

if 18 < age <= 31:
    print("Welcome aboard, {}! Enjoy the party!".format(name))
else:
    print("I am sorry, {0}, but being {1} means you unfortunately you can't enter the party.".format(name, age))