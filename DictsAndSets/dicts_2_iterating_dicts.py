vehicles_owners = {
    "gurgel": "Tonico",
    "fusca": "Antoine",
    "gol": "Antoinette",
    "fiat": "Maria",
    "hyundai": "Adriano",
    "peugeot": "Rafaela",
    "honda": "Antonio",
}

for key in vehicles_owners:
    print(key)

print("-"*60)

for key in vehicles_owners:
    print(key, vehicles_owners[key], sep=", ")
    # We use indexing to get the value from the key

print("-"*60)

# A more efficient way to iterate over items in a dictionary is by calling
# the .items() method. Similar to .enumerate() in lists and tuples:
for key, value in vehicles_owners.items():
        print(key, value, sep=", ")
# The output is the same as before, but it is more efficient