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
    9: "new nine",
    "IV": "four",
}

pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']

new_list = d.values()   # Returns the values of a dictionary
print(new_list)

d[10] = "ten"
print(new_list)

keys = list(d.keys())
values = list(d.values())

# Finding a key using its value:
if "four" in values:
    index = values.index("four")
    key = keys[index]
    print(f"{d[key]} was found with the key {key}")

print()

# Finding a key using its value (more efficient):
for key, value in d.items():
    if value == "four":
        print(f"{d[key]} was found with the key {key}")

print()

print(d[9])

# for key, value in d.items():
#     print(key, value)