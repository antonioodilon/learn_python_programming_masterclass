# Both functions are bad and shouldn't be used in real life. They're there
# just to demonstrate how Python dictionaries work behind the scenes.


def simple_hash(s: str) -> int:
    """
    A very simple hash function that shouldn't be used in real life.
    :param s: `str`
    :return: `int`
    """
    basic_hash = ord(s[0])
    return basic_hash % 10


def my_get(k: str) -> str:
    hash_code = simple_hash(k)
    if values[hash_code]:
        return values[hash_code]
    else:
        return None


data = [
    ("Fusca", "A classic car"),
    ("Chevette", "Beautiful and fast car"),
    ("Belina", "Your grandfather drove one in the 80s"),
    ("Gurgel", "Innovative Brazilian car that doesn't exist anymore"),
    ("Impala", "Name of a car, but also of a large feline"),
]

data.append(("Opala", "A great car that uses a lot of gasoline"))

print(data)

print("-" * 60)

keys = [""] * 10  # Creating a list with 10 values
print(keys)
values = keys.copy()
print(values)

for key, value in data:
    h = simple_hash(key)
    # h = hash(key)
    print(key, h)
    keys[h] = key  # Each key will be at index position h in the list keys.
    # Remember that for lists the [] square brackets represent the index position.
    values[h] = value  # Same thing for the list values

print(keys)
print(values)

print("-" * 60)

# Since simple_hash has already been called, my_get works from where simple_hash
# stopped
print(my_get("Fusca"))
print(my_get("Impala"))
print(my_get("Opala"))
print(my_get("pagero"))
print(my_get("Pagero"))  # We know that the functions are bad because the hash
# for Pagero (with capital P) is the same hash for Fusca. Again, this is just
# to demonstrate how Python dictionaries work and this code shouldn't be used.

print(simple_hash("pagero"))
print(simple_hash("Pagero"))
