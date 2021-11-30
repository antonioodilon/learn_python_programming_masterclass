age = int(input("Please tell us your age: "))

#if age >= 16 and age <= 65:
if 16 <= age <= 65:
    print("Have a good day at work!")
else:
    print("Enjoy your free time!")

print("-" * 80)

if 16 > age or 65 < age:
    print("Enjoy your free time!")
else:
    print("Have a good day at work!")