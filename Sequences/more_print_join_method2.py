plants = [
    "Desert flower",
    "Daffodil",
    "Rose",
    "Tree",
    "Grass",
    "Parsley",
    "Sage",
    "Rosemary",
    "Thyme"
]

for plant in plants:
    print(plant)

print("-" * 60)

separator = " | "
output = separator.join(plant for plant in plants)
# We don't need to use a for loop here because join() iterates over the list for us
# All the items in the iterable MUST BE STRINGS!
print(output)   # Each of the flowers has been joined into a single string

print("-" * 60)

separator2 = " | "
output2 = separator2.join(plants)
# We don't need to use a for loop here because join() iterates over the list for us
# All the items in the iterable MUST BE STRINGS!
print(output2)  # Each of the flowers has been joined into a single string

print("-" * 60)

print(", ".join(plants))