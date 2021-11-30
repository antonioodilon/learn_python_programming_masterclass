#Some things in Python are evaluated as false. For example, empty strings, the number 0 etc.
#See Python documentation: https://docs.python.org/3/library/stdtypes.html

if 0:
    print("True")
#Notice that this code is unreachable
else:
    print ("False")

print("-"*80)

name = input("What is your name? ")

if name != "":
    print("Greetings, {}! How are you doing in this fine morning?".format(name))
else:
    print("You don't have a name or you don't want to tell us?")