# This function doesn't return any values, but it performs a useful action:
# it centers the text in the screen

def banner_text(text):
    screen_width = 80
    if len(text) > screen_width - 4:
        print("EEEK!")
        print("The text is too big for the screen!")
    if text == "*":
        print("*" * screen_width)
    else:
        output_string = "**{0}**".format(text.center(screen_width - 4))
        print(output_string)


banner_text("*")
banner_text("Lord Khorne,")
banner_text(" ")
banner_text("grant me your power,")
banner_text(" ")
banner_text("that I might sweep this army aside!")
banner_text("*")

print()

result = banner_text("This returns None")
print(result)

print()

numbers = [5, 2, 4, 1, 9, 91, 43, 62, 78, 12]
print(numbers)
numbers.sort()
print(numbers)
print(numbers.sort())  # This returns none because the method sort() doesn't
# return a value