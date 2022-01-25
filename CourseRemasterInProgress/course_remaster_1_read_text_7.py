data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac- Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

# Another method to write data in a text file, different from print
plants_filename = "flowers_write.txt"

# The file object has a method called .write()
with open(plants_filename, 'w') as write_plant_file:
    for plant in data:
        write_plant_file.write(plant)  # write_plant_file is our file object
        # File objects have some methods, including .write()

print(data)
string_representation = data.__str__()
print(type(string_representation))  # Class is a string, so we can't put ints or
# floats in it, but we can find a way around it.

filename = "test_numbers.txt"
filename_2 = "test_numbers_2.txt"

with open(filename, 'w') as test_no:
    for i in range(21):
        print(i, file=test_no)

# As you can see, we can't write numbers on our file using .write(). So one
# way is to convert i to strings
with open(filename_2, 'w') as test_no_2:
    for i in range(21):
        test_no_2.write(str(i) + "\n")  # If we want to print each number on
        # a different line using .write(), we need to specify it with "\n",
        # for example

# .write() will only print EXACTLY what you tell it to write, whereas print()
# will perform various conversions, such as including default separators etc.
# So which is better: print or .write()? None of them, as it depends on the context
# Use whichever is more convenient to the task you are going to perform.
