def python_meal():
    print("Sausages and eggs")
    # This function returns nothing


def python_meal_2():
    width = 80
    text = "Sausages and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


def center_text(text):
    text = str(text)  # Now if the user types a number, it'll be converted
    # to a string and the program won't raise an error
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)

# Calling the function:
python_meal()
print(python_meal())  # As you can see, it returns none

print("-" * 100)

python_meal_2()

print("-" * 100)

center_text("Sausages and eggs")
center_text("Beef, liver, eggs, sausages, sausages")
center_text("Beef, liver, eggs, eggs, sausages, sausages and bacon")
center_text(121210000)
# center_text(1111111111)  -> Object int doesn't have type length. Interesting.
# That's because numbers are stored in computer memory in binary form. For
# example, the integer 12 is stored as 1100 in the computer's memory