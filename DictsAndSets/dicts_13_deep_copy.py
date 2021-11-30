import copy

living_beings = {
    "cat": ["brutal", "charming", "majestic"],
    "dog": ["dumb", "needy", "annoying"],
    "desert rose": ["cute", "autonomous", "quiet"],
}

# Performing a shallow copy:
# things = living_beings.copy()

# Performing a deep copy:
things = copy.deepcopy(living_beings)

# The IDs are different:
print(id(things["desert rose"])), things["desert rose"]
print(id(living_beings["desert rose"])), living_beings["desert rose"]

things["desert rose"].append("plant")   # Now this will only affect the things
# dictionary

print(things["desert rose"])
print(living_beings["desert rose"])