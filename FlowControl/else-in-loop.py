numbers = [1, 3, 4, 16, 26, 72, 31]

for number in numbers:
    if number % 5 == 0:
        print("This number is unacceptable")
        break
    print(number)
else:
    print("These numbers are acceptable")
# Notice the indentation of the else statement. else can be associated
# with either if or for