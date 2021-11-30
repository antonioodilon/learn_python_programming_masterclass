characters = [
    "Drizzt",
    "Vierna",
    "Drizzt",
    "Keldorn",
    "Vierna",
    "Drizzt",
    "Keldorn",
    "Jaheira",
]

unique_chars = sorted(set(characters))  # If we want it in alphabetical order.
# Python transforms the set into a list using the sorted() method
print(unique_chars)

unique_chars = dict.fromkeys(characters)    # If we want the items in alphabetical
# order and without being repeated. Transform into a dict
print(unique_chars)

unique_chars = list(dict.fromkeys(characters))  # Transform it into a dict,
# then into a list to remove the 'Key': None in the output
print(unique_chars)