d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']

d2 = {
    5: "this is five",
    11: "eleven (stranger things)",
    10: "ten",
    4: "new four",
}

d.update(d2)
for key, value in d.items():
    print(key, value)
# The order of the key-value pairs is preserved

print()

d.update(enumerate(pantry_items))
for key, value in d.items():
    print(key, value)
# Updating d with the items in pantry_items as values