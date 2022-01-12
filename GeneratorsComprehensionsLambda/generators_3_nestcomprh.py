# The same way we have nested for loops (for loops inside other for loops),
# we can also have nested comprehensions

meats = ["ground beef", "chicken legs", "pork rinds", "beef liver"]
extras = ["blue cheese", "eggs", "mozzarella cheese", "eggs and bacon",
          "eggs and cheese"]

meals = [(meat, extra) for meat in meats for extra in extras]
# Structure of this comprehension:
# 1) Expression: (meat, extra)
# 2) Iterations: for meat in meats and for extra in extras
# According to Tim this is technically probably not a nested comprehension,
# but a comprehension with two iterator parts
for meal in meals:
    print(meal)

print("=" * 80)

# Another way of doing the same thing:
for meal in [(meat, extra) for meat in meats for extra in extras]:
    # This is a list
    print(meal)

print("=" * 80)

# If you do it like this, Python will first iterate over extras, and only
# then iterate over meats
for meal in [(extra, meat) for extra in extras for meat in meats]:
    print(meal)

print("=" * 80)

# This is the equivalent code in a regular for loop:
for meat in meats:
    for extra in extras:
        print((meat, extra))  # Two parentheses so we can create tuples

print("=" * 80)

# Now we have a comprehension whose expression is another list comprehension.
# First it creates a list by checking for the first meat in meats.
# Since the second variable of the tuple is extra in extras, it checks for the
# first item in extras.
# Then it moves on to the second meat in meats, but the second variable of
# the tuple is still extra in extras, so it checks for the first value again,
# and so on, until all the possible combinations of meat with the first value
# of extras has been dealt with. This is the first list.
# Then it creates a second list by doing the same thing, but with the second
# value of extras, and so on until all the values of extras have been used
# to create out five lists.
for meal_nested in [[(meat, extra) for meat in meats] for extra in extras]:
    print(meal_nested)
# Structure:
# 1) Expression: list comprehension -> [(meat, extra) for meat in meats]
# 1a) Structure of the expression:
# - (meat, extra) -> expression: tuple
# - for meat in meats -> iteration
# 2) Iteration: for extra in extras

print("=" * 80)

meals_nested = [[(meat, extra) for meat in meats] for extra in extras]
print(meals_nested)

print("=" * 80)

# Therefore, if we want to produce a similar output, by first printing every
# value of meat in meats in order (ground beef, then chicken legs and so on),
# we just swap the iteration parts:
for meal_nested in [[(meat, extra) for extra in extras] for meat in meats]:
    print(meal_nested)