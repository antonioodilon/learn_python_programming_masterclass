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

for meal in menu:
    for item in range(len(meal) - 1, -1, -1):  # change item to index;
        # it's more intuitive
        if meal[item] == "eggs":
            del (meal[item])
    print(", ".join(meal))
    # All the items in the iterable MUST BE STRINGS!

print("-" * 60)

print(menu)