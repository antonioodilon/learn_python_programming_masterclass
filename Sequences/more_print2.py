menu = [
    ["cheddar cheese", "pork rinds", "ground beef", "bone marrow"],
    ["sausages", "bacon"],
    ["ground beef", "beef liver", "bacon", "pork rinds"],
    ["chicken legs", "chicken breast", "bone marrow", "butter", "burger patties"],
    ["lard", "eggs", "eggs", "eggs", "beef liver", "eggs"],
    ["eggs", "sausages", "ground beef", "eggs", "eggs"],
    ["bacon", "cheddar cheese", "chicken breast", "eggs"],
    ["eggs", "bacon", "ground beef", "chicken legs", "eggs"],
]

# meal2 = []

for meal in menu:
    for item in meal:
        if item != "eggs":
            print(item, end=", ")
            # to remove this comma in end we need a different code
    print()

print()
print("-"*90)
print()

for meal in menu:
    items = ", ".join((item for item in meal if item != "spam"))
    print(items)