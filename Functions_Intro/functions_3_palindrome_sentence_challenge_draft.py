string = "I am man"

for char in string:
    string = ''.join(char for char in string if char.isalnum())
print(string)

# for meal in menu:
#     items = ", ".join((item for item in meal if item != "spam"))
#     print(items)