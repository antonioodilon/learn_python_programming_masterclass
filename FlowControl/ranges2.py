#Getting the code from conditions.py. The code in conditions.py is better for this kind of situation.

age = int(input("Please tell us your age: "))

#if age >= 16 and age <= 65:
if age in range(16, 66):
    print("Have a good day at work!")
else:
    print("Enjoy your free time!")

print("-" * 80)

if 16 > age or 65 < age:
    print("Enjoy your free time!")
else:
    print("Have a good day at work!")