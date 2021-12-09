import shelve

scrambled_eggs = ["eggs", "butter", "salt", "cheese"]
ground_beef = ["ground beef", "salt", "pepper", "lard"]
chicken_breast = ["chicken breast", "butter", "sea salt"]
beef_liver = ["beef liver", "onions", "sea salt"]
sausages = ["sausages"]

with shelve.open("recipes") as recipes:
    recipes["scrambled_eggs"] = scrambled_eggs
    recipes["ground_beef"] = ground_beef
    recipes["chicken_breast"] = chicken_breast
    recipes["beef_liver"] = beef_liver
    recipes["sausages"] = sausages

    for meal, ingredients in recipes.items():
        print(meal, ingredients)

    print("-" * 60)

    for meal in recipes:
        print(meal, recipes[meal])

print("-" * 60)

# Now updating the shelve. For that we'll create a new recipes shelve so
# we can see the difference
with shelve.open("recipes_2") as recipes:
    recipes["scrambled_eggs"] = scrambled_eggs
    recipes["ground_beef"] = ground_beef
    recipes["chicken_breast"] = chicken_breast
    recipes["beef_liver"] = beef_liver
    recipes["sausages"] = sausages

    for meal, ingredients in recipes.items():
        print(meal, ingredients)

    print("-" * 60)

    append_list = recipes["beef_liver"]
    append_list.append("tomatoes")
    recipes["beef_liver"] = append_list

    print(recipes["beef_liver"])  # Notice that beef_liver has been appended

    append_list = recipes["chicken_breast"]
    append_list.append("garlic")
    recipes["chicken_breast"] = append_list

    print(recipes["chicken_breast"])  # chicken_breast has also been appended

    print("-" * 60)

    for meal in recipes:
        print(f"{meal}: {recipes[meal]}")

print("-" * 60)

# Another way to update a shelve is by setting writeback to True. I believe
# this approach is better because we write less code like this. But it can
# possibly have more memory usage
with shelve.open("recipes_3", writeback=True) as recipes_3:
    # recipes_3["scrambled_eggs"] = scrambled_eggs
    # recipes_3["ground_beef"] = ground_beef
    # recipes_3["chicken_breast"] = chicken_breast
    # recipes_3["beef_liver"] = beef_liver
    # recipes_3["sausages"] = sausages
    #
    # for meal in recipes_3:
    #     print(f"{meal}: {recipes_3[meal]}")

    # We've commented the code above because the data has already been written
    # to the database. No need to keep re-writing it.

    recipes_3["scrambled_eggs"].append("oregano")
    for meal in recipes_3:
        print(f"{meal}: {recipes_3[meal]}")
