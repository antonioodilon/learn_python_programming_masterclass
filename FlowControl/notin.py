activity = input("What would you like to do today? ")

if "rave" not in activity.casefold(): #casefold() is very useful for converting lowercase letters to uppercase and vice-versa
    print("But I wanna go to a rave party!")
else:
    print("Hell yeah, let's go to the {}!".format(activity))