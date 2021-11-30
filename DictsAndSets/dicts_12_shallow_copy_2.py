cat_list = ["brutal", "charming", "majestic"]
dog_list = ["dumb", "needy", "annoying"]
desert_rose_list = ["cute", "autonomous", "quiet"]

# This is what the code on lines 12 to 16 is actually doing:
living_beings_2 = {
    "cat": cat_list,
    "dog": dog_list,
    "desert rose": desert_rose_list,
}

# living_beings_2 = {
#     "cat": ["brutal", "charming", "majestic"],
#     "dog": ["dumb", "needy", "annoying"],
#     "desert rose": ["cute", "autonomous", "quiet"],
# }

things_2 = living_beings_2.copy()
print(things_2["desert rose"])
print(living_beings_2["desert rose"])

# This is what the code on line 27 is actually doing:
desert_rose_list.append("plant")
# The list isn't actually stored inside the dictionary. Rather, the values
# refer to lists.

# things_2["desert rose"].append("plant")
print(things_2["desert rose"])
print(living_beings_2["desert rose"])

living_beings_2["desert rose"].append("added via living_beings_2")
things_2["desert rose"].append("added via things_2")

print(things_2["desert rose"])
print(living_beings_2["desert rose"])
# We get the same output in both lines because they refer to the same list