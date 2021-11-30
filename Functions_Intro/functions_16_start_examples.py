numbers = (0, 1, 2, 3, 4, 5)

print(numbers, sep=";")
print(*numbers, sep=";")  # * unpacks numbers
print(0, 1, 2, 3, 4, 5, sep=";")
# * unpacks any sequence type

print()

names = ["Antonio", "Marcelo", "Maria", "Antoinette", "Biscoito", "Salém"]

print(names, sep="; ")
print(*names, sep="; ")

print()


def test_star(*args):
    print("Printing a tuple: ", args)  # here args is a tuple
    print("Printing an unpacked tuple: ", *args)
    for x in args:
        print(x)  # here the tuple has been unpacked


test_star(0, 1, 2, 3, 4, 5, 6)

print()

test_star()  # An empty tuple is printed