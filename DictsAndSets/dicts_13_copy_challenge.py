# from smart_fridge_contents import recipes

recipes = {
    "chicken": 300,
    "liver": 700,
    "ground beef": 1000,
    "eggs": 60,
}

# recipes2 = {}


def my_deepcopy(d1: dict) -> dict:
    d2 = {}
    for key, value in d1.items():
        # d2 = d1[key][value]
        d2[key] = value
    return d2


recipes_copy = my_deepcopy(recipes)
print(recipes_copy)
recipes_copy["chicken"] = 500
print(recipes_copy)
print(recipes)
# recipes2 = my_deepcopy(recipes)

#     for key, value in d.items():
#         print(key, value)
#     print(d)
#     return d
#
#
# recipes_copy = my_deepcopy(recipes)
# recipes_copy["chicken"] = 500
# print(recipes)
# print(recipes_copy)

# recipes_copy = my_deepcopy(recipes)
# recipes_copy["Butter chicken"]["ginger"] = 300
# print(recipes_copy["Butter chicken"]["ginger"])
# print(recipes["Butter chicken"]["ginger"])