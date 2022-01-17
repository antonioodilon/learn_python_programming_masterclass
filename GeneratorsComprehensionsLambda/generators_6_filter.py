menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["chicken", "chips"]
]

for meal in menu:
    if "spam" not in meal:
        print(meal)

meals = [meal for meal in menu if "spam" not in meal]
print(meals)

print("-" * 60)

# Now we will use filter to achieve the same result. Filter returns True
# if the given condition (no spam in the meal) is met; False otherwise


def meal_without_spam(menu_list: list) -> bool:
    return "spam" not in menu_list


print(meal_without_spam(menu))
print(type(meal_without_spam(menu)))  # When struggling to document the function,
# I think it is a good idea to print the type of the return

# filter() takes two arguments: a function and an iterable to iterate over.
# Notice that filter() needs a function
spamless_meals = list(filter(meal_without_spam, menu))
print(spamless_meals)