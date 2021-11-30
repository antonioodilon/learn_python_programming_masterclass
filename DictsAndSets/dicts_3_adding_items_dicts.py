# Dictionaries don't have an append() method
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

# The line of code below is part of Buchalka's challenge to add a new key
# and value to the dictionary. Hence why it doesn't make sense in real life
# when compared to the other key-value pairs.
vehicles_owners["toy"] = "glider"

for key, value in vehicles_owners.items():
    print(key, value, sep=", ")