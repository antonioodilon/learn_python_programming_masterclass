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

meals = []
for meal in menu:
    if "spam" not in meal:
        meals.append(meal)
    else:
        meals.append("a meal was skipped")
print(meals)

meals_2 = [meal for meal in menu if "spam" not in meal]
# 1) Expression: meal
# 2) Iteration: for meal in menu
# 3) Filter(s): if "spam" not in meal. It's not exactly a condition using "if";
# in fact, it's more like an actual filter.

# This produces an error. if here is not exactly a condition, but a filter.
# So we can't add an else here. We'll see how to deal with this later.
# meals_3 = [meal for meal in menu if "spam" not in meal else "a meal was skipped"]

print(meals_2)  # Output: the list meals
[print(meal) for meal in meals_2]  # Output: each meal in meals individually
print(meal for meal in meals_2)  # Output: <generator object <genexpr> at 0x000002746B165D20>