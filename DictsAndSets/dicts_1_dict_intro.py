vehicles_owners = {
    "gurgel": "Tonico",
    "fusca": "Antoine",
    "gol": "Antoinette",
    "fiat": "Maria",
    "hyundai": "Adriano",
    "peugeot": "Rafaela",
    "honda": "Antonio",
}

# Getting values from a dictionary using indexing:
identify_owner = vehicles_owners["fusca"]
print(identify_owner)
identify_owner2 = vehicles_owners["hyundai"]
print(identify_owner2)

# Getting values from a dictionary using the get() method:
identify_owner3 = vehicles_owners.get("honda")
print(identify_owner3)

# Remember that Python is case-sensitive! Notice what happens when we don't
# match the keys exactly:
identify_owner4 = vehicles_owners.get("Honda")
print(identify_owner4)  # None is printed

# If we don't match the keys exactly while indexing, an error appears:
identify_owner5 = vehicles_owners["Hyundai"]
print(identify_owner5)
# The .get() method is useful if you're not sure if the key exists or not