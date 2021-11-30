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

result = vehicles_owners.pop("f1", None)  # Key f1 doesn't exist, so the
# output is None
print(result)

print()

result2 = vehicles_owners.pop("honda", None)  # Key honda exists, so the
# output is the value that is bound to honda
print(result2)

print()

result3 = vehicles_owners.pop("nascar", "Key wasn't found in dictionary.")
print(result3)

# for key, value in vehicles_owners.items():
#     print(key, value, sep=", ")