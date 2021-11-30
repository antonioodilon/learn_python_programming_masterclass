# The setdefault method doesn't only return the items and values in a
# dictionary. It also adds an entry to that dictionary

from smart_fridge_contents import pantry

chicken_quantity = pantry.setdefault("chicken", 0)
print(f"chicken: {chicken_quantity}")

paprika_content = pantry.setdefault("paprika", 0)
print(paprika_content)

ketchup_content = pantry.get("ketchup", 0)
print(ketchup_content)
# get only returns the item, but doesn't add it to the dictionary.

print()

for item, quantity in sorted(pantry.items()):
    print(item, quantity)
# There are 500 grams of chicken here

print()

pantry["chicken"] = pantry.setdefault("chicken", 0) + 300

pantry["beef liver"] = pantry.setdefault("beef liver", 0) + 500

ground_beef_content = pantry.setdefault("ground beef", 1000)
# Another way to add items to our dictionary with a default value

z_quantity = pantry.setdefault("zucchini", "ten")

lettuce_content = pantry.setdefault("lettuce", 0)
print(lettuce_content)

print()

for item, quantity in sorted(pantry.items()):
    print(item, quantity)
# Now there are 800 grams of chicken, 500 grams of beef liver and 0
# lettuce.