living_beings = {
    "cat": "brutal",
    "dog": "dumb",
    "desert rose": "cute",
}

things = living_beings.copy()   # Creates a copy of the dictionary
living_beings["desert rose"] = "pink"
print(things["desert rose"])    # Here desert rose is pink. The value is
# unaffected
print(living_beings["desert rose"])

print("-"*60)

living_beings_2 = {
    "cat": ["brutal", "charming", "majestic"],
    "dog": ["dumb", "needy", "annoying"],
    "desert rose": ["cute", "autonomous", "quiet"],
}

things_2 = living_beings_2.copy()
print(things_2["desert rose"])
print(living_beings_2["desert rose"])

things_2["desert rose"].append("plant") # The append method, because the
# value of "desert rose" is a list
print(things_2["desert rose"])
print(living_beings_2["desert rose"])