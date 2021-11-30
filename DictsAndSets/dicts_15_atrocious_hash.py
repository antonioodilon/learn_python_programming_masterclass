# Tim Buchalka says that this is a very simple hash function that only
# demonstrates what a hash is. It should not be using when actually
# programming.


data = [
    ("Fusca", "A classic car"),
    ("Chevette", "Beautiful and fast car"),
    ("Belina", "Your grandfather drove one in the 80s"),
    ("Gurgel", "Innovative Brazilian car that doesn't exist anymore"),
    ("Impala", "Name of a car, but also of a large feline"),
]

print(ord("A"))
print(ord("j"))
print(ord("k"))
# Testing the ord() function

print("-"*60)


def simple_hash(s: str) -> int:
    """
    A very simple hash function that shouldn't be used in real life.
    :param s: `str`
    :return: `int`
    """
    basic_hash = ord(s[0])
    return basic_hash % 10


print(simple_hash("Antonio"))
print(simple_hash(data[1][0]))

print("-"*60)

for key, value in data:
    h = simple_hash(key)
    print(key, h)

print("-"*60)

for key, value in data:
    h = hash(key)   # Python's built-in hash function
    print(key, h)