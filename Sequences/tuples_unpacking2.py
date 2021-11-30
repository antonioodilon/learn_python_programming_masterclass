# Revisiting the code enumerate_example

for index, name in enumerate("abcdefghij"):
    print(index, name)

for t in enumerate("abcdefghij"):
    print(t)  # Creating a series of tuples

for t in enumerate("abcdefghij"):
    index, value = t
    print(index,value)

index, value = (0, "a")
print(index)
print(value)