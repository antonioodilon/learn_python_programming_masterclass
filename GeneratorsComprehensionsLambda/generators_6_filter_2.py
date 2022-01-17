import timeit

# Now we will use timeit to see which approach is faster: list comprehension
# or filter()

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


def spamless_comp() -> list:
    meals = [meal for meal in menu if "spam" not in meal]
    # meals = [meal for meal in menu if meal_without_spam(menu)]
    return meals
# What slows down spamless_filter() and this function here if you uncomment
# the line with meal_without_spam(menu) is the call to another function
# (meal_without_spam() in this case)


print("-" * 60)


def meal_without_spam(menu_list: list) -> bool:
    return "spam" not in menu_list


def spamless_filter() -> list:
    spamless_meals = list(filter(meal_without_spam, menu))
    return spamless_meals


if __name__ == "__main__":
    print(spamless_comp())
    print(spamless_filter())
    print(timeit.timeit(spamless_comp, number=10000))
    print(timeit.timeit(spamless_filter, number=10000))
# A list comprehension seems to be faster every time.
