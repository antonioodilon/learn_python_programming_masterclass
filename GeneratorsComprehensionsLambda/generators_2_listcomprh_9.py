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

# Conditional expressions:
x = 31
expression = "thirty" if x == 30 else "unknown"
# If we don't put an else here, what value will expression have if x != 30?
print(expression)

# What we are going to do now is to remove the filter and add a conditional
# expression. So if "spam" not in meal else "a meal was skipped" is a conditional
# expression just like "thirty" if x == 30 else "unknown". It is NOT a filter!
meals_2 = [meal if "spam" not in meal else "a meal was skipped" for meal in menu]
# Structure:
# 1) if "spam" not in meal else "a meal was skipped" = Conditional expression
# 2) for meal in menu = iteration
print(meals_2)

print("-" * 80)

# We can make our expressions as complex as we need or want:
for meal in menu:
    print(meal, "contains chicken" if "chicken" in meal else "contains bacon"
          if "bacon" in meal else "contains egg")
    # The order is very important! Notice in the output that the first two
    # meals contain egg AND bacon, but the output was "contains bacon" instead
    # of "contains egg" (even though egg is the first item in the first meal).
    # Python reads code from left to right and from top to bottom. "contains egg"
    # will only be printed if there is no chicken or bacon.

# expression = ""
# if x == 30:
#     expression = "thirty"
# print(expression)