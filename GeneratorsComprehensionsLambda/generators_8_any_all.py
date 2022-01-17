# In order to understand what any() and all() are doing, it is important to
# understand that Python interprets certain values as True, and others as False
# Have a look:
print("Values interpreted as False in Python")
print("""False: {0}
None: {1}
0: {2}
0.0: {3}
empty list []: {4}
empty tuple (): {5}
empty string '': {6}
empty string "": {7}
empty mapping {{}}: {8}
""".format(False, bool(None), bool(0), bool(0.0), bool([]), bool(()), bool(''), bool(""), bool({})))

print("-" * 60)

entries = [1, 2, 3, 4, 5]

print("all: {}".format(all(entries)))  # Are ALL values True values? Yes.
print("any: {}".format(any(entries)))  # Are ANY values True values? Yes.

print("Iterable with a 'False' value")
entries_with_zero = [1, 2, 0, 4, 5]
print("all: {}".format(all(entries_with_zero)))
# Are ALL values True values? No. Python interprets 0 (zero) as False
print("any: {}".format(any(entries_with_zero)))
# Are ANY values True values? Yes. Python interprets 0 (zero) as False, but
# there are other values in the list, and they are interpreted as True.

print("-" * 60)

name = ""
print(type(name))  # name is a string, although an empty string
if name:
    print("Hello there, {}!".format(name))
else:
    print("How are you doing, nameless individual?")
# name evaluates to False because the variable is an empty string

name_2 = "Antonio"
print(type(name_2))
if name_2:
    print("Hello there, {}!".format(name_2))
else:
    print("How are you doing, nameless individual?")
# now name_2 evaluates to True because the variable now has some content