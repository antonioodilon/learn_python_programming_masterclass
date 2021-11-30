for index, name in enumerate("abcdefghij"):
    print(index, name)

print()

computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse mat",
                  "stabilizer"
                  ]
print(list(enumerate(computer_parts, start=1)))
#   enumerate() returns the index position and the object in an iterable
# (list, string etc) in the form of a tuple

print()

name = "Antonio"
print(list(enumerate(name)))