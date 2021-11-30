vehicles_owners = {
    "gurgel": "Tonico",
    "fusca": "Antoine",
    "gol": "Antoinette",
    "fiat": "Maria",
    "hyundai": "Adriano",
    "peugeot": "Rafaela",
    "honda": "Antonio",
}

vehicles_owners["sandero"] = "Ionete"
vehicles_owners["ford"] = "André"
vehicles_owners["toy"] = "glider"

# Changing the owner of the car "gurgel"
vehicles_owners["gurgel"] = "Bruno"

print("-"*60)

del vehicles_owners["honda"]  # Deleting honda

for key, value in vehicles_owners.items():
    print(key, value, sep=", ")

print("-"*60)

# When deleting items, the pop() method is more efficient:
vehicles_owners.pop("gol")

for key, value in vehicles_owners.items():
    print(key, value, sep=", ")

print("-"*60)

# Deleting an item that doesn't exist produces an error:
vehicles_owners.pop("dodge")

for key, value in vehicles_owners.items():
    print(key, value, sep=", ")

print("-"*60)

# Reviewing del from lists
vehicles = ["honda", "gurgel", "gol", "hyundai", "gol"]
print(vehicles)
del vehicles[1]
print(vehicles)