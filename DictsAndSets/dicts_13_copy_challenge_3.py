# Tim Buchalka's solution:
from smart_fridge_contents import recipes


def my_deepcopy(d1: dict) -> dict:
    """Copy a dictionary, creating copies of the `list` or `dict` values.

    The function will crash with an AttributeError if the values aren't
    lists or dictionaries.

    :param d1: The dictionary to copy.
    :return: A copy of `d1`, with the values being copies of the original values.
    """
    d2 = {}
    for key, value in d1.items():
        value2 = value.copy()
        d2[key] = value2

    return d2


recipes_copy = my_deepcopy(recipes)
print(recipes_copy)
print(recipes_copy["Butter chicken"]["ginger"])
recipes_copy["Butter chicken"]["ginger"] = 300
print(recipes_copy["Butter chicken"]["ginger"])
print(recipes["Butter chicken"]["ginger"])