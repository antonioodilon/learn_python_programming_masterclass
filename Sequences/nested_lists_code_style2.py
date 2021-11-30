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
    if "eggs" not in meal:
        print(meal)
        for item in meal:
            print(item)
    else:
        print("'Eggs' appear {0} times in meal{1}".format(meal.count("eggs"),
                                                          meal))
        # For each meal in menu, print the meal and the number of times "eggs"
        # appears in the meal
        # In meal X, "eggs" appears Z times