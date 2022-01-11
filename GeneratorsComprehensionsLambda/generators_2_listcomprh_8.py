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
    if "spam" not in meal and "chicken" not in meal:
        meals.append(meal)
    else:
        meals.append("a meal was skipped")

meals_2 = [meal for meal in menu if "spam" not in meal and "chicken" not in meal]
# 1) Expression: meal
# 2) Iteration: for meal in menu
# 3) Filter(s): if "spam" not in meal. It's not exactly a condition using "if";
# in fact, it's more like an actual filter. If we want another filter, we can
# add if "chicken" not in meal also

# An alternative way to do the same thing:
# meals_2 = [meal for meal in menu if "spam" not in meal if "chicken" not in meal]

print(meals)
print(meals_2)  # Output: the list meals in meals_2
print("-" * 100)
[print(meal) for meal in meals_2]  # Output: each meal in meals individually
print(meal for meal in meals_2)  # Output: <generator object <genexpr> at 0x000002746B165D20>

print("-" * 100)

# Let's say that we have a customer that doesn't like bacon and sausage together
# (prefers them separately), but likes spam and eggs, no matter if they are
# together or not
picky_meals = [meal for meal in menu if "spam" in meal or "egg" in meal
               if not ("sausage" in meal and "bacon" in meal)]
print(picky_meals)

# picky_meals_2 is now using a single filter instead of two. Notice that we
# have one if here.
picky_meals_2 = [meal for meal in menu if ("spam" in meal or "egg" in meal)
                 and not ("sausage" in meal and "bacon" in meal)]
print(picky_meals_2)