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

for key, value in vehicles_owners.items():
    print(key, value, sep=", ")

vehicles = ["honda", "gurgel", "gol", "hyundai", "gol"]
print(vehicles)