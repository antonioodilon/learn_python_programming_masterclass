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
            print(item)
    print()
print("-" * 60)

for meal in menu:
    for item in range(len(meal) - 1, -1, -1):  # change item to index;
        # it's more intuitive
        if meal[item] == "eggs":
            del (meal[item])
    print(meal)

print("-" * 60)

print(menu)

#Code that didn't work:
'''
for meal in menu:
    for item in meal:
        if item != "eggs":
            meal2.append(item)
            meal = meal2
            print(meal2)
            # print(meal, item)
'''

'''For meal in menu:
        if, in the range of the meal going to the end, the item == "eggs",
        delete "eggs"
        print meal and item'''

'''print item if and only if item =! eggs'''
