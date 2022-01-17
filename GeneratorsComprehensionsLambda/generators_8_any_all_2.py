entries = [1, 2, 3, 4, 5]

print("all: {}".format(all(entries)))
print("any: {}".format(any(entries)))

print("-" * 60)

entries_empty = []

print("all: {}".format(all(entries_empty)))  # all() is returning True here,
# and this is not a bug!
print("any: {}".format(any(entries_empty)))

if entries_empty:
    print("all: {}".format(all(entries_empty)))
else:
    print(False)
print("any: {}".format(any(entries_empty)))

result = bool(entries_empty) and all(entries)
print(result)