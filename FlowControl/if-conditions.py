name = input("Please enter your name: ")
age = int(input("Please enter your age, {}: ".format(name)))
print(age)

'''
if age == 900:
    print("Sorry, mate, but you are too old.")
elif age >= 18:
    print("Congratulations. You are old enough to vote.")
    print("Please put the X in the box.")
else:
    print("I am sorry, but you are not old enough to vote.")
    print("Please come back in {} years.".format(18 - age))
'''

if age < 18:
    print("I am sorry, but you are not old enough to vote.")
    print("Please come back in {} years.".format(18 - age))
elif age == 900:
    print("Sorry, mate, but you are too old.")
else:
    print("Congratulations. You are old enough to vote.")
    print("Please put the X in the box.")